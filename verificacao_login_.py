import os
import time

def limpar_tela():
    # Limpa o console no iOS/Linux/Mac ou Windows
    os.system('clear' if os.name != 'nt' else 'cls')
    # Se o os.system nC#o funcionar no CodeRunner, imprimimos linhas em branco
    print("\n" * 20)

def mostrar_tela_login():
    limpar_tela()
    print("=" * 40)
    print("{:^40}".format("SISTEMA DE LOGIN"))
    print("=" * 40)
    print("\nDigite suas credenciais para acessar o designer:\n")
    
    usuario = input("UsuC!rio: ")
    senha = input("Senha: ")
    
    if usuario == "admin" and senha == "1234":
        print("\n[+] Login bem-sucedido! Carregando painel...")
        time.sleep(1.5)
        mostrar_designer_principal()
    else:
        print("\n[-] Erro: UsuC!rio ou senha incorretos!")
        input("\nPressione ENTER para tentar novamente...")
        mostrar_tela_login()

def mostrar_designer_principal():
    while True:
        limpar_tela()
        # Menu Superior / CabeC'alho do Designer
        print("=" * 60)
        print("{:^60}".format("PAINEL PRINCIPAL - DESIGNER PCS-LOGIN"))
        print("=" * 60)
        
        # Layout Simulado (Menu Lateral + ConteC:do)
        print(" [Menu]        |  Bem-vindo de volta, Admin!")
        print(" --------------| -------------------------------------------")
        print(" 1. Dashboard  |  EstatC-sticas de Acesso Hoje:")
        print(" 2. RelatC3rios |  ")
        print(" 3. Configs    |  +---------------------------------------+")
RIOS ATIVOS: 1,248               |")
        print("               |  |  STATUS DO BANCO: Online              |")
        print("               |  +---------------------------------------+")
        print("=" * 60)
        
        opcao = input("Escolha uma opC'C#o do menu (1-4): ")
        
        if opcao == "1":
            print("\nCarregando dados do Dashboard...")
            time.sleep(1)
        elif opcao == "2":
            print("\nGerando relatC3rios do sistema...")
            time.sleep(1)
        elif opcao == "3":
            print("\nAbrindo configuraC'C5es do designer...")
            time.sleep(1)
        elif opcao == "4":
            print("\nSaindo do sistema... AtC) logo!")
            break
        else:
            print("\nOpC'C#o invC!lida!")
            time.sleep(1)

# Inicia o programa
if __name__ == "__main__":
    mostrar_tela_login()        print(" 4. Sair       |  |  USUC
