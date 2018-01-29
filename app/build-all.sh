#!/bin/bash
# Force build posiapp.
# WARNING: This deletes existing files!
echo "* building QT UI file..."
python3 setup.py build_ui
echo "* installing dependencies..."
pip3 install -e .
echo "run: python3 -m posiapp"
