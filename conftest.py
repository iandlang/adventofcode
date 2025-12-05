"""
Pytest configuration for Advent of Code tests.
"""
import pytest


@pytest.fixture(params=["test.txt", "data.txt"])
def input_file(request):
    """
    Fixture that provides input filenames.
    Each test runs twice - once with test.txt, once with data.txt.
    """
    return request.param
