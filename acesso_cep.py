import requests

class BuscaEndereco:
    def __init__(self, cep):  # passamos o nº do cep e vamos valida-lo
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido")

    def __str__(self):  # função para retornar o print formatado
        return self.format_cep()

    def cep_e_valido(self, cep):  # se o nº informado tiver 8 digitos, será um cep valido para seguir
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):  # formatar o cep - primeiros 5 digitos + hífen + da posição 5 até o final
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessa_via_cep(self):  # buscando o cep na api e retornando o bairro, cidade e estado
        url = requests.get("https://viacep.com.br/ws/{}/json/".format(self.cep))
        acesso = url.json()
        return (
            acesso['bairro'],
            acesso['localidade'],
            acesso['uf']
        )

