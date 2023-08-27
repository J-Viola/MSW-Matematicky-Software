# DERIVACE FUNKCE JEDNE PROMĚNNÉ
import sympy as sp
import numpy as np
import math
import matplotlib.pyplot as plot
import time

# Nastavení symbolu
x = sp.symbols('x')

# Nastavení programu
pocet_vzorku = range(1, 2000, 500)
epsilon = 0.001  # Max přípustná chyba
int_start = 0.5  # Začátek vybraného intervalu
int_stop = 2*math.pi  # Konec vybraného intervalu
dyn_krok = 1e-3  # Nastavení dynamického kroku
stat_krok = 1e-3  # Nastavení statického kroku

# Vytvoření seznamů
stat_time_list = []
dyn_time_list = []
analytic_time_list = []
aktualne_vzorku = []
staticka_odchylka = []
dynamicka_odchylka = []


# Definice funkce
def logaritmic():
    return sp.log(x)


# Statická metoda derivace
def static_step(funkce, x_vec, krok):
    hodnoty_stat = []

    for i in range(len(x_vec)):
        f_x0 = funkce.subs(x, x_vec[i])
        f_x1 = funkce.subs(x, x_vec[i] + krok)
        iterace = (f_x1 - f_x0) / krok
        hodnoty_stat.append(iterace)

    print(f"Statický krok: {sum(hodnoty_stat)}")
    return sum(hodnoty_stat)


# Dynamická metoda derivace
def dynamic_step(funkce, x_vec, krok):
    hodnoty_dyn = []

    for i in range(len(x_vec)):
        h = krok  # Nastavení dynamického kroku na původní hodnotu pro každou iteraci
        f_x0 = funkce.subs(x, x_vec[i])
        f_x1 = funkce.subs(x, x_vec[i] + h)
        iterace = (f_x1 - f_x0) / h
        chyba = 1

        while chyba > epsilon:
            h /= 2  # Změna kroku
            f_x0 = funkce.subs(x, x_vec[i])
            f_x1 = funkce.subs(x, x_vec[i] + h)
            nova_iterace = (f_x1 - f_x0) / h
            chyba = abs(nova_iterace - iterace)  # Výpočet chyby
            iterace = nova_iterace
            hodnoty_dyn.append(iterace)

    print(f"Dynamický krok: {sum(hodnoty_dyn)}\n")
    return sum(hodnoty_dyn)


# Měření časové náročnosti
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time


# Vypiš výsledky a vytvoř grafy
def vysledek(f):
    for pocet in pocet_vzorku:
        print(f"Počítáme s {pocet} vzorky z intervalu <{int_start}, {int_stop}> funkce {f}.")
        x_vec = np.linspace(int_start, int_stop, pocet)

        start_time = time.time()
        analyticka_derivace = 1 / x_vec
        end_time = time.time()
        analytic_time = end_time - start_time
        print(f"Analytická derivace: {sum(analyticka_derivace)}")

        stat_values, stat_time = measure_time(static_step, f, x_vec, stat_krok)
        dyn_values, dyn_time = measure_time(dynamic_step, f, x_vec, dyn_krok)

        aktualne_vzorku.append(pocet)
        stat_time_list.append(stat_time)
        dyn_time_list.append(dyn_time)
        analytic_time_list.append(analytic_time)
        staticka_odchylka.append(sum(analyticka_derivace) - stat_values)
        dynamicka_odchylka.append(sum(analyticka_derivace) - dyn_values)
        print(f"Odchylka se statickým krokem = {sum(analyticka_derivace) - stat_values}")
        print(f"Odchylka s dynamickým krokem = {sum(analyticka_derivace) - dyn_values}")

    print(stat_time_list, dyn_time_list)

    # Grafy
    plot.figure(figsize=(10, 5))

    plot.plot(aktualne_vzorku,  stat_time_list, label="Statický krok")
    plot.plot(aktualne_vzorku,  dyn_time_list, label="Dynamický krok")
    plot.plot(aktualne_vzorku,  analytic_time_list, label="Analytická derivace")
    plot.xlabel('Počet vzorků')
    plot.ylabel('Čas (s)')
    plot.title('Časová náročnost')
    plot.legend()
    plot.grid()

    plot.tight_layout()
    plot.show()

    plot.figure(figsize=(10, 5))
    plot.plot(aktualne_vzorku, staticka_odchylka, label="Statický krok")
    plot.plot(aktualne_vzorku, dynamicka_odchylka, label="Dynamický krok")
    plot.xlabel('Počet vzorků')
    plot.ylabel('Odchylka')
    plot.title('Odchylka od analytické derivace')
    plot.legend()
    plot.grid()

    plot.tight_layout()
    plot.show()

    print(f"vzorku:{aktualne_vzorku}\nstat odchylka:{staticka_odchylka}\ndyn odchylka:{dynamicka_odchylka}")
    print("\n")

    return


#############################
f = logaritmic()
vysledek(f)




