# It contains various types of comments and blank lines to test the embedding functionality.
# anchor
     
import os           
import sys          
# --- Section 1: Basic Functionality --- 
         
def hello_world():    
    """    
    This is a docstring.         
    It should not be treated as a regular comment for embedding.
    """
    print("Hello, world!") # This is an inline comment.

# This is a standalone comment.

# Another standalone comment.
def another_function():
    # This function does nothing.
    pass
# --- Section 2: More Complex Code Structures ---

class MyClass:
    """A simple class to demonstrate methods and attributes."""
    def __init__(self, name):
        self.name = name # Initialize the name
        self.value = 0   # Default value

    def increment(self, amount=1):
        """Increments the internal value."""
        self.value += amount
        # A comment inside a method
        return self.value

    def get_info(self):
        """Returns information about the instance."""
        return f"Name: {self.name}, Value: {self.value}"
my_instance = MyClass("TestObject")
my_instance.increment(5) # Call a method
# --- Section 3: Control Flow and Loops ---

def calculate_sum(numbers):
    """Calculates the sum of a list of numbers."""
    total = 0
    for num in numbers:
        total += num # Add each number
    return total

data = [10, 20, 30, 40, 50]
result_sum = calculate_sum(data) # Get the sum

if result_sum > 100:
    print("Sum is greater than 100.") # Conditional print
elif result_sum == 100:
    print("Sum is exactly 100.")
else:
    print("Sum is less than 100.")

# --- Section 4: File Operations (Simulated) ---

def simulate_file_write(filename, content):
    """Simulates writing content to a file."""
    print(f"Simulating writing to {filename}...")

# --- Section 5: Extended Content for Fibonacci Testing ---

def another_dummy_function(x, y):
    # A simple arithmetic operation.
    z = (x * y) + (x / 2)
    return z # Return the result

class AnotherClass:
    # This class serves as another container for code.
    def __init__(self):
        # The constructor is intentionally simple.
        self.items = []

    def add_item(self, item):
        # Add an item to the internal list.
        self.items.append(item)
        # Log the addition for demonstration.
        print(f"Added {item} to the list.")

# More standalone comments to increase potential anchor points.
# Comment A
# Comment B
# Comment C

def final_function():
    # This is the last function in the test file.
    print("End of test file execution.")

# Final comment before the end of the file.