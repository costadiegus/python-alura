from conta import Conta
from datas import Data


def executa():
    cc = Conta(123, "Eric Clapton", 150.5)
    cc.extrato()

    cc.deposita(50)
    cc.extrato()

    cc.saca(50)
    cc.extrato()

    cc_2 = Conta(111, "Jonh Travolta", 250.0)
    cc_2.extrato()
    cc_2.transfere(45, cc)
    cc_2.extrato()

    print(Conta.codigo_banco())
    print(Conta.codigos_bancos())


if __name__ == "__main__":
    executa()
