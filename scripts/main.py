"""Pipeline para geracao do blog completo"""

import subprocess

subprocess.run(["python", "scripts/index.py"])
subprocess.run(["python", "scripts/about.py"])
