import os

from helper.print_msg_section import print_msg_section


# CPBA 281

print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)

print_msg_section('Limpando o terminal com clear')

# Set the TERM environment variable to a common terminal type.
os.environ['TERM'] = 'xterm'
os.system("/usr/bin/clear")
os.system('echo "Hello World"')
