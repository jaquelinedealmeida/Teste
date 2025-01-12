import json

def dados():
    
    dados_json = '''
    {
        "faturamento_diario": [
            {"dia": 1, "valor": 2000},
            {"dia": 2, "valor": 4500},
            {"dia": 3, "valor": 1000},
            {"dia": 4, "valor": 3000},
            {"dia": 5, "valor": 500},
            {"dia": 6, "valor": 7500},
            {"dia": 7, "valor": 2000},
            {"dia": 8, "valor": 5000},
            {"dia": 9, "valor": 1500},
            {"dia": 10, "valor": 2000}
        ]
    }
    '''
    
    dados = json.loads(dados_json)
    return dados['faturamento_diario']

def calculo_faturamento(faturamento_diario):
    faturamento_validos = [faturamento['valor'] for faturamento in faturamento_diario if faturamento['valor'] > 0]
    
    if not faturamento_validos:
        return "Não há faturamento válido para calcular as métricas."
    
    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)
    
    media_faturamento = sum(faturamento_validos) / len(faturamento_validos)
    
    dias_acima_media = sum(1 for valor in faturamento_validos if valor > media_faturamento)
    
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "media_faturamento": media_faturamento,
        "dias_acima_media": dias_acima_media
    }

def main():
    faturamento_diario = dados()
    
    resultados = calculo_faturamento(faturamento_diario)
    
    if isinstance(resultados, str):
        print(resultados)
    else:
        print(f"Menor faturamento: R${resultados['menor_faturamento']}")
        print(f"Maior faturamento: R${resultados['maior_faturamento']}")
        print(f"Média de faturamento: R${resultados['media_faturamento']:.2f}")
        print(f"Número de dias com faturamento superior a média: {resultados['dias_acima_media']}")

if __name__ == "__main__":
    main()