#!/bin/bash

alembic upgrade heads &
python ./main.py
