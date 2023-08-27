import sqlite3
import random
import time
import win32api
import cpuinfo

no_count = 7000
upper_limit = 10000


RNG_numbers = []
validatedNumbers = []
duplicity = []


def generate_seed(url, limit):
    selected_chars = url[:random.randint(1, len(url))]  # Vyber náhodný počet prvků z odkazu
    number = sum(ord(char) for char in selected_chars) # Převeď všechny charaktery na čísla a sečti je

    cpu_clock = int(time.process_time() * 1e9)  # CPU clock

    mouse_pos = win32api.GetCursorPos()  # Aktualni pozice myši
    mouse_seed = (mouse_pos[0] + mouse_pos[1])

    # Získání teploty procesoru pomocí knihovny py-cpuinfo -- Hodně zpomaluje RNG kvůli použité metodě (1s sleep time)
#    cpu_temp = cpuinfo.get_cpu_info().get("current_temp")
#    temperature_seed = int(cpu_temp) if cpu_temp else 0

    rng_seed = (number + mouse_seed + cpu_clock) % limit  # Výpočet čísla
    return rng_seed


# Kontrola duplicit
def validate_number():
    index = 0
    for number in RNG_numbers:
        if number not in validatedNumbers:
            validatedNumbers.append(number)
            RNG_numbers.pop(index)
            index += 1
        else:
            duplicity.append(number)
            RNG_numbers.pop(index)
            index += 1
    if len(RNG_numbers) != 0:
        validate_number()
    validate_count()


# Kontrola počtu vygenerovaných čísel
def validate_count():
    global no_count
    count = no_count
    if len(validatedNumbers) < no_count:
        no_count = count - len(validatedNumbers)
        collect_data()
        validate_number()


# Sběr dat a jejich manipulace
def collect_data():
    history_db_path = "C:/Users/XXX/AppData/Local/Google/Chrome/User Data/Default/History"

    # Připojení k databázi
    connection = sqlite3.connect(history_db_path)
    pointer = connection.cursor()

    # SQL dotaz pro získání posledních "no_count" navštívených stránek
    query = f"SELECT url FROM urls ORDER BY last_visit_time DESC LIMIT {no_count};"
    pointer.execute(query)
    results = pointer.fetchall() # Načtení výsledků do results

    # Ukončení spojení s databází historioe
    connection.close()

    # Generování náhodných čísel na základě URL adres
    for result in results:
        to_strip = result[0]
        stripped_url = to_strip.lstrip("https://") # Odstraní prefix
 #       print(result[0])
 #       print(stripped_url)
        rng_seed = generate_seed(stripped_url, upper_limit)
        RNG_numbers.append(rng_seed)
 #       print(rng_seed)


#######################
collect_data()
validate_number()

print(f"Počet pseudonáhodných čísel: {len(validatedNumbers)} Čísla: {validatedNumbers}\n"
      f"Počet duplicit: {len(duplicity)} Čísla: {duplicity}\n"
      f"Seznam vyghenerovaných čísel {RNG_numbers}")
