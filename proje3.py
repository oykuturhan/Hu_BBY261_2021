from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Fotoğraf Albümü")
pencere.geometry("640x427")
pencere.configure(bg="pink")

kapaklar = ["beach-g7714d799c_640.jpg", "meditation-geba56cf67_640.jpg", "yoga-g0358f3003_640.jpg"]

kapak = 0


def goster():
    gorsel = ImageTk.PhotoImage(Image.open(kapaklar[kapak]))
    cerceve = Label(image=gorsel)
    cerceve.image = gorsel
    cerceve.grid(row=1, column=3, padx= 10, pady=10)

goster()

def sonraki():
    global kapak
    if kapak < len(kapaklar)-1:
        kapak +=1
    else:
        kapak = 0
    print(kapak)
    goster()

buton = Button(text="İleri",fg="purple", command=sonraki)
buton.grid(row=2, column=1, padx=10, pady=10)
buton.config(font=("Time News Roman", 20))
def sonra():
    global kapak
    if kapak < len(kapaklar)+3:
        kapak -=1
    else:
        kapak=0
    print(kapak)

    goster()

buton=Button(text="Geri", fg="purple",command=sonra)
buton.grid(row=2,column=2, padx=10,pady=10)
buton.config(font=("Time News Roman",20))



baslik = Label(pencere,text="YOGA",fg="purple")
baslik.grid(row=0, column=0, padx= 10, pady=10)
baslik.config(font=("Bodoni MT", 40))

cıkıs=Button(text="Çıkış",fg="purple", command=pencere.quit)
cıkıs.grid(row=2,column=8,padx=10,pady=10)
cıkıs.config(font=("Time News roman",20))

mainloop()