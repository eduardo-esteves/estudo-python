from datetime import datetime, timedelta


# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
# CPBA 276

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

diferenca = data_fim - data_inicio
more_ten_days = timedelta(days=10)

print(data_fim > data_inicio)
print(diferenca.days, diferenca.seconds)
print(datetime.now() + more_ten_days)
