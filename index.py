
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo.lower() == "mago":
            ataque = "magia"
        elif self.tipo.lower() == "guerreiro":
            ataque = "espada"
        elif self.tipo.lower() == "monge":
            ataque = "artes marciais"
        elif self.tipo.lower() == "ninja":
            ataque = "shuriken"
        else:
            ataque = "um ataque desconhecido"

        print(f"{self.tipo} atacou usando {ataque}")


# Criando os objetos
heroi1 = Heroi("Merlin", 150, "mago")
heroi2 = Heroi("Arthur", 30, "guerreiro")
heroi3 = Heroi("Bruce", 35, "monge")
heroi4 = Heroi("Hattori", 28, "ninja")

# Executando os ataques
heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
