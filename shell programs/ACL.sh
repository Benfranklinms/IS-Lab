#!/bin/bash
# Experiment No.: 10 - ACCESS CONTROL LIST IN LINUX
# Aim: To understand and demonstrate the usage of Access Control Lists (ACLs)
# using getfacl and setfacl commands.

# 1. Create a sample file
touch my_test_file

# 2. Retrieve the default ACL entries
getfacl my_test_file

# 3. Add read and write permissions for user 'student'
setfacl -m u:student:rw my_test_file

# 4. Verify the modified ACL entries
getfacl my_test_file

# 5. Add read permissions for a group (e.g., 'staff')
setfacl -m g:staff:r my_test_file

# 6. Verify the group ACL entry
getfacl my_test_file

# 7. Remove the ACL entry for the specific user
setfacl -x u:student my_test_file

# 8. Retrieve and verify the removal
getfacl my_test_file

# 9. Remove all ACL entries
setfacl -b my_test_file

# 10. Final verification
getfacl my_test_file
