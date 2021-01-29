class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa): # Classe Homem herda de Pessoa os atributos
    def cumprimentar(self): #sobrescrever completamente o método Pessoa
        cumprimentar_da_classe = super().cumprimentar() #obtendo o cumprimentar da classe Pai
        return f'{cumprimentar_da_classe}. Aperto de mão' #agregando a frase da classe Pai com a frase do métod sobrescrito


class Mutante(Pessoa): # Classe Homem herda de Pessoa os atributos
    olhos = 3 # sobrescrevendi o atribudo da classe.

if __name__ == '__main__':
    renzo = Mutante(nome="renzo")
    luciano = Homem(renzo, nome="Luciano")
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar()) # no python o objeto p. é passado para a função e recebido pelo parâmetro self
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = "Ramalho"
    del luciano.filhos
    luciano.olhos = 1
    print(luciano.__dict__) #mostra os atributos de instância de um objeto
    print(renzo.__dict__)
    # Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(luciano.olhos), id(renzo.olhos), id(Pessoa.olhos))
    del luciano.olhos
    print(luciano.__dict__) #mostra os atributos de instância de um objeto
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(luciano.olhos), id(renzo.olhos), id(Pessoa.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())
