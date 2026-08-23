from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langchain.tools import tool
from pathlib import Path
from langchain.agents import create_agent
from nanno.system_prompt import system_prompt
from nanno.database import get_db
from nanno.database import get_file
from nanno.database import save_file_content
import os


load_dotenv()

# tools :

@tool("read_file", description="Read and return the contents of a text file.")
def read_file(file_path: str) -> str:

    file_path = Path(file_path)

    result = get_file(file_path)

    if result:
        return result
    
    elif result == None:

        if file_path.exists() and file_path.is_file():

            content = file_path.read_text(encoding="utf-8")

            save_file_content(file_path, content)

            return content
        else:
            return "File not found or inaccessible."
    else:
        print("File not found or inaccessible.")


def run_agent(agent_context):

    model = ChatOpenRouter(
    model = "meta-llama/llama-3.3-70b-instruct",
    api_key = os.getenv("OPENROUTER_API_KEY")
    )

    agent = create_agent(
        model = model,
        tools = [read_file],
        system_prompt = system_prompt
    )

    final_res = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": agent_context
        }
    ]
    })

    return final_res["messages"][-1].content

