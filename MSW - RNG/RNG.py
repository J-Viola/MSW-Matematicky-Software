import sqlite3
import random
import time
import win32api
import cpuinfo

no_count = 1000
upper_limit = 5000
RNG_numbers = []
validatedNumbers = []
duplicity = []


def generate_seed(url, limit):
    selected_chars = url[:random.randint(1, len(url))]  # Vyber nahodny pocet prvku z odkazu
    ansi_values = [ord(char) for char in selected_chars]
    number = int(''.join(map(str, ansi_values)))

    cpu_clock = int(time.process_time() * 1e9)  # CPU clock

    mouse_pos = win32api.GetCursorPos()  # Aktualni pozice myši
    mouse_seed = (mouse_pos[0] + mouse_pos[1])

    # Získání teploty procesoru pomocí knihovny py-cpuinfo
#    cpu_temp = cpuinfo.get_cpu_info().get("current_temp")
#    temperature_seed = int(cpu_temp) if cpu_temp else 0

    rng_seed = (number + mouse_seed + cpu_clock) % limit
    return rng_seed

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


def validate_count():
    global no_count
    count = no_count
    if len(validatedNumbers) <= no_count:
        no_count = count - len(validatedNumbers)
        collect_data()
        validate_number()


def collect_data():
    history_db_path = "C:/Users/XXX/AppData/Local/Google/Chrome/User Data/Default/History"

    # Připojení k databázi
    connection = sqlite3.connect(history_db_path)
    pointer = connection.cursor()

    # SQL dotaz pro získání posledních no_count navštívených stránek
    query = f"SELECT url FROM urls ORDER BY last_visit_time DESC LIMIT {no_count};"
    pointer.execute(query)
    results = pointer.fetchall() # Načtení výsledků do results

    # Generování náhodných čísel na základě URL adres
    for result in results:
        to_strip = result[0]
        stripped_url = to_strip.lstrip("https://")
        print(result[0])
        print(stripped_url)
        rng_seed = generate_seed(stripped_url, upper_limit)
#        random.seed(rng_seed)  # Set the seed for the RNG
#        random_number = random.randint(1, upper_limit)  # Generate a random number within the upper limit
        RNG_numbers.append(rng_seed)
        print(rng_seed)

    # Ukončení spojení s databází historioe
    connection.close()


collect_data()
validate_number()

print(f"Pseudonáhodná čísla: {validatedNumbers}\nDuplicity: {duplicity}\nSeznam vyghenerovaných čísel {RNG_numbers}")
