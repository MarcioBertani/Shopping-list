lista = []

while True:
    opcao = input('i[nseri [a]pagar [l]istar: ')

    # Inserir.
    if opcao == 'i': # Aparecer opcao 'i'
        valor = input('Valor: ') # Aparecer a opcao 'Valor'
        lista.append(valor) # Para adicionar um item ao valor
    
    # Apagar.
    elif opcao == 'a': # Aparecer opcao 'a'
        try:
            # Exbiir a mensagem para apagar o item da lista
            indice = int(input('Escolha o indice para apagar: '))
            del lista[indice] # comando para apagar o item
        except(ValueError, IndexError): # para tratar erros de
            # valores e indices.
            print('Indice invalido. ') 

    # Listar
    elif opcao == 'l': # Aparecer opcao 'l', usuario resolveu 
        # listar os itens.
        if lista: # verifica se a lista nao esta vazia.
            for i, valor in enumerate(lista): # serve para gerar 
                # pares de indice
                print(i, valor) # imprimir a lista apos usuario
                # pedir para listar itens.
        else: # caso a lista esteja vazia, a mensagem 'Nada para 
            # listar' sera exibida.
            print('Nada para listar. ')
    else: # caso o usuario digite alguma coisa invalida.
        print('Escolha invalida.')