teklifler={}
finish_program=False
enyuksek_teklif=0
enyuksek_name=""
print("Kapalı Açık Arttırmaya hoş geldiniz")
while finish_program is False:
    name=input("Adınız nedir?: ")
    bid=int(input("Teklifiniz ne kadar?: $"))
    kapat=input("Başka teklif var mı? (yoksa y yazın)")
    teklifler[name]=bid
    if kapat=="y":
        finish_program=True
        for name in teklifler:
            if teklifler[name]>enyuksek_teklif:
                enyuksek_teklif=teklifler[name]
                enyuksek_name=name
        print(f"En yüksek fiyatı {enyuksek_name} verdi. Teklifi: ${enyuksek_teklif}")
