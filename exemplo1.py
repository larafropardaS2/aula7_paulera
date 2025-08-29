
class Pessoa:
    def __init__(self, nome, data_nascimento, sexo):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo
    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")

class Aluno(Pessoa):
    def __init__(self, nome, data_nascimento, sexo, matricula):
        super(). __init__(nome, data_nascimento, sexo)
        self.matricula = matricula


pessoa1 = Pessoa("José", "20/10/1995" , "masclino")
pessoa2 = Pessoa("Maria", "15/01/2001" ,"feminino")

print(f"Nome: {pessoa1.nome} - Data de nascimento: {pessoa1.data_nascimento}")
print(f"Nome: {pessoa2.nome} - Data de nascimento: {pessoa2.data_nascimento}")

pessoa1.falar("Boa noite! Bem vindo(a)")
pessoa2.falar("Olá")

aluno1 = Aluno("João Silva", "10/01/2005", "Masculino", "222222222222")

print(f"Matrícula: {aluno1.matricula} - Nome: {aluno1.nome}")

