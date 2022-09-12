#!/bin/bash

cd /Users/Amagi/Desktop/jLock # your project directory
source ./venv/bin/activate # venv

unset HTTP_PROXY HTTPS_PROXY ALL_PROXY http_proxy https_proxy all_proxy # unset proxies 
python3 src/entrypoints/refresh_session.py
