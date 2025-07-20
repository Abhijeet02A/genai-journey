import math
def safe_square_root(number):
    try:
        square_root = math.sqrt(number)
    except TypeError:
        print(f"'{number}' is not a number please provide correct number")
    except ValueError:
        print("Error: Cannot calculate the square root of a negative number.")
        
    else:
        print("Successful!")
        return square_root
    finally:
        print(f"Attempted square root calculation.")
    

print(safe_square_root(25))
safe_square_root(-9)
safe_square_root("four")
print(safe_square_root(0))
