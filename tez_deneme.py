# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:59:05 2019

@author: muhsin
"""

from tkinter import *  #tkinter kütüphanesi eklendi.
import datetime
import threading     #Threading kütüphanesi eklendi.
import time          #saat kütüphanesi eklendi.
import socket        #Soket kütüphanesi eklendi.

s = socket.socket()            #socket fonksyonları tanımlandı.
s.bind(('0.0.0.0', 8090)) #Soket poru seçildi
s.listen(5)                # soket ile ilgili 
s.settimeout(1)
a = ""


dictionary = {      #verileri kaydedilen sözlük
        "14187000": "Ford",
        "14187001": "Mustang",
        "14187002": "veri",
        "14187003": "222",
        
        }  


degistir = False      #butona bastigimda degeri degisecek threading için kulanılmayacak
sayac = 0

def butona_basildiginda():     #butona basıldığında yapılacakları tanımladım
    global degistir    #global onemli nokta yoksa error verir
    degistir = True

def arka_plan():    #arkaplanda yapmak istediklerim
    global degistir
    global sayac
    while True:
        if not degistir:
            try:  # bağlantı hatası almamak için try ve except komutları kullanıldı.
                print("arkaplanda calisiyorum")   #eger butona basılmamıssa arkaplanda calısmaya devam ediyorum bastır
                client, addr = s.accept()
                while True:
                    at = client.recv(32)
                    
        
                    if len(at) == 0:
                        print("veri bulunamadı")
                        break
                    else:
                        an = datetime.datetime.now()                #Tarih gösterisi
                        tarih = datetime.datetime.strftime(an, '%X') #Saat gösterir.
                        tarih2 = datetime.datetime.strftime(an, '%c')
                        
                        a=at
                        att = str(at)
                        print(type(at))
                        direction.set(at)
                        att= at.decode()#gelen veri.
                        print(type(att))
                        
                        ayir = att.split(",")
                        print(ayir)
                        dicVeri = dictionary[ayir[0]]
                        dictionary[ayir[0]] = dicVeri + " " + tarih2 + " "+"hata: " +ayir[1]
                        
                          
                        if sayac==0: #gelen verileri ekrana yazdırmak için.
                            print("sayac 0")
                            sayac +=1
                            hata1.set("Seri No"+ ayir[0] +" Yeni arıza bilgisi :" + ayir[1])
                            zaman1.set(tarih)
                            messagebox.showwarning("Uyarı",("Arıza Bilgisi Geldi "+ tarih + ayir[1]))
                        elif sayac == 1:
                            print("sayac 1")
                            sayac +=1
                            hata2.set("Seri No"+ ayir[0] +" Yeni arıza bilgisi :" + ayir[1])
                            zaman2.set(tarih)
                            messagebox.showwarning("Uyarı",("Arıza Mesajı Geldi "+ tarih + ayir[1]))
                        elif sayac == 2:
                            print("sayac 2")
                            sayac = 0
                            hata3.set("Seri No"+ ayir[0] +" Yeni arıza bilgisi :" + ayir[1])
                            zaman3.set(tarih)
                            messagebox.showwarning("Uyarı",("Arıza Mesajı Geldi "+ tarih + ayir[1]))
            
#    print("a degeri",a)
                print("Bağlantı Kapatılıyor.")
#                client.close()
#                return(a)
            except:
                print("Bağlantı başarısız.")
                direction.set("Bağlantı başarısız.")
        else:
            print("arkaplanda calismayi durdur") #butona basıldıgında yapılacaklar
            direction.set("Bağlantı kapatıldı.")
            time.sleep(5)
            break
        

    
def arama1():
    veri = entry_1.get() #entry_1 veri alır.
    print(type(veri))
    print(veri)
    if veri in dictionary:
        print("Kayıt bulundu.")
        aramatext.set(dictionary[veri])
    else:
        aramatext.set("Kayıt bulunamadı.")
  

def ekle(): # sözlüğe yeni cihaz ekleme kodları.
    print(entry_2.get())
    print(type(entry_2.get()))
    print(entry_3.get())
    an = datetime.datetime.now()                #Tarih gösterisi
    tarih = datetime.datetime.strftime(an, '%c')
    print(type(tarih))
    dictionary[entry_2.get()] = entry_3.get() + tarih + ":"
    print(dictionary)
    sonuc.set("Yeni cihaz eklendi.")

thread_part = threading.Thread(target = arka_plan) #arka_plan adlı fonksiyonu thread e emanet edecegiz onun icin ilk olarak Thread sinifi tanimla
thread_part.daemon = True #daemonu True yap
thread_part.start() #fonksiyon arkaplanda calısmaya baslasın( siz de baska islerinize odaklanın boylece:))



pencere =  Tk()
pencere.geometry('400x600') # pencere boyutu
pencere.title("Tez Deneme") # pencere ismi


ment = ""

an = datetime.datetime.now()                #Tarih gösterisi
tarih = datetime.datetime.strftime(an, '%X') #Saat gösterir.
zaman1 = StringVar()
zaman1.set(tarih)
zaman2 = StringVar()
zaman2.set(tarih)
zaman3 = StringVar()
zaman3.set(tarih)

hata1 = StringVar()
hata1.set("Veri Bekleniyor.")
hata2 = StringVar()
hata2.set("Veri Bekleniyor.")
hata3 = StringVar()
hata3.set("Veri Bekleniyor.")

aramatext = StringVar()
aramatext.set("                                         Aranan seri numarası yok.")

img = PhotoImage(file ="pauLogo.png")
panel = Label(pencere, image=img)
panel.place(x=290,y=0)

label_0 = Label(pencere, text="Arama:",width=20,font=("bold", 10))
label_0.place(x=20,y=28)
entry_1 = Entry(pencere, textvariable=ment, )
entry_1.place(x=130,y=30)
abtn = Button(text="Ara",command = arama1)
abtn.place(x = 260,y = 26)
w1 = Message(pencere,textvariable=aramatext,fg="blue",width=300)
w1.place(x=0,y=70)

ciz=Label(pencere, text="____________________________________________________________________________________________________________________________________",fg="green")
ciz.place(x = -45,y = 55+100)
baslik1 = Label(pencere, text="Son Üç Arıza",width=20,font=("bold", 10),fg="blue")
baslik1.place(x=110,y=80+100)
wLbl=Label(pencere, textvariable=zaman1,fg="red",font=("Open Sans","12","underline"))
wLbl.place(x = 30,y = 120+100)
w1Lbl=Label(pencere, textvariable=zaman2,fg="red",font=("Open Sans","12","underline"))
w1Lbl.place(x = 150,y = 120+100)
w2Lbl=Label(pencere, textvariable=zaman3,fg="red",font=("Open Sans","12","underline"))
w2Lbl.place(x = 270,y = 120+100)

w = Message(pencere,textvariable=hata1)
w.place(x=10,y=150+100)
w1 = Message(pencere,textvariable=hata2)
w1.place(x=130,y=150+100)
w2 = Message(pencere,textvariable=hata3)
w2.place(x=250,y=150+100)

ciz2=Label(pencere, text="___________________________________________________________________________________________________________________________________________________",fg="green")
ciz2.place(x = -45,y = 250+100)
baslik2 = Label(pencere, text="Yeni Cihaz Ekle",width=20,font=("bold", 10),fg="blue")
baslik2.place(x=110,y=280+100)
label_1 = Label(pencere, text="Seri No:",width=20,font=("bold", 10))
label_1.place(x=-45,y=298+100)
entry_2 = Entry(pencere, textvariable=ment,width=20 )
entry_2.place(x=70,y=300+100)
label_2 = Label(pencere, text="Marka:",width=20,font=("bold", 10))
label_2.place(x=-43,y=320+100)
entry_3 = Entry(pencere, textvariable=ment,width=20 )
entry_3.place(x=70,y=320+100)
eklebtn = Button(text="Ekle",width=15,height=3,command = ekle)
eklebtn.place(x = 250,y = 300+100)
sonuc = StringVar()
sonuc.set("Yeni cihaz eklemeye hazır.")
sonuc2 = Label(pencere, textvariable=sonuc,width=20,font=("bold", 10),fg="red")
sonuc2.place(x=110,y=370+100)


data ="Veri Bekleniyor..."
direction = StringVar()
direction.set(data)

directionLbl=Label(pencere, textvariable=direction,fg="red",font=("Open Sans","12","underline"))
directionLbl.place(x = 200,y = 500)

bttn = Button(text="Arka planda çalışmayı durdur.",command = butona_basildiginda)
bttn.place(x = 10,y = 500)

pencere.mainloop()