#!/bin/bash

dependencies=("pyfiglet" "random-word")

for package in "${dependencies[@]}"; do
    pip install "$package"
done