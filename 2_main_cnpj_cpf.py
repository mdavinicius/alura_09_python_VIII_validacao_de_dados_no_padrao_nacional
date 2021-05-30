from cpf_cnpj import Documento

# printando um cpf e cnpj formatado e verificando se são reais

# cpf_invalido = Cpf(11111111122) # vai dar erro ao tentar imprimir pois é um cpf inválido
print("-----------------------------------")

cpf = Documento.cria_documento(38135199880)
print(f"CPF: {cpf}")
print("-----------------------------------")

cnpj = Documento.cria_documento(35379838000112)
print("CNPJ: {}".format(cnpj))
