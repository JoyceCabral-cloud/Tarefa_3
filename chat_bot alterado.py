import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()
    # if comando in ('olá', 'boa tarde', 'bom dia'):
    #     return 'Olá tudo bem!'
    # if comando == 'como estás':
    #     return 'Estou bem, obrigado!'
    # if comando == 'como te chamas':
    #     return 'O meu nome é: Bot :)'
    # if comando == 'tempo':
    #     return 'Está um dia de sol!'
    # if comando in ('bye', 'adeus', 'tchau'):
    #     return 'Gostei de falar contigo! Até breve...'
    # if 'horas' in comando:
    #     return f'São: {datetime.now():%H:%M} horas'
    # if 'data' in comando:
    #     return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
    ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
    'como estás': 'Estou bem, obrigado!',
    'como te chamas': 'O meu nome é: Bot :)',
    'tempo': 'Está um dia de sol!',
    ('que horas são', 'podes dizer as horas', 'qual é a hora agora'): 'Infelizmente, não tenho um relógio comigo, mas posso tentar adivinhar!',
    ('que dia é hoje', 'qual é a data de hoje', 'podes dizer a data'): 'Hoje é um dia muito especial! Vá ao seu calendário para confirmar. :)',
    ('gostas de música', 'tens uma música favorita'): 'Gosto de todas as músicas que as pessoas amam! Qual é a sua favorita?',
    ('qual é o melhor filme', 'tens um filme favorito'): 'Eu gosto de ouvir sobre "filmes favoritos". Qual o seu?',
    ('sabes programar', 'consegues programar'): 'Sim! Sou bom em resolver problemas.'
    ("Qual é o teu animal favorito?"): "Eu gosto de todos os animais! Mas acho gatos e cães muito populares. E você?"

    ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...'
}

      
   


    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'

    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()
