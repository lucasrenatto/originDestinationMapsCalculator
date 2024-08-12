import pandas as pd
import googlemaps

# Chave da API do Google Maps
chave_api = 'SUA CHAVE GOOGLE'
gmaps = googlemaps.Client(key=chave_api)

caminho_arquivo = 'caminhoDoSeuArquivo.xlsx'
dados = pd.read_excel(caminho_arquivo)


def calcular_distancia_tempo(origem, destino):
    try:
        resultado = gmaps.distance_matrix(origem, destino, mode='driving')
        distancia = resultado['rows'][0]['elements'][0]['distance']['text']
        duracao = resultado['rows'][0]['elements'][0]['duration']['text']
        return distancia, duracao
    except Exception as e:
        print(f"Erro ao calcular a distância para {origem}: {e}")
        return None, None

for index, row in dados.iterrows():
    origem = f"{row['Cidade']}, {row['UF']}"
    destino = row['Endereço']
    distancia, duracao = calcular_distancia_tempo(origem, destino)
    
    dados.at[index, 'Distância'] = distancia
    dados.at[index, 'Tempo'] = duracao


novo_caminho_arquivo = 'resultado.xlsx'
dados.to_excel(novo_caminho_arquivo, index=False)

print(f"Arquivo gerado com sucesso: {novo_caminho_arquivo}")
