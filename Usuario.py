class Usuario:		
    nombre_banco = "Banco de Chile"		
    def __init__(self, nombre):
        self.nombre = "Alicia"
        self.balance = 0
        
    def hacer_deposito(self, deposito):
        self.balance += deposito

    def hacer_retiro(self, giro):
        self.balance -= giro

    def mostrar_balance_usuario(self):
        print(self.balance)

    def transferir_dinero(self, transferencia, usuario):
        self.balance -= transferencia
        usuario.balance += transferencia
    




