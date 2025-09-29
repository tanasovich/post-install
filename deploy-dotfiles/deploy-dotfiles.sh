#!/bin/bash

set -euo pipefail

if [ -z "${1:-}" ]; then
    echo "Git repo URL is mandatory!"
    exit -1
fi

if [ ! -f "$HOME/.bashrc" ]; then
    echo "Is not possible to create dotfile alias!"
    exit -2
fi

echo -n "Adding alias to .bashrc... "

cat << EOF >> $HOME/.bashrc
# Manage dotfiles using specialised alias

alias dotfiler='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

EOF

echo "OK"

echo -n "Ignoring Git directory to avoid recursion conflicts... "

echo ".dotfiles" >> $HOME/.gitignore

echo "OK"

echo -n "Cloning dotfiles from remote Git repository... "

git clone --bare $1 $HOME/.dotfiles

echo "OK"
