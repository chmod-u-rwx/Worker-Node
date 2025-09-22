"""
This file contains test functions for stdout and stderr outputs.
It includes functions to test both standard output and error outputs.
If the test type is True, it will print to stdout; otherwise, it will raise an error to stderr.
This is useful for verifying that the system handles both types of outputs correctly.
BURAT
"""

def stdout_test():
    print("This is a test output to stdout.")

def stderr_test():
    raise NotImplementedError("This is a test error to stderr.")

def test_vm_output(test_type:bool=True):
    if test_type:
        stdout_test()
    else:
        stderr_test()

if __name__ == "__main__":
    import sys
    # Take argument from command line: "stdout" or "stderr"
    test_type = True if len(sys.argv) < 2 or sys.argv[1].lower() == "stdout" else False
    test_vm_output(test_type)
