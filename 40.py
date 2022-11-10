from datetime import date
nascimento= int(input('Qual o ano em que você nasceu'))
ano_atual= date.today().year
idade= ano_atual-nascimento
sexo =(input('Digite se você M para mulher H para homem'))
print('Quem  nasceu em {} tem {} anos em {}'.format(nascimento,idade, ano_atual))
if sexo == 'M':
   print('Você não precisa se alistar')
elif  idade == 18:
   print('Esta na hora de se alistar')
elif idade > 18:

   print('Ja passou {} anos, da idade para de alistar'.format(idade - 18))
elif idade < 18:
   print('Falta {} anos para se alistar'.format(18 - idade))
