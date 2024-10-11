# Python Variable Annotations Project

## Project Overview

This project focuses on using Python’s variable annotations feature. You'll implement various type-annotated functions to help build a deeper understanding of Python’s type hinting capabilities. This will improve code readability, maintainability, and overall quality.

## General Requirements

- **Allowed editors**: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7).
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should use `pycodestyle` style (version 2.5).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have documentation.
- All your classes should have documentation.
- All your functions (inside and outside a class) should have documentation.

## Task Descriptions

### 0. Basic Annotations - Add

Write a type-annotated function `add` that takes two `float` arguments and returns their sum as a `float`.

- **Prototype**: `def add(a: float, b: float) -> float:`
  
### 1. Basic Annotations - Concat

Write a type-annotated function `concat` that takes two `string` arguments and returns a concatenated string.

- **Prototype**: `def concat(str1: str, str2: str) -> str:`

### 2. Basic Annotations - Floor

Write a type-annotated function `floor` that takes a `float` argument and returns the floor of the float as an `int`.

- **Prototype**: `def floor(n: float) -> int:`

### 3. Basic Annotations - To String

Write a type-annotated function `to_str` that takes a `float` argument and returns the string representation of the float.

- **Prototype**: `def to_str(n: float) -> str:`

### 4. Define Variables

Define and annotate the following variables with their specified values:
- `a`, an integer with a value of `1`.
- `pi`, a float with a value of `3.14`.
- `i_understand_annotations`, a boolean with a value of `True`.
- `school`, a string with a value of `"Holberton"`.

### 5. Complex Types - List of Floats

Write a type-annotated function `sum_list` that takes a list of floats and returns their sum as a float.

- **Prototype**: `def sum_list(input_list: List[float]) -> float:`

### 6. Complex Types - Mixed List

Write a type-annotated function `sum_mixed_list` that takes a list of integers and floats and returns their sum as a float.

- **Prototype**: `def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:`

### 7. Complex Types - String and Int/Float to Tuple

Write a type-annotated function `to_kv` that takes a string and an int/float, and returns a tuple where the first element is the string and the second is the square of the int/float (annotated as a `float`).

- **Prototype**: `def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:`

### 8. Complex Types - Functions

Write a type-annotated function `make_multiplier` that takes a float and returns a function that multiplies a float by the given multiplier.

- **Prototype**: `def make_multiplier(multiplier: float) -> Callable[[float], float]:`

### 9. Let’s Duck Type an Iterable Object

Annotate the following function’s parameters and return values with appropriate types:
  
- **Prototype**: `def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:`

---

## Repository

- **GitHub repository**: `alx-backend-python`
- **Directory**: `0x00-python_variable_annotations`
