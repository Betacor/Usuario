from Usuario import Usuario

alicia = Usuario("Alicia Araya")
bernardo = Usuario("Bernardo Borquez")
carlos = Usuario("Carlos Carmona")

alicia.hacer_deposito(100)
alicia.hacer_deposito(700)
alicia.hacer_deposito(1000)
alicia.hacer_retiro(300)

alicia.mostrar_balance_usuario()

bernardo.hacer_deposito(800)
bernardo.hacer_deposito(500)
bernardo.hacer_retiro(300)
bernardo.hacer_retiro(100)

bernardo.mostrar_balance_usuario()

carlos.hacer_deposito(3000)
carlos.hacer_retiro(200)
carlos.hacer_retiro(500)
carlos.hacer_retiro(400)

carlos.mostrar_balance_usuario()

alicia.transferir_dinero(150, carlos)

alicia.mostrar_balance_usuario()
carlos.mostrar_balance_usuario()







