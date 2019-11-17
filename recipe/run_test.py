import os
import pytest
import jupyter_client
import sys

WIN = sys.platform.startswith("win")
OSX = sys.platform == "darwin"

PY38 = sys.version_info >= (3, 8)

args = [
    os.path.dirname(jupyter_client.__file__),
    "--cov", "jupyter_client",
    "-vv"
]

if WIN or (OSX and PY38):
    args += ["-k", "not start_parallel_process_kernels"]

sys.exit(pytest.main(args))
