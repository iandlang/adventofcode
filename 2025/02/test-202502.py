"""
Advent of Code solution tests
"""
import pytest
from timeit import default_timer
from part1 import load_data as load_data_p1, solve as solve_p1
from part2 import load_data as load_data_p2, solve as solve_p2


class TestPart1:
    """Tests for Part 1"""

    @pytest.mark.part1
    def test_solution(self, input_file):
        """Test part 1 solution with specified input file"""
        # Define expected values for each input file
        expected_values = {
            "test.txt": 1227775554,
            "data.txt": 52316131093,
        }

        start_time = default_timer()
        data = load_data_p1(input_file)
        result = solve_p1(data)
        end_time = default_timer()
        print(f"Part 1 - {input_file}: {result} ({end_time - start_time:.6f}s)", end = " ")
        expected = expected_values[input_file]

        if expected is None:
            pytest.skip(f"Expected value not set for {input_file}")

        assert result == expected, f"Expected {expected}, got {result}"


class TestPart2:
    """Tests for Part 2"""

    @pytest.mark.part2
    def test_solution(self, input_file):
        """Test part 2 solution with specified input file"""
        # Define expected values for each input file
        expected_values = {
            "test.txt": 4174379265,
            "data.txt": 69564213293,
        }

        start_time = default_timer()
        data = load_data_p2(input_file)
        result = solve_p2(data)
        end_time = default_timer()
        print(f"Part 2 - {input_file}: {result} ({end_time - start_time:.6f}s)", end = " ")
        expected = expected_values[input_file]

        if expected is None:
            pytest.skip(f"Expected value not set for {input_file}")

        assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    # Allow running tests directly
    pytest.main([__file__, "-v"])
