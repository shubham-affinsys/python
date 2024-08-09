import subprocess

# # Print working directory
# subprocess.run(["bash", "-c", "pwd"])

# # Print "exiting program" without a newline
# subprocess.run(["echo", "-ne", "exiting program"])

# # Sleep for 5 seconds
# subprocess.run(["zsh", "-c", "sleep 5"])

# # Print periods without newlines, with pauses in between
# subprocess.run(["echo", "-ne", "."])
# subprocess.run(["zsh", "-c", "sleep 5"])
# subprocess.run(["echo", "-ne", "."])
# subprocess.run(["zsh", "-c", "sleep 5"])
# subprocess.run(["echo", "-ne", "."])
# subprocess.run(["zsh", "-c", "sleep 5"])

# # Print 'hi'
# subprocess.run(["echo", "hi"])


subprocess.run(['echo',"-ne","starting program"])

for i in range(4):
    subprocess.run(["bash", "-c", "sleep 1"])
    subprocess.run(["echo", "-ne", "."])
subprocess.run(["echo"])

subprocess.run(["bash","-c","python3 shell_progess.py"])