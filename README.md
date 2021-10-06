<h1 align="center">
  <img alt="FundsScraping" title="FundsScraping" src="./github/demo.gif", width="685", height="345" >
</h1>
<p align="center">Esse projeto foi feito em Python, utilizando a biblioteca BeautifulSoup para raspagem de dados.</p>
<p align="center">
  <a href="#sobre">Sobre</a> •
  <a href="#tecnologias">Tecnologias</a> •
  <a href="#pré-requisitos">Pré Requisitos</a> •
  <a href="#licença">Licença</a> •
  <a href="#autor">Autor</a>
</p>

## 📄 Sobre
  Robô feito em **Python**  para ser executado no terminal, com o proposito de **automatizar a coleta de dados de fundos imobiliários**.\
  Utilizando o **BeautifulSoup** para raspagem e o **yagmail** para o envio de email com o conteúdo.

## ⚙️ Tecnologias
  - [**Python 3.+**](https://www.python.org/)
  - [**BeautifulSoup**](https://pypi.org/project/beautifulsoup4/)
  - [**YagMail**](https://yagmail.readthedocs.io/en/latest/)
  - [**Rich**](https://rich.readthedocs.io/en/stable/introduction.html)

## 📜 Pré Requisitos
  Antes de continuar você precisa ter instalado em sua maquina as [**tecnologias**](#Tecnologias) citadas a cima.

## 🎲 Rodando o Aplicativo
### Baixar
 - Baixe o repositório com `git clone` ou diretamente no site do repositório.
    ```bash
    # Clone o repositório do projeto
    > git clone https://github.com/Kawdrin/FundsScraping.git
    # Entre na pasta do repositório
    > cd FundsScraping
    ```
### Configurações
 - Modifique o arquivo `confs.ini`, ele vai estar assim:
    ```
    [FundosConfig]
    Fundos = []

    [EmailConfig]
    EmailRemetente =  ...

    EmailPostador = ...
    SenhaPostador = ...
    ```
 - **EXEMPLO**\
 para mandar um email para **kawan.office@gmail.com** como os fundos **KISU11, VGHF11, MXRF11, VSLH11, HGLG11**, preciso conectar ao meu gmail de bot no caso usarei como exemplo **kawan.investimentos@gmail**, com a senha **pipocadenutella**.\
Ficara assim no arquivo:
    ```bash
    [FundosConfig]
    Fundos = [KISU11, VGHF11, MXRF11, VSLH11, HGLG11]

    [EmailConfig]
    EmailRemetente = kawan.office@gmail.com

    EmailPostador = kawan.investimentos@gmail
    SenhaPostador = pipocadenutella
    ```
 - Agora só executar:
    ```bash
    # Execute o app com python
    > python .\scraping.py
    ```

## 🔰 Licença
    Licença MIT

    Copyright (c) 2021 Kawan Henrique

    A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia
    deste software e arquivos de documentação associados (o "Software"), para lidar
    no Software sem restrição, incluindo, sem limitação, os direitos
    para usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e / ou vender
    cópias do Software, e para permitir que as pessoas a quem o Software é
    fornecido para fazê-lo, sujeito às seguintes condições:

    O aviso de direitos autorais acima e este aviso de permissão devem ser incluídos em todos
    cópias ou partes substanciais do Software.

    O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU
    IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO,
    ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA E NÃO VIOLAÇÃO. EM NENHUMA HIPÓTESE O
    AUTORES OU TITULARES DE DIREITOS AUTORAIS SÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTROS
    RESPONSABILIDADE, SEJA EM AÇÃO DE CONTRATO, DELITO OU DE OUTRA FORMA, DECORRENTE DE,
    FORA DE OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO
    PROGRAMAS.
## 👋 Autor
 ![Link Badge](https://img.shields.io/badge/-Feito%20POR-7AA5FF?&style=for-the-badge&logoColor=white)
  [![Link Badge](https://img.shields.io/badge/-Kawan%20Henrique%20Pereira-7AA5FF?&style=for-the-badge&logoColor=white&logo=linkedin)](https://www.linkedin.com/in/kawan-henrique-pereira/)
