from acesso_cep import BuscaEndereco
# com api acesso_cep podemos trazer e validar toda as informações de um cep

cep = 14020620
objeto_cep = BuscaEndereco(cep)  # valida se um cep tem 8 digitos
print(objeto_cep)
print("-----------------------------------")

cep_invalido = 14020621
objeto_cep_invalido = BuscaEndereco(cep_invalido) # valida se um cep tem 8 digitos
print(objeto_cep_invalido)
print("-----------------------------------")

bairro, localidade, uf = objeto_cep.acessa_via_cep()  # aqui validaremos se é de fato um cep existem
print("{}, {} - {}".format(bairro, localidade, uf))
print("-----------------------------------")

bairro, localidade, uf = objeto_cep_invalido.acessa_via_cep()  # aqui dará erro pois é um cep fictício
print("{}, {} - {}".format(bairro, localidade, uf))