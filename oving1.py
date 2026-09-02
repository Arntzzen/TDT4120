# -------------------------------------------
#                  Oppgave 8
# -------------------------------------------

#!/usr/bin/python3
# coding=utf-8
import random

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å generere
# tilfeldig instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å juste på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = False
# Antall tilfeldige tester som genereres
random_tests = 10
# Lavest mulig antall verdier i generert instans.
n_lower = 3
# Høyest mulig antall verdier i generert instans.
n_upper = 10
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0


# Funksjonsinnholdet skal limes inn på Inginious
def insertion_sort(A, n):
    # Din kode
    for i in range(1, n):
        j = i - 1
        key = A[i]
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


# Hardkodete tester
tests = [
    [],
    [1, 2, 3],
    [3, 2, 1],
    [9, 7, 3, 5, 2, 6],
    [-1, 1, -1, 2],
    [-5, 8, 3, 10, 2, 15],
]


# Genererer k tilfeldige tester, hver med et tilfeldig antall elementer plukket
# uniformt fra intervallet [nl, nu].
def gen_examples(k, nl, nu):
    for _ in range(k):
        yield [random.randint(-99, 99) for _ in range(random.randint(nl, nu))]


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(random_tests, n_lower, n_upper))

failed = False
for A in tests:
    answer = sorted(A)
    student = insertion_sort(A[:], len(A))
    if student != answer:
        if failed:
            print("-"*50)
        failed = True

        print(f"""
Koden feilet for følgende instans:
A: {A}
n: {len(A)}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")



# -------------------------------------------
#                  Oppgave 10
# -------------------------------------------

# Etter i iterasjoner av den ytre løkka gjelder følgende:
# de i minste elementene i tabellen ligger på plassene 1, ... i, og de i største elementene ligger på plassene n-1+1, ..., n i stigende rekkefølge.
# Før den første iterasjonen er i = 0, så vi har ingen plasserte/sorterte elementer i starten eller slutten av tabellen.
# I neste iterasjon erstatter hhv. minste verdi a_i = a_1 og største verdi erstatter a_n-i+1 = a_n av elementene i A[a_i+1,..., a_n-i+1]
# Nå vil de i minste elementene være sortert de første i indeksene og de største elementene sortert på de siste i indeksene.

# Funksjonen her er feil.

# def dual_sort(A):
#     n = int(len(A))
#     s = 0
#     b = 0
#     for i in range(n // 2):
#         for j in range(1, n - i):
#             if A[j] < A[i]:
#                 s = A[j]
#             elif A[j] > A[i]:
#                 b = A[j]
#         A[i] = s
#         A[i] = b
#     return A

# the_list = [13, 5, 7, 1, 3, 11]
# dual_sort(the_list)
# print(the_list)