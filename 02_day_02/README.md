# Day 2 - Data Types and Tip Calculator 📊

**Date**: September 3, 2025  
**Focus**: Python Data Types & Basic Calculator Project

## What I Learned Today

Day 2 was all about understanding Python's fundamental data types and applying that knowledge to build a practical tip calculator application.

### Key Concepts Covered:

1. **Python Data Types**
   - Strings (`str`) - text data
   - Integers (`int`) - whole numbers
   - Floats (`float`) - decimal numbers
   - Booleans (`bool`) - True/False values

2. **Type Conversion**
   - Using `int()`, `float()`, `str()` functions
   - Understanding when and why to convert types
   - Handling user input conversion

3. **Mathematical Operations**
   - Basic arithmetic operations
   - Order of operations
   - Working with decimal precision

4. **User Input and Output**
   - Getting user input with `input()`
   - Converting input to appropriate data types
   - Formatting output for better user experience

### Files Created

- **`datatypes.py`** - Exploration of different Python data types and type conversion
- **`tip_calculator.py`** - Interactive tip calculator application

### Project Highlight: Tip Calculator

Built a functional tip calculator that:
- Takes bill amount as input
- Asks for desired tip percentage
- Calculates total amount per person when splitting
- Handles decimal formatting for currency

### Code Examples

```python
# Type conversion examples
age = int(input("Enter your age: "))
price = float(input("Enter price: "))
name = str(input("Enter your name: "))

# Tip calculation logic
total_with_tip = bill * (1 + tip_percentage / 100)
amount_per_person = total_with_tip / number_of_people
```

### Challenges Faced

- Understanding the difference between different numeric types
- Handling decimal precision in currency calculations
- Converting user input to the correct data type
- Formatting output to look professional

### Next Steps

- Explore more complex data structures (lists, dictionaries)
- Learn about string manipulation methods
- Practice more with conditional statements

### Reflection

Data types are the building blocks of programming! Understanding when to use each type and how to convert between them is crucial. The tip calculator project was a great way to apply these concepts in a real-world scenario.

---

**Time Spent**: ~1 hour  
**Status**: ✅ Completed  
**Difficulty**: ⭐⭐☆
