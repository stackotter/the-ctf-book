from pip import _internal
_internal.main(["install", "-r", "requirements.txt"])

import os
from sys import platform

if platform == "linux":
  os.system("apt-get install -y libnss3")

import Hidden.app
