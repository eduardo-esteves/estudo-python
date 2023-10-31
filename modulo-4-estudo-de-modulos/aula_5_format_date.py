from datetime import datetime, timedelta


# CPBA 277

br_fmt = '%d/%m/%Y %H:%M'
database_fmt = '%Y-%m-%d %H:%M:%S'

# Dada uma data recebida em uma string com formato BR e queremos fazer calculos
# de diferenças entre datas, primeiro devemos criar uma data a partir desta string
database_dt = datetime.strptime('2022-04-20 09:30:30', database_fmt)
br_dt = datetime.strptime('15/04/2022 02:00', br_fmt)

# Após transformar em um objeto data podemos fazer os cálculos
diferenca = database_dt - br_dt

# A partir do momento que tenho um objeto data posso fazer a
# formatação do jeito que eu desejar
print(br_dt, database_dt, br_dt.strftime(br_fmt), diferenca, sep="\n")
