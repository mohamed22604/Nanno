
def error_detection(output):
    """
    Detects errors in the terminal output.

    Returns:
        str: A message indicating whether an error was detected or not.
    """
    if output["returncode"] != 0:
        return f"Error detected: {output['stderr']}"
    elif output["returncode"] == 0:
        return