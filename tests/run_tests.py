import pytest
import sys

sys.dont_write_bytecode = True

retcode = pytest.main([".", "-v", "-p", "no:cacheprovider"])

assert retcode == 0, "The pytest invocation failed. See the log for details."