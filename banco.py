sistema_ligado = True

reserva = 0.0
historico = []

while(sistema_ligado == True):
    
    print("""
          --------------------------------------------------------------------------------------------------------
          ||             Bem vindo a sua conta bancária! Qual ação gostaria de fazer neste momento?             ||
          ||----------------------------------------------------------------------------------------------------||
          ||-- (Se quiser voltar para esta tela, envie letras que não sejam as que são pedidas pelo programa) --||
          ||----------------------------------------------------------------------------------------------------||
          ||-------------|| D = Depositar || S = Saque || E = Extrato || P = Parar programa ||------------------||
          --------------------------------------------------------------------------------------------------------
          """)
    
    resposta = input()

    if(resposta.upper() == "D"):
        print("""
              --------------------------------------------------------------------------------------
              || Qual quantia gostaria de depositar?  (Digite 0 para voltar para a tela principal) ||
              --------------------------------------------------------------------------------------
              """)
        
        quantia = input()
    
        try:
            quantia = float(quantia)
            if quantia <= 0:
                continue
            else:
                print(f"""\nVocê está desejando depositar R${quantia}. Tem certeza que quer proceder?
                                    S = Sim                N = Não\n""")
                
                resposta = input()

                if(resposta.upper() in ["SIM", "S"]):
                    reserva += quantia
                    quantia = "%0.2f" % quantia
                    historico.append(f"DR${quantia}")
                else:
                    continue

        except ValueError:
            print("""
                  ------------------------------------------------------------------------------------------------
                  || A entrada não foi reconhecida como sendo um número positivo.  Por favor insira outro valor ||
                  ------------------------------------------------------------------------------------------------
                  || ----------------------- Aperte qualquer tecla + Enter para continuar ----------------------||
                  ------------------------------------------------------------------------------------------------
                  """)
            resposta = input()
 
    elif(resposta.upper() == "S"):
        print("""
              --------------------------------------------------------------------------------------
              || Qual quantia gostaria de retirar?    (Digite 0 para voltar para a tela principal) ||
              --------------------------------------------------------------------------------------
              """)
        
        quantia = input()

        try:
            quantia = float(quantia)
            if quantia <= 0:
                continue
            elif(quantia > reserva):
                print("""
                  ------------------------------------------------------------------------------------------------
                  || A quantia colocada é maior que a sua reserva bancária atual. Por favor use um valor menor. ||
                  ------------------------------------------------------------------------------------------------
                  || ----------------------- Aperte qualquer tecla + Enter para continuar ----------------------||
                  ------------------------------------------------------------------------------------------------
                  """)
            
                resposta = input()
                continue
            else:
                print(f"""\nVocê está desejando retirar R${quantia}. Tem certeza que quer proceder?
                                    S = Sim                N = Não\n""")
                
                resposta = input()

                if(resposta.upper() in ["SIM", "S"]):
                    reserva -= quantia
                    quantia = "%0.2f" % quantia
                    historico.append(f"SR${quantia}")
                else:
                    continue

        except ValueError:
            print("""
                  ------------------------------------------------------------------------------------------------
                  || A entrada não foi reconhecida como sendo um número positivo.  Por favor insira outro valor ||
                  ------------------------------------------------------------------------------------------------
                  || ----------------------- Aperte qualquer tecla + Enter para continuar ----------------------||
                  ------------------------------------------------------------------------------------------------
                  """)
            resposta = input()
    
    elif(resposta.upper() == "E"):
        print("""
              ------------------------------------------------------------------------------------------------------------
              || C = Ver extrato completo || D = Ver extrato (Apenas os depósitos) || S = Ver extrato (Apenas os saques) ||
              ------------------------------------------------------------------------------------------------------------
              """)
        
        resposta = input()

        if(resposta.upper() == "C"):
            for item in historico:
                if(item.startswith("D")):
                    print(f"Depósito: {item[2:]}\n")
                elif(item.startswith("S")):
                    print(f"Saque: {item[2:]}\n")
        
        elif(resposta.upper() == "D"):
            for item in historico:
                if(item.startswith("D")):
                    print(f"Depósito: {item[2:]}\n")

        elif(resposta.upper() == "S"):
            for item in historico:
                if(item.startswith("S")):
                    print(f"Saque: {item[2:]}\n")
        
        else:
            continue

        print(f"\nReserva bancária atual: R${reserva:.2f}")
    
    elif(resposta.upper() == "P"):
        sistema_ligado = False

    else:
        continue
    
    resposta = ":P" # Resetando a resposta