#!/bin/bash
# Quick test script - tests only test.txt and test2.txt (not data.txt)

passed=0
failed=0
total=0

echo "============================================================"
echo "Quick Test - test.txt and test2.txt only"
echo "============================================================"
echo ""

for day in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 22 23 24; do
    if [ -d "$day" ]; then
        cd "$day"

        # Run only test files (exclude data.txt)
        output=$(python -m pytest "test-2024$day.py" -k "not data.txt" --tb=no -q 2>&1)

        if echo "$output" | grep -q "passed"; then
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

        cd ..
    fi
done

echo ""
echo "============================================================"
echo "QUICK TEST SUMMARY"
echo "============================================================"
echo "✅ Passed: $passed"
echo "❌ Failed: $failed"
echo "📊 Total: $total"
if [ $total -gt 0 ]; then
    success_rate=$((100 * passed / total))
    echo "🎯 Success Rate: $success_rate%"
fi
echo "============================================================"
echo ""
echo "Note: This only tests example inputs (test.txt/test2.txt)"
echo "Run './run_all_tests.sh' to include data.txt validation"
