import pyautogui
import time

def auto_type(text, delay=0.0001):
    """
    Automatically types the given text with a specified delay between keystrokes.
    
    Parameters:
    - text: The string to be typed.
    - delay: The delay between keystrokes in seconds (default is 0.1 seconds).
    """
    time.sleep(2)  # Wait for 2 seconds before starting to type
    for char in text:
        pyautogui.write(char, interval=delay)
    
# Example usage:
text_to_type ="""
def all_divisible(arr, X):
    return all(a % X == 0 for a in arr)

def make_elements_divisible(arr, X):
    Y = 0
    
    while not all_divisible(arr, X):
        # Increment Y
        Y += 1
        
        # Check each element to see if adding Y would make it divisible by X
        for i in range(len(arr)):
            if (arr[i] + Y) % X == 0:
                arr[i] += Y
                break
        else:
            # If no element was updated, try the next Y increment
            continue
    
    return Y

# Example usage:
# Input number of elements
n = int(input("Enter the number of elements in the array: "))

# Input the array elements
arr = []
for _ in range(n):
    arr.append(int(input("Enter an element: ")))

# Input the value of X
X = int(input("Enter the value of X: "))

# Get the result
result = make_elements_divisible(arr, X)

print("Value of Y when all elements are divisible by X:", result)


"""
auto_type(text_to_type)
