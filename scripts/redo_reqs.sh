#!/bin/bash

echo "Installing pipreqs..."
pip install pipreqs

echo "Generating requirements.txt..."
pipreqs . --force

echo "The requirements.txt has been updated."