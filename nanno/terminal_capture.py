import subprocess


def capture_terminal_output(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        return {
            "command": command,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }

    except subprocess.CalledProcessError as e:
        return {
            "command":command,
            "stderr": e.stderr,
            "stdout": e.stdout,
            "returncode": e.returncode
        }

