"""Monte Carlo"""
# Import knihoven
import random
import matplotlib.pyplot as plot


# Hody kostek
def hod_kostky(pocet_kostek, hozena_cisla):
    soucet_kostek = 0
    hodnoty_hodu = []

    for i in range(pocet_kostek):
        kostka = random.randint(1, 6)
        soucet_kostek += kostka
        hodnoty_hodu.append(kostka)
        hozena_cisla.append(kostka)

    #vratime si hodnoty a jejich soucet
    return soucet_kostek, hodnoty_hodu


def hra(pocet_her, pocet_kostek):
    # Výstupní hodnoty hry
    vyhra_hrac1 = 0
    vyhra_hrac2 = 0
    hodnoty_hrac1 = []
    hodnoty_hrac2 = []
    remiza = 0
    pomer_vyher1 = 0
    pomer_vyher2 = 0
    pomer_remiz = 0

    # Vlastní hra
    for i in range(pocet_her):
        hrac1, hodnoty_hodu1 = hod_kostky(pocet_kostek, hozena_cisla)
        hrac2, hodnoty_hodu2 = hod_kostky(pocet_kostek, hozena_cisla)

        hodnoty_hrac1.append(hodnoty_hodu1)
        hodnoty_hrac1.append(hozena_cisla)
        hodnoty_hrac2.append(hodnoty_hodu2)
        hodnoty_hrac2.append(hozena_cisla)

        print(f"Hrac 1 hodil {hodnoty_hodu1}, v souctu se jedna o hodnotu {hrac1}")
        print(f"Hrac 2 hodil {hodnoty_hodu2}, v souctu se jedna o hodnotu {hrac2}" + "\n")

        # Vyhodnocení výsledků hodů
        if hrac1 > hrac2:
            vyhra_hrac1 += 1
        elif hrac2 > hrac1:
            vyhra_hrac2 += 1
        else:
            remiza += 1

        # Výpočet poměrů
        pomer_vyher1 = vyhra_hrac1 / pocet_her * 100
        pomer_vyher2 = vyhra_hrac2 / pocet_her * 100
        pomer_remiz = remiza / pocet_her * 100

    return vyhra_hrac1, vyhra_hrac2, remiza, hodnoty_hrac1, hodnoty_hrac2, pomer_vyher1, pomer_vyher2, pomer_remiz


# Vyhodnocení výsledků do textu
def vyhodnoceni(kumulativni_prumer_hrac1, kumulativni_prumer_hrac2, kumulativni_prumer_remiz,kumulativni_prumer_hodu1
                , kumulativni_prumer_hodu2):
    is_six = 0
    is_five = 0
    is_four = 0
    is_three = 0
    is_two = 0
    is_one = 0
    for i in range(len(hozena_cisla)):
        if hozena_cisla[i] == 6:
            is_six += 1
        elif hozena_cisla[i] == 5:
            is_five += 1
        elif hozena_cisla[i] == 4:
            is_four += 1
        elif hozena_cisla[i] == 3:
            is_three += 1
        elif hozena_cisla[i] == 2:
            is_two += 1
        else:
            is_one += 1

    f_pomer_vyher1 = "{:.2f}".format(kumulativni_prumer_hrac1)
    f_pomer_vyher2 = "{:.2f}".format(kumulativni_prumer_hrac2)
    f_pomer_remiz = "{:.2f}".format(kumulativni_prumer_remiz)
    f_prumer_hody1 = "{:.2f}".format(kumulativni_prumer_hodu1)
    f_prumer_hody2 = "{:.2f}".format(kumulativni_prumer_hodu2)
    vysledky = f"Z {pocet_her} her je pomer vyher hrace 1 {f_pomer_vyher1}%, pomer vyher hrace 2 je" \
               f" {f_pomer_vyher2}%." \
               f" Pocet her, ktere skoncily remizou je {f_pomer_remiz}%.\n" \
               f"Prumer hodnot hrace 1 je {f_prumer_hody1}, prumer hodnot hrace 2 je {f_prumer_hody2}.\n" \
               f"Pravdepodobnost hozeni 6 {is_six/len(hozena_cisla)*100}%\n" \
               f"Pravdepodobnost hozeni 5 {is_five/len(hozena_cisla)*100}%\n" \
               f"Pravdepodobnost hozeni 4 {is_four/len(hozena_cisla)*100}%\n" \
               f"Pravdepodobnost hozeni 3 {is_three/len(hozena_cisla)*100}%\n" \
               f"Pravdepodobnost hozeni 2 {is_two/len(hozena_cisla)*100}%\n" \
               f"Pravdepodobnost hozeni 1 {is_one/len(hozena_cisla)*100}%\n"

    return vysledky


# Funkce pro tisk grafů
def tiskni_grafy(pocet_her, pocet_kostek):
    """
    pomer hrac 1 / hrac 2 v zavislosti na poctu her
    prumerna hodnota kostek hracu v zavislosti na poctu her
    odchylka od prumeru hodnot kostky v zavislosti na poctu her
    """
    osa_x = []
    osa_x_odchylka = [0]
    osa_y_prumer_hrac1 = []
    osa_y_prumer_hrac2 = []
    osa_y_prumer_remiz = []
    osa_y_prumer_hody1 = []
    osa_y_prumer_hody2 = []
    osa_y_odchylka_hrac1 = [0]
    osa_y_odchylka_hrac2 = [0]
    prumery_hrac1 = 0
    prumery_hrac2 = 0
    prumery_remiz = 0
    hody_hrac1 = []
    hody_hrac2 = []
    prumer_hodnot = 3.5
    pocitadlo_odchylka = 0
    for n in range(1, pocet_her+1):
        vyhra_hrac1, vyhra_hrac2, remiza, hodnoty_hrac1, hodnoty_hrac2, pomer_vyher1, pomer_vyher2, pomer_remiz\
            = hra(1, pocet_kostek)

        prumery_hrac1 += pomer_vyher1
        prumery_hrac2 += pomer_vyher2
        prumery_remiz += pomer_remiz
        hody_hrac1 += hodnoty_hrac1
        hody_hrac2 += hodnoty_hrac2
        kumulativni_prumer_hrac1 = prumery_hrac1 / n
        kumulativni_prumer_hrac2 = prumery_hrac2 / n
        kumulativni_prumer_remiz = prumery_remiz / n
        hody_hrac1_flat = [item for sublist in hody_hrac1 for item in sublist]
        hody_hrac2_flat = [item for sublist in hody_hrac2 for item in sublist]
        kumulativni_prumer_hodu1 = sum(hody_hrac1_flat) / len(hody_hrac1_flat) if hody_hrac1_flat else 0
        kumulativni_prumer_hodu2 = sum(hody_hrac2_flat) / len(hody_hrac2_flat) if hody_hrac2_flat else 0

        osa_x.append(n)
        osa_y_prumer_hrac1.append(kumulativni_prumer_hrac1)
        osa_y_prumer_hrac2.append(kumulativni_prumer_hrac2)
        osa_y_prumer_remiz.append(kumulativni_prumer_remiz)
        osa_y_prumer_hody1.append(kumulativni_prumer_hodu1)
        osa_y_prumer_hody2.append(kumulativni_prumer_hodu2)
        pocitadlo_odchylka += 1

        if pocitadlo_odchylka == 10:
            print(f"osa x:{osa_x_odchylka}, osa y 1: {osa_y_odchylka_hrac1}, osa y 2 : {osa_y_odchylka_hrac2}")
            pocitadlo_odchylka = 0
            odchylka_hrac1 = round((kumulativni_prumer_hodu1 - prumer_hodnot), 4)
            odchylka_hrac2 = round((kumulativni_prumer_hodu2 - prumer_hodnot), 4)
            print(f"Průměrná hodnota hodů od první hry po {n}. hru u hráče 1 je {kumulativni_prumer_hodu1},"
                  f" hráče 2 je {kumulativni_prumer_hodu2},"
                  f"odchylka od průměru hráče 1 je {odchylka_hrac1}, odchylka hráče 2 je {odchylka_hrac2}" + "\n")
            osa_x_odchylka.append(n)
            osa_y_odchylka_hrac1.append(odchylka_hrac1)
            osa_y_odchylka_hrac2.append(odchylka_hrac2)

        if n == pocet_her:
            print(vyhodnoceni(kumulativni_prumer_hrac1, kumulativni_prumer_hrac2, kumulativni_prumer_remiz,
                              kumulativni_prumer_hodu1, kumulativni_prumer_hodu2))

    # Graf průměrné hodnoty výher hráčů a remíz
    plot.figure(figsize=(12, 6))
    plot.plot(osa_x, osa_y_prumer_hrac1, label="Průměr hráč 1", alpha=0.7)
    plot.plot(osa_x, osa_y_prumer_hrac2, label="Průměr hráč 2", alpha=0.7)
    plot.plot(osa_x, osa_y_prumer_remiz, label="Průměr remíz", alpha=0.7)
    plot.xlabel("Počet her (n)")
    plot.ylabel("Výher (%)")
    plot.title("Poměr výher hráčů a remíz v průběhu her")
    plot.ylim(0, 100)
    plot.legend()
    plot.grid(True)

    plot.tight_layout()
    plot.show()

    # Graf průměrné hozené hodnoty
    plot.figure(figsize=(12, 6))
    plot.plot(osa_x, osa_y_prumer_hody1, label="Průměr hráč 1", alpha=0.7)
    plot.plot(osa_x, osa_y_prumer_hody2, label="Průměr hráč 2", alpha=0.7)
    plot.axhline(y=prumer_hodnot, color='k', linestyle='--', linewidth=1, alpha=0.4)
    plot.xlabel("Počet her")
    plot.ylabel("Průměrná hodnota hodů (Celkem)")
    plot.title("Průměrná hodnota hodů (Celkem) v průběhu her")
    plot.ylim(1, 6)
    plot.legend()
    plot.grid(True)

    plot.tight_layout()
    plot.show()

    # Graf průměrné odchylky od průměru hodů v průběhu her
    plot.figure(figsize=(12, 6))
    plot.plot(osa_x_odchylka, osa_y_odchylka_hrac1, label="Odchylka hráč 1", alpha=0.7)
    plot.plot(osa_x_odchylka, osa_y_odchylka_hrac2, label="Odchylka hráč 2", alpha=0.7)
    plot.xlabel("Počet her")
    plot.ylabel("Průměrná odchylka od průměru (Celkem)")
    plot.title("Průměrná odchylka hodů (Celkem) od průměrné hodnoty v průběhu her")
    plot.ylim(-0.75, 0.75)
    plot.legend()
    plot.grid(True)

    plot.tight_layout()
    plot.show()


##########################################################
pocet_kostek = 6
pocet_her = 200
hozena_cisla = []
tiskni_grafy(pocet_her, pocet_kostek)
#vyhra_hrac1, vyhra_hrac2, remiza, hodnoty_hrac1, hodnoty_hrac2 = hra(pocet_her, pocet_kostek)
#print(hodnoty_hrac1)
#print(hodnoty_hrac2)
#vyhodnoceni_pomeru(vyhra_hrac1, vyhra_hrac2, remiza, pocet_her, pocet_kostek)
#print(hra(10, pocet_kostek))
#print(vyhodnoceni_pomeru(vyhra_hrac1, vyhra_hrac2, remiza, pocet_her, pocet_kostek))
