# Introduction

A simple utility for pacman, the package manager for Arch Linux

This project offers:
1. a python script that automatically list all explicitly installed packages outside of base and base-devel group
2. a pacman hook that runs after installation/removal of packages

# Dependency

python3.6

# Usage

1. place the backup-pacman.py file in /usr/bin/
2. place the update-pkg-list.hook file in /etc/pacman.d/hooks/
3. the package list is saved to ~/package-list

# Hack

Feel free to change
1. the list of excluded packages
2. the path of the backup file
3. the path of the backup-pacman.py script (you will need to change the exec line in update-pkg-list.hook accordingly)
