
def build_context(result):
   context = {
    "execution": {
        "command": result["command"],
        "stdout": result["stdout"],
        "stderr": result["stderr"],
        "returncode": result["returncode"]
    }
}
   return context

