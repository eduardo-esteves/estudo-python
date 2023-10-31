from datetime import datetime
from pytz import timezone

from helper.print_msg_section import print_msg_section

# CPBA 275

data_str = '2022-04-21 07:00:01'
data = datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S')

data_h_sp = datetime.now(timezone('America/Sao_Paulo'))
data_h_manaus = datetime.now(timezone('America/Manaus'))
time_stamp_sp = data_h_sp.timestamp()

print_msg_section('Conferindo o tipo datetime object')
print(type(data))
print(data, data_h_sp, data_h_manaus, time_stamp_sp, sep="\n")


