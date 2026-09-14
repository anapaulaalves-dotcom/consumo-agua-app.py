def classificar_consumo():
    # Solicitação e tratamento do tipo de imóvel
    tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()
    
    # Validação do consumo mensal
    try:
        consumo = float(input("Digite o consumo mensal de água em m³: "))
        if consumo < 0:
            print("O consumo não pode ser negativo.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, insira um número decimal para o consumo.")
        return

    # Regras de negócio para classificação
    if tipo_imovel == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
    elif tipo_imovel == "apartamento" and consumo < 10:
        print("Consumo econômico – excelente controle de água!")
    elif tipo_imovel in ["apartamento", "casa"] and consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

if __name__ == "__main__":
    classificar_consumo()
