#!/usr/bin/bash

# Free repo
dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm

# Non-free repo
dnf install https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

# Explicitely enable openh264 library
dnf config-manager setopt fedora-cisco-openh264.enabled=1
