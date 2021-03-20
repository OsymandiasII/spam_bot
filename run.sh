#!/bin/bash

python3 -m venv spammer
source spammer/bin/activate
pip install -r requirements.txt
python3 spam3000.py
