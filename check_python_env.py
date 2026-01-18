import getpass
import sys

print('This job is running as "{}".'.format(getpass.getuser()))
print(sys.executable, sys.version_info)
