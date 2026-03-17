print("🤖 Agente de IA iniciado! (digite 'sair' para encerrar)\n")

while True:
    pergunta = input("Você: ").lower()

    if pergunta == "sair":
        print("Agente: Encerrando... Até mais!")
        break

    elif "oi" in pergunta or "olá" in pergunta:
        print("Agente: Olá! Como posso te ajudar?")

    elif "seu nome" in pergunta:
        print("Agente: Sou um agente de IA simples criado em Python.")

    elif "ajuda" in pergunta:
        print("Agente: Posso responder perguntas básicas ou simular automações.")

    elif "python" in pergunta:
        print("Agente: Python é uma linguagem muito usada em automação e IA.")

    else:
        print("Agente: Ainda estou aprendendo, mas posso tentar te ajudar!")