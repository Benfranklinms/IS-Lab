#!/bin/bash
# Experiment No.: 9 - FILE PERMISSIONS IN LINUX
# Aim: To understand and demonstrate file and directory permission management

# 1. Display File Permissions:
ls -l

# 2. Create File and Directory:
touch file.txt
mkdir mydir

# 3. Add Permissions (Symbolic Mode):
chmod u+x file.txt
chmod g+w file.txt
chmod o+r file.txt

# 4. Remove Permissions (Symbolic Mode):
chmod u-x file.txt
chmod g-w file.txt
chmod o-r file.txt

# 5. Assign Permissions to All Users:
chmod a+rwx file.txt

# 6. Set Exact Permissions (Symbolic Mode):
chmod u=rwx,g=rx,o=r file.txt

# 7. Change Permissions Using Numeric (Octal) Mode:
chmod 777 file.txt
chmod 755 file.txt
chmod 644 file.txt

# 8. Change Directory Permissions:
chmod 755 mydir
chmod 700 mydir

# 9. Verify Changes:
ls -l file.txt
ls -ld mydir
