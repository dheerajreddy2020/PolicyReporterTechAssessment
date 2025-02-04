from best_threshold import *


threshold_data_1 = {
    0.1: {"TP": 90, "TN": 50, "FP": 10, "FN": 10},  # Recall = 0.9
    0.2: {"TP": 85, "TN": 60, "FP": 15, "FN": 5},   # Recall = 0.944
    0.3: {"TP": 80, "TN": 70, "FP": 20, "FN": 5},   # Recall = 0.94
    0.4: {"TP": 75, "TN": 80, "FP": 25, "FN": 5},   # Recall = 0.937
    0.5: {"TP": 70, "TN": 90, "FP": 30, "FN": 10},  # Recall = 0.875
}

threshold_data_2 = {
    0.1: {"TP": 50, "TN": 100, "FP": 20, "FN": 50},  # Recall = 0.5
    0.2: {"TP": 60, "TN": 90, "FP": 25, "FN": 40},   # Recall = 0.6
    0.3: {"TP": 70, "TN": 80, "FP": 30, "FN": 30},   # Recall = 0.7
    0.4: {"TP": 85, "TN": 75, "FP": 35, "FN": 15},   # Recall = 0.85
    0.5: {"TP": 90, "TN": 60, "FP": 40, "FN": 10},   # Recall = 0.9
    0.6: {"TP": 95, "TN": 50, "FP": 45, "FN": 5},    # Recall = 0.95
}

threshold_data_3 = {
    0.1: {"TP": 30, "TN": 50, "FP": 10, "FN": 70},  # Recall = 0.3
    0.2: {"TP": 40, "TN": 60, "FP": 15, "FN": 60},  # Recall = 0.4
    0.3: {"TP": 50, "TN": 70, "FP": 20, "FN": 50},  # Recall = 0.5
    0.4: {"TP": 60, "TN": 80, "FP": 25, "FN": 40},  # Recall = 0.6
    0.5: {"TP": 70, "TN": 90, "FP": 30, "FN": 30},  # Recall = 0.7
}  # No threshold reaches recall >= 0.9, expected output: None

# Running test cases
print(f'Test case 1')
print(threshold_data_1)
print(f'best threshold for test case 1 is {best_threshold(threshold_data_1)}')  # Expected Output: 0.1 (first satisfying recall >= 0.9)

print('\n')
print(f'Test case 2')
print(threshold_data_2)
print(f'best threshold for test case 1 is {best_threshold(threshold_data_2)}')  # Expected Output: 0.5 (first satisfying recall >= 0.9)


print('\n')
print(f'Test case 3')
print(threshold_data_3)
print(f'best threshold for test case 3 is {best_threshold(threshold_data_3)}')  # Expected Output: None (no threshold meets recall >= 0.9)
