class Televisao_3:
    def __init__(self, marca, ano, preco, n_canais):
        self.marca = marca
        self.ano = ano
        self.preco = preco
        self.n_canais = n_canais

    def __str__(self):
        return f"Marca:{self.marca}, Ano:{self.ano}, Preço:{self.preco}, Números de Canais:{self.n_canais}"


t1 = Televisao_3('LG', 2023, 12.500, 120)
# Crio um novo objeto apontando para o mesmo valor já alocado em memória de t1 (Valor por referência)
t2 = t1

# A partir de agora tudo que modifico no objeto t1 vai refletir em cópias por referências feitas desse objeto como t2
t1.ano = 2024

print(f"{t1=}")
print(f"{t2=}")

print()

print(t1)
print(t2)
