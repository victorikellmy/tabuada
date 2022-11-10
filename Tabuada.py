n1=int(input('fale um numero:'))
t=0
while t !=6:
    print('''        1-soma
        2-subtraça0
        3-multipicaçao
        4-divisao
        5-mudar numero
        6-sair da operaça0''')
    t = int(input('qual a opçao:'))
    if t == 1:
         print('{}+1={}\n'
               '{}+2={}\n' \
               '{}+3={}\n' \
               '{}+4={}\n' \
               '{}+5={}\n' \
               '{}+6={}\n' \
               '{}+7={}\n' \
               '{}+8={}\n' \
               '{}+9={}\n' \
               '{}+10={}\n'.format(n1, n1 + 1, n1, n1 + 2, n1, n1 + 3, n1, n1 + 4, n1, n1 + 5, n1, n1 + 6, n1, n1 + 7,
                                   n1, n1 + 8, n1, n1 + 9, n1, n1 + 10))
    elif t == 2:
         print('{}-1={}\n'
               '{}-2={}\n' \
               '{}-3={}\n' \
               '{}-4={}\n' \
               '{}-5={}\n' \
               '{}-6={}\n' \
               '{}-7={}\n' \
               '{}-8={}\n' \
               '{}-9={}\n' \
               '{}-10={}\n'.format(n1, n1 - 1, n1, n1 - 2, n1, n1 - 3, n1, n1 - 4, n1, n1 - 5, n1, n1 - 6, n1, n1 - 7,
                                   n1, n1 - 8, n1, n1 - 9, n1, n1 - 10))
    elif t == 3:
         print('{}*1={}\n'
               '{}*2={}\n' \
               '{}*3={}\n' \
               '{}*4={}\n' \
               '{}*5={}\n' \
               '{}*6={}\n' \
               '{}*7={}\n' \
               '{}*8={}\n' \
               '{}*9={}\n' \
               '{}*10={}\n'.format(n1, n1 * 1, n1, n1 * 2, n1, n1 * 3, n1, n1 * 4, n1, n1 * 5, n1, n1 * 6, n1, n1 * 7,
                                   n1, n1 * 8, n1, n1 * 9, n1, n1 * 10))
    elif t == 4:
         print('{}/1={}\n'
               '{}/2={}\n' \
               '{}/3={}\n' \
               '{}/4={}\n' \
               '{}/5={}\n' \
               '{}/6={}\n' \
               '{}/7={}\n' \
               '{}/8={}\n' \
               '{}/9={}\n' \
               '{}/10={}\n'.format(n1, n1 / 1, n1, n1 / 2, n1, n1 / 3, n1, n1 / 4, n1, n1 / 5, n1, n1 / 6, n1, n1 / 7,
                                   n1, n1 / 8, n1, n1 / 9, n1, n1 / 10))
    elif t== 5:
        print('mudar valor')
        n1=int(input('qual novo numero:'))
    elif t== 6:
        print('volte sempre!!')
    else:
        print('erro!!')