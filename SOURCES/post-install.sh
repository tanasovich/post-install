#!/usr/bin/bash

# Explicitely enable openh264 library
dnf config-manager setopt fedora-cisco-openh264.enabled=1

# Import GPG key for VS Code repo
rpm --import https://packages.microsoft.com/keys/microsoft.asc

# Provide commands to manage DNF repos
dnf install -y dnf-plugins-core
