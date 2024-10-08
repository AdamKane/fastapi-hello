import pytest
import sys
from io import StringIO
from datetime import datetime
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="zeep.utils")
warnings.filterwarnings("ignore", message="'cgi' is deprecated and slated for removal in Python 3.13")

def run_tests_and_save_results():
    # Redirect stdout to capture test output
    stdout_backup = sys.stdout
    sys.stdout = StringIO()

    # Run pytest with warning filters
    pytest.main(['-v', '-W', 'ignore::DeprecationWarning'])

    # Get the test output
    output = sys.stdout.getvalue()

    # Restore stdout
    sys.stdout = stdout_backup

    # Get current time in 12-hour format
    current_time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

    # Write test results to file with current time at the top
    with open('test_results.txt', 'w') as f:
        f.write(f"Test run at: {current_time}\n\n")
        f.write(output)

    print(f"Test results have been written to 'test_results.txt'")

if __name__ == '__main__':
    run_tests_and_save_results()
