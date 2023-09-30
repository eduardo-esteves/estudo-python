from helper.print_msg_section import print_msg_section

x = ("Gabriel", "Danny", "Arthur", "Danny")

print(iter(x))

for name in x:
    print(name)

print_msg_section('Interando sobre os valores com range')

for i in range(len(x)):
    print(x[i])
