# CPBA 273
def soma(x: float, y: float) -> float:
    return x + y

def main() -> None:
    if __name__ == '__main__':
        print(__name__)

# Verifico se o script principal que está sendo executado no momento
# é este, em caso positivo ele será o main e com isso a função main()
# será executada, porém se estiver sendo executada através de outro script
# via importação então este script não será o principal main.
if __name__ == '__main__':
    main()
