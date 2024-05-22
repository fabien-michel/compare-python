#!/usr/bin/env python
from operator import itemgetter
import subprocess
import concurrent.futures
import sys


TEST_SCRIPT = "test.py"
QUANTITY = sys.argv.pop(1) if len(sys.argv) > 1 else 15000

RUNS = {
    "local": ["python3.12"],
    # "local310": ["python3.10","test.py"]
    # "local311": ["python3.11","test.py"],
    # "local313": ["python3.13","test.py"],
    # "custom": ["docker","run", "-w", "/app", "-v", ".:/app", "custom_python", "python3.12"],
    "official-docker": ["docker","run", "-w", "/app", "-v", ".:/app", "python:3.12", "python3.12"],
    "arch-on-docker": ["docker","run", "-w", "/app", "-v", ".:/app", "python_arch", "python3.12"],
    "debian-on-docker": ["docker","run", "-w", "/app", "-v", ".:/app", "python_debian", "python3.12"],
    "ubuntu-on-docker": ["docker","run", "-w", "/app", "-v", ".:/app", "python_ubuntu", "python3.12"],
    "fedora-on-docker": ["docker","run", "-w", "/app", "-v", ".:/app", "python_fedora", "python3.12"],
    # "redhat-python": ["docker","run", "-w", "/app", "-v", ".:/app", "registry.access.redhat.com/ubi9/python-312", "python3.12"],
}

results = {}


def do_run(run_name):
    run_cmd = RUNS[run_name] + [TEST_SCRIPT, str(QUANTITY)]
    print(" ".join(run_cmd))
    process = subprocess.run(run_cmd, capture_output=True, encoding="utf8")
    if process.returncode != 0:
        exit(process.stderr)
    output = process.stdout.strip()
    return (run_name, float(output))


# with concurrent.futures.ThreadPoolExecutor() as executor:
#    results = executor.map(do_run, RUNS.keys()) 
#    results = dict(results)

for run_name in RUNS:
    print(run_name.ljust(20), end="\t", flush=True)
    _, result = do_run(run_name)
    print(result)
    results[run_name] = result

print("--")
reference = results['official-docker']

for run_name, result in sorted(results.items(), key=itemgetter(1)):
    diff = (result-reference)*100/reference
    print(f"{run_name.ljust(20)}\t{result}\t{diff}%")
