# P2 - FP // Miguel Regouga, 83530 // Paulo Reves, 83537 // Grupo 26



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                             #
#                             FUNCOES AUXILIARES                              #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# funcao que recebe um tuplo de tuplos e devolve um inteiro correspondente ao tamanho do maior tuplo
def maior_esp(t):
    tamanho_maximo = 0
    for i in range(len(t)):
        if len(t[i]) > tamanho_maximo:
            tamanho_maximo = len(t[i])
    return tamanho_maximo


# funcao que recebe um elemento do tipo tabuleiro e devolve uma lista contendo as coordenadas das celulas do tabuleiro que estao vazias
def tabuleiro_celulas_vazias(t):
    lista = []
    linhas = (tabuleiro_dimensoes(t))[0]
    colunas = (tabuleiro_dimensoes(t))[1]
    for l in range(1,linhas+1):
        for c in range(1,colunas+1):
            if tabuleiro_celula(t, cria_coordenada(l,c)) == 0: # caso o valor na celula seja zero, criacao de uma nova lista contendo a coordenada dessa celula
                lista = lista + [cria_coordenada(l,c)]      
    return lista
                        

# funcao que recebe um tuplo com a especificacao de uma linha/coluna e uma lista contendo os valores das celulas de uma linha/coluna e verifica se a linha ou coluna satisfaz as especificacoes.                      
def linha_completa (t, l):
    soma_dois = 0
    soma_dois_consecutivos = 0
    soma_especificacoes = 0
    f = 0
    for k in range(len(l)): # percorre a linha / coluna fornecida
        valor_linha = l[k]
        if valor_linha == 0: # caso o valor da coordenada seja 0, o tabuleiro ainda esta por preencher
            return False
        elif valor_linha == 2: # caso seja dois, verificamos se se repetem
            soma_dois = soma_dois + 1
            soma_dois_consecutivos = soma_dois_consecutivos + 1
        else:
            if soma_dois_consecutivos != 0: 
                if soma_dois_consecutivos != t[f]: # caso nao hajam dois numeros seguidos de acordo com as especificacoes, o tabuleiro esta incorreto
                    return False
                else:
                    f= f + 1 
                    soma_dois_consecutivos = 0
    for j in range(len(t)): # percorre o tuplo das especificacoes
        soma_especificacoes = soma_especificacoes + t[j]
    if soma_especificacoes != soma_dois:
        return False
    
    if soma_dois_consecutivos > 0:
        if soma_dois_consecutivos != t[-1]:
            return False 
        
    return True

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                             #
#                               TAD COORDENADA                                #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# CONSTRUTORES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# cria_coordenada: int x int -> coordenada
# recebe dois inteiros positivos, o primeiro correspondente a uma linha l e o segundo a uma coluna c, e devolve um elemento do tipo coordenada
def cria_coordenada (l, c):
    if isinstance (l, int) and l > 0 and isinstance (c, int) and c > 0:
        return (l, c)
    else:
        raise ValueError('cria_coordenada: argumentos invalidos')
    
    
# SELETORES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# coordenada_linha: coordenada -> inteiro
# recebe um elemento do tipo coordenada e devolve a respetiva linha
def coordenada_linha (l):
    return l[0]


# coordenada_coluna: coordenada -> inteiro
# recebe um elemento do tipo coordenada e devolve a respetiva coluna
def coordenada_coluna (c):
    return c[1]


# RECONHECEDORES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# e_coordenada: universal -> logico
# recebe um argumento e verifica se e do tipo coordenada
def e_coordenada (x):
    return isinstance (x, tuple) and len(x) == 2 and isinstance (x[0], int) \
    and x[0] > 0 and isinstance (x[1], int) and x[1] > 0


# TESTE # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# coordenadas_iguais: coordenada x coordenada -> logico
# recebe dois elementos do tipo coordenada e verifica se ambos correspondem a mesma celula do tabuleiro
def coordenadas_iguais (x, y):
    return x[0] == y[0] and x[1] == y[1]


# TRANSFORMADORES DE SAIDA # # # # # # # # # # # # # # # # # # # # # # # # # # #

# coordenada_para_cadeia: coordenada -> cad. caracteres
# recebe um elemento do tipo coordenada e devolve uma cadeia de caracteres que a representa
def coordenada_para_cadeia (x):
    return '(' + str(x[0]) + ' ' + ':' + ' '+ str(x[1]) + ')'



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                             #
#                                TAD TABULEIRO                                #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# CONSTRUTORES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# cria_tabuleiro: tuplo -> tabuleiro
# recebe um tuplo contendo as especificacoes das linhas e das colunas do tabuleiro e devolve um elemento do tipo tabuleiro
def cria_tabuleiro (t):
    if not (isinstance(t[0], tuple) and isinstance(t[1], tuple)) and len(t) == 2:
        raise ValueError("cria_tabuleiro: argumentos invalidos")
    linhas = t[0]
    colunas = t[1]
    numero_linhas = len(t[0])
    numero_colunas = len(t[1])
    tabuleiro = []
    
    # veficiacao dos argumentos
    for l in range(numero_linhas): # verificacao se os elementos dentro das especificacoes das linhas sao tuplos                               
        if not isinstance(linhas[l], tuple):
            raise ValueError("cria_tabuleiro: argumentos invalidos") # se nao se verifica esta condicao, emite-se um erro
        tuplozinhosl = linhas[l]
        for i in range(len(tuplozinhosl)): # caso sejam, verificacao se os valores dentro deles sao inteiros positivos
            if not ((isinstance(linhas[l][i], int)) and (linhas[l][i]>0)):
                raise ValueError("cria_tabuleiro: argumentos invalidos")
           
            for c in range(numero_colunas): # verificacao se os elementos dentro das especificacoes das colunas sao tuplos    
                if not isinstance(colunas[c], tuple):
                    raise ValueError("cria_tabuleiro: argumentos invalidos")
                tuplozinhosc = colunas[c]
                for p in range(len(tuplozinhosc)): # caso sejam, verificacao se os valores dentro deles sao inteiros positivos
                    if not ((isinstance(colunas[c][p], int)) and (colunas[c][p]>0)):
                        raise ValueError("cria_tabuleiro: argumentos invalidos")
                    
    for i in range(numero_linhas): # caso se verifiquem todas as condicoes, cria-se um tabuleiro vazio (preenchido com zeros)
        tabuleiro = tabuleiro + [[0] * numero_colunas]
    return [t[0], t[1], tabuleiro]
                         
        
# SELETORES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# tabuleiro_dimensoes: tabuleiro -> tuplo
# recebe um elemento do tipo tabuleiro e devolve um tuplo contendo dois elementos: o primeiro corresponde ao numero de linhas do tabuleiro e o segundo o de colunas
def tabuleiro_dimensoes (t):
    return (len(t[0])), len(t[1])


# tabuleiro_especificacoes: tabuleiro -> tuplo
# recebe um elemento do tipo tabuleiro e devolve um tuplo contendo dois elementos: o primeiro corresponde a especificacoes das linhas do tabuleiro e o segundo das colunas
def tabuleiro_especificacoes(t):
    return (t[0],t[1])


# tabuleiro_celula: tabuleiro x coordenada -> {0, 1, 2}
# recebe um elemento do tipo tabuleiro e um do tipo coordenada e devolve um inteiro entre 0 e 2; caso a celula esteja vazia, devolve 0; caso esteja em branco, devolve 1; caso esteja preenchida, devolve 2
def tabuleiro_celula(t, c):
    if e_coordenada(c) and e_tabuleiro(t) and coordenada_linha(c) <= (tabuleiro_dimensoes(t))[0] and coordenada_coluna(c) <= (tabuleiro_dimensoes(t))[1]:
        tabuleiro = t[2]
        linha = coordenada_linha(c)
        coluna = coordenada_coluna(c)
        linha_tabuleiro = tabuleiro[linha-1]
        coluna_tabuleiro = linha_tabuleiro[coluna-1]
        return coluna_tabuleiro
    raise ValueError('tabuleiro_celula: argumentos invalidos')


# MODIFICADORES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# tabuleiro_preenche_celula: tabuleiro x coordenada x {0, 1, 2} -> tabuleiro
# recebe um elemento do tipo tabuleiro, um elemento do tipo coordenada e um elemento do tipo inteiro, e modifica o tabuleiro, preenchendo a celula referente as coordenadas com o inteiro recebido
def tabuleiro_preenche_celula (t, c, e):
    if e_coordenada(c) and e_tabuleiro(t) and e in (0,1,2) and coordenada_linha(c) <= (tabuleiro_dimensoes(t))[0] and coordenada_coluna(c) <= (tabuleiro_dimensoes(t))[1]:
        tabuleiro = t[2]
        coord_linha = coordenada_linha(c)-1
        coord_coluna = coordenada_coluna(c)-1
        tabuleiro[coord_linha][coord_coluna] = e
        return t
    raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')


# RECONHECEDORES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# e_tabuleiro: universal -> logico
# recebe um elemento e verifica se se trata de um elemento do tipo tabuleiro
def e_tabuleiro (t):
    return len(t) == 3 and isinstance(t[0], tuple) and isinstance(t[1], tuple) and isinstance(t[2], list)


# tabuleiro_completo: tabuleiro -> logico
# recebe um elemento do tipo tabuleiro e verifica se este esta corretamente preenchido de acordo com as suas especificacoes
def tabuleiro_completo(t):
    if e_tabuleiro(t):       
        for l in range((tabuleiro_dimensoes (t))[0]):
            lista_l = []
            lista_c = []            
            for c in range((tabuleiro_dimensoes (t))[1]):
                elemento_l = tabuleiro_celula(t, cria_coordenada(l+1, c+1)) # percorre-se as listas e os valores destas no tabuleiro
                lista_l = lista_l + [elemento_l] # criacao de uma lista com os valores de uma lista do tabuleiro
                elemento_c = tabuleiro_celula(t, cria_coordenada(c+1, l+1)) # percorre-se as colunas e os valores destas no tabuleiro
                lista_c = lista_c + [elemento_c] # criacao de uma lista com os valores de uma coluna do tabuleiro
            if not (linha_completa(tabuleiro_especificacoes(t)[0][l], lista_l) and linha_completa(tabuleiro_especificacoes(t)[1][l], lista_c)): # caso os valores das linhas e das colunas do tabuleiro nao estejam de acordo com as respetivas especificacoes, o tabuleiro nao esta completo.
                    return False
        return True # caso contrario, o tabuleiro esta completo
    raise ValueError('tabuleiro_completo: argumentos invalidos')
        

                        

# tabuleiros_iguais: tabuleiro x tabuleiro -> logico
# recebe dois elementos do tipo tabuleiro e verifica se tem as mesmas especificacoes e se tem quadros com o mesmo conteudo
def tabuleiros_iguais (t1, t2):
    return tabuleiro_especificacoes(t1) == tabuleiro_especificacoes(t2) and t1[2]==t2[2]


# TRANSFORMADORES DE SAIDA # # # # # # # # # # # # # # # # # # # # # # # # # # #

# escreve_tabuleiro: tabuleiro -> {}
# recebe um elemento do tipo tabuleiro e escreve para o ecra a representacao externa de um tabuleiro
def escreve_tabuleiro(t):
    if not e_tabuleiro(t):
        raise ValueError('escreve_tabuleiro: argumento invalido')
    especificacoes = tabuleiro_especificacoes(t)
    especificacoes_linhas = especificacoes[0]
    especificacoes_colunas = especificacoes[1]
    dimensoes_tabuleiro = tabuleiro_dimensoes(t)
    dimensoes = dimensoes_tabuleiro[0]
    simbolos = {0: '?', 1: '.', 2: 'x'} # simbolos a preencher na representacao externa
    maior_espe_coluna= maior_esp(especificacoes_colunas) # chama a funcao auxiliar e guarda o valor do maior tuplo
    contador = maior_espe_coluna                                        
    st= ''
   
    # escrita das especificacoes das colunas
    while contador != 0:
        for b in range(len(especificacoes_colunas)):
            espes = especificacoes_colunas[b]
            if len(espes) >= contador:
                st = st + ' ' * 2 + str(especificacoes_colunas[b][-contador]) + ' '*2
            else:
                st = st+ ' ' * 5
        contador = contador - 1
        st = st + ' ' *2
        print (st)
        st= ''
        
    # escrita do tabuleiro    
    for l in range(dimensoes):
        for c in range(dimensoes):
            v = tabuleiro_celula(t,cria_coordenada(l+1, c+1)) # guarda o valor coorespondente da celula. e necessario que as coordenadas comecem em (1, 1)
            st = st+'[ '+ simbolos[v] + ' ]' # consoante o valor de v, escreve o caracter corresponde do dicionario simbolos, de acordo com a forma exterior
            
    # escrita das especificacoes das linhas 
        for p in range(len(especificacoes_linhas[l])):
            st= st + ' ' + str(especificacoes_linhas[l][p])
        if len(especificacoes_linhas[l]) < maior_esp(especificacoes_linhas):
            st= st + ' ' * maior_esp(especificacoes_linhas) # escrita dos espacos consoante o comprimento do maior tuplo das especificacoes
        st= st + '|'
        print (st) 
        st= ''
    print ()



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                             #
#                                  TAD JOGADA                                 #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# CONSTRUTORES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# cria_jogada: coordenada x {1, 2} -> jogada
# recebe um elemento do tipo coordenada e um inteiro com valor 1 ou 2 e devolve um elemento do tipo jogada
def cria_jogada (c, i):
    if not (e_coordenada(c) and i in (1, 2)):
        raise ValueError('cria_jogada: argumentos invalidos')
    return (c, i)


# SELETORES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# jogada_coordenada: jogada -> coordenada
# recebe um elemento do tipo jogada e devolve a coordenada respetiva
def jogada_coordenada(j):
    if not (e_jogada(j)):
        raise ValueError('jogada_coordenada: argumentos invalidos')
    return j[0]


# jogada_valor: jogada -> {1, 2}
# recebe um elemento do tipo jogada e devolve o valor respetivo
def jogada_valor(j):
    if not(e_jogada(j)):
        raise ValueError('jogada_valor: argumentos invalidos')
    return j[1]


# RECONHECEDORES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# e_jogada: universal -> logico
# recebe um argumento e verifica se este e do tipo jogada
def e_jogada(j):
    return isinstance (j, tuple) and len(j) == 2 and (j[1] in (1, 2)) and (e_coordenada(j[0]))


# TESTE # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# jogadas_iguais: jogada x jogada -> logico
# recebe dois argumentos do tipo jogada e verifica se correspondem a mesma jogada
def jogadas_iguais (j1, j2):
    if e_jogada(j1) and e_jogada(j2):
        return j1 == j2

# jogadas_para_cadeia: jogada -> cad. caracteres
# recebe um elemento do tipo jogada e devolve uma cadeia de caracteres que a represente
def jogada_para_cadeia (j):
    if e_jogada(j):
        return coordenada_para_cadeia(j[0]) + ' --> ' + str(j[1])
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                             #
#                             FUNCOES ADICIONAIS                              #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# le_tabuleiro: cad. caracteres -> tuplo
# recebe uma cadeia de caracteres correspondente ao nome do ficheiro com os dados de especificacao do jogo, e devolve um tuplo com as especificacoes do jogo
def le_tabuleiro(n):
    fich_tabuleiro = open(n, 'r') # abre o ficheiro em modo de leitura ('r')
    tabuleiro = fich_tabuleiro.read() # le todo o ficheiro
    fich_tabuleiro.close()
    return eval(tabuleiro) # devolve o tuplo correspondente as especificacoes das linhas e colunas


# pede_jogada: tabuleiro -> jogada
# recebe um elemento do tipo tabuleiro e devolve a jogada que o jogador pretende executar
def pede_jogada(t):
    dimensoes = tabuleiro_dimensoes(t)
    tamanho = dimensoes[0]
    c = input('Introduza a jogada\n- coordenada entre (1 : 1) e ' + '(' + str(tamanho) + ' ' + ':' + ' '+ str(tamanho) + ') ' + '>>' + ' ') # formato de introducao da coordenada
    v = input('- valor >> ') # formato de introducao do valor
    linha = int(c[1])
    coluna = int(c[5])
    valor = int(v)
    coordenadas = cria_coordenada(linha, coluna)
    if (coordenada_linha(coordenadas) <= tamanho and coordenada_coluna(coordenadas) <= tamanho): # caso a coordenada esteja dentro dos limites do tabuleiro, cria uma jogada
        return cria_jogada(coordenadas, valor)
    else:
        return False

# jogo_picross: cad. caracteres -> logico
# recebe uma cadeia de caracteres que representa o nome do ficheiro com a especificacao do tabuleiro e verifica se este esta corretamente completo ou nao. caso nao o esteja, ira pedir uma nova jogada ao jogador.
def jogo_picross (t):
    print('JOGO PICROSS')
    c = le_tabuleiro(t)
    tabuleiro = cria_tabuleiro(c)
    escreve_tabuleiro(tabuleiro)
    while len(tabuleiro_celulas_vazias(tabuleiro)) != 0: # enquanto houverem celuas vazias, continua-se a pedir uma jogaa
        jogada = pede_jogada(tabuleiro)
        if not jogada: # verificacao se a jogada e ou nao valida
            print('Jogada invalida.')        
        else: # caso seja, pede-se uma jogada
            c_jogada = jogada_coordenada(jogada)
            v_jogada = jogada_valor(jogada)
            tabuleiro_preenche_celula(tabuleiro, c_jogada, v_jogada)
            escreve_tabuleiro(tabuleiro)
    if tabuleiro_completo(tabuleiro): # caso a solucao seja encontrada
        print('JOGO: Parabens, encontrou a solucao!')
        return True
    else: # caso a solucao nao seja encontrada
        print('JOGO: O tabuleiro nao esta correto!')
        return False
