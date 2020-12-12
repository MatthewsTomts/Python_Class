print('-_' * 13)
print('Analisador de Triângulos')
print('_-' * 13)
reta1 = float(input('Digite o comprimento do primeiro segmento: '))
reta2 = float(input('Digite o comprimento do segundo segmento: '))
reta3 = float(input('Digite o comprimento do terceiro segmento: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('\033[32;1mEsses segmentos podem formar um triângulo.\033[m')
    if reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print('Eles formam um triângulo Escaleno')
    elif reta1 == reta2 and reta2 == reta3:
        print('Eles formam um triângulo Equilátero')
    else:
        print('Eles formam um triângulo Isósceles')
else:
    print('\033[31;1mEsses segmentos não podem formar um triângulo.')
