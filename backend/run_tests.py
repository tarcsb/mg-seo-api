import sys
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()


def run_tests(test_type=None, coverage=False):
    """
    Run the specified tests with or without coverage.

    :param test_type: 'unit', 'integration', or 'all'
    :param coverage: Boolean, whether to include coverage report
    """
    test_dir = {
        "unit": "tests/unit/",
        "integration": "tests/integration/",
        "all": "tests/",
    }

    command = []

    # If coverage is enabled
    if coverage:
        command = ["coverage", "run", "--source=app", "-m", "pytest", "-v"]
    else:
        command = ["pytest", "-v"]

    if test_type in test_dir:
        command.append(test_dir[test_type])
    else:
        print(f"Invalid test type '{test_type}'. Use 'unit', 'integration', or 'all'.")
        sys.exit(1)

    # Run the tests
    result = subprocess.run(command)
    if result.returncode != 0:
        print(f"Tests failed with return code {result.returncode}.")
        sys.exit(result.returncode)

    # Generate coverage report if enabled
    if coverage:
        subprocess.run(["coverage", "report", "-m"])
        subprocess.run(["coverage", "html"])
        print("Coverage report generated at: htmlcov/index.html")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_tests.py <unit|integration|all> [--coverage]")
        sys.exit(1)

    test_type = sys.argv[1]
    coverage = "--coverage" in sys.argv

    run_tests(test_type=test_type, coverage=coverage)
