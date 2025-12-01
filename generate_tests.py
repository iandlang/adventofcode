#!/usr/bin/env python3
"""
Script to generate test files for all Advent of Code solutions.

Usage:
    python generate_tests.py              # Generate tests for all days
    python generate_tests.py 2024 01     # Generate test for specific day
    python generate_tests.py --dry-run   # Preview what would be generated
"""
import os
import sys
from pathlib import Path
from typing import List, Tuple


TEST_TEMPLATE = '''"""
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
        expected_values = {{
            "test.txt": None,  # TODO: Update with actual result from test.txt
            "data.txt": None,  # TODO: Update with actual result from data.txt
        }}

        start_time = default_timer()
        data = load_data_p1(input_file)
        result = solve_p1(data)
        end_time = default_timer()
        print(f"Part 1 - {{input_file}}: {{result}} ({{end_time - start_time:.6f}}s)")
        expected = expected_values[input_file]

        if expected is None:
            pytest.skip(f"Expected value not set for {{input_file}}")

        assert result == expected, f"Expected {{expected}}, got {{result}}"


class TestPart2:
    """Tests for Part 2"""

    @pytest.mark.part2
    def test_solution(self, input_file):
        """Test part 2 solution with specified input file"""
        # Define expected values for each input file
        expected_values = {{
            "test.txt": None,  # TODO: Update with actual result from test.txt
            "data.txt": None,  # TODO: Update with actual result from data.txt
        }}

        start_time = default_timer()
        data = load_data_p2(input_file)
        result = solve_p2(data)
        end_time = default_timer()
        print(f"Part 2 - {{input_file}}: {{result}} ({{end_time - start_time:.6f}}s)")
        expected = expected_values[input_file]

        if expected is None:
            pytest.skip(f"Expected value not set for {{input_file}}")

        assert result == expected, f"Expected {{expected}}, got {{result}}"


if __name__ == "__main__":
    # Allow running tests directly
    pytest.main([__file__, "-v"])
'''


def find_solution_days(base_path: Path) -> List[Tuple[str, str]]:
    """
    Find all year/day combinations that have solutions.

    Returns list of (year, day) tuples
    """
    solutions = []

    for year_dir in base_path.iterdir():
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue

        year = year_dir.name

        for day_dir in year_dir.iterdir():
            if not day_dir.is_dir():
                continue

            day = day_dir.name

            # Check if this day has the necessary files
            has_part1 = (day_dir / "part1.py").exists()
            has_part2 = (day_dir / "part2.py").exists()
            has_test_data = (day_dir / "test.txt").exists()

            if has_part1 and has_part2 and has_test_data:
                solutions.append((year, day))

    return sorted(solutions)


def generate_test_file(base_path: Path, year: str, day: str, dry_run: bool = False) -> bool:
    """
    Generate test file for a specific day.

    Returns True if file was created/would be created, False if skipped.
    """
    day_dir = base_path / year / day
    test_file = day_dir / f"test-{year}{day}.py"

    if test_file.exists():
        print(f"  ⊘ {year}/{day}: Test file already exists")
        return False

    if dry_run:
        print(f"  ✓ {year}/{day}: Would create test file")
        return True

    content = TEST_TEMPLATE.format(year=year, day=day)
    test_file.write_text(content)
    print(f"  ✓ {year}/{day}: Created test file")
    return True


def main():
    """Main entry point"""
    dry_run = "--dry-run" in sys.argv
    base_path = Path(__file__).parent

    # Check if specific year/day provided
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if len(args) == 2:
        year, day = args
        if dry_run:
            print(f"Dry run: Generating test for {year}/{day}")
        else:
            print(f"Generating test for {year}/{day}")

        generate_test_file(base_path, year, day, dry_run)
        return

    # Generate for all days
    if dry_run:
        print("Dry run: Finding all solutions to generate tests for...")
    else:
        print("Finding all solutions to generate tests for...")

    solutions = find_solution_days(base_path)
    print(f"Found {len(solutions)} solution days\n")

    if not solutions:
        print("No solution days found!")
        return

    created_count = 0
    for year, day in solutions:
        if generate_test_file(base_path, year, day, dry_run):
            created_count += 1

    print(f"\n{'Would create' if dry_run else 'Created'} {created_count} test file(s)")


if __name__ == "__main__":
    main()
