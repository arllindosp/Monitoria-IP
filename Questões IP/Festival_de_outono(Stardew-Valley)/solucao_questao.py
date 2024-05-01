#codigo da questão

dim_bancada = input().split(' ')#--> Primeiro recebemos a string que contém as dimenões da matriz 
M,N = int(dim_bancada[0]), int(dim_bancada[2])#--> Em seguida as salvamos em variavies 
bancada = [[0 for _ in range(N)] for _ in range(M)]#--> Construindo uma matriz constituida inteiramente por zeros

#--> Laço que usaremos para alocar os itens em suas posições iniciais
N = int(input())
for i in range(N):
    dados = input().split(' ')
    atratividade,coordenadas = int(dados[0]), dados[1]
    i,j = int(coordenadas[1:2]),int(coordenadas[3:4])#--> Usamos o slicing para fatiar os números da string
    bancada[i][j] = atratividade

#--> Laço que usaremos para efetuar as operações instruidas pelo oráculo
stop = False
while not stop:
    operacao = input()
    
    if operacao == 'Fim':#--> Se a operação for igual a fim, o ciclo se encerra
        stop = True
    
    elif operacao == 'Remover':
        
        menos_atrativo = float('inf')#--> Uso de um valor infinito para comparar com os valores da matriz e ir salvando-os
        linha,coluna = 0,0 
        num_linhas = len(bancada)
        num_colunas = len(bancada[0])
        
        #--> Laço que usaremos para buscar o elemento de menor valor
        for i in range(num_linhas):
            for j in range(num_colunas):
                atual = bancada[i][j]
                
                if atual == 0:#--> Se o elemento analisado for zero nada será feito, pois zero denota posições vazias
                    pass
                else:
                    #--> Se o elemento for menor do que o que já está salvo, ele é substituido pelo armazenado pela variavel menos_atrativo
                    if atual < menos_atrativo:
                        menos_atrativo = atual
                        linha = i
                        coluna = j
        
        bancada[linha][coluna] = 0 #--> A remoção consiste em atribuir zero para posição em que o elemento originalmete se encontrava     
        
    elif operacao == 'Permutar':
        
        dados = input().split(' ')
        par_1,par_2 = dados[0],dados[1]
        #--> Salvando as coordenadas dos elementos que devem ser permutados
        i1,j1 = int(par_1[1:2]),int(par_1[3:4])
        i2,j2 = int(par_2[1:2]),int(par_2[3:4])
        
        #--> Permutando-os
        bancada[i1][j1],bancada[i2][j2] = bancada[i2][j2],bancada[i1][j1]
            
    elif operacao == 'Transposição':
        
        bancada_primordial = bancada #--> Primeiro salvamos a bancada original numa variavel
        linhas = len(bancada_primordial[0])#--> As linhas da transposta serão igual ao total de colunas da matriz primordial
        transposta = [[] for i in range(linhas)]#--> Construímos uma matriz de listas vazias com quantidade de linhas igual á de colunas da matriz primordial

        for linha in bancada_primordial:#--> Vamos acessar cada uma das linhas da matriz primordial
            posicao = 0
            
            for a in linha:#--> vamos acessar cada um dos elementos de cada linha da matriz originária
                transposta[posicao].append(a)#--> Em seguida adicionamos cada elemento em uma linha diferrente da transposta
                posicao += 1
        #--> Esse procedimento nos permitirá inverter as linhas pelas colunas
        bancada = transposta #--> Por fim, nossa bancada virá a transposta

#Print da Matriz
print('Atual Arranjo:')#--> Primeiro o print da frase
num_linhas = len(bancada)
num_colunas = len(bancada[0])

#--> Laço para acessar cada um dos elementos
for l in range(num_linhas):
    
    for k in range(num_colunas):
        print(bancada[l][k], end= '')
        if k < num_colunas - 1:#--> Se o elemento a ser printado nao for o ultimo, entao printamos um espaço após ele
            print(" ", end="")#--> Mas se não for, então não printamos o espaço 
    
    if l == num_linhas -1:#--> Se estivermos na ultima linha, a quebra de linha não é printada
        pass
    else:#--> Caso contrário, será printada
        print()