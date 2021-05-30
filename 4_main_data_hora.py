from datas import DatasBr

hoje = DatasBr()
print(hoje.momento_cadastro)  # data pela função datetime.today()
print("-----------------------------------")

print(hoje.mes_cadastro())  # apenas o mês
print("-----------------------------------")

print(hoje.semana_cadastro())  # apenas o dia da semana
print("-----------------------------------")

print(hoje)  # data formatada
print("-----------------------------------")

print(hoje.tempo_cadastro())

