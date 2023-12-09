#örneğin bir blog uygulaması yapalım bu proje üzerinden adım adım djangoyu birlikte kavrayacağız
#program kurulumlarını vs indirip kurduktan sonra blog projemizi oluşturmak için ilk olarak

#! djongo-admin startproject BlogProje 


#adında bir proje başlatıyoruz içerisinde ilk olarak post adında bir uygulama oluşturuyoruz 

#! python manage.py startupp PostApp


#Bu proje dosyasını oluşturduktan sonra 
#dosyasa dizinimizde bu dosyalarla karşılaşacağız

#__init__.py
#asgi.py
#settings.py
#urls.py
#wsgi.py
#manage.py =>bu yönetim dosyası projemizin dışında oluşur.

#!__init__.py
#?Python paketlerini içeren dizinlerin bulunduğu dosyadır. __init__.py dosyası, projenin Python paketi olarak tanınmasını sağlar ve projeyi içeren modüllerin veya alt paketlerin doğru şekilde içe aktarılmasını sağlar. Bu dosya, projenin çeşitli bileşenlerini düzenlemek veya yapılandırmak 
#?için kullanılabilir, ancak genellikle boş olarak kalır.

#Burada aklımıza takılabilecek bir kaç soru gelebilir  

#?Neden Paket olarak tanımlıyoruz ?
# Python'da paketler, ilgili modüllerin veya alt paketlerin düzenli bir şekilde
# gruplandırılmasını sağlar. Paketler, kodun daha iyi organize edilmesini, tekrar kullanılabilirliği 
# artırmasını ve proje yönetimini kolaylaştırmasını sağlar. Ayrıca, paketler, 
# kodun başka projelerle entegrasyonunu kolaylaştırır ve isim çakışmalarını önler.

# __init__.py dosyası, bir dizini Python paketi olarak tanımak için kullanılır. 
# Bu dosyanın varlığı, Python'ın, ilgili dizini bir paket olarak kabul etmesini 
# sağlar ve içindeki modüllerin veya alt paketlerin doğru şekilde içe aktarılmasını sağlar.


#################################################################################


# Bu dosya genellikle boş bırakılır, çünkü çoğu durumda, projenin başlatılması 
# için özel bir başlatma veya yapılandırma koduna ihtiyaç duyulmaz. Django,
# projeyi tanımak ve yapılandırmak için özel bir dosya olan settings.py dosyasını kullanır.

# Ancak, projenizin ihtiyaçlarına bağlı olarak, __init__.py dosyasını 
# özelleştirebilir ve projenizin başlatılması sırasında çalışmasını istediğiniz 
# özel kodları içerebilirsiniz. Örneğin, Django projenizde özel bir başlangıç süreci yapmak veya
# bazı başka işlemleri gerçekleştirmek 
# istediğiniz durumlarda __init__.py dosyasını kullanabilirsiniz.

#?_init__.py dosyasını özel durumlar için kullanmanın birkaç örneği şunlar olabilir:



#!Paket düzeyindeki başlatma kodları
# Bu kodlar, paketin genel yapılandırması, değişkenlerin tanımlanması, 
# ön yüklemelerin yapılması veya başka işlemlerin gerçekleştirilmesi gibi görevleri yerine getirebilir.

#!İçe aktarılacak modüllerin belirtilmesi: 
# __init__.py dosyası, paketin dışarıya açık modüllerini 
# veya alt paketlerini belirtebilir. Bu, paketin kullanıcı tarafından kolaylıkla içe aktarılmasını 
# sağlar. Örneğin, __init__.py dosyası içinde from . import module_name ifadesi kullanılarak 
# belirli bir modülün paketin bir parçası olarak içe aktarılması sağlanabilir.

#!İsim alanı (namespace) ayarlamaları: 
# __init__.py dosyası, paket içindeki değişken veya fonksiyonların hangi isimler 
# altında dışarıya açılacağını belirlemek için kullanılabilir. 
# Bu, paketin kullanıcıya sunulan arayüzünü kontrol etmeye yardımcı olur.


#!Gerekli dosya ve kaynakları yüklemek: 
# __init__.py dosyası, paketin başlatılması sırasında gerekli dosyaları, kaynakları
# veya diğer bağımlılıkları yüklemek için kullanılabilir. 
# Bu, paketin çalışması için gereken önceden yüklenmesi gereken bileşenleri içerebilir.



#!Neden bu dosya boş kalır ?

#?Minimalizm: 
# __init__.py dosyasını boş bırakmak, paket veya modülün 
# temiz ve basit bir yapısı olduğunu gösterir. Eğer paket veya 
# modül için özel bir başlatma veya yapılandırma koduna ihtiyaç yoksa,
# dosyanın boş kalması gereksiz karmaşıklığı önler.

#?Standartlarla Uyum: 
# Boş bir __init__.py dosyası, 
# Python'ın paketi doğru şekilde tanıması ve paketi içe aktarılabilir
# hale getirmesi için bir gerekliliktir.
# Bu, diğer geliştiricilerin ve araçların projenizi daha iyi anlamasını sağlar ve 
# Python topluluğu tarafından kabul edilen bir standartı takip etmenizi sağlar.

#?Gelecekteki Genişletilebilirlik: 
# Boş bir __init__.py dosyası, paketin veya modülün gelecekteki genişletmelerine olanak sağlar. 
# İleride pakete veya modüle ek özellikler veya başlatma kodları eklemeniz gerektiğinde, 
# mevcut __init__.py dosyasını güncelleyebilirsiniz.

#?İsim Çakışmalarını Önleme: 
# Boş bir __init__.py dosyası, paket veya modül adının, altında 
# yer alan modül veya alt paket adlarından ayırt edilmesini sağlar. 
# Bu, isim çakışmalarını önler ve projenin daha modüler bir yapıda olmasını sağlar.

#?#?#?#?######?#####?######?#####?#####?#########?###########?######?###?##???##


#!asgi.py dosyası ne işe yarar ?

# asgi.py dosyası, Django projelerinde ASGI (Asynchronous Server Gateway Interface) sunucusu 
# için giriş noktasıdır. ASGI, Django uygulamalarının asenkron ve 
# gerçek zamanlı talepleri işleyebilmesini sağlayan bir web sunucusu arabirimidir.


#ASGI.PY

# ASGI (Asynchronous Server Gateway Interface), Python tabanlı web uygulamalarının 
# asenkron ve gerçek zamanlı talepleri işlemek için kullanılan bir sunucu arabirimidir. 
# ASGI, Django ve diğer Python web çatıları için tasarlanmıştır.

# ASGI, gelen talepleri asenkron olarak işlemek için bir protokol ve bir sunucu 
# tarafından uygulanacak bir API (Uygulama Programlama Arayüzü) sağlar.
# Bu sayede, web uygulamaları aynı anda birden fazla talebi eşzamanlı olarak işleyebilir 
# ve yanıt süreleri düşürülebilir.

# Geleneksel olarak, Python web uygulamaları WSGI (Web Server Gateway Interface) standardını kullanır.
# Ancak WSGI, asenkron işlem desteği sağlamadığı için
# büyük ölçekli gerçek zamanlı uygulamalar için uygun değildir. 
# ASGI, WSGI'nin eksikliklerini gidermek 
# ve asenkron işlemleri desteklemek amacıyla geliştirilmiştir.

#?asgi.py dosyasının içinde blog projemizi başlattıktan sonra
#?otomatik olarak şöyle bir kod ortaya çıktı

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlogProje.settings')

# application = get_asgi_application()



#?import os: os modülünü projeye dahil eder. 
#Bu modül, işletim sistemi işlevlerine erişim sağlar.

# ?from django.core.asgi import get_asgi_application: 
# Django'nun django.core.asgi 
# modülünden get_asgi_application fonksiyonunu projeye dahil eder. Bu fonksiyon,
# Django uygulamasını ASGI sunucusu için hazır hale getiren bir örnekleme döndürür.

#?os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlogProje.settings'): 
# os.environ sözlüğünü kullanarak DJANGO_SETTINGS_MODULE ortam değişkenini ayarlar. 
# Bu, Django'nun projenin yapılandırma ayarlarını yüklemek için hangi modülü kullanması gerektiğini belirtir. 
# Burada 'BlogProje.settings' 
# değeri, projenin settings.py dosyasının bulunduğu modülün adını temsil eder. Bu değer, projenize özgü olarak değişebilir.(sizin adını verdiğiniz proje neyse o olur)


#?application = get_asgi_application(): get_asgi_application() 
# fonksiyonunu çağırarak Django uygulamasını ASGI sunucusuna uyumlu hale getiren bir uygulama örneği oluşturur. 
# Bu örneği application adlı bir değişkene atar. 
# ASGI sunucusu, bu uygulamayı kullanarak gelen talepleri işler ve yanıtları gönderir.


#!#!#!#!#!#!#!#!#!#!############################################################################

#?settings.py

#Django projelerinde yer alan ve projenin yapılandırma ayarlarını içeren dosyadır. 
#Bu dosya, projenin çalışma şeklini ve davranışını belirlemek için kullanılan bir dizi parametreyi içerir.


#?İşte settings.py dosyasında sıkça kullanılan bazı ayarlar:

# DEBUG: Projenin hata ayıklama modunu belirler. Geliştirme aşamasında
 
# True olarak ayarlanırken, yayına alındığında False olarak ayarlanması önemlidir.

# ALLOWED_HOSTS: Projenin hangi host adlarına izin verileceğini belirler.

# DATABASES: Veritabanı bağlantısı ve yapılandırmasını belirler. Veritabanı türü, ana bilgisayar, 
# kullanıcı adı, şifre gibi bilgileri içerir.

# STATIC_URL ve STATIC_ROOT: Statik dosyaların URL'si ve kök dizinini belirler.

# MEDIA_URL ve MEDIA_ROOT: Medya dosyalarının URL'si ve kök dizinini belirler.

# LANGUAGE_CODE ve TIME_ZONE: Projenin dilini ve zaman dilimini belirler.

# INSTALLED_APPS: Projede etkinleştirilmiş uygulama listesini içerir. Django'nun dahili uygulamaları ve 
# üçüncü taraf eklentiler bu listede yer alır.

# MIDDLEWARE: Proje için kullanılacak ara yazılımların (middleware) sıralamasını belirler.

#?#?#?#?###########################################################################################


#!urls.py

# Django projelerinde yer alan ve URL yönlendirmelerini tanımlayan bir dosyadır. Bu dosya, 
# gelen taleplerin URL'lerine göre doğru view (görünüm) veya işlevi eşleştirmek için kullanılır.

# urls.py dosyası genellikle projenin ana dizininde veya her uygulama için ayrı ayrı oluşturulan urls.py dosyalarında bulunur.
# Django'nun URL yönlendirme mekanizmasını kullanarak, 
# gelen taleplerin belirli bir URL kalıbına göre nasıl işleneceğini belirleyebilirsiniz.

#urls.py dosyasında sıkça kullanılan bazı örnekler:

#YÖNTEMLER

# from django.urls import path 
# from . import views

# urlpatterns = [
#     path('hello/', views.hello_world),
# ]


#!from django.urls import path: 
# Django'nun path işlevini 
# django.urls modülünden almak için 
# kullanılır. path, URL kalıplarını yönlendirmek için kullanılan bir işlevdir.

# from . import views: Projenin mevcut dizinindeki views.py dosyasından view işlevlerini 
# içe aktarmak için kullanılır. Burada, mevcut dizindeki views.py dosyasından view işlevlerini almak için kullanılır.

# urlpatterns: Bu değişken, URL yönlendirmelerini tanımlayan bir liste veya demet nesnesidir. 
# Bu liste, URL kalıplarını ve ilgili view veya işlevleri eşleştiren yönlendirme tanımlamalarını içerir.

# path('hello/', views.hello_world): Bu satır, "/hello/" URL'sine gelen talepleri hello_world adlı bir view işlevine yönlendirir.
# path işlevi, URL kalıbını (burada "hello/") ve eşleştiğinde çalışacak view işlevini alır. 
# Bu şekilde, "/hello/" URL'sine yapılan talepler hello_world view işlevine yönlendirilir.

# views.hello_world ifadesi, views.py dosyasında tanımlanmış olan hello_world adlı bir view işlevine işaret eder. 
# Bu view işlevi, gelen talepleri işleyerek bir HTTP yanıtı döndürür. 
# Örneğin, "Merhaba Dünya" gibi bir metin yanıtı olabilir veya bir HTML şablonuyla render edilmiş bir sayfa olabilir.

# View işlevleri, kullanıcının taleplerini işleyen, veritabanından veri alabilen, 
# işlemler gerçekleştirebilen ve sonunda bir yanıt döndürebilen Python fonksiyonlarıdır. 
# Bu fonksiyonlar, Django projelerinde kullanıcıların etkileşimde bulunduğu sayfaların arkasındaki iş mantığını gerçekleştirir.

# Bu örnek kod parçası, "/hello/" URL'sine gelen talepleri hello_world view işleviyle eşleştirir ve bu işlevin döndürdüğü yanıtı istemciye gönderir.

#? include()


#  işlevi, Django'da başka bir urls.py dosyasını dahil etmek için kullanılır.
#  Bu, projenizde farklı uygulamalar arasında URL tanımlamalarını ayrı dosyalarda düzenlemenizi sağlar 
#  ve kodunuzun daha düzenli ve modüler olmasını sağlar.

# from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myapp/', include('myapp.urls')),
    
# ]
# Yukarıdaki örnekte, include() işlevini kullanarak myapp.urls dosyasını ana urls.py 
# dosyasına dahil ediyoruz. myapp uygulamasına gelen talepler, 
# myapp.urls dosyasında tanımlanan URL kalıplarına yönlendirilecektir.

#!Peki Neden include() ihtiyaç duyarız bunu inceleyelim 
# Projenizde birden fazla uygulama varsa: Eğer Django projenizde birden fazla uygulama varsa, her bir uygulamanın 
# kendi urls.py dosyasını kullanarak URL tanımlamalarını yönetebilirsiniz. include() işlevini kullanarak, ana urls.py dosyasında her bir uygulamanın urls.py dosyasını dahil edebilirsiniz. 
# Bu, uygulamalar arasında URL tanımlamalarını ayrı tutmanıza ve daha modüler bir yapı oluşturmanıza yardımcı olur.

# Uygulamalar arasında URL isim çakışması varsa: Birden fazla uygulama aynı URL kalıplarını kullanıyorsa
# veya URL'lerde çakışma varsa, include() işlevini kullanarak uygulama özgü URL isim uzaylarını ayrı tutabilirsiniz.
# Her bir uygulamanın kendi urls.py dosyasında tanımladığı URL'ler, uygulama adlarıyla birlikte öneki olur ve 
# böylece URL çakışmalarını önlemiş olursunuz.

# Kodun daha temiz ve düzenli olmasını isterseniz: include() işlevi, projenin ana urls.py dosyasını daha okunabilir
# ve düzenli hale getirir. Ana urls.py dosyası sadece uygulama URL'lerini içe alır, böylece dosya içeriği daha az 
# karmaşık olur ve projenin farklı bölümlerini daha iyi ayırabilirsiniz.

# Uygulamalar arasında bağımsızlık sağlamak isterseniz: Her uygulamanın kendi urls.py dosyasına sahip olması, 
# uygulamaların birbirinden bağımsız olarak çalışabilmesini sağlar. Bir uygulamayı projeden ayrıştırıp 
# başka bir projede kullanmak istediğinizde, uygulamanın urls.py dosyasını da taşıyabilir ve başka projede kolayca kullanabilirsiniz.

# include() işlevini kullanarak, projenizdeki farklı uygulamaların URL tanımlamalarını ayrı
# dosyalarda düzenleyebilir ve projenin daha modüler ve düzenli bir yapıya sahip olmasını sağlayabilirsiniz. 
# Bu işlev, projenizin ölçeklenebilirliğini ve bakımını kolaylaştırabilir.
# Ancak, küçük ve basit projelerde tek bir urls.py dosyası kullanmak da uygundur.

#?Değişken URL kalıpları: 
    
# URL kalıplarında dinamik parçalar kullanmanız gerektiğinde,
# değişkenler veya parametreler kullanabilirsiniz. Örneğin:

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('users/<int:user_id>/', views.user_profile),
# ]


#Bu örnek, "users/1/" gibi bir URL'sine gelen talepleri user_profile 
# adlı bir view işlevine yönlendirir
#ve user_id parametresini dinamik olarak geçirir.


#!Peki böyle bir şeye neden ihtiyaç duyarız 
# çünkü kullanıcı profilleri genellikle benzersiz bir kimlik veya tanımlayıcıya sahiptir.
#  Bu kimlik veya tanımlayıcı, URL içinde belirtilen parametre olarak kullanılır ve
#  kullanıcı profili sayfasının dinamik olarak oluşturulmasını sağlar.

# Örneğin, users/1/ URL'si, kullanıcının kimlik numarası 1 olan profilini görüntülerken, 
# users/2/ URL'si kullanıcının kimlik numarası 2 olan profilini görüntüler.
# Bu sayede, kullanıcı profillerini farklı URL'lere dayalı olarak görüntülemek mümkün olur.

# Django'nun URL yönlendirme sistemi, bu tür dinamik parametreleri kolayca yakalayabilir
# ve view işlevine geçirebilir. Bu sayede, kullanıcı profilleri gibi benzersiz kaynaklara erişimi
# kolaylaştırır ve dinamik içerik sunmamızı sağlar.



#?#######################################################################################################################


#!wsgi.py

# Django projelerinde WSGI (Web Server Gateway Interface) sunucusuna projeyi başlatmak için 
# kullanılan bir dosyadır. WSGI, Python web uygulamalarının web sunucusuyla 
# iletişim kurmasını sağlayan bir standart arayüzdür.


# wsgi.py dosyası, projenin ana dizininde yer alır ve 
# Django projesinin WSGI sunucusu tarafından çalıştırılmasını sağlar. 
# WSGI sunucusu, gelen HTTP taleplerini alır ve bu dosyayı kullanarak Django uygulamasını başlatır.


#!import os
#!from django.core.wsgi import get_wsgi_application
#!os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
#!application = get_wsgi_application()





# Yukarıdaki örnekte, os ve django.core.wsgi modüllerini dahil ediyoruz. 
# Ardından, get_wsgi_application() işlevini kullanarak Django uygulamasını alıyoruz.

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings') satırı, 
# DJANGO_SETTINGS_MODULE ortam değişkenini kontrol eder ve projenin ayar dosyasının nerede olduğunu belirtir. project.settings ifadesi, projenin settings.py dosyasının project alt dizininde olduğunu gösterir. 
# Bu, Django'nun projenin ayarlarını doğru şekilde yüklemesini sağlar.

# Son olarak, application adlı bir değişkene get_wsgi_application() işlevinden 
# dönen uygulamayı atıyoruz. Bu, WSGI sunucusuna Django uygulamasını sağlar.

# wsgi.py dosyası, genellikle Django projelerini sunucuya dağıtırken kullanılır. 
# WSGI sunucusu, bu dosyayı kullanarak Django uygulamasını başlatır ve gelen 
# HTTP taleplerini yönlendirir. Bu dosya, projenin WSGI sunucusu ile etkileşimini sağlar ve 
# Django uygulamasının web sunucusunda çalışmasını mümkün kılar.

#  projeye dahil etmek için get_wsgi_application fonksiyonunu çağırmamıza gerek yoktur. 
# Ancak projeyi çalıştırmak için get_wsgi_application() fonksiyonunu parantez içinde çağırarak çalıştırmamız gerekmektedir.




#!##########################


#!manage.py

manage.py dosyası, projenin kök dizininde bulunur ve Django'nun komut satırı arayüzüne erişim sağlar. 
Bu dosyayı kullanarak Django projeleriyle ilgili birçok işlemi gerçekleştirebilirsiniz.

# İşte manage.py dosyasıyla yapabileceğiniz bazı işlemler:

# Django projenizi çalıştırma: python manage.py runserver komutunu kullanarak yerel sunucunuzu başlatıp 
# Django projenizi çalıştırabilirsiniz. 
# Varsayılan olarak http://localhost:8000/ adresinde çalışan bir geliştirme sunucusu başlatılır.

# Veritabanı işlemleri: python manage.py migrate komutuyla veritabanı tablolarını oluşturabilir veya güncelleyebilirsiniz. 
# Ayrıca python manage.py makemigrations komutuyla model değişikliklerini veritabanı migrasyonlarına dönüştürebilirsiniz.

# Yönetici hesabı oluşturma: python manage.py createsuperuser komutunu kullanarak Django yönetici hesabı oluşturabilirsiniz. 
# Bu hesapla Django yönetici paneline erişebilir ve projenizi yönetebilirsiniz.

# Uygulama oluşturma: python manage.py startapp app_name komutunu kullanarak yeni bir Django uygulaması oluşturabilirsiniz.
# Bu, projenize yeni bir uygulama eklemek için kullanılan temel bir komuttur.

# Testlerin çalıştırılması: python manage.py test komutunu kullanarak testlerinizi çalıştırabilirsiniz. 
# Bu, Django projenizdeki testleri otomatik olarak yürütür ve sonuçları raporlar.

# manage.py dosyası, Django projelerinde sıklıkla kullanılan ve projenin yönetimini kolaylaştıran bir araçtır. 
# Komut satırı üzerinden bu dosyayı kullanarak Django projesiyle ilgili birçok işlemi gerçekleştirebilirsiniz.