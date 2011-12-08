#!/usr/bin/env python

import os

SOURCE_DIR='/media/storage/ylmadmin/comptabilite'
DESTINATION_DIR = '/root/compta_git'

print('#!/bin/bash')

for f in os.listdir(SOURCE_DIR):
    if f.startswith('.'):
        continue
    line = 'gpg --batch --yes --always-trust --encrypt --recipient E7CE11EB --output %(dest)s/%(fname)s.gpg %(src)s/%(fname)s' % {'dest': DESTINATION_DIR, 'src': SOURCE_DIR, 'fname': f}
    print(line)
