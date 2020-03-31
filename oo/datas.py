class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        # # print("{}/{}/{}.format(self.dia, self.mes, self.ano)")
        # print(f"{self.dia}/{self.mes}/{self.ano}")
        print(self.dia, self.mes, self.ano, sep="/")


def executa():
    d = Data(21, 11, 2007)
    d.formatada()


if __name__ == "__main__":
    executa()
