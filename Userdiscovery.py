import os
import wmi

w = wmi.WMI()

admins = None
#get list of administrators in the system
try:
    for group in w.Win32_Group():
        if group.Name == "Administrators":
            admins = [a.Name for a in group.associators(wmi_result_class="Win32_UserAccount")]
except Exception:
    pass

#list users accounts in the OS
for user in w.Win32_UserAccount():
    print("Username: %s" % user.Name)
    print("Administrators: %s" % (user.Name in admins))
    print("Disabled: %s" % user.Disabled)
    print("Local: %s" % user.LocalAccount)
    print("Password Changeable: %s" % user.PasswordChangeable)
    print("Password Expires: %s" % user.PasswordExpires)
    print("Password Required: %s" % user.PasswordRequired)
    print("\n")

#print Windows password policy
print("Password policy:")
print(os.system("net accounts"))