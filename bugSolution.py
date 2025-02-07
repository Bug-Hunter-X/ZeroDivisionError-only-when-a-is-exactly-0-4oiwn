def function_with_uncommon_error_solution(a, b):
    if a == 0:
        return float('inf') # Or handle it in a more meaningful way based on application context.
        #raise ZeroDivisionError("Division by zero") # Raise explicit error for better debugging
    return a + b