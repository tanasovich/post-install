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

cat << EOF >> $HOME/.bashrc
# Manage dotfiles using specialised alias

alias dotfiler='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

EOF

echo ".dotfiles" >> $HOME/.gitignore

git clone --bare $1 $HOME/.dotfiles
