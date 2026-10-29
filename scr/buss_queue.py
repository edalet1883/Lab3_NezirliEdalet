from collections import deque

prioritet_nove = deque() 
normal_nove = deque()      
 
PRIORITET_YASI = 65
 
def elave_et(ad, yas):
    if yas >= PRIORITET_YASI:
        prioritet_nove.append({"ad": ad, "yas": yas})
        print(f"{ad} ({yas} yaş) PRIORİTET növbəsinə əlavə olundu.")
    else:
        normal_nove.append({"ad": ad, "yas": yas})
        print(f"{ad} ({yas} yaş) normal növbəyə əlavə olundu.")
 
 
def avtobusa_min():
    if prioritet_nove:
        sernisin = prioritet_nove.popleft()
        print(f"{sernisin['ad']} ({sernisin['yas']} yaş) prioritetlə avtobusa mindi.")
    elif normal_nove:
        sernisin = normal_nove.popleft()
        print(f"{sernisin['ad']} ({sernisin['yas']} yaş) avtobusa mindi.")
    else:
        print("Avtobusa minəcək sərnişin yoxdur — hər iki növbə boşdur!")
 
 
def siyahi_goster():
    print(" PRIORİTET növbəsi (65+)")
    if not prioritet_nove:
        print("(boş)")
    for i, s in enumerate(prioritet_nove, start=1):
        print(f"{i}. {s['ad']} — {s['yas']} yaş")
 
    print(" Normal növbə ")
    if not normal_nove:
        print("(boş)")
    for i, s in enumerate(normal_nove, start=1):
        print(f"{i}. {s['ad']} — {s['yas']} yaş")
if __name__ == "__main__":
    while True:
        print("\n AVTOBUS DAYANACAĞI NÖVBƏSİ ")
        print("1) Sərnişin əlavə et")
        print("2) Avtobusa mindir")
        print("3) Növbələri göstər")
        print("4) Çıxış")
        secim = input("Seçiminizi daxil edin: ")
 
        if secim == "1":
            ad = input("Sərnişinin adı: ")
            yas = int(input("Sərnişinin yaşı: "))
            elave_et(ad, yas)
        elif secim == "2":
            avtobusa_min()
        elif secim == "3":
            siyahi_goster()
        elif secim == "4":
            print("Proqram dayandırıldı.")
            break
        else:
            print("Yanlış seçim! 1-4 arası rəqəm daxil edin.")
