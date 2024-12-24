#!/usr/bin/env bash
cd "$(dirname "$0")"
poetry install --no-root && poetry run python main.py
