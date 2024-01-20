from queue import Queue

class Estadio:
    def __init__(self):
        self.fila_torcedores = Queue()

    def entrar_no_estadio(self, torcedor):
        self.fila_torcedores.put(torcedor)
        print(f"Torcedor {torcedor} entrou na fila para entrar no estádio.")

    def permitir_entrada(self):
        if not self.fila_torcedores.empty():
            torcedor = self.fila_torcedores.get()
            print(f"Torcedor {torcedor} entrou no estádio.")
        else:
            print("O estádio está vazio. Não há torcedores na fila.")

    def mostrar_fila(self):
        print("Fila de torcedores:", list(self.fila_torcedores.queue))

# Exemplo de uso
estadio = Estadio()

estadio.entrar_no_estadio("João")
estadio.entrar_no_estadio("Maria")
estadio.entrar_no_estadio("Carlos")

estadio.mostrar_fila()

estadio.permitir_entrada()
estadio.mostrar_fila()

estadio.permitir_entrada()
estadio.mostrar_fila()
