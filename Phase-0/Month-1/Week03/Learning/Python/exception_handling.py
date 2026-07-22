# Day 12

class SecurityError(object):
    pass




def safe_divide(a, b):
    if a < 0:
        raise SecurityError("Negative numbers are not allowed in this operation.")
    try:
        divide = a / b 
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input type. Please enter numbers.")
        return None
    except SecurityError as e:
        print(e)
        return None
    else:
        print(f"Result: {divide}.")
        return divide
    finally:
        print("Division attempt finished.")


safe_divide(-2,5)