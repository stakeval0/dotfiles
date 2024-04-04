#!/bin/bash

if groups | grep sudo >/dev/null ; then
  sudo apt install trash-cli && exit 0
fi
pip3 install trash-cli