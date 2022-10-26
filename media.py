nota1=int(input("digite 1ª nota: "))
nota2=int(input("digite 2ª nota: "))
nota3=int(input("digite 3ª nota: "))
nota4=int(input("digite 4ª nota: "))
media=(nota1 + nota2 + nota3 + nota4)/4

#notas=(nota1,nota2,nota3,nota4)
#total=sum(media)
#media=total/4

if media>=6:
    print("aluno aprovado")
elif media<6 and media >=4:
    print("aluno de recuperação")
else:
    print("aluno reprovado")
