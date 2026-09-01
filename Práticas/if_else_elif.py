import subprocess

def par_impar():
    numero = int(input("\nDigite um numero: "))
    
    if numero < 0:
        print("Apenas numeros com valor acima de 0!\n")
        return
        
    if numero % 2 == 0:
        print(f"Numero {numero} é par\n")
    else:
        print(f"Numero {numero} é impar\n")
        
def idade_categoria():
    idade = int(input("Digite sua idade: "))
    
    if idade < 0:
        print("Apenas idades acima de 0 são aceitas!\n")
        return
    
    if idade > 0 and idade <= 12:
        print(f"Categoria criança, com base na sua idade {idade}\n")
    elif idade >= 13 and idade <= 18:
        print(f"Categoria adolescente, com base na sua idade {idade}\n")
    else:
        print(f"Categoria adulto, com base na sua idade {idade}\n")
        
def autenticacao_login():
    nome = input("Digite seu nome: ")
    senha = int(input("Digite sua senha: "))
    
    if nome == "victor" and senha == 102030:
        print(f"Bem vindo senhor {nome}\n")
    else:
        print("Login invalido, verifique nome e senha!\n")
        
def coordenadas():
    x = int(input("Digite a coordenada de x: "))
    y = int(input("Digite a coordenada de y: "))
    
    if x > 0 and y > 0:
        print(f"Primeiro quadrante, com x: {x} e y: {y}\n")
    elif x < 0 and y > 0:
        print(f"Segundo quadrante, com x: {x} e y: {y}\n")
    elif x < 0 and y < 0:
        print(f"Terceiro quadrante, com x: {x} e y: {y}\n")
    elif x > 0 and y < 0:
        print(f"Quarto quadrante, com x: {x} e y: {y}\n")

def iniciar_sistema():
    iniciar = int(input("Para iniciar o sistema, digite 1 ou 0 (1 == sim e 0 == não): "))
    
    if iniciar == 1:
        par_impar()
        idade_categoria()
        autenticacao_login()
        coordenadas()
    else:
        subprocess.run(["cmd", "/c", "cls"])
        print("Sistema não iniciado, tenha um otimo dia!")
        
iniciar_sistema()