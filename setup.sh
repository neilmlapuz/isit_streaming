#!/bin/bash

if [[ "$OSTYPE" == "darwin"* ]]; then
    echo 'MAC'
    wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz
    Package_name='geckodriver-v0.26.0-macos.tar.gz'
elif [[ "$OSTYPE" == "linux"* ]]; then
    echo 'LINUX'
    wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
    Package_name='geckodriver-v0.26.0-linux64.tar.gz'

fi

tar -xzvf $Package_name
rm -rf geckodriver-v* && mv ./geckodriver* scripts


