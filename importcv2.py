import cv2 as cv              # OpenCV kütüphanesi: görüntü işleme için
import numpy as np            # NumPy: matris işlemleri ve görüntüleri birleştirmek için
import os                     # OS: dosya/dizin işlemleri için


# Trackbar oluştururken callback fonksiyonu zorunlu olduğu için tanımlanıyor.
# Burada 'pass' ile boş bırakılmış, yani trackbar oynatıldığında bu fonksiyon bir şey yapmıyor.
def callback(input):
    pass


def cannyEdge():
    # Çalışılan dizini (klasörü) al
    root = os.getcwd()

    # Resim yolunu oluştur
    imgPath = os.path.join(root, 'C:/Users/ozgea/Downloads/imagefor.jpg')

    # Görüntüyü oku
    img = cv.imread(imgPath)

    # OpenCV BGR formatında okur, RGB'ye çeviriyoruz
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Görüntünün orijinal boyutlarını al (yükseklik, genişlik, kanal sayısı)
    height, width, _ = img.shape

    # Ölçeklendirme katsayısı (%70)
    scale = 0.7
    heightScale = int(height * scale)  # Yeni yükseklik
    widthScale = int(width * scale)    # Yeni genişlik

    # Görüntüyü yeniden boyutlandır
    img = cv.resize(img, (widthScale, heightScale), interpolation=cv.INTER_LINEAR)

    # Pencere ismi tanımla
    winname = 'canny'
    cv.namedWindow(winname)  # Yeni bir pencere oluştur

    # Trackbar ekle (min eşik değeri)
    cv.createTrackbar('minThres', winname, 0, 255, callback)

    # Trackbar ekle (max eşik değeri)
    cv.createTrackbar('maxThres', winname, 0, 255, callback)

    # Sonsuz döngü: kullanıcı trackbar ile oynadıkça görüntü güncellenecek
    while True:
        # Eğer kullanıcı 'q' tuşuna basarsa döngüden çık
        if cv.waitKey(1) == ord('q'):
            break

        # Trackbar'lardan güncel eşik değerlerini al
        minThres = cv.getTrackbarPos('minThres', winname)
        maxThres = cv.getTrackbarPos('maxThres', winname)

        # Canny kenar algılama uygula
        cannyEdge = cv.Canny(img, minThres, maxThres)

        # Canny çıktısı tek kanallıdır (siyah-beyaz). 
        # Bunu 3 kanallı hale çeviriyoruz ki orijinal resim ile yan yana gösterelim.
        canny_bgr = cv.cvtColor(cannyEdge, cv.COLOR_GRAY2RGB)

        # Orijinal ve Canny çıktısını yatayda birleştir (yan yana koy)
        combined = np.hstack((img, canny_bgr))

        # Sonucu ekranda göster
        cv.imshow(winname, combined)
        
    # Döngüden çıkınca tüm pencereleri kapat
    cv.destroyAllWindows()


# Program doğrudan çalıştırılırsa cannyEdge fonksiyonunu başlat
if __name__ == '__main__':
    cannyEdge()
