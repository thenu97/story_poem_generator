#!/bin/bash
source /var/lib/jenkins/.bashrc

python3 -m coverage run --source=. -m pytest ~/Service_1/tests/testing.py
python3 -m coverage report -m