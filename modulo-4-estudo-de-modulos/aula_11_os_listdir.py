import os

# CPBA 283

base_dir = os.path.dirname(__file__)
modulo_3_dir = os.path.join(base_dir, '..', 'modulo-3-poo')

if os.path.exists(modulo_3_dir):
    for file in os.listdir(modulo_3_dir):
        print(file)
