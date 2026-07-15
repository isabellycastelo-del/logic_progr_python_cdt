'''
COMO FRITAR BATATA FRITA;

Passo 1: Pegar uma panela funda, para que o óleo nâo caia e seja mais fácil de manusear a batata.
Passo 2: Pegar o óleo de cozinha e colocar o óleo em relação ao tamanho da porção de batata (normalmente 500ml a 1L)
Passo 3: Com o óleo já na panela você vai colocar a panela na boca do fogão que voê deseja usar, e então liga-lá
Passo 4: Espere o óleo esquentar, mas tomando cuidado para não queima-ló.
Passo 5: Enquanto o óleo esquenta pegue o saco de batata e o abra.
Passo 6: Quando o óleo estiver no ponto de fervura ideal, jogue uma pequena quantidade de batata(a batata tem que ficar coberta pelo óleo,
então não utrapasse a linha do óleo).
Passo 7: Deixe a batata fritando até ela ficar dourada!
Passo 8: Assim que a batata estiver dourado e durinha pegue um utencílio de sua preferência (como garfo ou espátula).
Passo 9: Deixe a batata frita tirando o óleo em um pote ou prato (ou recipiente de sua preferência) com papel toalha para que não fique oleosa.
passo 10: Coloque sal ou o tempero ou molho de sua preferência



'''



def fritar_batata(tipo_porção):
    print('🍟 Como fritar uma porção de batata - Simples e rápido')
    print('1. Pegar uma panela funda, para que o óleo nâo caia e seja mais fácil de manusear a batata.')
    print('2. Pegar o óleo de cozinha e colocar o óleo em relação ao tamanho da porção de batata (normalmente 500ml a 1L)')
    print('3. Com o óleo já na panela você vai colocar a panela na boca do fogão que voê deseja usar, e então liga-lá')
    print('4. Espere o óleo esquentar, mas tomando cuidado para não queima-ló.')
    print('5. Enquanto o óleo esquenta pegue o saco de batata e o abra.')
    print('6. Quando o óleo estiver no ponto de fervura ideal, jogue uma pequena quantidade de batata(a batata tem que ficar coberta pelo óleo, então não utrapasse a linha do óleo).')
    print('7. Deixe a batata fritando até ela ficar dourada!')
    print('8. Assim que a batata estiver dourado e durinha pegue um utencílio de sua preferência (como garfo ou espátula).')
    print('9. Deixe a batata frita tirando o óleo em um pote ou prato (ou recipiente de sua preferência) com papel toalha para que não fique oleosa.')
    print('10. Coloque sal ou o tempero ou molho de sua preferência')

    if tipo_porção.lower() == 'tempo':
        resultado = 'Batata mole e crua'
    
    else:
        resultado = 'Batata no ponto ideal'

    return resultado

minha_batata = fritar_batata ('tempo')
print(f'Minha batata está: {minha_batata}')