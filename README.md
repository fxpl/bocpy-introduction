# BocPy Introduction

This repository provides a minimal starting point for using [`bocpy`](https://github.com/microsoft/bocpy) with Python.

## Prerequisites

- Python 3.10+ installed
- `pip` available in your Python installation

## 1. Create a virtual environment

From the project root:

```bash
python3 -m venv .venv
```

If `python3` is not available on your machine, try:

```bash
python -m venv .venv
```

## 2. Activate the virtual environment

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Windows (Command Prompt):

```bat
.venv\Scripts\activate.bat
```

You should now see your shell prompt prefixed with `(.venv)`.

## 3. Install dependencies

Install `bocpy` from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 4. Verify installation

BocPy comes with several [examples](https://github.com/microsoft/bocpy/blob/main/examples/README.md).
We can run the fibonacci example to verify the installation:

```bash
bocpy-fibonacci
```

# Getting started

Now you can simply run any Python file using `python <file>`. [`hello.py`](./hello.py) has a minimal
"hello <name>" example you can run with this:

```
python hello.py
```

## Cooking with Boc

You can find the cooking with BoC example from the lecture
in [`cooking.py`](./cooking.py). You can try adding a plating
step or maybe another ingredient.

## Passwords

[`passwords.py`](./passwords.py) contains a simple brute-force
hash cracking script. It currently uses one core, try making
it concurrent using BocPy. You only need to modify the `crack`
function for this.

The implementation doesn't need to terminate early.

## Dining Philosophers

[`philosophers.py`](./philosophers.py) contains a basic setup for
[dining philosophers](https://en.wikipedia.org/wiki/Dining_philosophers_problem).
However, currently all philosophers dine in order. Try enabling them to dine
concurrently using BocPy.

# Additional Resources

- BocPy website: https://microsoft.github.io/bocpy/
- BocPy documentation: https://microsoft.github.io/bocpy/sphinx/index.html
- BocPy examples with descriptions: https://github.com/microsoft/bocpy/blob/main/examples/README.md
