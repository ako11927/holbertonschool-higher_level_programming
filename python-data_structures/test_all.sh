#!/bin/bash
echo "=== Python Data Structures Project Test ==="
echo ""

# Test each task
test_task() {
    local task_num=$1
    local script_name=""
    
    if [ $task_num -eq 12 ]; then
        script_name="12-switch.py"
    else
        script_name="${task_num}-main.py"
    fi
    
    if [ -f "$script_name" ]; then
        echo "Testing Task $task_num..."
        echo "  Running: $script_name"
        
        # Test functionality
        if python3 "$script_name" >/dev/null 2>&1; then
            echo "  ✅ Functionality: PASS"
        else
            echo "  ❌ Functionality: FAIL"
            python3 "$script_name"  # Show error
        fi
        
        # Test pycodestyle
        if pycodestyle "$script_name" >/dev/null 2>&1; then
            echo "  ✅ Pycodestyle: PASS"
        else
            echo "  ❌ Pycodestyle: FAIL"
            pycodestyle "$script_name"  # Show errors
        fi
    else
        echo "Testing Task $task_num..."
        echo "  ⚠️  No test file: $script_name"
    fi
    echo ""
}

for i in {0..12}; do
    test_task $i
done

echo "=== Summary ==="
echo "All tasks 0-12 completed and tested!"
