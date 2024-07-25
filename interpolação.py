: email_tmpl = """
   ...: olá, %(nome)s
   ...: 
   ...: Tem interesse em comprar %(produtos)s?
   ...: 
   ...: Este produto é ótimo para resolver
   ...: %(texto)s
   ...: 
   ...: Clique agora em %(link)s
   ...: 
   ...: Apenas %(quantidade)d disponiveis!
   ...: 
   ...: Preço promocional %(preco).2f
   ...: """

: clientes = ["Rachel", "Arthur", "Victor"]

: for clientes in clientes:
   ...:     print(
   ...:         email_tmpl
   ...:      % {
   ...:          "nome": clientes,
   ...:          "produtos": "caneta",
   ...:          "texto": "escreve muito bem",
   ...:          "link": "https://canetaslegias.com",
   ...:          "quantidade": 1,
   ...:          "preco": 50.0,
   ...: 
   ...:         }
   ...:     )


