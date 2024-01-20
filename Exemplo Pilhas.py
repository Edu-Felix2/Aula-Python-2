class PartidaFutebol:
    def __init__(self):
        self.pilha_gols = []

    def marcar_gol(self, jogador):
        self.pilha_gols.append(f"Gol de {jogador}!")
        print(f"Gol marcado por {jogador}.")

    def desfazer_ultimo_gol(self):
        if self.pilha_gols:
            gol_desfeito = self.pilha_gols.pop()
            print(f"Último gol de {gol_desfeito.split(' ')[2][:-1]} desfeito.")
        else:
            print("Não há gols para desfazer.")

    def mostrar_gols(self):
        print("Gols marcados:", self.pilha_gols)

# Exemplo de uso
partida = PartidaFutebol()

partida.marcar_gol("Messi")
partida.marcar_gol("Neymar")
partida.marcar_gol("Cristiano Ronaldo")

partida.mostrar_gols()

partida.desfazer_ultimo_gol()
partida.mostrar_gols()

partida.desfazer_ultimo_gol()
partida.mostrar_gols()
