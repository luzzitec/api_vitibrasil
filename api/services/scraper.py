# Importa a biblioteca 'requests' para fazer requisições HTTP
import requests

# Importa a biblioteca 'pandas' para manipular dados em formato tabular (como planilhas)
import pandas as pd

# Importa StringIO para simular um arquivo a partir de uma string (necessário para ler o conteúdo CSV em memória)
from io import StringIO

# Define a função que extrai os dados de produção a partir da URL da Embrapa
def extrair_tabela_producao():
    # Define a URL que aponta diretamente para o arquivo CSV de produção da Embrapa
    url_csv = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"

    # Define um cabeçalho para simular o acesso por um navegador, evitando bloqueios do servidor
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Faz a requisição HTTP (GET) para a URL, passando os cabeçalhos definidos
    response = requests.get(url_csv, headers=headers)

    # Verifica se a requisição foi bem-sucedida (código HTTP 200)
    if response.status_code == 200:
        # Converte o conteúdo de texto (CSV) para um DataFrame do pandas usando ponto e vírgula como separador
        df = pd.read_csv(StringIO(response.text), sep=";")
        return df  # Retorna o DataFrame com os dados estruturados
    else:
        # Em caso de erro na requisição, imprime o código de status
        print(f"Erro ao acessar o arquivo CSV. Status code: {response.status_code}")
        return None  # Retorna None se algo deu errado

# Executa este bloco apenas se o script for executado diretamente (e não importado por outro)
if __name__ == "__main__":
    # Executa a função para extrair os dados e armazena no DataFrame
    df = extrair_tabela_producao()
    
    # Verifica se os dados foram carregados com sucesso
    if df is not None:
        # Mostra as 5 primeiras linhas do DataFrame no terminal
        print(df.head())

        # Exporta os dados extraídos para um arquivo CSV local (para consulta e uso offline)
        df.to_csv("producao_embrapa.csv", index=False)

        # Mensagem para o usuário confirmando a exportação bem-sucedida
        print("Arquivo CSV exportado com sucesso.")