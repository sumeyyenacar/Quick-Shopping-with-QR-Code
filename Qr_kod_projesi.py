import tkinter  # arayüz olarak tkinter kullanmak için import edilir.
from tkinter import *  # tkinter modülündeki her fonksiyonu kullanmak için import edilir.
from tkinter import ttk  # oluşturulan bazı çerçeve stilleri için import edilir.
from tkcalendar import DateEntry  # tarih kullanımı için takvim import edilir.
from tkinter import messagebox  # yapılan işlem sonucu uyarı vermek için messagebox import edilir.
import sqlite3 as db  # database kullanmak için sqlite3 import edilir.
import csv  # csv dosyası kullanmak için import edilir.
import pyqrcode  # qr kod kullanmak için import edilir.
import png  # png dosyalarını görüntülemek için import edilir.
import pandas as pd  # qr kod adına veri işlemesi ve analizi için import edilir.

global window  # giriş ve kaydol ekranını farklı fonksiyonlarda da kullanabilmek için global olarak tanımlıyoruz.


def giris():  # giriş ve kaydol ekranının fonksiyonu.
    f = ('Times', 14)  # font tipi ve boyutu tanımlanır.

    con = db.connect('userdata.db')  # kullanıcı bilgilerinin tutulduğu database oluşturulur.
    cur = con.cursor()  # database'in kullanımı için database'de imleç oluşturulur.
    cur.execute('''CREATE TABLE IF NOT EXISTS record(  
                        name text, 
                        email text, 
                        contact number, 
                        gender text, 
                        country text,
                        password text
                    ) 
                ''')  # database'de record adında tablo yoksa oluşturulur ve yukarıdaki başlıkların sutünları oluşur.
    con.commit()  # tablonun içeriği databese'e işlenir.

    ws = Tk()  # Tk() sınıfından 'ws' adında bir obje oluşturulur.
    ws.title('QR Kodla Hizli Alisveris')  # objenin başlığı oluşturulur.
    ws.geometry('1100x500')  # objenin boyutu oluşturulur.
    ws.config(bg='#EB910C')  # objenin rengi, rengin kodu girilerek belirlenir.

    def insert_record():  # kayıt olma fonksiyonu yazılır.
        check_counter = 0  # bilgilerin kontrolü için bir değişken oluşturur.
        warn = ""  # hata yazısı için bir değişken oluşturulur.
        if register_name.get() == "":  # kayıt için isim yeri boş bırakılırsa
            warn = "İsminizi Giriniz!"  # ekrana hata mesajı verilir.
        else:  # kayıt için isim yeri boş değilse
            check_counter += 1  # kontrol değişkeni 1 artırılır.

        if register_email.get() == "":  # kayıt için email yeri boş bırakılırsa
            warn = "Emailinizi Giriniz!"  # ekrana hata mesajı verilir.
        else:  # kayıt için email yeri boş değilse
            check_counter += 1  # kontrol değişkeni 1 artırılır.

        if register_mobile.get() == "":  # kayıt için telefon yeri boş bırakılırsa
            warn = "Telefonunuzu Giriniz!"  # ekrana hata mesajı verilir.
        else:  # kayıt için telefon yeri boş değilse
            check_counter += 1  # kontrol değişkeni 1 artırılır.

        if var.get() == "":  # kayıt için cinsiyet yeri seçilmezse
            warn = "Cinsiyetinizi Seciniz!"  # ekrana hata mesajı verilir.
        else:  # kayıt için cinsiyet seçilmişse
            check_counter += 1  # kontrol değişkeni 1 artırılır.

        if variable.get() == "":  # kayıt için şehir seçilmezse
            warn = "Sehrinizi Seciniz!"  # ekrana hata mesajı verilir.
        else:  # kayıt için şehir seçilmişse
            check_counter += 1  # kontrol değişkeni 1 artırılır.

        if register_pwd.get() == "":  # kayıt için parola yeri boş bırakılırsa
            warn = "Parolanizi Giriniz!"  # ekrana hata mesajı verilir.
        else:  # kayıt için parola yeri boş değilse
            check_counter += 1  # kontrol değişkeni 1 artırılır.

        if pwd_again.get() == "":  # kayıt için parola tekrarlama yeri boş bırakılırsa
            warn = "Parolanizi Tekrar Giriniz!"  # ekrana hata mesajı verilir.
        else:  # kayıt için parola tekrarlama yeri boş değilse
            check_counter += 1  # kontrol değişkeni 1 artırılır.

        if register_pwd.get() != pwd_again.get():  # parola ve parola tekrarı aynı değilse
            warn = "Parolaniz Eslesmedi!"  # ekrana hata mesajı verilir.
        else:  # parola ve parola tekrarı aynı ise
            check_counter += 1  # kontrol değişkeni 1 artırılır.

        if check_counter == 8:  # kontrol değişkeni 8 ise
            try:  # hata oluşumunu engellemek için database'e veri yazımı işlemleri try-except bloğu içerisine alınır.
                con = db.connect('userdata.db')  # kullanıcı bilgilerinin tutulduğu database açılır.
                cur = con.cursor()  # database'in kullanımı için database'de imleç oluşturulur.
                cur.execute("INSERT INTO record VALUES (:name, :email, :contact, :gender, :country, :password)",
                            {  # record tablosuna
                                'name': register_name.get(),  # girilen isim eklenir.
                                'email': register_email.get(),  # girilen email eklenir.
                                'contact': register_mobile.get(),  # girilen telefon  eklenir.
                                'gender': var.get(),  # girilen cinsiyet eklenir.
                                'country': variable.get(),  # girilen şehir eklenir.
                                'password': register_pwd.get()  # girilen parola eklenir.

                            })
                con.commit()  # tablonun içeriği databese'e işlenir.
                messagebox.showinfo('Kayit Denemesi',
                                    'Kayit Basarili!')  # kaydın gerçekleştirildiği hakkında kullanıcıya mesaj verilir.

            except Exception as ep:  # bir hata oluşursa
                messagebox.showerror('', ep)  # kaydın gerçekleştirilmediği hakkında kullanıcıya mesaj verilir.
        else:  # kontrol değişkeni 8 değilse
            messagebox.showerror('Kayit Denemesi', warn)  # hata mesajı ekrana verilir.

    def login_response():  # giriş yapma fonksiyonu oluşturulur.
        try:  # oluşacak hataları yakalamak için try-except bloğu oluşturulur.
            con = db.connect('userdata.db')  # kullanıcı bilgilerinin tutulduğu database açılır.
            c = con.cursor()  # database'in kullanımı için database'de imleç oluşturulur.
            for row in c.execute("Select * from record"):  # record tablosundaki tüm veriler seçilir.
                username = row[1]  # 1.satırdaki veri username değişkenine atanır.
                pwd = row[5]  # 5.satırdaki veri pwd değişkenine atanır.

        except Exception as ep:  # bir hata yakalanırsa
            messagebox.showerror('', ep)  # hata mesajı ekrana verilir.

        uname = email_tf.get()  # email yazı alanı 'uname' adında bir değişkene atanır.
        upwd = pwd_tf.get()  # parola yazı alanı 'upwd' adında bir değişkene atanır.
        check_counter = 0  # kontrol değişkeni oluşturulur.
        if uname == "":  # 'uname' değişkeni boş bırakıldıysa
            warn = "Emailinizi Giriniz!"  # ekrana hata mesajı verilir.
        else:  # bunun dışındaki olaylarda
            check_counter += 1  # kontrol değişkeni 1 artırılır.
        if upwd == "":  # 'upwd' değişkeni boş bırakıldıysa
            warn = "Parolanizi Giriniz!"  # ekrana hata mesajı verilir.
        else:  # bunun dışındaki olaylarda
            check_counter += 1  # kontrol değişkeni 1 artırılır.
        if check_counter == 2:  # kontrol değişkeni 2'ye eşitse
            if (
                    uname == username and upwd == pwd):  # 'uname' değeri kayıtlı olan isime, 'upwd' değeri kayıtlı olan parolaya eşitse
                messagebox.showinfo('Giris Denemesi',
                                    'Giris Basarili!')  # ekrana girişin başarılı olduğu mesajı verilir.
                ws.destroy()  # kayıt&giriş ekranı kapatılır.
                sayfa()  # alışveriş sayfası ekrana getirilir.

            else:  # girilen ve kayıtlı olan değerlerin herhangi biri eşit değilse
                messagebox.showerror('Giris Denemesi',
                                     'Gecersiz Email veya Parola!')  # ekrana girişin başarısız olguğu mesajı verilir.

        else:  # kontrol değişkeni 2'ye eşit değilse
            messagebox.showerror('', warn)  # ekrana hata mesajı verilir

    var = StringVar()  # 'var' adında string değer oluşturulur.
    var.set('Erkek')  # varsayılan değer 'erkek' olarak oluşturulur.

    countries = []  # şehirler için kullanılacak liste oluşturulur.
    variable = StringVar()  # 'variable' adında string değer oluşturulur.
    world = open('sehirler.txt', 'r')  # 'sehirler' adındaki text dosyası, içeriği okunmak üzere açılır.
    for country in world:  # dosya içerisindeki değerler
        country = country.rstrip('\n')  # sağındaki \n ifadesi atılarak alınır.
        countries.append(country)  # listeye atanır.
    variable.set(countries[29])  # 'variable' değerine 'countries' listesi atanır.

    left_frame = Frame(  # ws objesinin solunda bir çerçeve oluşturulur.
        ws,
        bd=2,
        bg='#F2EABD',
        relief=SOLID,
        padx=10,
        pady=50
    )  # çerçevenin kalınlığı, arka plan rengi, konumu gibi bilgileri girilir.

    Label(
        left_frame,
        text="Email:",
        bg='#F2EABD',
        font=f).grid(row=0, column=0, sticky=W,
                     pady=10)  # soldaki çerçeve içerisinde email bilgisi için label oluşturulur.
    # ve labelın yazısı, arka plan rengi, konumu gibi bilgileri girilir.
    Label(
        left_frame,
        text="Parola:",
        bg='#F2EABD',
        font=f
    ).grid(row=1, column=0, pady=10)  # soldaki çerçeve içerisinde parola bilgisi için label oluşturulur.
    # ve labelın yazısı, arka plan rengi, konumu gibi bilgileri girilir.
    email_tf = Entry(
        left_frame,
        font=f
    )  # email girilmesi için bir yazı alanı oluşturulur.
    # bu giriş yerinin konum ve font bilgileri girilir.
    pwd_tf = Entry(
        left_frame,
        font=f,
        show='*'
    )  # parola girilmesi için bir yazı alanı oluşturulur.
    # bu giriş yerinin konum, font ve yazı girildiğinde ekranda gözükecek olan işaretin bilgileri girilir.
    login_btn = Button(
        left_frame,
        width=15,
        bg='#F7EA72',
        text='Giris',
        font=f,
        relief=SOLID,
        cursor='hand2',
        command=login_response
    )  # giriş için buton oluşturulur.
    # butonun konumu, büyüklüğü, rengi, yazısı, fontu, basıldığında hangi fonksiyonu çalıştıracağı bilgileri girilir.

    right_frame = Frame(  # ws objesinin sağında bir çerçeve oluşturulur.
        ws,
        bd=2,
        bg='#F2EABD',
        relief=SOLID,
        padx=10,
        pady=10
    )  # çerçevenin kalınlığı, arka plan rengi, konumu gibi bilgileri girilir.

    Label(  # sağdaki çerçeve içerisinde isim bilgisi için label oluşturulur.
        right_frame,
        text="İsminizi Giriniz",
        bg='#F2EABD',
        font=f
    ).grid(row=0, column=0, sticky=W, pady=10)  # ve labelın yazısı, arka plan rengi, konumu gibi bilgileri girilir.

    Label(  # sağdaki çerçeve içerisinde email bilgisi için label oluşturulur.
        right_frame,
        text="Email:",
        bg='#F2EABD',
        font=f
    ).grid(row=1, column=0, sticky=W, pady=10)  # ve labelın yazısı, arka plan rengi, konumu gibi bilgileri girilir.

    Label(  # sağdaki çerçeve içerisinde telefon bilgisi için label oluşturulur.
        right_frame,
        text="Telefon No:",
        bg='#F2EABD',
        font=f
    ).grid(row=2, column=0, sticky=W, pady=10)  # ve labelın yazısı, arka plan rengi, konumu gibi bilgileri girilir.

    Label(  # sağdaki çerçeve içerisinde cinsiyet bilgisi için label oluşturulur.
        right_frame,
        text="Cinsiyet:",
        bg='#F2EABD',
        font=f
    ).grid(row=3, column=0, sticky=W, pady=10)  # ve labelın yazısı, arka plan rengi, konumu gibi bilgileri girilir.

    Label(  # sağdaki çerçeve içerisinde şehir bilgisi için label oluşturulur.
        right_frame,
        text="Sehir:",
        bg='#F2EABD',
        font=f
    ).grid(row=4, column=0, sticky=W, pady=10)  # ve labelın yazısı, arka plan rengi, konumu gibi bilgileri girilir.

    Label(  # sağdaki çerçeve içerisinde parola bilgisi için label oluşturulur.
        right_frame,
        text="Parola:",
        bg='#F2EABD',
        font=f
    ).grid(row=5, column=0, sticky=W, pady=10)  # ve labelın yazısı, arka plan rengi, konumu gibi bilgileri girilir.

    Label(  # sağdaki çerçeve içerisinde parola tekrarı bilgisi için label oluşturulur.
        right_frame,
        text="Parola Tekrar:",
        bg='#F2EABD',
        font=f
    ).grid(row=6, column=0, sticky=W, pady=10)  # ve labelın yazısı, arka plan rengi, konumu gibi bilgileri girilir.

    gender_frame = LabelFrame(  # cinsiyet bilgisi için sağdaki çerçeveye bir çerçeve eklenir.
        right_frame,
        bg='#F7EA72',
        padx=10,
        pady=10,
    )  # çerçevenin yazısı, arka plan rengi, konumu gibi bilgileri girilir.

    register_name = Entry(
        right_frame,
        font=f
    )  # kayıt ismi girilmesi için bir yazı alanı oluşturulur.
    # bu giriş yerinin konum ve font bilgileri girilir.
    register_email = Entry(
        right_frame,
        font=f
    )  # kayıt emaili girilmesi için bir yazı alanı oluşturulur.
    # bu giriş yerinin konum ve font bilgileri girilir.
    register_mobile = Entry(
        right_frame,
        font=f
    )  # kayıt oluştururken telefon girilmesi için bir yazı alanı oluşturulur.
    # bu giriş yerinin konum ve font bilgileri girilir.
    male_rb = Radiobutton(
        gender_frame,
        text='Erkek',
        bg='#F7EA72',
        variable=var,
        value='Erkek',
        font=('Times', 10),

    )  # kayıt oluştururken cinsiyet seçimi için 'gender_frame' çerçevesine, 'erkek' değerinde radyobuton oluşturulur.
    # bu radyobutonun yazı stili, renk, konum ve font bilgileri girilir.
    female_rb = Radiobutton(
        gender_frame,
        text='Kadin',
        bg='#F7EA72',
        variable=var,
        value='Kadin',
        font=('Times', 10),

    )  # kayıt oluştururken cinsiyet seçimi için 'gender_frame' çerçevesine, 'kadın' değerinde radyobuton oluşturulur.
    # bu radyobutonun yazı stili, renk, konum ve font bilgileri girilir.
    others_rb = Radiobutton(
        gender_frame,
        text='Belirtmek istemiyorum',
        bg='#F7EA72',
        variable=var,
        value='Belirtmek istemiyorum',
        font=('Times', 10)

    )  # kayıt oluştururken cinsiyet seçimi için 'gender_frame' çerçevesine, 'diğer' değerinde radyobuton oluşturulur.
    # bu radyobutonun yazı stili, renk, konum ve font bilgileri girilir.
    register_country = OptionMenu(  # sağdaki çerçevede şehir seçimi için bir seçenek menüsü oluşturulur.

        right_frame,
        variable,
        *countries)
    # bu menünün konum, değer ve hangi listeden bilgi alacağı bilgileri girilir.
    register_country.config(
        bg='#F7EA72',
        width=15,
        font=('Times', 12)
    )  # bu menünün renk, büyüklük ve font bilgileri girilir.
    register_pwd = Entry(
        right_frame,
        font=f,
        show='*'
    )  # kayıt oluşturken parola girilmesi için bir yazı alanı oluşturulur.
    # bu giriş yerinin konum, font ve giriş yazı girldiğinde hangi karakterin görüleceği bilgileri girilir.
    pwd_again = Entry(
        right_frame,
        font=f,
        show='*'
    )  # kayıt oluşturken parola tekrarının girilmesi için bir yazı alanı oluşturulur.
    # bu giriş yerinin konum, font ve giriş yazı girldiğinde hangi karakterin görüleceği bilgileri girilir.
    register_btn = Button(  # sağ çerçevede kayıt olma butonu oluşturulur.
        right_frame,
        bg='#F7EA72',
        width=15,
        text='Kayit Ol',
        font=f,
        relief=SOLID,
        cursor='hand2',
        command=insert_record
    )  # butonun konumu, büyüklüğü, rengi, yazısı, fontu, basıldığında hangi fonksiyonu çalıştıracağı bilgileri girilir.

    email_tf.grid(row=0, column=1, pady=10,
                  padx=20)  # giriş için email yazı girişi alanının konum bilgileri oluşturulur.
    pwd_tf.grid(row=1, column=1, pady=10,
                padx=20)  # giriş için parola yazı girişi alanının konum bilgileri oluşturulur.
    login_btn.grid(row=2, column=1, pady=10, padx=20)  # giriş yapma butonunun konum bilgileri oluşturulur.
    left_frame.place(x=50, y=50)  # sol çerçevenin boyut bilgileri girilir.

    register_name.grid(row=0, column=1, pady=10,
                       padx=20)  # kayıt oluştururken isim değeri için yazı girişi alanının konum bilgileri oluşturulur.
    register_email.grid(row=1, column=1, pady=10,
                        padx=20)  # kayıt oluştururken email değeri için yazı girişi alanının konum bilgileri oluşturulur.
    register_mobile.grid(row=2, column=1, pady=10,
                         padx=20)  # kayıt oluştururken telefon numarası için yazı girişi alanının konum bilgileri oluşturulur.
    register_country.grid(row=4, column=1, pady=10,
                          padx=20)  # kayıt oluştururken şehir değeri için yazı girişi alanının konum bilgileri oluşturulur.
    register_pwd.grid(row=5, column=1, pady=10,
                      padx=20)  # kayıt oluştururken parola değeri için yazı girişi alanının konum bilgileri oluşturulur.
    pwd_again.grid(row=6, column=1, pady=10,
                   padx=20)  # kayıt oluştururken parola tekrar değeri için yazı girişi alanının konum bilgileri oluşturulur.
    register_btn.grid(row=7, column=1, pady=10, padx=20)  # kayıt oluşturma butonunun konum bilgileri oluşturulur.
    right_frame.place(x=500, y=50)  # sağ çerçevenin boyut bilgileri girilir.

    gender_frame.grid(row=3, column=1, pady=10, padx=20)  # 'gender_frame' çerçevesinin konum bilgileri oluşturulur.
    male_rb.pack(expand=True, side=LEFT)  # radiobutonda 'erkek' seçiminin konum bilgileri girilir.
    female_rb.pack(expand=True, side=LEFT)  # radiobutonda 'kadın' seçiminin konum bilgileri girilir.
    others_rb.pack(expand=True, side=LEFT)  # radiobutonda 'diğer' seçiminin konum bilgileri girilir.

    ws.mainloop()  # kodun sınırsız döngü olarak çalışması için mainloop() yazılır.


def sayfa():  # alışveriş ekranı için fonksiyon oluşturulur.
    def connection():  # database'in kullanımı için fonksiyon oluşturulur.
        connectObj = db.connect("shopManagement.db")  # alışveriş bilgilerinin tutulduğu database oluşturulur.
        cur = connectObj.cursor()  # database'in kullanımı için database'de imleç oluşturulur.
        sql = '''
        create table if not exists sellings (
            date string,
            product string,
            price number,
            quantity number,
            total number
            )
        '''  # selling adında bir tablo yoksa oluşturulur ve yukarıdaki başlıkların sutünları oluşur.
        cur.execute(sql)  # sql değişkenindeki bilgiler database'e girilir.
        connectObj.commit()  # tablonun içeriği databese'e işlenir.

    connection()  # database'in kullanımı için yazılan fonksiyon çağırılır.
    window = Tk()  # Tk() sınıfından 'window' adında bir obje oluşturulur.
    window.title("QR Kodla Hizli Alisveris")  # objenin başlığı oluşturulur.
    tabs = ttk.Notebook(window)  # oluşturulan objede çerçeve değişkeni oluşturulur.
    frame_style = ttk.Style()  # çerçevenin stili için bir değişken oluşturulur.
    frame_style.configure('TFrame', background='#EB910C')  # çerçeve stili bilgileri girilir.
    root = ttk.Frame(tabs, style='Frame1.TFrame')  # oluşturulan tab menünün ilk çerçevesi için değişken oluşturulur.
    tabs.add(root, text='Alisveris')  # tab menünün ilk çerçevesinin bilgileri girilir.
    tabs.pack(expand=1, fill="both")  # tab menünün ilk çerçevesinin konum bilgileri girilir.

    # ----------------------------------------------tab1 ----------------------------------
    global billarea  # fatura değişkeni fonksiyon dışında da kullanabilmek için global olarak tanımlanır.

    def GenerateBill():  # fatura oluşturma fonksiyonu yazılır.
        connectObj = db.connect("shopManagement.db")  # alışveriş bilgilerinin tutulduğu database açılır.
        cur = connectObj.cursor()  # database'in kullanımı için database'de imleç oluşturulur.

        if p1quantity.get() == 0 and p2quantity.get() == 0 and p3quantity.get() == 0 and p4quantity.get() == 0 \
                and p5quantity.get() == 0 and p6quantity.get() == 0 and p7quantity.get() == 0 and p8quantity.get() == 0:
            # herhangi bir ürünün adet değeri 0'a eşitse
            messagebox.showerror("Hata!", "Hicbir urun eklenmedi!")  # ekrana hata mesajı verilir.
        else:  # bunun dışındaki durumlarda
            billarea.delete('1.0', END)  # fatura ekranı oluşturulur.
            billarea.insert(END, "Tarih\t Urunler \tFiyat Adet\t   Toplam")  # fatura ekranı oluşturulur.
            billarea.insert(END, "\n==========================================")  # fatura ekranı oluşturulur.

            price = []  # tutar değerlerinin tutulacağı liste oluşturulur.
            for i in price:
                i = +1  # liste içerisindeki değerler birbirine eşitlenir.
                price = IntVar()  # atanılacak değişkenler integer olarak tanımlanır.

            weight = []  # ağırlık değerlerinin tutulacağı liste oluşturulur.
            for j in weight:
                j = +1  # liste içerisindeki değerler birbirine eşitlenir.
                weight = IntVar()  # atanılacak değişkenler integer olarak tanımlanır.

            print(dateE.get())
            price1 = price2 = price3 = price4 = price5 = price6 = price7 = price8 = 0 # Tum fiyatlar sifira esitlenir.
            weight1 = weight2 = weight3 = weight4 = weight5 = weight6 = weight7 = weight8 = 0 # tum agirliklar sifira esitlenir.
            if p1quantity.get() != 0: # Miktar sifira esit olmadigi sürece islem yapilir.
                price1 = p1quantity.get() * p1price.get() # Toplam price1 hesaplanir.
                weight1 = p1quantity.get() * p1weight.get() # Toplam weigth1 hesaplanir.
                # print(price)
                billarea.insert(END, f"\n{dateE.get()}\t Urun-1 \t{p1price.get()}\t {p1quantity.get()}\t {price1}") # birinci urunun
                # deegerleri listeye ekler.
                sql = '''
                INSERT INTO Sellings VALUES 
                (?, ?, ?, ?,?)
                '''
                cur.execute(sql, (dateE.get(), 'Urun-1', p1price.get(), p1quantity.get(), price1)) # Veriler ( urun1) veritabanina eklenir.
                connectObj.commit()
            if p2quantity.get() != 0: # Miktar2 sifira esit olmadigi sürece islem yapilir.
                price2 = p2quantity.get() * p2price.get() # Toplam price2 hesaplanir.
                weight2 = p2quantity.get() * p2weight.get() # Toplam weigth2 hesaplanir.
                # print(price2)
                billarea.insert(END, f"\n{dateE.get()}\t Urun-2 \t{p2price.get()}\t {p2quantity.get()}\t {price2}") # Degerleri (ikinci) listeye ekler.
                sql = '''
                INSERT INTO Sellings VALUES 
                (?, ?, ?, ?,?)
                '''
                # print(dateE.get(), 'Product-2', p2price.get(), p2quantity.get(), price2)
                cur.execute(sql, (dateE.get(), 'Urun-2', p2price.get(), p2quantity.get(), price2)) # Veriler (urun 2) veritabanina eklenir.
                connectObj.commit()
            if p3quantity.get() != 0: # Miktar3 sifira esit olmadigi sürece islem yapilir.
                price3 = p3quantity.get() * p3price.get() # Toplam price3 hesaplanir.
                weight3 = p3quantity.get() * p3weight.get() # Toplam weigth3 hesaplanir.
                # print(price3)
                billarea.insert(END, f"\n{dateE.get()}\t Urun-3 \t{p3price.get()}\t {p3quantity.get()}\t {price3}")
                sql = '''
                INSERT INTO Sellings VALUES 
                (?, ?, ?, ?,?)
                '''
                cur.execute(sql, (dateE.get(), 'Urun-3', p3price.get(), p3quantity.get(), price3))# Veriler (urun 2) veritabanina eklenir.
                connectObj.commit()
            if p4quantity.get() != 0: # Miktar4 sifira esit olmadigi sürece islem yapilir.
                price4 = p4quantity.get() * p4price.get()  # Toplam price4 hesaplanir.
                weight4 = p4quantity.get() * p4weight.get() # Toplam weigth4 hesaplanir.
                billarea.insert(END, f"\n{dateE.get()}\t Urun-4 \t{p4price.get()}\t {p4quantity.get()}\t {price4}")
                sql = '''
                INSERT INTO Sellings VALUES 
                (?, ?, ?, ?,?)
                '''
                cur.execute(sql, (dateE.get(), 'Urun-4', p4price.get(), p4quantity.get(), price4))  # Veriler (urun 4) veritabanina eklenir.
                connectObj.commit()
            if p5quantity.get() != 0: # Miktar5 sifira esit olmadigi sürece islem yapilir.
                price5 = p5quantity.get() * p5price.get() # Toplam price5 hesaplanir.
                weight5 = p5quantity.get() * p5weight.get()# Toplam weigth5 hesaplanir.
                # print(price)
                billarea.insert(END, f"\n{dateE.get()}\t Urun-5 \t{p5price.get()}\t {p5quantity.get()}\t {price5}")
                sql = '''
                INSERT INTO Sellings VALUES 
                (?, ?, ?, ?,?)
                '''
                cur.execute(sql, (dateE.get(), 'Urun-5', p5price.get(), p5quantity.get(), price5))  # Veriler (urun 5) veritabanina eklenir.
                connectObj.commit()
                connectObj.commit()
            if p6quantity.get() != 0:  # Miktar6 sifira esit olmadigi sürece islem yapilir.
                price6 = p6quantity.get() * p6price.get() # Toplam price6 hesaplanir.
                weight6 = p6quantity.get() * p6weight.get() # Toplam weigth6 hesaplanir.
                # print(price2)
                billarea.insert(END, f"\n{dateE.get()}\t Urun-6 \t{p6price.get()}\t {p6quantity.get()}\t {price6}")
                sql = '''
                INSERT INTO Sellings VALUES 
                (?, ?, ?, ?,?)
                '''
                # print(dateE.get(), 'Product-6', p6price.get(), p6quantity.get(), price6)
                cur.execute(sql, (dateE.get(), 'Urun-6', p6price.get(), p6quantity.get(), price6)) # veriler (urun 6) veritabanina eklenir.
                connectObj.commit()
            if p7quantity.get() != 0:  # Miktar7 sifira esit olmadigi sürece islem yapilir.
                price7 = p7quantity.get() * p7price.get() # Toplam price7 hesaplanir.
                weight6 = p7quantity.get() * p7weight.get() # Toplam weigth7 hesaplanir.
                # print(price2)
                billarea.insert(END, f"\n{dateE.get()}\t Urun-7 \t{p7price.get()}\t {p7quantity.get()}\t {price7}")
                sql = '''
                INSERT INTO Sellings VALUES 
                (?, ?, ?, ?,?)
                '''
                # print(dateE.get(), 'Product-6', p6price.get(), p6quantity.get(), price6)
                cur.execute(sql, (dateE.get(), 'Urun-7', p7price.get(), p7quantity.get(), price7)) # Veriler (urun 7) veritabanina eklenir.
                connectObj.commit()
            if p8quantity.get() != 0: # Miktar8 sifira esit olmadigi sürece islem yapilir.
                price8 = p8quantity.get() * p8price.get() # Toplam price8 hesaplanir.
                weight8 = p8quantity.get() * p8weight.get() # Toplam weigth8 hesaplanir.
                # print(price2)
                billarea.insert(END, f"\n{dateE.get()}\t Urun-8 \t{p8price.get()}\t {p8quantity.get()}\t {price8}")
                sql = '''
                INSERT INTO Sellings VALUES 
                (?, ?, ?, ?,?)
                '''
                # print(dateE.get(), 'Product-2', p2price.get(), p2quantity.get(), price2)
                cur.execute(sql, (dateE.get(), 'Urun-8', p8price.get(), p8quantity.get(), price8)) # Veriler (urun 7) veritabanina eklenir.
                connectObj.commit()

            global Totalprice # Totalprice ve Total weight global olarak tanimlanir.
            global Totalweight
            Totalprice = IntVar() # Totalprice, Intvar fonksiyonunda integer deger olarak tutulur.
            Totalprice = price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8 #Toplam fiyat hesaplanir.
            Totalweight = IntVar() # Totalweight, Intvar fonksiyonunda integer deger olarak tutulur.
            Totalweight = weight1 + weight2 + weight3 + weight4 + weight5 + weight6 + weight7 + weight8 # Toplam agirlik hesaplanir.
            Totalquantity = IntVar() # Totalquantity, Intvar fonksiyonunda integer deger olarak tutulur.
            Totalquantity = p1quantity.get() + p2quantity.get() + p3quantity.get() + p4quantity.get() + p5quantity.get() \
                            + p6quantity.get() + p7quantity.get() + p8quantity.get() # Toplam urun miktari hesaplanir.
            billarea.insert(END, "\n------------------------------------------\n")
            billarea.insert(END, f"Total \t \t  \t {Totalquantity}\t {Totalprice}") # Degerler ana ekrana eklenir.

            with open('payment.csv', 'w') as file: # payement adinda bir cvs dosyasi qr kodda kulllanilicak veriler aktarilmak uzere olusturulur.

                writer = csv.writer(file)
                liste = [Totalprice] # Toplam fiyat verileri tutulmak üzere bir liste olusturulur.
                liste1 = [Totalweight] # Toplam fiyat verileri tutulmak üzere bir liste olusturulur.
                writer.writerow(liste) # Cvs dosyaya tek satir olarak yazdirilir.
                writer.writerow(liste1) # Cvs dosyaya tek satir olarak yazdirilir.
            createQRCode() # QR kod olusturulur.

    def createQRCode(): # QR kodun olusturlulmasi icin createQRCode fonksiyonu olusturulur.
        global Totalprice
        global Totalweight
        total = f'''
                Toplam Fiyat: {Totalprice} TL \n
                Toplam Agirlik: {Totalweight} gr   
                '''
        image = pyqrcode.create(total)
        image.png("payment.png", scale="5") # Olusturulan qr kod png olarak kaydedilir.

        print(total)

    def view():
        connectObj = db.connect("shopManagement.db") # Alisveris verileri yazilmak üzere shopManagement adinda bir veri tabani olusturulur.
        cur = connectObj.cursor()
        sql = 'Select * from Sellings'
        cur.execute(sql) # Veriler veri tabanina eklenir.
        rows = cur.fetchall()
        viewarea.insert(END, f"Tarih\t\tUrun\tAdet Fiyati\t  Adet \t Toplam Fiyat\n")

        for i in rows: # For dongusu kullanilirak ekran duzenlenir.
            allrows = ""
            for j in i:
                allrows += str(j) + '       '
            allrows += '\n'
            viewarea.insert(END, allrows)

    dateL = Label(root, text="Tarih", bg="#EB910C", width=12, font=('arial', 15, 'bold')) # Ana ekranda Tarih yazisinin boyutu vs. ayarlanir.
    dateL.grid(row=0, column=0, padx=7, pady=7) # Traih yazisinin ekrandaki konumu belirlenir.
    dateE = DateEntry(root, width=12, font=('arial', 15, 'bold')) # Tarih girdisinin  yazi tipi vs. ayarlanir.
    dateE.grid(row=0, column=1, padx=7, pady=7) # Ekrandaki konum belirlenir.
    l = Label(root, text="Urunler", font=('arial', 15, 'bold'), bg="#F2EABD", width=12) # Ana ekranda Urunler yazisinin boyutu vs. ayarlanir.
    l.grid(row=1, column=0, padx=7, pady=7)
    l = Label(root, text="Fiyat", font=('arial', 15, 'bold'), bg="#F2EABD", width=12) # Ana ekranda Fiyat yazisinin boyutu vs. ayarlanir.
    l.grid(row=1, column=1, padx=7, pady=7)
    l = Label(root, text="Adet", font=('arial', 15, 'bold'), bg="#F2EABD", width=12) # Ana ekranda Adet yazisinin boyutu vs. ayarlanir.
    l.grid(row=1, column=2, padx=7, pady=7)

    # ---- URUN 1 ----------------------------------------------------
    p1name = StringVar() # Isim bilgiisi string olarak StringVar fonksiyonunda tutulur.
    p1name.set('Urun1') # Urun1 yazisi ana ekrana bastirilir.
    p1price = IntVar() # Fiyat degeri integer olarak IntVar fonksiyonuda tutulur.
    p1price.set(100) # Urun1'in ekrandaki konumunu belirler.
    p1weight = IntVar() # Urun1' in agirlik degeri integer olarak IntVar fonksiyonuda tutulur.
    p1weight.set(10)
    p1quantity = IntVar() # Urun1' in miktar degeri integer olarak IntVar fonksiyonuda tutulur.
    p1quantity.set(0)
    l = Label(root, text=p1name.get(), font=('arial', 15, 'bold'), width=12) #Urun1 in isim bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=2, column=0, padx=7, pady=7) # Ekrandaki konumu belirlenir.
    l = Label(root, text=p1price.get(), font=('arial', 15, 'bold'), width=12)#Urun1 in fiyat bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=2, column=1, padx=7, pady=7)
    t = Entry(root, textvariable=p1quantity, font=('arial', 15, 'bold'), width=12)#Urun1 in miktar bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    t.grid(row=2, column=2, padx=7, pady=7)

    # ---- URUN 2 -------------------------------------------------------------
    p2name = StringVar() # Isim bilgiisi string olarak StringVar fonksiyonunda tutulur.
    p2name.set('Urun2') # Urun2 yazisi ana ekrana bastirilir.
    p2price = IntVar()# Fiyat degeri integer olarak IntVar fonksiyonuda tutulur.
    p2price.set(200) # Urun2'in ekrandaki konumunu belirler.
    p2weight = IntVar() # Urun2' in agirlik degeri integer olarak IntVar fonksiyonuda tutulur.
    p2weight.set(20)
    p2quantity = IntVar()# Urun2' in miktar degeri integer olarak IntVar fonksiyonuda tutulur.
    p2quantity.set(0)
    l = Label(root, text=p2name.get(), font=('arial', 15, 'bold'), width=12) #Urun2 in isim bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=3, column=0, padx=7, pady=7)
    l = Label(root, text=p2price.get(), font=('arial', 15, 'bold'), width=12) #Urun2 in fiyat bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=3, column=1, padx=7, pady=7) # Ekrandaki konumu belirlenir.
    t = Entry(root, textvariable=p2quantity, font=('arial', 15, 'bold'), width=12)#Urun2 in miktar bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    t.grid(row=3, column=2, padx=7, pady=7)

    # ---- URUN 3 -----------------------------------------------------
    p3name = StringVar()
    p3name.set('Urun3') # Urun3 yazisi ana ekrana bastirilir.
    p3price = IntVar() # Fiyat degeri integer olarak IntVar fonksiyonuda tutulur.
    p3price.set(300) # Urun3'un ekrandaki konumunu belirler.
    p3weight = IntVar() # Urun3' un agirlik degeri integer olarak IntVar fonksiyonuda tutulur.
    p3weight.set(30)
    p3quantity = IntVar()# Urun3' un miktar degeri integer olarak IntVar fonksiyonuda tutulur.
    p3quantity.set(0)
    l = Label(root, text=p3name.get(), font=('arial', 15, 'bold'), width=12) #Urun3 un isim bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=4, column=0, padx=7, pady=7)
    l = Label(root, text=p3price.get(), font=('arial', 15, 'bold'), width=12) #Urun3 un fiyat bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=4, column=1, padx=7, pady=7)
    t = Entry(root, textvariable=p3quantity, font=('arial', 15, 'bold'), width=12) #Urun3 un miktar bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    t.grid(row=4, column=2, padx=7, pady=7)

    # ---- URUN 4 ----------------------------------------------
    p4name = StringVar()
    p4name.set('Urun4') # Urun4 yazisi ana ekrana bastirilir.
    p4price = IntVar() # Fiyat degeri integer olarak IntVar fonksiyonuda tutulur.
    p4price.set(400) # Urun4'un ekrandaki konumunu belirler.
    p4weight = IntVar() # Urun4' un agirlik degeri integer olarak IntVar fonksiyonuda tutulur.
    p4weight.set(40)
    p4quantity = IntVar() # Urun4' un miktar degeri integer olarak IntVar fonksiyonuda tutulur.
    p4quantity.set(0)
    l = Label(root, text=p4name.get(), font=('arial', 15, 'bold'), width=12)#Urun4 un isim bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=5, column=0, padx=7, pady=4)
    l = Label(root, text=p4price.get(), font=('arial', 15, 'bold'), width=12)#Urun4 un fiyat bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=5, column=1, padx=7, pady=4)
    t = Entry(root, textvariable=p4quantity, font=('arial', 15, 'bold'), width=12)#Urun4 un miktar bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    t.grid(row=5, column=2, padx=7, pady=4)

    # ---- URUN 5 --------------------------------------------------
    p5name = StringVar()
    p5name.set('Urun5') # Urun5 yazisi ana ekrana bastirilir.
    p5price = IntVar() # Fiyat degeri integer olarak IntVar fonksiyonuda tutulur.
    p5price.set(500) # Urun5 in ekrandaki konumunu belirler.
    p5weight = IntVar() # Urun5 in agirlik degeri integer olarak IntVar fonksiyonuda tutulur.
    p5weight.set(50)
    p5quantity = IntVar() # Urun5 in miktar degeri integer olarak IntVar fonksiyonuda tutulur.
    p5quantity.set(0)
    l = Label(root, text=p5name.get(), font=('arial', 15, 'bold'), width=12)#Urun5 in isim bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=6, column=0, padx=7, pady=4)
    l = Label(root, text=p5price.get(), font=('arial', 15, 'bold'), width=12)#Urun5 in fiyat bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=6, column=1, padx=7, pady=4)
    t = Entry(root, textvariable=p5quantity, font=('arial', 15, 'bold'), width=12)#Urun5 in miktar bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    t.grid(row=6, column=2, padx=7, pady=4)

    # ---- URUN 6 -------------------------------------------------------------
    p6name = StringVar()
    p6name.set('Urun6')  # Urun6 yazisi ana ekrana bastirilir.
    p6price = IntVar() # Fiyat degeri integer olarak IntVar fonksiyonuda tutulur.
    p6price.set(600)  # Urun6 nin ekrandaki konumunu belirler.
    p6weight = IntVar()  # Urun6 nin agirlik degeri integer olarak IntVar fonksiyonuda tutulur.
    p6weight.set(60)
    p6quantity = IntVar()  # Urun6 nin miktar degeri integer olarak IntVar fonksiyonuda tutulur.
    p6quantity.set(0)
    l = Label(root, text=p6name.get(), font=('arial', 15, 'bold'), width=12)#Urun6 nin isim bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=7, column=0, padx=7, pady=7)
    l = Label(root, text=p6price.get(), font=('arial', 15, 'bold'), width=12)#Urun6 nin fiyat bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=7, column=1, padx=7, pady=7)
    t = Entry(root, textvariable=p6quantity, font=('arial', 15, 'bold'), width=12)#Urun6 nin miktar bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    t.grid(row=7, column=2, padx=7, pady=7)

    # ---- URUN 7-------------------------------------------------------------
    p7name = StringVar()
    p7name.set('Urun7') # Urun7 yazisi ana ekrana bastirilir.
    p7price = IntVar() # Fiyat degeri integer olarak IntVar fonksiyonuda tutulur.
    p7price.set(700)  # Urun7 nin ekrandaki konumunu belirler.
    p7weight = IntVar() # Urun7 nin agirlik degeri integer olarak IntVar fonksiyonuda tutulur.
    p7weight.set(70)
    p7quantity = IntVar() # Urun7 nin miktar degeri integer olarak IntVar fonksiyonuda tutulur.
    p7quantity.set(0)

    l = Label(root, text=p7name.get(), font=('arial', 15, 'bold'), width=12)#Urun7 nin isim bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=8, column=0, padx=7, pady=7)
    l = Label(root, text=p7price.get(), font=('arial', 15, 'bold'), width=12)#Urun7 nin fiyat bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=8, column=1, padx=7, pady=7)
    t = Entry(root, textvariable=p7quantity, font=('arial', 15, 'bold'), width=12)#Urun7 nin miktar bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    t.grid(row=8, column=2, padx=7, pady=7)

    # ---- URUN 8 ----------------------------------------------------
    p8name = StringVar()
    p8name.set('Urun8') # Urun8 yazisi ana ekrana bastirilir.
    p8price = IntVar()  # Fiyat degeri integer olarak IntVar fonksiyonuda tutulur.
    p8price.set(800) # Urun8 in ekrandaki konumunu belirler.
    p8weight = IntVar() # Urun7 in agirlik degeri integer olarak IntVar fonksiyonuda tutulur.
    p8weight.set(80)
    p8quantity = IntVar()  # Urun8 in miktar degeri integer olarak IntVar fonksiyonuda tutulur.
    p8quantity.set(0)
    l = Label(root, text=p8name.get(), font=('arial', 15, 'bold'), width=12)#Urun8 in isim bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=9, column=0, padx=7, pady=7)
    l = Label(root, text=p8price.get(), font=('arial', 15, 'bold'), width=12)#Urun8 in fiyat bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    l.grid(row=9, column=1, padx=7, pady=7)
    t = Entry(root, textvariable=p8quantity, font=('arial', 15, 'bold'), width=12)#Urun8 in miktar bilgileri alinir ve yazi tipi, boyut gibi ozellikleri belirlenir.
    t.grid(row=9, column=2, padx=7, pady=7) # Ekrandaki konumu ayarlanir.

    def cikis(): # Bu fonksion kullaniciların sistemden cikis yapabilmelerini saglamak icin olusturulmustur.

        messagebox.showinfo('**IYI GUNLER** ', "Giris ekranina yonlendiriliyorsunuz...")
        window.destroy()
        giris() # Cikis yapildiginda tekrar giris ekranina dönülür.

    # ------------------------ FATURA -------------------------
    cikisbtn = Button(root, command=cikis, text="Cikis",
                      font=('arial', 15, 'bold'), bg='#EB310C', width=5) # Cikis butonunun rengi, boyutu vs ayarlanır.
    cikisbtn.grid(row=0, column=2, padx=7, pady=7) # Ekrandaki konumu ayarlanir.
    billarea = Text(root)
    submitbtn = Button(root, command=GenerateBill, text="Fatura ve QR Kod Oluştur", # Butonun islevi GenerateBill fonksiyonu eklenerekbelirlenir.
                       font=('arial', 15, 'bold'), bg='#F2EABD', width=25)  # Fatura QR kod olustur butonunun rengi, boyutu vs ayarlanır.
    submitbtn.grid(row=10, column=0, padx=7, pady=7)
    viewbtn = Button(root, command=view, text="Gecmis Alisverisler", # Gecmis Alisverisler butonuna view fonksiyonu eklenerek islevi ayarlanir.
                     font=('arial', 15, 'bold'), bg='#F2EABD', width=20) # Butonun rengi, boyutu vs ayarlanır.
    viewbtn.grid(row=10, column=2, padx=7, pady=7)

    billarea.grid(row=13, column=0, padx=7, pady=7) # Sonuclarin ekrana yazildigi text area düzenlenir.
    viewarea = Text(root)
    viewarea.grid(row=13, column=2, padx=7, pady=7)

    window.mainloop() # window ekrani cagirilarak tum islemlerin gerceklestirilmesi saglanir.


giris() # giris fonksiyonu cagirilarak tum islemlerin gerceklestirilmesi saglanir.