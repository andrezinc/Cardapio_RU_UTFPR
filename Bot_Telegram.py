import telebot
import gdown
import os
from datetime import date
URL_RU='https://drive.google.com/drive/folders/10GEyvT-ma0iOGz-ale1CpdPM5Lt2fdhQ'
TOKEN=''
ID=''
num= date.today().weekday()
sem=("segunda","terça","quarta","quinta","sexta","sábado","domingo","NULL")
def send_message(Mensage):
    bot = telebot.TeleBot(TOKEN)
    bot.send_message(ID,Mensage,parse_mode='MarkdownV2')
def download():
    gdown.download_folder(URL_RU,output='Cardapio')
def totext():
    os.system("pdftotext -layout -fixed 13 Cardapio/*.pdf")
def reader_manipuler():
    finalz = [ "```"]
    a=0
    txt_file = [f for f in os.listdir('Cardapio') if f.endswith('.txt')]
    with open('Cardapio/'+txt_file[0]) as reader:
        second=(sum(1 for _ in reader ))-1
        first=second
    with open('Cardapio/'+txt_file[0]) as reader:
        data=reader.readlines()
        for line in data:
            a=a+1
            if(a>28): #cara eu realmente nao sei programar em python eu pulei as 28 linhas
                if line.find(sem[num]) != -1:
                    first=data.index(line)
                if line.find(sem[(num+1)]) != -1:
                    second=data.index(line)
        for val in range(first,second-3):
            finalz.append(data[val])
    return finalz
 
def clean():
    os.system("cd .. & rm -r Cardapio")
def main():
    download()
    totext()
    mensagem="\n".join(reader_manipuler())
    mensagem+="```"
    send_message(mensagem)
    clean()
if __name__=='__main__':
    main()
