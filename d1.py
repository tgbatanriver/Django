
#!DJANGO NEDİR ?

# Django, Python dilinde yazılmış, özgür ve açık kaynak kodlu 
# bir web çatısıdır(framework). Disqus, Instagram, Pinterest, and Mozilla gibi bir 
# çok büyük şirket Django’yu kullanmaktadır.

#Yani Php ile hazırlanan Wordpress, OpenCart, NukePHP gibi Django'da Python kodlarıyla
# geliştirilmiş bir araçtır diyebiliriz. Tam olarak Türkçe karşılığı
# terimi bulamıyoruz ancak kısa sürede web siteleri oluşturmanızı sağlar. 

#!KURULUM

#Pip yöntemi ile kurulum
#Pip python kütüphanelerini barındıran bir paket yönetim sistemidir. Node.js için npm, Ubuntu için apt neyse python için de pip odur. Paket yönetim sistemi nedir peki?
# Paket yönetim sistemi geliştiriciler tarafından hazırlanan o dile ya da yazılıma 
# ait kütüphaneleri tek komut kullanarak kolayca yükleyebilmenizi, güncelleyebilmenizi ve 
# isterseniz silebilmenizi sağlayan araçtır

#!Peki python pip’i ne zaman kullanacağız?

# Python django kütüphanesini kullanarak artık web uygulamaları geliştirmek istiyorsanız
#  o zaman önce işletim sitemimize pip uygulamasına ekleyip sonra da django kütüphanesini çekip 
#gerçekleştirebilirsiniz


#?UBUNTU

#sudo apt-get install python-pip

#?Windows
#sudo apt-get install python-pip

#?Mac OS:
# sudo easy_install pip
# pip kurulumundan sonra pip ile kurulumlara başlayabiliriz.

#Kullanım Örneği:

#Mac OS:
#sudo pip install django


#Windows:
#pip install django


#Toplu kurulum için
#sudo pip install -r requirements.txt

#pip kullanarak indirmek isterseniz şöyle bir avantajı var 
#hem eski versiyonu otomatik kaldırıyor hemde tek bir dosya
#oluşturup tümünü bir arada kurabiliyoruz.


#Komut isteminde aşağıdaki komutu çalıştırarak 
# Djangonun yüklü olup olmadığına ve Django sürümüne ulaşabilirsin :

    

#!windows için
#python -m django --version


#!mac için
#python3 -m django --version

#!Proje oluşturmak için 

#django-admin startproject mySite


#!her proje uygulamalar oluşturur bu yüzden projelerimizin içerisinde uygulamaları şu şekilde oluşturabiliriz
#python manage.py startupp myApp


#!projemizi çalıştırmak için 

#python manage.py runserver

#hangi dizinde olduğumuzu görmek için => #!ls

# Bulunduğunuz klasörden bir üst klasöre çıkmak için:
# Windows, macOs ve Linux tabanlı sistemlerde terminale #!cd komutunu yazabilirsiniz

# klasörden çıkmak için => #!cd..

# Bulunduğunuz klasördeki içerikleri ekrana yazdırmak için, bir başka deyişle bulunduğunuz
# klasörün içerisinde bulunan dosya ve klasörleri görebilmeniz için #!dir

#yeni bir klasör oluşturmak için : #!mkdir

#Kullanılan portu değiştirme

#! python manage.py runserver 8080


#Eğer sunucunun IP adresini değiştirmek isterseniz port ile birlikte belirtin. 
# Örnek olarak kullanılabilir tüm IP’leri dinlemek istiyorsanız şu kodu çalıştırın:

#!python manage.py runserver 0:8000