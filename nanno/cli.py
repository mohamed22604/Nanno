import sys
from .terminal_capture import capture_terminal_output
from .error_detection import error_detection
from .context_builder import build_context
from nanno.main import run_agent
import json

def main():
    command = sys.argv[1:] if len(sys.argv) > 1 else ["echo", "No command provided"]

    command = " ".join(command)

    result = capture_terminal_output(command)

    output = error_detection(result)

    context = build_context(result)

    json_context = json.dumps(context)

    answer = input("Send context to Agent? [y/n]: ")

    agent_context = None
    
    if answer.lower() in ("y", "yes"):
        agent_context = run_agent(json_context)
        print(agent_context)
    
    elif answer.lower() in ("n", "no"):
        print("Error details: \n")
        print(json_context)
        return
    else:
        print("Invalid choice. Please enter y or n.")
    return
    


if __name__ == "__main__":

    agent_context = main()

