#1.2.1

def limpa_texto(str):
    '''
    limpa_texto: cad. carateres → cad. carateres

    Esta função recebe uma cadeia de carateres qualquer e devolve a cadeia de carateres
    limpa que corresponde à remoção de carateres brancos.
    '''

    return ' '.join(str.strip().split())


#1.2.2

def corta_texto(str, n):
    '''
    corta_texto: cad. carateres × inteiro → cad. carateres × cad. carateres

    Esta função recebe uma cadeia de carateres e um inteiro
    que representam um texto limpo e uma largura de coluna respetivamente.

    São devolvidas duas subcadeias de carateres limpas "cortadas".
    '''

    if n < len(str):
        if str[n-1] == " ":              #se o n elemento, onde a string é cortada for um espaço
            s1, s2 = str[:n-1], str[n:]
            return s1, s2
        else:
            while str[n-1] != " ":
                n = n -1
            s1, s2 = str[:n-1], str[n:]
            return s1, s2
    else:
        return str, ""


#1.2.3

def insere_espacos(string, width):
    '''
    insere_espacos: cad. carateres × inteiro → cad. carateres

    Esta função recebe uma cadeia de carateres e um inteiro positivo
    que correspondem a um texto limpo e uma largura de coluna respetivamente

    É devolvida uma cadeia de carateres, cujo comprimento
    é igual à largura da coluna dada
    '''

    str_list = string.split()
    # Número de espaços totais que queremos ter quando a string não é vazia
    if len(string) != 0:
        n_espacos = (width - len(string)) + (len(str_list) - 1)
    # Número de espaços totais que queremos quando a string é vazia
    else:
        n_espacos = width

    # Se a string dada tiver duas ou mais palavras
    if len(str_list) >= 2:
        n_inserir = n_espacos // (len(str_list) - 1)    # Número de espaços a inserir entre duas palavras
        n_resto = (n_espacos % (len(str_list) - 1))    # Numero de espaços que sobram
        str_restos = ((n_inserir+1)*' ').join(str_list[:n_resto+1])
        str_final = (n_inserir*' ').join(str_list[n_resto+1:])
        res = str_restos + (n_inserir*' ') + str_final
        return res

    # Se a string dada tiver menos do que duas palavras
    else:
        sum = ""
        for i in range(n_espacos):
            sum += ' '

        return string + sum


#1.2.4

def justifica_texto(string, n):
    '''
    justifica_texto: cad. carateres × inteiro → tuplo

    Esta função recebe uma cadeia de carateres não vazia e um inteiro positivo
    que correspondem a um texto qualquer e uma largura de coluna.

    É devolvido um tuplo de cadeias de carateres justificadas, onde cada cadeia
    tem comprimento igual à largura da colunas através da insereção de espaços
    no meio das palavras.

    É verificada a validade dos seus argumentos, gerando um ValueError
    com a mensagem ‘justifica texto: argumentos invalidos’ caso necessário
    '''

    # Levantamento de Erros
    if type(string) != str or len(string) < 1 or type(n) != int:
        raise ValueError('justifica_texto: argumentos invalidos')
    str_list = string.split()
    for i in str_list:
        if len(i) > n:
            raise ValueError('justifica_texto: argumentos invalidos')

    str_copy = limpa_texto(string)
    list1, list2 = [], corta_texto(str_copy, n)
    list1.append(list2[0])

    # No caso do comprimento da string limpa for superior à largura da coluna
    if len(str_copy) > n:
        while True:
            # Dividir a str_copy em strings de n elementos (no máximo)
            list2 = corta_texto(list2[1], n)
            list1.append(list2[0])
            if len(list2[1]) < n:
                list1.append(list2[1])
                break

        res = []
        for el in list1[:-1]:
            res.append(insere_espacos(el, n))
        # Última linha do tuplo, que tem os espaços no fim
        if len(list1[-1]) != n:
            res.append(list1[-1] + (n-len(list1[-1]))*' ')
        else:
            res.append(list[-1])
        return tuple(res)

    # No caso do comprimento da string limpa for igual à largura da coluna
    elif len(str_copy) == n:
        return (str_copy,)

    # No caso do comprimento da string limpa for inferior à largura da coluna
    else:
        return (str_copy + (n-len(str_copy))*' ',)


#2.2.1

def calcula_quocientes(dict, n):
    '''
    calcula_quocientes: dicionário × inteiro → dicionário

    Esta função recebe um dicionário com os votos apurados num círculo
    e um inteiro positivo representando o número de deputados.

    É devolvido o dicionário com as mesmas chaves do dicionário argumento (correspondente a partidos)
    contendo a lista (de comprimento igual ao número de deputados) com os quocientes
    calculados através do método de Hondt ordenados em ordem decrescente.
    '''

    new_dict = {}
    for key in dict:
        list = []
        for i in range(n):
            list.append(dict[key] / (i + 1))
            new_dict[key] = list

    return new_dict


#2.2.2

def atribui_mandatos(dct, n):
    '''
    atribui_mandatos: dicionário × inteiro → lista

    Esta função recebe um dicionário com os votos apurados num círculo e um inteiro
    que representa o número de deputados,

     É devolvida a lista ordenada de tamanho igual ao número de deputados contendo
     as cadeias de carateres dos partidos que obtiveram cada mandato
    '''

    new_dct = calcula_quocientes(dct, n)
    list, res = [], []
    for key in new_dct:
        for valor in new_dct[key]:
            list.append(valor)
    list_n = sorted(list, reverse=True)[:n] #Criação de uma nova lista ordenada em forma decrescente com n elementos
    partidos = sorted(dct.items(), key=lambda x:x[1]) #Ordenação dos partidos com base nos votos totais


    for votos in list_n:
        for el in partidos:
            if votos in new_dct[el[0]]:
                res.append(el[0])
                new_dct[el[0]].remove(votos)


    # É devolvida a lista com n elementos
    return res[:n]

#2.2.3

def obtem_partidos(dct):
    '''
    obtem_partidos: dicionário → lista

    Esta função recebe um dicionário com a informação sobre as eleições num território

     É devolvida a lista por ordem alfabética com o nome de todos os partidos que participaram nas eleições.
    '''

    lst = []
    for key in dct:
        for partido in dct[key]['votos']:
            if partido not in lst:
                lst.append(partido)

    return sorted(lst)


#2.2.4

def obtem_resultado_eleicoes(dct):
    '''
    obtem_resultado_eleicoes: dicionário → lista

    Esta função recebe um dicionário com a informação sobre as eleiões
    num terriório com vários círculos eleitorais

    É devolvida a lista ordenada de comprimento igual número total de partidos
    com os resultados das eleições. Cada elemento da lista é um tuplo de tamanho 3
    contendo o nome de um partido, o número total de deputados obtidos e o número total de votos obtidos.
    Esta funçãao verifica a validade dos seus argumentos, gerando um
    ValueError com a mensagem ‘obtem resultado eleicoes: argumento invalido’
    caso o seu argumento não seja válido.
    '''

    # Levantamento de erros
    error_message = 'obtem_resultado_eleicoes: argumento invalido'
    if type(dct) != dict:
        raise ValueError(error_message)
    for key, value in dct.items():
        if type(key) != str:
            raise ValueError(error_message)
        if type(value) != dict:
            raise ValueError(error_message)
        new_dct = value
        if len(new_dct) != 2:
            raise ValueError(error_message)
        if 'deputados' not in new_dct or 'votos' not in new_dct:
            raise ValueError(error_message)
        if type(new_dct['deputados']) != int:
            raise ValueError(error_message)
        if type(new_dct['votos']) != dict or len(new_dct['votos']) == 0:
            raise ValueError(error_message)
        for letter, number in (new_dct['votos']).items():
            if type(letter) != str or len(letter) == 0:
                raise ValueError(error_message)
            if type(number) != int:
                raise ValueError(error_message)

    res = []
    n_deputados = []

    for partido in obtem_partidos(dct):
        soma_deputados = 0
        soma_votos = 0
        for key in dct:
            soma_deputados += atribui_mandatos(dct[key]['votos'], dct[key]['deputados']).count(partido)
            if partido in dct[key]['votos']:
                soma_votos += dct[key]['votos'][partido]
        res.append((partido, soma_deputados, soma_votos,))


    res = sorted(res, key=lambda x:(-x[1], -x[2]))
    return res


#3.2.1

def produto_interno(tup1, tup2):
    '''
    produto_interno: tuplo × tuplo → real
    '''

    sum = 0
    for i in range(len(tup1)):
        sum += tup1[i] * tup2[i]
    return float(sum)


#3.2.2

def verifica_convergencia(tup1, tup2, tup3, n):
    '''
    verifica_convergencia: tuplo × tuplo → real
    '''

    for c in range(len(tup1)):
        sum = 0
        for i in range(len(tup2)):
            sum += tup1[c][i] * tup3[i]
        if abs(sum - tup2[c]) >= n:
            return False

    return True


#3.2.3

def retira_zeros_diagonal(tup1, tup2):
    '''
    retira_zeros_diagonal: tuplo × tuplo → tuplo × tuplo
    '''

    # tornar o tuplo de tuplos numa listas de listas
    lines = [list(x) for x in tup1]
    # Adicionar o coeficiente a cada elemento da lista
    lst = [lines[x] + [tup2[x]] for x in range(len(lines))]
    diagonal = [lst[i][i] for i in range(len(lines))]
    c = 0

    while not all(diagonal):
        for c in range(len(lines)):
            if lst[c][c] == 0:
                for i in range(len(lines)):
                    if (lst[i] != lst[c] and lst[i][c] != 0):
                        lst[c], lst[i] = lst[i], lst[c]
                        break

            diagonal = [lst[i][i] for i in range(len(lines))]


    list_c, new_list = [], []
    for x in lst:
        list_c.append(x.pop(-1))
    res = (tuple([tuple(x) for x in lst]),) + (tuple(list_c),)

    return res


#3.2.4

def eh_diagonal_dominante(tup):
    '''
    eh_diagonal_dominante: tuplo → booleano
    '''

    for x in range(len(tup)):
        lst = list(range(len(tup)))
        lst.remove(x)
        sum = 0
        for i in lst:
            sum += abs(tup[x][i])
        if abs(tup[x][x]) < sum:
            return False

    return True


#3.2.5

def resolve_sistema(tup1, tup2, num):
    '''
    resolve_sistema: tuplo × tuplo × real → tuplo
    '''

    # Levantamento dos Erros
    arg_invalido = 'resolve_sistema: argumentos invalidos'
    diag_nao_dominante = 'resolve_sistema: matriz nao diagonal dominante'
    if type(tup1) != tuple or type(tup2) != tuple or type(num) != float or num < 0:
        raise ValueError(arg_invalido)
    for tup in tup1:
        if type(tup) != tuple:
            raise ValueError(arg_invalido)
        for n in tup:
            if type(n) != int:
                raise ValueError(arg_invalido)
    #Verificar se tup1 é matriz quadrada
    n_linhas = len(tup1)
    for tup in tup1:
        if len(tup) != n_linhas:
            raise ValueError(arg_invalido)
    for n in tup2:
        if type(n) != int:
            raise ValueError(arg_invalido)
    if not eh_diagonal_dominante(tup1):
        raise ValueError(diag_nao_dominante)

    tup1 = retira_zeros_diagonal(tup1, tup2)[0]
    tup2 = retira_zeros_diagonal(tup1, tup2)[1]
    listx = [0 for i in range(len(tup1))]

    while not verifica_convergencia(tup1, tup2, tuple(listx), num):
        for i in range(len(tup1)):
            listx[i] = listx[i] + (tup2[i] - produto_interno(tup1[i], tuple(listx)))/tup1[i][i]

    return tuple(listx)






