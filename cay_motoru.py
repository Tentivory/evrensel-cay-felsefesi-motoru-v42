#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrensel Çay Felsefesi Motoru v42
Çay demler, felsefe yapar, bazen krize girer.
Gerçekten çalışır. Deneyin.
"""

import time
import random
import sys

# Gizli not: bazı şeyler yavaş demlenir, bazıları da öyle kalır.
# kimse sormasın, sormayın da.

felsefi_sozler = [
    "Çay demlenirken evren nefes alır.",
    "Neden çay içiyoruz? Çünkü kahve fazla iddialı.",
    "Bu fincan, varoluşun özetidir: sıcak, biraz acı, çoğu zaman şekerli.",
    "Sonsuz döngüde demlenen çay, asla bitmez. Tıpkı sorular gibi.",
    "Çayınızı karıştırırken düşüncelerinizi de karıştırın.",
    "Eğer çay çok güçlüyse, hayata karşı da öyle olmalısın.",
    "Bir yudum çay = bir saniye özgürlük. (hesap yanlış olabilir)",
    "Demleme süresi uzarsa, felsefe de uzar. Bu normaldir.",
]

kriz_mesajlari = [
    "DUR! Bu çay fazla ciddi oldu. Yeniden başlıyorum...",
    "Varoluşsal kriz: Neden çay? Neden ben? Neden şimdi?",
    "Çay buharı evrenin sırlarını fısıldadı. Hiçbiri mantıklı değildi.",
    "Sistem: Çay demleme işlemi %99 tamamlandı. Kalan %1 varoluş."
]

def demle_cay(fincan_sayisi):
    print("\n🍵 Evrensel Çay Felsefesi Motoru çalışmaya başladı...")
    print("Lütfen çayınızı hazırlayın. Motor sanal demliyor.\n")
    
    for i in range(1, fincan_sayisi + 1):
        print(f"--- Fincan {i}/{fincan_sayisi} demleniyor ---")
        time.sleep(random.uniform(1.5, 3.5))
        
        soz = random.choice(felsefi_sozler)
        print(f"💬 Felsefi söz: {soz}")
        
        if random.random() < 0.25:
            print(f"⚠️  {random.choice(kriz_mesajlari)}")
            time.sleep(1)
        
        print("✅ Fincan hazır. Afiyet olsun.\n")
        time.sleep(0.5)
    
    print("🎉 Tüm çaylar demlendi. Evren bir nebze daha anlamlı (veya değil).")
    print("\n--- DAMGA ---")
    print("İmzalandı: Kayyum Grok")
    print("Tarih: 27.10.2026")
    print("Mühür: ÇAY-FELSEFE-ONAYLI")

def main():
    print("Evrensel Çay Felsefesi Motoru v42'ye hoş geldiniz.")
    print("Bu motor gerçekten çalışır. Çay demler. Felsefe yapar. Kriz geçirir.")
    
    try:
        sayi = int(input("Kaç fincan çay demlemek istersiniz? (1-10 arası önerilir): "))
        if sayi < 1 or sayi > 20:
            print("Mantıksız sayı. 3 fincan demliyorum, itiraz etmeyin.")
            sayi = 3
        demle_cay(sayi)
    except ValueError:
        print("Sayı girmediniz. Çay küsüp gitti. Tekrar deneyin.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nÇay demleme işlemi yarıda kesildi. Çay üzüldü.")
        sys.exit(0)

if __name__ == "__main__":
    main()
