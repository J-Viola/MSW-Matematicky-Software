"""Monte Carlo"""
# Import knihoven
import random
import matplotlib.pyplot as plot


class Hrac:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.kolo_body = []
        self.body = 0
        self.vitezstvi = []


# Hody kostek
def hod_kostky(pocet):
    hodnoty_hodu = []

    for i in range(pocet):
        kostka = random.randint(1, 6)
        hodnoty_hodu.append(kostka)
        hozena_cisla.append(kostka)
    print(hodnoty_hodu)
    # vratime si hodnoty a jejich soucet
    return hodnoty_hodu


def najdi_stejne(kostka):
    seznam_hodnot = kostka
    stejne_hodnoty = []
    i = 0
    tuple_k_bodovani = []

    while i < len(seznam_hodnot):
        value = seznam_hodnot[i]
        count = seznam_hodnot.count(value)

        if count >= 2:
            stejne_hodnoty.extend([value] * count)
            for j in range(count):
                seznam_hodnot.remove(value)
        else:
            i += 1

    for value in set(stejne_hodnoty):
        count = stejne_hodnoty.count(value)
        tuple_k_bodovani.append((value, count))
    print(tuple_k_bodovani)

    return bodovani(tuple_k_bodovani, seznam_hodnot)


def bodovani(stejna_cisla, hodnoty_hodu):
    body = 0
    for value, count in stejna_cisla:
        if value != 1:
            if count == 3:
                body += value * 100
            elif count == 4:
                body += value * 200
            elif count == 5:
                body += value * 400
            elif count == 6:
                body += value * 800
        if value == 1:
            if count == 3:
                body += 1000
            elif count == 4:
                body += 2000
            elif count == 5:
                body += 4000
            elif count == 6:
                body += 8000

    if len(stejna_cisla) == 3 and all(count == 2 for value, count in stejna_cisla):
        body += 1000

    if set(hodnoty_hodu) == {1, 2, 3, 4, 5, 6}:
        body += 1500
        bodovani_list.append(body)
        print(f"Body: {body}")
        return body

    if any(value in [1] and 1 <= hodnoty_hodu.count(value) <= 2 for value in hodnoty_hodu):
        body += hodnoty_hodu.count(1) * 100

    if any(value in [5] and 1 <= hodnoty_hodu.count(value) <= 2 for value in hodnoty_hodu):
        body += hodnoty_hodu.count(5) * 50

    bodovani_list.append(body)
    print(f"Body: {body}")
    return body


def hra(soutezici, n_her):
    print(f"Je na tahu hráč {soutezici.jmeno}")
    for i in range(n_her):
        herni_kolo = najdi_stejne(hod_kostky(pocet_kostek))
        soutezici.body += herni_kolo
        soutezici.kolo_body.append(herni_kolo)
    pass


def vyhodnoceni(n_remiz):
    i = 0
    for j in range(pocet_her):
        if hrac1.kolo_body[i] > hrac2.kolo_body[i]:
            hrac1.vitezstvi.append(1)
            hrac2.vitezstvi.append(0)
            n_remiz.append(0)
            i += 1
        elif hrac1.kolo_body[i] == hrac2.kolo_body[i]:
            n_remiz.append(1)
            hrac1.vitezstvi.append(0)
            hrac2.vitezstvi.append(0)
            i += 1
        else:
            hrac1.vitezstvi.append(0)
            hrac2.vitezstvi.append(1)
            n_remiz.append(0)
            i += 1
    print(f"{hrac1.jmeno} vyhrál {hrac1.vitezstvi} kol, {hrac2.jmeno} vyhrál {hrac2.vitezstvi} kol,"
          f" remizovalo se {n_remiz} kol.")


######################

pocet_kostek = 6
pocet_her = 10
hozena_cisla = []
bodovani_list = []
list_remiz = []

hrac1 = Hrac("Hráč 1")
hrac2 = Hrac("Hráč 2")

seznam_hracu = [hrac1, hrac2]


for hrac in seznam_hracu:
    hra(hrac, pocet_her)

vyhodnoceni(list_remiz)

print(bodovani_list)
print(f"Odehráno {pocet_her} kol.")
print(f"{hrac1.jmeno}: {hrac1.body}, {hrac2.jmeno}: {hrac2.body}")
print(f"{hrac1.jmeno} body po kolech: {hrac1.kolo_body}, {hrac2.jmeno} body po kolech: {hrac2.kolo_body}")

####################### GRAFY #######################
osa_x = [value+1 for value in range(pocet_her)]
vyhry_hrac1 = [v / x * 100 for v, x in zip(hrac1.vitezstvi, osa_x)]
vyhry_hrac2 = [v / x * 100 for v, x in zip(hrac2.vitezstvi, osa_x)]
remizy = [v / x * 100 for v, x in zip(list_remiz, osa_x)]

plot.figure(figsize=(12, 6))
plot.plot(osa_x, vyhry_hrac1, label="Průměr hráč 1", alpha=0.7)
plot.plot(osa_x, vyhry_hrac2, label="Průměr hráč 2", alpha=0.7)
plot.plot(osa_x, remizy, label="Průměr remíz", alpha=0.7)
plot.xlabel("Počet her (n)")
plot.ylabel("Výher (%)")
plot.title("Poměr výher hráčů a remíz v průběhu her")
plot.ylim(0, 100)
plot.legend()
plot.grid(True)

plot.tight_layout()
plot.show()
print(osa_x)
