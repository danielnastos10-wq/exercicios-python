from dataclasses import dataclass
from datetime import datetime
#1.O sistema precisa ter agendamento onde o cliente escolhe o barbeiro
#2.O sistema precisa ter cadastro da agenda do barbeiro
#4.O sistema precisa ter cadastro de cliente 
#6.O sistema precisa ter reagendamento. 
#7.O sistema precisa ter um lembrete via email para o cliente
#8.O sistema precisa ter o faturamento da barbearia no mês

@dataclass
class Pessoa:
    nome:str
    celular:str
    email:str

class Barbeiro:
    nome:str
    disponibilidade:str
    complemento:str
    horario:str
    corte:str

class Agendamento:
    data:str
    hora:str
    tipodecorte:str
    barbeiro:str
    
lista = []

def agendar():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    barbeiro = input("Escolha seu barbeiro: ")
    data = input("Digite a data desejada: ")
    hora = input("Digite seu horario: ")
    celular = input("Qual seu contato: ")
    cliente_digitado = cliente(nome,email,celular)
    lista.append(cliente_digita)
    print("Cadastro realizado com sucesso")
    
def menu():
    print("1 - Cadastrar agendamento")
    print("2 - Ver serviços")
    print("3 - Preço do serviço ")
    print("4 - Ver horario disponivel")
    print("5 - Ver clientes cadastrados")
    print("6 - Sair")
    return input("Escolha uma opção: ")
#variaveis de controle


while True:
    opcao = menu()
        
    if opcao == "1":
        nome = input("Nome do cliente: ")
        contato = input("Inserir contato: ")
        data = input("Inserir data: ")
        hora = input("Digite o horário: ")
        barbeiro = input("Escolha seu barbeiro: ")
        serviço = input("Tipo de serviço: ")
        print(f"agendamento '{agendamento}' agendado com sucesso!")
        
    if opcao == "2":
        corte = input("Digite o corte: ")
        barba = input("Barba: ")
        sobrancelha = input("Sobrancelha: ")
        print("Serviço confirmado!")
        
    if opcao == "3":
        valor_do_corte=40
            print(f"O valor do corte é R$ {valor_do_corte},00")
        valor da barba:
            print("R$20")
        valor da sobrancelha:
            print("R$10")
