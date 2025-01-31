# Value Error Exception Handler

A Python utility function designed to simplify input validation by handling `ValueError` exceptions and ensuring user input meets specified criteria. This function is ideal for interactive CLI applications where user input needs to be validated against type, minimum, and maximum value constraints.

## Features

- Supports dynamic input type conversion (`int`, `float`, `str`, etc.).
- Validates input against optional `min_value` and `max_value` constraints.
- Provides customizable input and error messages.
- Loops until the user provides valid input.

## Installation

```bash
pip install value-error-exception-handler
```

## Usage

```python
from value_error_exception_handler import value_error_exception_handler

# Example: Asking for an integer between 1 and 10
user_input = value_error_exception_handler(
    value_type=int, 
    input_message="Enter a number between 1 and 10: ", 
    error_message="Invalid input. Please enter a valid number.", 
    min_value=1, 
    max_value=10
)

print(f"You entered: {user_input}")
```

## Function Signature

```python
def value_error_exception_handler(
    value_type=int, 
    input_message="Please enter a number: ", 
    error_message="Invalid input. Please enter a number.", 
    max_value=None, 
    min_value=None
):
    """
    Validates and handles user input, ensuring it meets specified criteria.

    Parameters:
        value_type (type): The type to which user input should be converted (default: int).
        input_message (str): Message displayed to prompt the user (default: "Please enter a number: ").
        error_message (str): Message displayed on invalid input (default: "Invalid input. Please enter a number.").
        max_value (Optional[int/float]): The maximum allowable value for input (default: None).
        min_value (Optional[int/float]): The minimum allowable value for input (default: None).

    Returns:
        user_input: Validated and converted user input.
    """
```


## How It Works

1. Prompts the user with a custom message (`input_message`).
2. Attempts to convert user input to the specified `value_type`.
3. Validates the converted input against optional `min_value` and `max_value`.
4. If the input is invalid:
   - Displays the `error_message` or a specific constraint violation message.
   - Re-prompts the user until valid input is received.
5. Returns the validated input.

## Examples

### Basic Example

```python
age = value_error_exception_handler(value_type=int, input_message="Enter your age: ")
print(f"Your age is {age}")
```

### Using Minimum and Maximum Values

```python
score = value_error_exception_handler(
    value_type=float, 
    input_message="Enter your score (0.0 - 100.0): ", 
    error_message="Please enter a valid score.", 
    min_value=0.0, 
    max_value=100.0
)
print(f"Your score is {score}")
```

### Non-Numeric Input

```python
name = value_error_exception_handler(
    value_type=str, 
    input_message="Enter your name: ", 
    error_message="Please enter a valid name."
)
print(f"Hello, {name}!")
```

## Contribution

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details. 

---

Elevate your CLI application's user experience with robust input validation using `value_error_exception_handler`!
