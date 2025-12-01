"""
Pytest configuration for Advent of Code tests.

Provides custom command line options for selecting input files.
"""
import os
from pathlib import Path
import pytest


def pytest_addoption(parser):
    """Add custom command line options to pytest."""
    parser.addoption(
        "-T",
        "--test-data",
        action="store_true",
        default=False,
        help="Run tests using test.txt input file",
    )
    parser.addoption(
        "-D",
        "--data",
        action="store_true",
        default=False,
        help="Run tests using data.txt input file",
    )


@pytest.fixture(scope="session")
def input_file(request):
    """
    Fixture that provides the input filename based on command line options.

    Usage in tests:
        def test_solution(input_file):
            data = load_data(input_file)
            ...

    Command line usage:
        pytest -T          # Uses test.txt
        pytest -D          # Uses data.txt
        pytest             # Defaults to test.txt
    """
    use_test = request.config.getoption("--test-data")
    use_data = request.config.getoption("--data")

    if use_data:
        return "data.txt"
    elif use_test:
        return "test.txt"
    else:
        # Default to test.txt
        return "test.txt"


@pytest.fixture(scope="session")
def expected_results(input_file):
    """
    Fixture that provides expected results based on the input file.

    Returns a dict that tests can use to look up expected values.
    Tests should define their own expected values for each input file.
    """
    return {"input_file": input_file}


@pytest.fixture(scope="module", autouse=True)
def change_test_dir(request):
    """
    Automatically change to the directory containing the test file.
    This ensures relative file paths work correctly.
    """
    # Get the directory of the test module
    test_dir = Path(request.fspath).parent
    # Save the original directory
    original_dir = Path.cwd()
    # Change to test directory
    os.chdir(test_dir)
    # Yield control to the test
    yield
    # Restore original directory after all tests in module complete
    os.chdir(original_dir)
