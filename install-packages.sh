#!/usr/bin/bash

if [ ! -f assets/package-list.txt ]; then
    echo "List of installation packages is not found!"
    exit -1
fi

dnf install -y $(cat assets/package-list.txt)
