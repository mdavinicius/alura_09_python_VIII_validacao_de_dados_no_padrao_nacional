from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()  # com datetime.today() puxamos a data completa (ano-mes-dia) com hora (hora-min-seg)

    def __str__(self):  # função para retornar o print formatado
        return self.data_formatada()

    def mes_cadastro(self):  # vamos trazer apenas o mês do datetime.today()
        meses_do_ano = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month -1  # usamos month() e -1 porque a lista começa na posição 0
        return meses_do_ano[mes_cadastro]

    def semana_cadastro(self):  # vamos trazer o dia da semana de hoje
        dias_da_semana = [
            "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira",
            "sexta-feira", "sábado", "domingo"
        ]
        semana_cadastro = self.momento_cadastro.weekday()  # com o weekday() pega o nº o dia da semana, começando com segunda = 0
        return dias_da_semana[semana_cadastro]

    def data_formatada(self):  # formatar a data no padrão BR
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y - %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=365)) - self.momento_cadastro
        return tempo_cadastro