import telebot
import gdown
import os
import time 
from datetime import date
from openai import OpenAI
URL_RU='https://drive.google.com/drive/folders/10GEyvT-ma0iOGz-ale1CpdPM5Lt2fdhQ'
TOKEN=''
ID=''
client = OpenAI(
  api_key="sk-",base_url="https://api.deepseek.com"
)
num = date.today().weekday()  # qual é o dia de hoje
sem = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo", "NULL")


def send_message(Mensage):  # envio de mensagem, retorna 1 quando da erro e 0 quando envia a mensagem
    try:
        bot = telebot.TeleBot(TOKEN)
        bot.send_message(ID, Mensage, parse_mode='MarkdownV2')
        time.sleep(2)
        return 0
    except Exception as e:
        time.sleep(2)
        return 1


def download():  # download da pasta do cardápio
    gdown.download_folder(URL_RU, output='Cardapio')


def totext():  # conversão pela pdftotext version 24.06.1
    os.system("pdftotext -layout -fixed 13 Cardapio/*.pdf")


def reader_manipuler():  # manipulação de texto
    finalz_a = ["```"]
    finalz_b = ["```"]
    a = 0
    txt_file = [f for f in os.listdir('Cardapio') if f.endswith('.txt')]
    with open('Cardapio/' + txt_file[0]) as reader:
        second = (sum(1 for _ in reader)) - 1
        first = second

    with open('Cardapio/' + txt_file[0]) as reader:
        data = reader.readlines()
        for line in data:
            a = a + 1
            if a > 28:  # cara eu realmente não sei programar em python eu pulei as 28 linhas
                if line.lower().find(sem[num]) != -1:
                    first = data.index(line)
                if line.lower().find(sem[num + 1]) != -1:
                    second = data.index(line)

        for val in range(first, second - 3):
            s1 = slice(30)
            s = data[val][s1] + "\n"
            finalz_a.append(s.strip())
            s1 = slice(30, len(data[val]))
            s = data[val][s1]
            finalz_b.append(s.strip())

    return finalz_a, finalz_b


def clean():
    os.system("cd .. & rm -r Cardapio")


def tratamento(Mensagem):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "Formate o seguinte cardápio para ser enviado no Telegram com ícones e coloque em formato de codigo para telegram sem nenhuma indicado como markdown ou codigo. Use títulos, emojis e uma estrutura organizada, não escreve mais nada alem do cardapio destacando os principais comidas, não altere nada descarte coisas que nao envolvem comida, nao escreva alem:"},
                {"role": "user", "content": str(Mensagem)},
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

def main():
    mesagem_a = []
    mesagem_b = []
    # download()
    # totext()
    mesagem_a,mesagem_b = reader_manipuler()


    mensagem = tratamento(mesagem_a)
    for x in range(10):
        try:
            send_message(mensagem)
            break
        except Exception as e:
            time.sleep(30)
        else:
            print("xiiiiiii n deu deu")

    mensagem = tratamento(mesagem_b)
    for x in range(10):
        try:
            send_message(mensagem)
            break
        except Exception as e:
            time.sleep(30)
        else:
            print("xiiiiiii n deu deu")

    # clean()
