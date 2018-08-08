#! /usr/bin/env python3

import subprocess
import re
import os

base_group = ['bash', 'bzip2', 'coreutils', 'cryptsetup', 'device-mapper', 'dhcpcd', 'diffutils', 'e2fsprogs', 'file', 'filesystem', 'findutils', 'gawk', 'gcc-libs', 'gettext', 'glibc', 'grep', 'gzip', 'inetutils', 'iproute2', 'iputils', 'jfsutils', 'less', 'licenses',
              'linux', 'logrotate', 'lvm2', 'man-db', 'man-pages', 'mdadm', 'nano', 'netctl', 'pacman', 'pciutils', 'perl', 'procps-ng', 'psmisc', 'reiserfsprogs', 's-nail', 'sed', 'shadow', 'sysfsutils', 'systemd-sysvcompat', 'tar', 'texinfo', 'usbutils', 'util-linux', 'vi', 'which', 'xfsprogs']
base_devel = ['autoconf', 'automake', 'binutils', 'bison', 'fakeroot', 'flex', 'gcc',
              'groff', 'libtool', 'm4', 'make', 'patch', 'pkgconf', 'sudo', 'systemd']

file_path = os.environ['HOME'] + '/package-list'


def delete_base_packages(item):
    if item in base_group:
        return False
    elif item in base_devel:
        return False
    else:
        return item


read_list = subprocess.Popen(
    ['pacman', '-Qqe'], stdout=subprocess.PIPE)
pacman_list = re.split('\s', str(subprocess.check_output(
    ['grep', '\w'], stdin=read_list.stdout), 'UTF-8'))

my_pkg_list = list(filter(lambda x: x, map(
    delete_base_packages, pacman_list)))

try:
    with open(file_path, 'r') as f:
        existing_pkg = list(map(lambda x: re.sub("\n", "", x), f.readlines()))
except FileNotFoundError:
    existing_pkg = []

with open(file_path, 'w') as f:
    for i in my_pkg_list:
        f.write(i + '\n')
        if i not in existing_pkg:
            print('pkg ' + i + ' recorded')

# print removed pkg info
removed_pkg = (i for i in existing_pkg if i not in my_pkg_list)
for i in removed_pkg:
    print('pkg ' + i + ' has been removed')
