from collections import deque
 
nove = deque()
 
 
def elave_et(ad, derman):
    """Növbəyə yeni müştəri əlavə edir (enqueue əməliyyatı)."""
    nove.append({"ad": ad, "derman": derman})
    print(f"{ad} növbəyə əlavə olundu.")
 
 
def xidmet_et():
    """Növbədəki İLK müştərini dərmanı verdikdən sonra çıxarır (dequeue)."""
    if not nove:
        print("Növbə boşdur — xidmət ediləcək müştəri yoxdur!")
        return
    musteri = nove.popleft()
    print(f"{musteri['ad']} öz dərmanını ({musteri['derman']}) aldı və növbədən çıxdı.")
 
 
def siyahi_goster():
    """Növbədəki bütün müştəriləri gəliş sırası ilə ekrana çıxarır."""
    if not nove:
        print("Növbə boşdur.")
        return
    print(" Növbədəki müştərilər (gəliş sırası ilə) ")
    for i, musteri in enumerate(nove, start=1):
        print(f"{i}. {musteri['ad']} — {musteri['derman']}")
if __name__ == "__main__":
    while True:
        print("\n APTEK NÖVBƏSİ ")
        print("1) Müştəri əlavə et")
        print("2) Xidmət et (ilk müştərini çıxar)")
        print("3) Növbəni göstər")
        print("4) Çıxış")
        secim = input("Seçiminizi daxil edin: ")
 
        if secim == "1":
            ad = input("Müştərinin adı: ")
            derman = input("Tələb olunan dərmanın adı: ")
            elave_et(ad, derman)
        elif secim == "2":
            xidmet_et()
        elif secim == "3":
            siyahi_goster()
        elif secim == "4":
            print("Proqram dayandırıldı.")
            break
        else:
            print("Yanlış seçim! 1-4 arası rəqəm daxil edin.")
