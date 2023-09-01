#!/usr/bin/env bash

read -rp "Enter a filename: " filename

echo "# pylint: disable=all
\"\"\"
\"\"\"


def func(n, star='*'):
    pass


n = 5
func(n)" > "$filename.py"

vim "$filename.py"
