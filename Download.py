import os
import gdown
from datetime import date
URL_RU='https://drive.google.com/drive/folders/10GEyvT-ma0iOGz-ale1CpdPM5Lt2fdhQ'
day_= date.today().day #codigo será executado toda segunda feira, pega o dia 
def download():
    gdown.download_folder(URL_RU,output='Cardapio') #sera baixado o cardapio 
def totext():
    if(os.system("pdftotext -layout -fixed 13 Cardapio/"+str(day_)+"*.pdf")>0): #sera executado no sistema pega o numero do dia atual e transforma para txt
     	os.system("pdftotext -layout -fixed 13 Cardapio/"+'0'+str(day_)+"*.pdf") #caso der erro ele vai colocar um 0 na frente pois os cardapios vem com 0(dia atual)
def clean():
    os.system("cd .. & rm -r Cardapio") #limpa o arquivo anterior
def main():
    clean()
    download()
    totext()
if __name__=='__main__':
    main()
