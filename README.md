
# Projeto de Testes Automatizados com Selenium

Este projeto contém testes automatizados para a tela de login do sistema SIGAA da UFRRJ usando Selenium e unittest.


## Pré-requisitos

1. **Python**: Certifique-se de ter o Python instalado. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

2. **ChromeDriver**: Baixe o ChromeDriver compatível com a versão do seu navegador Chrome [aqui](https://sites.google.com/chromium.org/driver/downloads).

3. **Ambiente Virtual (Opcional, mas Recomendado)**: Crie um ambiente virtual para isolar suas dependências.
   ```bash
   python -m venv env
   source env/Scripts/activate  # Windows
   source env/bin/activate      # Linux/Mac
   ```

## Configuração

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/arielmdc/test-selenium.git
   cd test-selenium
   ```

2. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verifique o Caminho do ChromeDriver**:

   Certifique-se de que o nome de usuário e senha estão corretos dentro de `teste_sigaa.py`
   Certifique-se de que o arquivo `chromedriver.exe` está na pasta raiz do projeto.

## Executando os Testes

1. **Execute o Script de Teste**:
   ```bash
   python teste_sigaa.py
   ```

## Detalhes do Teste

O script `teste_sigaa.py` contém um teste para verificar o login no sistema SIGAA da UFRRJ. O teste preenche os campos de usuário e senha, clica no botão de login e verifica se o login foi bem-sucedido ao procurar o elemento de logout na página pós-login.