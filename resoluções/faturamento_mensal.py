
def calcular_percentuais(faturamento):
    total_faturamento = sum(faturamento.values())
    
    percentuais = {}
    for estado, valor in faturamento.items():
        percentual = (valor / total_faturamento) * 100
        percentuais[estado] = percentual
    
    return percentuais, total_faturamento

def main():
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    percentuais, total_faturamento = calcular_percentuais(faturamento)
    

    print(f"Valor total de faturamento: R${total_faturamento:.2f}")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")
    
if __name__ == "__main__":
    main()