"""
Pytest configuration for Advent of Code tests.
"""
import pytest
import os


def pytest_generate_tests(metafunc):
    """
    Dynamically generate test parameters based on which files exist.
    - Part 1 tests use: test.txt, data.txt
    - Part 2 tests use: test2.txt (if exists) OR test.txt, plus data.txt
    """
    if "input_file" in metafunc.fixturenames:
        # Check which test class we're in
        if "TestPart2" in metafunc.function.__qualname__:
            # Part 2: use test2.txt if it exists, otherwise test.txt
            test_files = []
            if os.path.exists("test2.txt"):
                test_files.append("test2.txt")
            elif os.path.exists("test.txt"):
                test_files.append("test.txt")
            test_files.append("data.txt")
            metafunc.parametrize("input_file", test_files)
        else:
            # Part 1: use test.txt
            test_files = []
            if os.path.exists("test.txt"):
                test_files.append("test.txt")
            test_files.append("data.txt")
            metafunc.parametrize("input_file", test_files)
