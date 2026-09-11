# Tracing Regions Introduction

## Setup

```
bash ./setup.bash
```

## Virtual environment

```
source .venv/bin/activate
```

## Running Examples

```
PYTHON_REGION_GRAPH=region-error.md python ./examples/bank.py
```

The `PYTHON_REGION_GRAPH` environment variable will create a markdown document with the traced object graph, if closing a region failed.
