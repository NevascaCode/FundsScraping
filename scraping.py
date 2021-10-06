import requests
import csv
import yagmail
import smtplib
import requests.exceptions


from bs4 import BeautifulSoup
from configparser import ConfigParser
from rich.console import Console
from time import sleep

class WebScraping:
    def __init__(self, url):
        self.console = Console()
        self.configs = ConfigParser()
        self.configs.read("confs.ini")
        try:
            site = requests.get(url)
            self.html_puro = site.content

            self.iniciar_processos()
            if site.status_code != 200:
                self.console.print("🛑 [#ff5680]Não foi possível se conectar ao site! 🛑")

        except requests.exceptions.ConnectionError:
            self.console.print("🛑 [#ff5680]O site não existe ou está fora de ar! 🛑")

    def iniciar_processos(self):

        with self.console.status("🏂 [#d57bff]Raspando Dados...", spinner="dots"):
            dados = self.raspar_dados_do_site()
            self.console.print("🏂 [#fffc58]- [#00ff9c]Raspagem Concluida!")

        with self.console.status("📝 [#d57bff]Salvando dados...", spinner="dots"):
            self.salvar_dados_em_csv(dados)
            sleep(1)
            self.console.print("📝 [#fffc58]- [#00ff9c]Salvo com êxito!")

        with self.console.status("📨 [#d57bff]Enviando Email...", spinner="dots"):
            self.enviar_email()
            self.console.print("📨 [#fffc58]- [#00ff9c]Email Enviado!")

    @staticmethod
    def salvar_dados_em_csv(lista_dados:list):
        with open("FIIs.csv", "w", newline="") as arquivo_csv:
            fiis_escritor = csv.writer(arquivo_csv, dialect='excel')
            fiis_escritor.writerow(["Nome", "Setor", "Liquidez Diária", "P/VPA", "Valor Atual", "Patrimônio Liquido", "Dividendo","DY", "DY A.A", "Ativos"])
            for dados in lista_dados:
                fiis_escritor.writerow(dados)

    def raspar_dados_do_site(self) -> list:

        dados = []

        html = BeautifulSoup(self.html_puro, "html.parser")

        tabela = html.find("tbody")
        tabela_fundos = tabela.findAll("tr")
        for fundo in tabela_fundos:
            colunas = fundo.findAll("td")

            nome_fundo = colunas[0].find("a")
            if nome_fundo.text in self.configs['FundosConfig']['Fundos'] or self.configs['FundosConfig']['Fundos'] == '[]':
                setor_fundo = colunas[1]
                valor_fundo = colunas[2]
                dividendo_fundo = colunas[4]
                dividend_yield_fundo = colunas[5]
                p_vpa_fundo = colunas[18]
                dy_anual = colunas[12]
                liquidez_fundo = colunas[3]
                patrimonio = colunas[16]
                ativos_fundo = colunas[-1]

                dados.append([
                    nome_fundo.text,
                    setor_fundo.text,
                    liquidez_fundo.text,
                    p_vpa_fundo.text,
                    valor_fundo.text,
                    patrimonio.text,
                    dividendo_fundo.text,
                    dividend_yield_fundo.text,
                    dy_anual.text,
                    ativos_fundo.text
                ])

        return dados

    def enviar_email(self):

        try:
            email = yagmail.SMTP(self.configs['EmailConfig']['EmailPostador'], self.configs['EmailConfig']['SenhaPostador'])
            email.send(
                to = self.configs['EmailConfig']['EmailRemetente'],
                subject = 'FIIs',
                contents = 'Aqui está os FIIs que você tem interesse em saber!',
                attachments = 'FIIs.csv'
            )

        except smtplib.SMTPAuthenticationError:
            self.console.print("🛑 [#ff5680]Usuário ou senha inválidos! 🛑")


WebScraping("https://www.fundsexplorer.com.br/ranking")
