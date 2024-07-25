class Calculator:
  def __init__(self, value):
    self.value = value

  def add(self, other):
    return Calculator(self.value + other.value)

  def sub(self, other):
    return Calculator(self.value - other.value)

def mystery_function(a, b):
    addition_result = a.add(b)  # Use the add method of Calculator class
    subtraction_result = a.sub(b)  # Use the sub method of Calculator class
    return addition_result, subtraction_result

# Create instances of the Calculator class
x = Calculator(10)
y = Calculator(5)

# Use the mystery function with Calculator instances
add_result, sub_result = mystery_function(x, y)

# Print the results
print("Addition Result:", add_result.value)
print("Subtraction Result:", sub_result.value)