import telebot
import gdown
import os
from datetime import date
URL_RU='https://drive.google.com/drive/folders/10GEyvT-ma0iOGz-ale1CpdPM5Lt2fdhQ'
TOKEN=''
ID=''
num= date.today().weekday() #qual é o dia de hoje
sem=("segunda","terça","quarta","quinta","sexta","sábado","domingo","NULL") 
def send_message(Mensage): #envio de mensagem
    bot = telebot.TeleBot(TOKEN)
    bot.send_message(ID,Mensage,parse_mode='MarkdownV2')
def download(): #download da pastado cardapio
    gdown.download_folder(URL_RU,output='Cardapio')
def totext(): #conversão pela pdftotext version 24.06.1 
    os.system("pdftotext -layout -fixed 13 Cardapio/*.pdf")
def reader_manipuler(): #manipulacao de texto
    finalz_a=["```"]
    finalz_b=["```"]
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
            s1= slice(30)
            s= data[val][s1]+"\n"
            finalz_a.append(s.strip())
            s1= slice(30,len(data[val]))
            s= data[val][s1]
            finalz_b.append(s.strip())


    return finalz_a,finalz_b
 
def clean():
    os.system("cd .. & rm -r Cardapio")
def main():
    mesagem_a = []
    mesagem_b = []
    #download()
    #totext()
    mesagem_a,mesagem_b =  reader_manipuler()
    mensagem="\n".join(mesagem_a)
    mensagem+="```"
    send_message(mensagem)
    mensagem="\n".join(mesagem_b)
    mensagem+="```"
    send_message(mensagem) #shit code :p
    #clean()
if __name__=='__main__':
    main()
