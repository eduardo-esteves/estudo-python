
num_500 = None
i = 1

while num_500 != True:

    if (i >= 500):
        num_500 = True

    par = (i % 2) == 0

    if (par):
        print(f"O número atual é {i}")

    i+= 1
