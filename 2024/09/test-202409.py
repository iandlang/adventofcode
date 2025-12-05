"""
Advent of Code solution tests
"""
import pytest
from timeit import default_timer
from part1 import load_data as load_data_p1, solve as solve_p1
from part2 import load_data as load_data_p2, solve as solve_p2


class TestPart1:
    """Tests for Part 1"""

    EXPECTED = {
        "test.txt": 1928,  # TODO: Add expected test value from puzzle description
        "data.txt": 6386640365805,
    }

    @pytest.mark.part1
    def test_solution(self, input_file):
        """Test part 1 solution"""
        if self.EXPECTED[input_file] is None:
            pytest.skip(f"No expected value for {input_file}")
        start = default_timer()
        data = load_data_p1(input_file)
        result = solve_p1(data)
        elapsed = default_timer() - start
        print(f"Part1 {input_file}: {result} ({elapsed:.6f}s)", flush=True)
        assert result == self.EXPECTED[input_file]


class TestPart2:
    """Tests for Part 2"""

    EXPECTED = {
        "test.txt": 2858,  # TODO: Add expected test value from puzzle description
        "data.txt": 6423258376982,
    }

    @pytest.mark.part2
    def test_solution(self, input_file):
        """Test part 2 solution"""
        if self.EXPECTED[input_file] is None:
            pytest.skip(f"No expected value for {input_file}")
        start = default_timer()
        data = load_data_p2(input_file)
        result = solve_p2(data)
        elapsed = default_timer() - start
        print(f"Part2 {input_file}: {result} ({elapsed:.6f}s)", flush=True)
        assert result == self.EXPECTED[input_file]
