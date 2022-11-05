class Usuario:
    def __init__(self, nombre, balance):
        self.balance = balance
        self.nombre = nombre
    
    def hacer_deposito(self, monto):
        self.balance += monto
        return self

    def hacer_retiro(self, monto):
        self.balance -= monto
        return self

    def mostrar_balance(self):
        print(f"El cliente {self.nombre} tiene en su cuenta : $ {self.balance}")
        return self
        

    def transfer_dinero(self, otro_usuario, monto):
        if type(otro_usuario) is not Usuario:
            print("El usuario no existe")
            return
        if self.balance<monto:
            print("Usted no cuenta con suficiente monto")
            return
        self.hacer_retiro(monto)
        otro_usuario.hacer_deposito(monto)


usuario_1 = Usuario('Andrea',3540)
usuario_1.hacer_deposito(2000)
usuario_1.hacer_deposito(430)
usuario_1.hacer_deposito(30000)
usuario_1.hacer_retiro(2430)
usuario_1.mostrar_balance()

usuario_2 = Usuario('Analia',99)
usuario_2.hacer_deposito(2570)
usuario_2.hacer_deposito(4530)
usuario_2.hacer_retiro(2430)
usuario_2.hacer_retiro(967)
usuario_2.mostrar_balance()

usuario_3 = Usuario('Manuel', 5400)
usuario_3.hacer_deposito(114530)
usuario_3.hacer_retiro(10000)
usuario_3.hacer_retiro(10)
usuario_3.hacer_retiro(146)
usuario_3.mostrar_balance()

usuario_3.transfer_dinero(usuario_2, 200)
usuario_2.mostrar_balance()

usuario_3.transfer_dinero(usuario_2, 200)
usuario_2.mostrar_balance()
