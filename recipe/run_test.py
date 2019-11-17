import os
import pytest
import jupyter_client
import sys

WIN = sys.platform.startswith("win")
OSX = sys.platform == "darwin"

PY38 = sys.version_info >= (3, 8)

args = [
    os.path.dirname(jupyter_client.__file__),
    "-vv"
]

skips = []

if WIN or (OSX and PY38):
    skips += ["not start_parallel_process_kernels"]

if WIN:
    skips += [
        "not start_sequence_process_kernels",
        "not tcp_lifecycle"
    ]

if skips:
    args += ["-k", " and ".join(skips)]

print("PYTEST ARGS", args)

sys.exit(pytest.main(args))
