# 📚 IS211 – Assignment 1

This repository contains the implementation of **Assignment 1** for IS211, covering **Python functions, exceptions, and object-oriented programming**.

---

## 📌 Part 1 – Functions and Exceptions

- **File:** `assignment1_part1.py`
- Implements the function:
  ```python
  list_divide(numbers, divide=2)
Returns the count of elements divisible by divide.

Defines a custom exception:

class ListDivideException(Exception): pass


Includes automated test cases in test_list_divide().

✅ Behavior

If all tests pass → prints "All tests passed."

Example Output (Success):

<img width="226" height="112" alt="Tests passed" src="https://github.com/user-attachments/assets/5b4a6da8-423b-4804-8879-90b912fe9483" />

If any test fails → raises ListDivideException

Example Output (Failure):

<img width="443" height="95" alt="Failure trace" src="https://github.com/user-attachments/assets/1fa18993-165a-4ba9-915f-7b820265b223" />

Result Section:

<img width="370" height="31" alt="Failure result" src="https://github.com/user-attachments/assets/0ac576d7-a835-4678-b38f-96d0dca74917" />


## 📌 Part 2 – Simple Class

- **File:** `assignment1_part2.py`
- Implements a `Book` class with attributes `author` and `title`.
- Defines a method:
  ```python
  def display(self):
      print(f"{self.title}, written by {self.author}")
✅ Example Output
Harry Potter and the Goblet of Fire, written by J. K. Rowling
Ivanhoe: A Romance, written by Walter Scott


Screenshot of Successful Run:

<img width="448" height="61" alt="image" src="https://github.com/user-attachments/assets/e59e5bb7-60af-47e5-aa3b-77f45531d0e1" />


## ▶️ How to Run the Code

1. **Clone the repository**
   ```bash
   git clone https://github.com/adanielloza/Week-1-Assignment.git
   cd Week-1-Assignment

    └── part2_output.png

2. (Optional) Create and activate a virtual environment

Mac/Linux

python3 -m venv venv
source venv/bin/activate


Windows

python -m venv venv
venv\Scripts\activate


3. Run Part 1

python assignment1_part1.py


4. Run Part 2

python assignment1_part2.py
