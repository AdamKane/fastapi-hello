import pytest
import sys
from io import StringIO

def run_tests_and_save_results():
    # Redirect stdout to capture test output
    stdout_backup = sys.stdout
    sys.stdout = StringIO()

    # Run pytest
    pytest.main(['-v'])

    # Get the test output
    output = sys.stdout.getvalue()

    # Restore stdout
    sys.stdout = stdout_backup

    # Write test results to file
    with open('test_results.txt', 'w') as f:
        f.write(output)

    print(f"Test results have been written to 'test_results.txt'")

if __name__ == '__main__':
    run_tests_and_save_results()
