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

Now you can simply run any Python file using `python <file>`. [`main.py`](./main.py) has a minimal
"hello <name>" example you can run with this:

```
python main.py
```

Try modifying it by adding additional cowns and behaviours.

When you're up for a challenge you can checkout [philosophers.py](./philosophers.py) and try to
implement dining philosophers using BocPy.

# Additional Resources

- BocPy website: https://microsoft.github.io/bocpy/
- BocPy documentation: https://microsoft.github.io/bocpy/sphinx/index.html
- BocPy examples with descriptions: https://github.com/microsoft/bocpy/blob/main/examples/README.md
