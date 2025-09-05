#!/usr/bin/bash

# Provide commands to manage DNF repos
dnf install dnf-plugins-core

# Add repo
dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
