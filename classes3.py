
#aspas duplas 
print ("Hello, World!") 
# aspas simples
print ('Hello, World!')
#escape 
print("Hello \"World\"")
#aparecer aspas
print (1, '"Hello, World!"')
print (2, "'Hello, World!'")

#tipos de int e float 
#int e considerado qualquer tipo de numero, seja positivo ou negativo 
#float e considerado numeros com ponto flutuante (casas decimais, issacional) 
#funcao 'type' mostra o tipo do objeto 
print (type (10 == 10)) #sim -> True -> Verdadeiro 

#aula 5
# Tipo de dado bool (boolean)
# Ao questionar algo em um programa, 
# so existem duas respostas possiveis:
# sim (True) ou nao (false).
# existem varios operadores para "questionar".
# Dentre eles o ==, que e um operador logico que 
# questiona se um valor e igual o outro
print (10 == 10) #sim -> True -> Verdadeiro 
print (10== 11) #nao -> Falso -> False

# conversao de tipos, coercao 
# type convertion, typecasting, coercion 
#é o ato de converter em um tipo em outro 
#tipos imutaveis e primitivos:
str, int, float, bool 

print (1 + 1)
print ('a' + 'b')
# print ('1' +1) -> erro 
print (int ('1') + 1)
print (float ('1') + 1)

#uso: nome_variavel = expressao 
nome_sobrenome = 'rafaele campos dos santos'
idade = 2025-1999 
print (nome_sobrenome, idade)

#exemplos 
nome = 'Rafaele'
idade = 25
maior_de_idade = idade >= 21
print ('Nome: ', nome, 'Idade', idade, maior_de_idade)

nome = 'rafaele '
sobrenome = ' dos santos '
idade = 26
ano_de_nascimento = 2025 - idade
maior_de_idade = idade >= 18 
altura_em_metros = 1.68 
print ('Nome:', nome)
print ('Sobrenome:', sobrenome)
print ('Idade:', idade)
print ('Ano de nascimento:', ano_de_nascimento)
print ('É maior de idade?', maior_de_idade)
print ('Altura em metros:', altura_em_metros)

#matematica 
adicao = 10 + 10 
print ('Adiçao', adicao)

subtracao = 10 - 5 
print ('Subtraçao', subtracao)

multiplicacao = 10 * 5
print ('Multiplicacao', multiplicacao)

divisao = 10/3 #retorno sempre vai ser em float (casas decimais)
print ('Divisao', divisao)

divisao_inteira = 10//3
print ('Divisao inteira', divisao_inteira)

exponenciacao = 2 ** 10 
print ("Exponenciação", exponenciacao)

modulo = 25 % 5 #resto da divisao 
print ('Módulo', modulo)

print (10 % 8 == 0)
print (16 % 8 == 0)
print (10 % 2 == 0)
print (15 % 2 == 0)

# matematica exemplo 
a_dez_vezes = 'A' * 10 
tres_vezes_rafa = 'Rafa' * 3
print (a_dez_vezes)
print (tres_vezes_rafa)

#  1. (n  + n)
# 2. **
# 3. * / // % 
# 4. + - 
conta_1 = (1 + 1) ** (5 + 5) #7 
print (conta_1)

a = 'AAA'
b = 'B'
c = 1.1
string ='a={} b={} c={:.2f}'
formato = string .format (a,b,c)
print (formato)

# nome = input ('Qual seu nome? ')
# print (f'O seu nome é: {nome}')

numero_1 = int (input ('Digite um numero: '))
numero_2 = int (input ('Digite outro numero: '))
print (f'A soma dos numeros e: {numero_1 + numero_2}')

# se / se nao se / se nao 
# sempre if vem primeiro e else vem por ultimo, o elif nao e obrigatorio, 
# mas se for usar o elif vem sempre depois do if e antes do else 


entrada = input ('voce quer "entrar" ou "sair"? ')
if entrada == 'entrar': 
    print ('Voce entrou no sistema')

    print ('9i3874397')
elif entrada == 'sair': 
    print ('Voce saiu do sistema')

else: 
    print ('voce nao digitou entrar e nem sair')

"""
Operadores de comparacao (relacionais)
OP          Significado            Exemplo (true)
>           maior                  2 > 1    
>=          Maior ou igual         2 >= 2
<           Menor                  1 < 2
<=          menor ou igual         2 <= 2 
==          igual                  'a'== 'a'
!=          diferente               'a' != 'b'
"""
maior = 2 > 1    
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2 
igual = 'a'== 'a'
diferente = 'a' != 'b'
print (diferente)


primeiro_valor = input ('digite um valor: ')
segundo_valor = input ('digite outro valor: ')

if primeiro_valor > segundo_valor:
    print (f'{primeiro_valor} valor e maior que o ' f'{segundo_valor} valor')

else:
    print ('o segundo valor e maior que o primeiro')