#!/usr/bin/env bash

set -euo pipefail

echo "Running setup..."

mkdir -p .deps

# CPython
git clone --branch tregion-main --single-branch --depth 1 git@github.com:fxpl/cpython.git .deps/cpython
cd .deps/cpython
./configure --with-pydebug --with-mimalloc --without-pymalloc --with-assertions --with-undefined-behavior-sanitizer
make -j8
cd ../..

# BocPy
git clone --branch tracing-regions --single-branch --depth 1 git@github.com:fxpl/bocpy.git .deps/bocpy

# Virtual Environment
.deps/cpython/python.exe -m venv .venv
.venv/bin/pip install .deps/bocpy --verbose
