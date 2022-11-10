class Empregado:
    def __init__(self, nome: str, salario: float, imposto: float):
        self.nome = nome
        self.salario = salario
        self.__imposto = imposto

    def salario_liquido(self):
        self.__calcularImposto()
        salario = self.salario - (self.salario * self.__imposto)
        return salario

    def aumento(self):
        percentual = float(input("Informe a % do aumento"))
        aumento = (percentual + 100) / 100
        self.salario = self.salario * aumento


    def imprimir(self):
        print("Funcionario:{}\n"
              "Salario:{}".format(self.nome, self.salario))

    def __calcularImposto(self):
        if self.salario <= 2000:
            self.__imposto = (10 * 100)

        elif 2000 < self.salario <= 5000:
            self.__imposto = (15 * 100)

        elif self.salario > 5000:
            self.__imposto = (20 * 100)


empregado = Empregado(nome=input("qual o nome de funcionario: "),
                      salario=float(input("Qual o salario de funcionario: ")), imposto=0)
empregado.imprimir()
empregado.salario_liquido()
empregado.imprimir()
empregado.aumento()
empregado.imprimir()