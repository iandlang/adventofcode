#!/bin/bash

passed=0
failed=0
skipped=0
total=0

echo "============================================================"
echo "Testing with test.txt files"
echo "============================================================"
echo ""

for day in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 22 23 24; do
    if [ -d "$day" ]; then
        cd "$day"

        # Use timeout command to limit test time to 30 seconds
        output=$(timeout 30 python -m pytest "test-2024$day.py" --tb=no -q 2>&1)
        exit_code=$?

        if [ $exit_code -eq 124 ]; then
            echo "Day $day: ⏱️  timeout (>20s)"
        elif echo "$output" | grep -q "passed"; then
            count=$(echo "$output" | grep -o '[0-9]\+ passed' | head -1 | grep -o '[0-9]\+')
            echo "Day $day: ✅ $count passed"
            passed=$((passed + count))
            total=$((total + count))

            # Check for failures too
            if echo "$output" | grep -q "failed"; then
                fail_count=$(echo "$output" | grep -o '[0-9]\+ failed' | head -1 | grep -o '[0-9]\+')
                echo "         ⚠️  $fail_count failed"
                failed=$((failed + fail_count))
                total=$((total + fail_count))
            fi
        elif echo "$output" | grep -q "failed"; then
            count=$(echo "$output" | grep -o '[0-9]\+ failed' | head -1 | grep -o '[0-9]\+')
            echo "Day $day: ❌ $count failed"
            failed=$((failed + count))
            total=$((total + count))
        fi

        if echo "$output" | grep -q "skipped"; then
            skip_count=$(echo "$output" | grep -o '[0-9]\+ skipped' | head -1 | grep -o '[0-9]\+')
            if [ ! -z "$skip_count" ]; then
                skipped=$((skipped + skip_count))
            fi
        fi

        cd ..
    fi
done

echo ""
echo "============================================================"
echo "SUMMARY - test.txt results"
echo "============================================================"
echo "✅ Passed: $passed"
echo "❌ Failed: $failed"
echo "⏭️  Skipped: $skipped"
echo "📊 Total: $total"
if [ $total -gt 0 ]; then
    success_rate=$((100 * passed / total))
    echo "🎯 Success Rate: $success_rate%"
fi
echo "============================================================"
