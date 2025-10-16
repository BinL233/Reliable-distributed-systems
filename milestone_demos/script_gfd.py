import subprocess
import sys
import os
import json


try:
    with open(os.path.join(os.path.dirname(__file__), "command_param.json"), "r") as file:
        config = json.load(file)

except:
    print("Json File Not Found !")

HOST = config["gfd_host"]
PORT = config["gfd_port"]
timeout = config["gfd_time_out"]

file_path = os.path.join(os.path.dirname(__file__), "..", "src", "gfd", "gfd.py")

try:

    subprocess.run([sys.executable, file_path, "--host", HOST, "--port", str(PORT),  "--timeout", str(timeout)])

except KeyboardInterrupt:

    print("LFD Process End.")