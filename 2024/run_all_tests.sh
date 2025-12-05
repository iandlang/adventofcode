#!/bin/bash

passed=0
failed=0
total=0

echo "========================================="
echo "Running 2024 Advent of Code Tests"
echo "========================================="
echo ""

for day in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24; do
    if [ -d "$day" ]; then
        cd "$day"
        output=$(python -m pytest "test-2024$day.py" -k "data.txt" --tb=no -q 2>&1)
        if echo "$output" | grep -q "passed"; then
            count=$(echo "$output" | grep -o '[0-9]\+ passed' | grep -o '[0-9]\+')
            echo "Day $day: ✅ $count passed"
            passed=$((passed + count))
            total=$((total + count))
        elif echo "$output" | grep -q "failed"; then
            count=$(echo "$output" | grep -o '[0-9]\+ failed' | grep -o '[0-9]\+')
            echo "Day $day: ❌ $count failed"
            failed=$((failed + count))
            total=$((total + count))
        fi
        cd ..
    fi
done

echo ""
echo "========================================="
echo "FINAL SUMMARY"
echo "========================================="
echo "✅ Passed: $passed"
echo "❌ Failed: $failed"
echo "📊 Total: $total"
if [ $total -gt 0 ]; then
    success_rate=$((100 * passed / total))
    echo "🎯 Success Rate: $success_rate%"
fi
echo "========================================="
