#!/usr/bin/env bash

TESTING=true ENVIRONMENT=test PYTHONPATH=.:backend-exercise/ mamba -f documentation test/unit/$1