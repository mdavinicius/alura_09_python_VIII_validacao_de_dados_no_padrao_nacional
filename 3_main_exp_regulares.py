from telefone import TelefoneBr
import re

# criar um padrão de para encontrar endereços de email no meio de strings
padrao_email = "\w{1,50}@\w{1,10}.\w{2,3}.\w{2,3}"  # padrão contém caracteres entre 1 e 50 + @ + novamente caracteres entre 1 a 10 + '.' + 2 ou 3 caracteres + '.' + 2 ou 3 caracteres
texto = "teste123 triloko@gmail.com.br teste456 789teste"
procura_email = re.search(padrao_email, texto)  # com a função search() da biblioteca re, passamos um padrão e qual será o texto em que iremos procurar esse padrão
print(procura_email.group())
print("-----------------------------------")

# criar um padrão de para encontrar nº de telefone no meio de strings
padrao_telefone = "[0-9]{2}[0-9]{4,5}[0-9]{4}"  # padrão contém nºs de 0 a 9 que devem aparecer 2x + nºs que devem aparecer 4 ou 5x + nºs que devem aparecer 4x
telefone = "515151 5151 16991338552 515151 5151 "
procura_telefone = re.findall(padrao_telefone, telefone)
print(procura_telefone)
print("-----------------------------------")

# com a classe TelefoneBr vamos formatar um telefone no padrão BR: +55(DDD)XXXX-XXXX
telefone = "551691338552"
telefone_objeto = TelefoneBr(telefone)
print(telefone_objeto)