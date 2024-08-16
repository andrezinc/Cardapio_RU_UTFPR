import os
import gdown
from datetime import date
URL_RU='https://drive.google.com/drive/folders/10GEyvT-ma0iOGz-ale1CpdPM5Lt2fdhQ'
day_= date.today().day #codigo será executado toda segunda feira, pega o dia 
def download():
    gdown.download_folder(URL_RU,output='Cardapio') #sera baixado o cardapio 
def totext():
     os.system("pdftotext -layout -fixed 13 Cardapio/"+str(day_)+"*.pdf") #sera executado no sistema pega o numero do dia atual e transforma para txt
def clean():
    os.system("cd .. & rm -r Cardapio") #limpa o arquivo anterior
def main():
    clean()
    download()
    totext()
if __name__=='__main__':
    main()
