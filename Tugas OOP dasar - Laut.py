# TUBES PBO || Muhammad Hafidz Darul Quro || 1103223052 || TK-46-05

import pandas as pd

from abc import ABC,abstractmethod 
import matplotlib.pyplot as plt
import wikipedia 
import secrets 
import string
import numpy as np
from colorama import Fore, Back, Style
from tabulate import tabulate, SEPARATING_LINE

wikipedia.set_lang("id")

data = {
    'No' :[1,2,3,4,5],
    'Nama':['Tuna','Salmon','Kepiting','Gurita','Udang'],
    'Kualitas':[5,5,3,5,5],
    'Harga':[1000,3000,1500,2000,750],
    'Stok':[10,20,15,25,50]
}

data1={
    'Nama':['Tuna','Salmon','Kepiting','Gurita','Udang'],
    'Stok':[30,50,5,5,100]
}

data2={
    'Nama':['Tuna','Salmon','Kepiting','Gurita','Udang'],
    'Stok':[10,30,20,10,10]
}

years_data = {
    'Year': [2011, 2012, 2013, 2014, 2015]
}

df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df_years = pd.DataFrame(years_data)
df.index = df.index + 1
df1.index = df1.index + 1
df2.index = df2.index + 1
df.to_csv('datahasillaut.csv',index=False)
df1.to_csv('Stok_2012.csv',index=False)
df2.to_csv('Stok_2013.csv',index=False)

class Laut() :
    
    def __init__ (self,nama,nim,kelas) :
        self.__nama=nama
        self.__nim=nim
        self.__kelas=kelas

    def User(self) :
        print('')
        print(Style.DIM + 'The Creator : ')
        print(Style.DIM + self.__nama)
        print(Style.DIM + self.__nim)
        print(Style.DIM + self.__kelas)
        print(Style.RESET_ALL)
        print('')
        print("======    Selamat datang di Perusahaan SeaVerything!     ======") 
        print('')


    def Stop(self) :
        print('')
        print('========  Terimakasih sudah menggunakan layanan kami!  ========')
        print('')
    
    @abstractmethod
    def TampilCSV(self) :
        pass

class Rinci_Laut() :
    def menu(self) :
        while True :
            print('')
            print('========                    MENU                       ========')
            print('')
            print('1. Samudra Hindia')
            print('2. Samudra Pasifik')
            print('3. Samudra Atlantik')
            print('4. Samudra Selatan')
            print('5. Samudra Arktik')
            print('6. Stop Menu')
            print('')
            ipm=int(input(("Masukkan Pilihan yang anda inginkan (1,2,3,4,5,6) : ")))
            print('')
            if ipm == 1 :
                tdl.SamudraHindia()
            elif ipm == 2 :
                tdl.SamudraPasifik()
            elif ipm == 3 :
                tdl.SamudraAtlantik()
            elif ipm == 4 :
                tdl.SamudraSelatan()
            elif ipm == 5 :
                tdl.SamudraArktik()
            elif ipm == 6 :
                break

    def SamudraHindia(self):
        resultHindia = wikipedia.summary("Samudra_Hindia", sentences = 3)
        print(resultHindia) 

    def SamudraPasifik(self):
        resultPasifik = wikipedia.summary("Samudra_Pasifik", sentences = 3) 
        print(resultPasifik) 

    def SamudraAtlantik(self):
        resultAtlantik = wikipedia.summary("Samudra_Atlantik", sentences = 3) 
        print(resultAtlantik) 

    def SamudraSelatan(self):
        resultSelatan = wikipedia.summary("Samudra_Selatan", sentences = 3) 
        print(resultSelatan)

    def SamudraArktik(self):
        resultArktik = wikipedia.summary("Samudra_Arktik", sentences = 3) 
        print(resultArktik)
        
    
class Hasil_laut(Laut) :
    def __init__ (self,namapembeli,*inputmenu):
        self.inputmenu = inputmenu
        self._namapembeli = namapembeli
    
    def Bukadata(self) :
        print('')
        print('========            Data Hasil Laut Perusahaan         ========')
        print('')
        print(df)
        print('')
    
        
    def Jualbeli(self) : 
        print('')
        print('========            Data Hasil Laut Perusahaan         ========')
        print('')
        print(df)
        print('')

        jenisbeli=int(input('Jenis yang ingin anda beli (1,2,3,4,5)): '))
        jmlbeli=int(input("Masukkan jumlah hasil laut yang ingin anda beli : "))
        print('')

        for i in range(len(df)) :
            kualitas = df.at[jenisbeli, 'Kualitas']
            harga = df.at[jenisbeli, 'Harga']
            stok = df.at[jenisbeli, 'Stok'] - jmlbeli

            if jenisbeli == 0 :
                ttl=jmlbeli*(harga*kualitas)
            elif jenisbeli == 1 :
                ttl=jmlbeli*(harga*kualitas)
            elif jenisbeli == 2 :
                ttl=jmlbeli*(harga*kualitas)
            elif jenisbeli == 3 :
                ttl=jmlbeli*(harga*kualitas)
            elif jenisbeli == 4 :
                ttl=jmlbeli*(harga*kualitas)
            else : 
                print('Tolong input dengan sesuai angka yang tersedia!')
                jenisbeli=int(input('Jenis yang ingin anda beli (1,2,3,4,5): '))
        df.at[jenisbeli, 'Stok'] = stok
        ttls=ttl
        
        alphabet = string.ascii_letters + string.digits 
        cu = ''.join(secrets.choice(alphabet) for i in range(10)) 

        print('')
        print('========        Berikut rincian transaksi anda !       =======')
        print('')
        clmndata = [[cu,self._namapembeli,df.at[jenisbeli, 'Nama'], df.at[jenisbeli, 'Harga'],str(jmlbeli),ttls,df.at[jenisbeli, 'Stok']]]
        dataclm = ["Kode Transaksi","Nama Pembeli","Nama Barang","Harga", "Jumlah","Total Harga","Stok sisa"]
        print(tabulate(clmndata,dataclm,tablefmt="psql",colalign=("center","center","center","center","center","center","center",)))
        print('')
    
    def TampilCSV(self) :
        print('')
        print('========== Berikut file dalam bentuk CSV ==========')
        print('')
        df.to_csv('datahasillaut.csv',index=False)
        lookdat=pd.read_csv('datahasillaut.csv')
        print(lookdat)
    
    def TampilPlt(self) :
        fig, ax = plt.subplots()

        bar_width = 0.25
        bar_positions = df_years['Year']
        bar1 = ax.bar(bar_positions - bar_width, df['Stok'], bar_width, label='Tahun 2011')
        bar2 = ax.bar(bar_positions, df1['Stok'], bar_width, label='Tahun 2012')
        bar3 = ax.bar(bar_positions + bar_width, df2['Stok'], bar_width, label='Tahun 2013')

        ax.set_xlabel('Tahun')
        ax.set_ylabel('Stok')
        ax.set_title('Perbandingan Stok per Tahun')

        def add_labels(bars, data):
            for i, rect in enumerate(bars):
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., height,
                        f"{data.at[i + 1, 'Nama']}\n{data.at[i + 1, 'Stok']}",
                        ha='center', va='bottom', rotation=0, color='black', fontsize=8)

        add_labels(bar1, df)
        add_labels(bar2, df1)
        add_labels(bar3, df2)

        ax.set_xticks(bar_positions)
        ax.set_xticklabels(df_years['Year'])

        plt.show()
    
    def TampilNil(self):
        sorted_data = df.sort_values(by='Harga', ascending=True)

        nilmax = np.max(sorted_data['Harga'], axis=0)
        nilmin = np.min(sorted_data['Harga'], axis=0)
        nilrat = np.mean(sorted_data['Harga'], axis=0)

        print(f'Harga Terendah dalam data  :{nilmin}')
        print(f'Harga Tertinggi dalam data :{nilmax}')
        print(f'Rata-rata Harga dalam data :{nilrat}')
    
    def Tambah(self,*args):
        i = len(df)
        databaru = {'No':args[0],'Nama' : args[1], 'Kualitas' : args[2] , 'Harga' : args[3] , 'Stok' : args[4]}
        df.loc[i+1] = databaru
        
        
if __name__ == "__main__":
    tmpillaut = Laut("Muhammad Hafidz Darul Quro",'1103223052','TK4605')
    tmpillaut.User()

    tdl = Rinci_Laut()

    while True:
        print('')
        print('========                    MENU                       ========')
        print('')
        print('1. Akses data hasil laut perusahaan tahun ini')
        print('2. Jual Beli Hasil Laut')
        print('3. Tampil data hasil laut perusahaan dalam bentuk CSV')
        print('4. Visualiasi data hasil laut menggunakan matplotlib')
        print('5. Melihat harga terendah, tertinggi dan rata-rata harga dari data hasil laut')
        print('6. Menampilkan Wikipedia dari masing-masing Samudra di dunia')
        print('7. Tambah data hasil laut perusahaan')
        print('0. Stop Menu')
        print('')
        inputmenu=int(input(("Masukkan Pilihan yang anda inginkan (1,2,3,4,5,6,7) : ")))
        print('')

        tmpilhsllaut = Hasil_laut('Jonathan',inputmenu)
        if inputmenu == 1 :
            tmpilhsllaut.Bukadata()
        elif inputmenu == 2 :
            tmpilhsllaut.Jualbeli()
        elif inputmenu == 3 :
            tmpilhsllaut.TampilCSV()
        elif inputmenu == 4 :
            tmpilhsllaut.TampilPlt()
        elif inputmenu == 5 :
            tmpilhsllaut.TampilNil()
        elif inputmenu == 6 :
            tdl.menu()
        elif inputmenu == 7 :
            tmpilhsllaut.Tambah(6,'Kerapu',2,3500,20)
        elif inputmenu == 0 :
            tmpillaut.Stop()
            break