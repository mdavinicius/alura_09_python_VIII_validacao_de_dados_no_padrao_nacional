import re
# com a função search() da biblioteca re, passamos um padrão e qual será o texto em que iremos procurar esse padrão

class TelefoneBr:
    def __init__(self, telefone):  # precisamos passar o número de telefone e ele será validado se encaixa no nosso padrão
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto")

    def __str__(self):  # função para retornar o print formatado
        return self.format_numero()

    def valida_telefone(self, telefone):  # validação do padrão que buscamos junto ao objeto
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):  # formatação do nosso padrão
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        numero_formatado = "+{}({}){}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return numero_formatado

