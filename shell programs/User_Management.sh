#!/bin/bash
# Experiment No.: 8 - USER MANAGEMENT IN LINUX
# Aim: To understand and demonstrate user management in Linux

# 1. List out all users:
cat /etc/passwd | cut -d: -f1

# 2. Add a user:
sudo adduser mec1

# 3. Assign password to a user:
sudo passwd mec1

# 4. Access user configuration file:
cat /etc/passwd

# 5. Change user login name of a user:
sudo usermod -l mec2 mec1

# 6. Delete a user:
sudo userdel mec2
