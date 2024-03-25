from config import *


class Contador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contador = db.Column(db.Integer)

    def __str__(self):
        return f'contador {id}: {self.contador}'

    def json(self):
        return {
            "id": self.id,
            "contador": self.contador
        }

    def incrementar(self):
        self.contador += 1
        self.__commit_change()

    def decrementar(self):
        self.contador -= 1
        self.__commit_change()

    def __commit_change(self):
        db.session.add(self)
        db.session.commit()


if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    c1 = Contador(contador=1)

    db.session.add(c1)
    db.session.commit()

    print(c1)
    print(c1.json())

    c1.incrementar()
    c1.incrementar()

    print(c1)
    print(c1.json())

    c1.decrementar()
    c1.decrementar()

    print(c1)
    print(c1.json())
