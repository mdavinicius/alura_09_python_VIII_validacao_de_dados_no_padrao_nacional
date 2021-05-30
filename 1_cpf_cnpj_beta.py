from validate_docbr import CPF, CNPJ
# validade_docbr é uma api que permite validar se os CPFs e CNPJs são reais

class CpfCnpj:
    def __init__(self, documento, tipo_documento):  # precisamos passar o número e dizer se é 'cpf' ou 'cnpj'
        documento = str(documento)
        self.tipo_documento = tipo_documento
        if tipo_documento == "cpf":
            if self.validador_de_cpf(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF Inválido!!")
        elif tipo_documento == "cnpj":
            if self.validador_de_cnpj(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ Inválido!!")
        else:
            raise ValueError("Documento Inválido!!")

    def validador_de_cpf(self, cpf):  # chama classe CPF e usamos a função validade() da api validade_docbr para validar o cpf
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos errada!!")

    def __str__(self):  # função para retornar o print formatado
        if self.tipo_documento == "cpf":
            return self.formatar_cpf()
        elif self.tipo_documento == "cnpj":
            return self.formatar_cnpj()

    def formatar_cpf(self):  # com a mask() da api, formatamos o CPF no padrão xxx.xxx.xxx-xx
        mascara = CPF()
        return mascara.mask(self.cpf)

    def validador_de_cnpj(self, cnpj):  # chama classe CNPJ e usamos a função validade() da api validade_docbr para validar o cpf
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos errada!!")

    def formatar_cnpj(self):  # com a mask() da api, formatamos o CNPJ no padrão xx.xxx.xxx/xxxx-xx
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    # def formatar_cpf(self):          # forma arcaica de formatar o cpf
    #     fatia_um = self.cpf[:3]
    #     fatia_dois = self.cpf[3:6]
    #     fatia_tres = self.cpf[6:9]
    #     fatia_quatro = self.cpf[9:]
    #
    #     return (
    #         "{}.{}.{}-{}".format(
    #             fatia_um,
    #             fatia_dois,
    #             fatia_tres,
    #             fatia_quatro
    #         )
    #     )