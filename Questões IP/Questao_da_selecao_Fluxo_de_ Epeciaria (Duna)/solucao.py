#Decodigicador implementado recursivamente 
def decodificador(data,stop,aux,val_decodificado):
    
    if aux == stop:
        
        return val_decodificado
    
    else:
        simbolo = data[aux]
        
        if simbolo == 'ꖔ':
            val_decodificado +=1
            aux += 1
            
            return decodificador(data,stop,aux,val_decodificado)
        
        elif simbolo == '𐋀':
            val_decodificado +=2
            aux +=1
            return decodificador(data,stop,aux,val_decodificado)
        
        elif simbolo == 'ꖡ':
            val_decodificado +=3
            aux +=1
            return decodificador(data,stop,aux,val_decodificado)
        
        elif simbolo == '𐊾':
            val_decodificado += 5
            aux+= 1
            return decodificador(data,stop,aux,val_decodificado)
        
        elif simbolo == '𐊿':
            val_decodificado +=4
            aux += 1
            return decodificador(data,stop,aux,val_decodificado)
       
def decodificador_fremen(vibracao1,vibracao2):
    
    simbolos1 = list(vibracao1)
    simbolos2 = list(vibracao2)
    
    val_decodificado1 = decodificador(simbolos1,len(simbolos1),aux = 0,val_decodificado=0)
    val_decodificado2 = decodificador(simbolos2,len(simbolos2),aux = 0,val_decodificado = 0)
    
    return val_decodificado1,val_decodificado2

#Implementação recursiva do algoritmo de euclides    
def conversor_sismico(a,b):
    
    if b == 0:
        
        return a
    
    else:
        
        if a < b:
            a,b = b,a
            r = a % b 
            return conversor_sismico(b,r)
        
        else:
            r = a % b
            return conversor_sismico(b,r)

#Função de Alerta implementada recursivamente             
def alerta_VermedeAreia(horas,mdc=0):

    if mdc == 1 or horas == 0:
        
        if mdc == 1:
            razao = 'Verme de Areia'
            print(f'Onda sísmica provocada por: {razao}')
            return 'Verme de Areia'
        else:
            return 'Concluído'
              
    else:
        onda_sismica1 = input()
        onda_sismica2 = input()
    
        dados = decodificador_fremen(onda_sismica1,onda_sismica2)
        mdc = conversor_sismico(dados[0],dados[1])
        if mdc >= 2 and mdc <=6:
            razao = 'Areia de Percussão'
            print(f'Onda sísmica provocada por: {razao}')
            horas -= 1
            return alerta_VermedeAreia(horas)
        
        elif mdc >= 7  and mdc <= 10:
            razao = 'Atividade Humana'
            print(f'Onda sísmica provocada por: {razao}')
            horas -= 1
            return alerta_VermedeAreia(horas)
            
        elif mdc > 10:
            razao = 'Atividade Geológica'
            print(f'Onda sísmica provocada por: {razao}')
            horas -= 1
            return alerta_VermedeAreia(horas)
        
        else:
            horas -= 1
            return alerta_VermedeAreia(horas,mdc)
            
numb_dias = int(input())

for i in range(numb_dias):
    
    condicao_climatica = input()
    
    if condicao_climatica == 'Clima Ameno':
        horas = int(input())
        situacao = alerta_VermedeAreia(horas)
        
        if situacao == 'Verme de Areia':
            dia = i +1
            print(f'Dia {dia} | Situação: Colheita não finalizada| Razão: Verme de Areia')
        
        else:
            dia = i + 1
            print(f'Dia {dia} | situação: Colheita concluída')
    
    else:
        dia = i + 1
        print(f'Dia {dia} | Situação: Colheita não finalizada| Razão: Tempestade de Areia')