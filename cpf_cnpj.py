from validate_docbr import CPF, CNPJ
# validade_docbr é uma api que permite validar se os CPFs e CNPJs são reais

class Documento:

    @staticmethod
    def cria_documento(documento):  # criamos uma classe que pelo tamanho da objeto saberá escolher se será CNPJ ou CPF, cortamos a necessidade de mencionar isso explicitamente
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos incorreta!!")

class DocCpf:
    def __init__(self, documento):
        if self.validador_de_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!!")

    def __str__(self):  # função para retornar o print formatado
        return self.formatar_cpf()

    def validador_de_cpf(self, documento):  # chama classe CPF e usamos a função validade() da api validade_docbr para validar o cpf
        validador = CPF()
        return validador.validate(documento)

    def formatar_cpf(self):  # com a mask() da api, formatamos o CPF no padrão xxx.xxx.xxx-xx
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.validador_de_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!!")

    def __str__(self):  # função para retornar o print formatado
        return self.formatar_cnpj()

    def validador_de_cnpj(self, documento):  # chama classe CNPJ e usamos a função validade() da api validade_docbr para validar o cpf
        validador = CNPJ()
        return validador.validate(documento)

    def formatar_cnpj(self):  # com a mask() da api, formatamos o CNPJ no padrão xx.xxx.xxx/xxxx-xx
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
