print("*-Bilet Sistemi-*")
Seçim=str(input("Sinema veya Tiyatro seçimini yapınız :"))

Kişi=str(input("Kaç kişiniz? :"))
Öğrenci=str(input("Öğrenci misiniz? :"))
fiyat=0


#halk
if Seçim =='Tiyatro' or Seçim=='tiyatro' or Seçim=='TİYATRO':
    fiyat=30#tiyatro
elif Seçim =='Sinema' or Seçim=='sinema'or Seçim=='SİNEMA':
    fiyat=20#sinema
elif Seçim=='Tiyatro ve Sinema' or Seçim=='sinema ve tiyatro' or Seçim=='Sinema ve Tiyatro' or Seçim=='tiyatro ve sinema' or Seçim=='Tiyatro ve Sinema' or Seçim=='TİYATRO VE SİNEMA' or Seçim=='SİNEMA VE TİYATRO':
    fiyat=50 #sinema ve tiyatro""""""""""""""""""""""""""""""


fiyat *=int (Kişi)

#öğrenci indirimi
if Öğrenci== 'Evet' or Öğrenci=='evet' :
 fiyat=fiyat/2 #Yarı Fiyat
 print("--Vermeniz Gereken Ücret--:", fiyat)
else:
    print("--Vermeniz Gereken Ücret--:",fiyat,"Tl")