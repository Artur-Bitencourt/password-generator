import random
import string
import os

def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_numeros=True, incluir_especiais=True):
    caracteres = string.ascii_lowercase
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def salvar_senha(nome, senha):
    with open("senhas_salvas.txt", "a") as arquivo:
        arquivo.write(f"{nome}: {senha}\n")
    print("Senha salva com sucesso!")

def carregar_senhas():
    if not os.path.exists("senhas_salvas.txt"):
        print("Nenhuma senha salva ainda.")
        return
    with open("senhas_salvas.txt", "r") as arquivo:
        print("\nSenhas salvas:")
        print(arquivo.read())

def menu():
    while True:
        print("\n=== Gerador de Senhas Seguras ===")
        print("1. Gerar nova senha")
        print("2. Exibir senhas salvas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            tamanho = int(input("Digite o tamanho da senha (padrão 12): ") or 12)
            incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
            incluir_numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
            incluir_especiais = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'
            
            senha_gerada = gerar_senha(tamanho, incluir_maiusculas, incluir_numeros, incluir_especiais)
            print("\nSenha gerada:", senha_gerada)
            
            salvar = input("Deseja salvar essa senha? (s/n): ").strip().lower()
            if salvar == 's':
                nome = input("Digite um nome para essa senha: ")
                salvar_senha(nome, senha_gerada)
        
        elif opcao == "2":
            carregar_senhas()
        
        elif opcao == "3":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
