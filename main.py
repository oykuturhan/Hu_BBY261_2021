import tkinter
from tkinter import*
from random import randint

sayfa = Tk()
sayfa.geometry("300x300+200+200")
sayfa.configure(bg="light blue")
sayfa.title("Sayısal Loto")

metinKutusu = Label(sayfa, text= "Büyük İkramiye Bu Rakamlarda", fg= "white", bg="black")
metinKutusu.config(font=("Times New roman", 18))
metinKutusu.pack()
def loto():

   i = 0
   secilenler = [0,0,0,0,0,0]
   for rastgele in secilenler:
       while i < len(secilenler):
           secilen = randint(1, 90)
           if secilen not in secilenler:
              secilenler[i] = secilen
              i+=1

       secilmis = (sorted(secilenler))
       i=0
       başka = Label(sayfa, text=secilenler)
       başka.config(font=("Arial",14))
       başka.pack()
tıkla = Button(sayfa, text="Çılgın Sayılar", fg= "black", command=loto )
tıkla.config(font=("Times New Roman",14))
tıkla.pack()
def baska():
    degisik=("Ekranda gördüğünüz, seçilen sayı butonuna tıklandığında ekranda rastgele sayılar gelir.")
    farklı=Label(sayfa, text=degisik)
    farklı.config(font=("Arial", 14))
    farklı.pack()
yardım = Button(sayfa, text="Yardım", fg="black", command= baska)
yardım.config(font=("Times New Roman",14))
yardım.pack()

cıkıs = Button(sayfa, text= "Çıkış Yap",fg= "black", command = sayfa.quit)
cıkıs.config(font=("Times New Roman",14))
cıkıs.pack()
sayfa.mainloop()
