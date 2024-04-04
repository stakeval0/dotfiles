#!/bin/bash

if groups | grep sudo >/dev/null ; then
  read -p "Want to install Zsh in System? (y/n): " answer
  case $answer in
    [yY]* ) sudo apt install -y zsh && exit 0;;
    [nN]* ) echo "Please manually install for user."; exit 1;;
    * ) echo "invalid input: $answer. expected y or n";;
  esac
fi
