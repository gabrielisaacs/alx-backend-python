# 0x01. Python - Async

## Project Overview
This project focuses on asynchronous programming in Python, utilizing the `async` and `await` syntax to improve program efficiency when dealing with I/O-bound operations. Throughout the exercises, we explore how to create, manage, and measure asynchronous tasks using the `asyncio` module and Python's `random` module for delays.

### Resources
To complete this project, you may find the following resources helpful:
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

### Learning Objectives
By the end of this project, you should be able to:
- Understand and apply `async` and `await` syntax in Python.
- Execute asynchronous programs using `asyncio`.
- Run multiple coroutines concurrently.
- Create asyncio tasks and understand their use cases.
- Use the `random` module to generate random delays.

## Project Requirements
- **Python Version**: Code will be tested on Python 3.7.
- **Code Style**: Must follow the `pycodestyle` (version 2.5.x) standards.
- **Documentation**: All functions and modules should have docstrings.
- **Environment**: The project will be run and tested on Ubuntu 18.04 LTS.

---

## Project Structure
The project directory should contain the following files:

### Task 0: The Basics of Async
**File**: `0-basic_async_syntax.py`

Write an asynchronous coroutine `wait_random` that takes in an integer argument `max_delay` (default: 10). This coroutine waits for a random delay between 0 and `max_delay` (inclusive) seconds and then returns the delay value.

Example:
```python
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
print(asyncio.run(wait_random()))
Task 1: Executing Multiple Coroutines Concurrently
File: 1-concurrent_coroutines.py

Create an async function wait_n that takes two arguments, n and max_delay. The function spawns wait_random n times with max_delay. It returns a list of all delays in ascending order (without using sort() due to concurrency).

Example:

python
Copy code
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n
print(asyncio.run(wait_n(5, 5)))
Task 2: Measure the Runtime
File: 2-measure_runtime.py

Define a measure_time function that takes n and max_delay as parameters and measures the runtime of wait_n(n, max_delay). It returns the average execution time per coroutine.

Example:

python
Copy code
measure_time = __import__('2-measure_runtime').measure_time
print(measure_time(5, 9))
Task 3: Creating Asyncio Tasks
File: 3-tasks.py

Implement a function task_wait_random that takes an integer max_delay and returns an asyncio.Task. This function wraps wait_random into a Task without using async def.

Example:

python
Copy code
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random
asyncio.run(task_wait_random(5))
Task 4: Executing Multiple Tasks Concurrently
File: 4-tasks.py

Create an async function task_wait_n, similar to wait_n, but it should use task_wait_random to spawn tasks. This function returns a list of delays in ascending order.

Example:

python
Copy code
import asyncio
task_wait_n = __import__('4-tasks').task_wait_n
print(asyncio.run(task_wait_n(5, 6)))
Usage
To run the examples for each task, use the following command:

bash
Copy code
$ python3 <task_file>.py
Repository
GitHub Repository: alx-backend-python
Directory: 0x01-python_async_function
Happy coding, and enjoy learning async programming in Python!
