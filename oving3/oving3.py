# ============================================================
#                          Oppgave 1
# ============================================================
# Jeg forstår veldig lite. Jeg lurer på hva jeg må gjøre for å forstå det bedre. Lese mer, gjøre flere eksempeloppgaver. Vet ikke.



# ============================================================
#                          Oppgave 9
# ============================================================
import numpy as np

def merge(A, p, q, r):
    nL = q - p + 1
    nR = r - q
    L = np.zeros(nL)
    R = np.zeros(nR)

    for i in range(len(L)):
        L[i] = A[p + i]
    for j in range(len(R)):
        R[j] = A[q + j + 1]
    i = 0
    j = 0
    k = p
    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1



def merge_sort(A, p, r):
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)



# ------------------ Tests -----------------
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# import random
# from itertools import combinations

# # Testsettet på serveren er større og mer omfattende enn dette.
# # Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# # er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# # De lokale testene består av to deler. Et sett med hardkodete
# # instanser som kan ses lengre nede, og muligheten for å generere
# # tilfeldig instanser. Genereringen av de tilfeldige instansene
# # kontrolleres ved å juste på verdiene under.

# # Kontrollerer om det skal kjøres tester for merge
# test_merge = True
# # Kontrollerer om det skal kjøres tester for merge_sort
# test_merge_sort = True
# # Kontrollerer om det genereres tilfeldige instanser for merge.
# generate_random_tests_merge = False
# # Kontrollerer om det genereres tilfeldige instanser for merge_sort.
# generate_random_tests_merge_sort = False
# # Antall tilfeldige tester som genereres
# random_tests = 10
# # Lavest mulig antall verdier i generert instans.
# n_lower = 3
# # Høyest mulig antall verdier i generert instans.
# # NB: Om denne verdien settes høyt (>=50) kan testene for merge ta veldig
# #     lang tid om koden din ikke produserer riktig svar..
# n_upper = 10
# # Om denne verdien er 0 vil det genereres nye instanser hver gang.
# # Om den er satt til et annet tall vil de samme instansene genereres
# # hver gang, om verdiene over ikke endres.
# seed = 0


# # Hardkodete tester for merge på format (A, p, q, r)
# tests_merge = [
#     ([1], 0, 0, 0),
#     ([1, 3, 2], 0, 0, 1),
#     ([3, 1, 2], 0, 0, 1),
#     ([1, 2, 1, 2], 0, 1, 3),
#     ([1, 2, 1, 2], 0, 1, 2),
#     ([1, 2, 1, 2], 1, 1, 3),
#     ([1, 2, 1, 2], 1, 1, 2),
#     ([1, 2, 1, 2], 1, 2, 3),
#     ([1, 3, 1, 3, 1, 2, 4, 3], 2, 3, 6),
#     ([99, 2, 3, 4, 5, 6, 7, 8, 7], 0, 0, 5),
# ]

# if seed:
#     random.seed(seed)


# # Tilfeldig genererte tester for merge
# def generate_merge_tests(k, nl, nu):
#     for _ in range(k):
#         n = random.randint(nl, nu)
#         p = random.randint(0, n - 2)
#         q = p + random.randint(0, n - p - 2)
#         r = q + random.randint(0, n - q - 1)

#         yield [random.randint(0, 99) for _ in range(n)], p, q, r


# # Finner en løsning for merge gjennom bruteforce
# def answer_merge(A, p, q, r):
#     n = r - p + 1
#     for z in combinations(range(n), q - p + 1):
#         S = [None] * n
#         for i, x in enumerate(z):
#             S[x] = A[p + i]

#         ci = 1
#         for i in range(n):
#             if S[i] is not None:
#                 continue
#             S[i] = A[q + ci]
#             ci += 1

#         X = A[:p] + S + A[r + 1:]
#         if verify_merge(A, p, q, r, X):
#             return X


# # Verifiserer at answer er et riktig svar for merge problemet
# def verify_merge(A, p, q, r, answer):
#     if type(A) != type(answer) or len(A) != len(answer):
#         return False
#     if A[:p] != answer[:p]:
#         return False
#     if A[r + 1:] != answer[r + 1:]:
#         return False

#     def c(B, C, S):
#         if len(B) == 0:
#             return C == S
#         if len(C) == 0:
#             return B == S
#         if S[0] == B[0] and B[0] <= C[0]:
#             return c(B[1:], C, S[1:])
#         if S[0] == C[0] and C[0] < B[0]:
#             return c(B, C[1:], S[1:])
#         return False

#     return c(A[p:q + 1], A[q + 1:r + 1], answer[p:r + 1])


# if generate_random_tests_merge:
#     tests_merge.extend(generate_merge_tests(random_tests, n_lower, n_upper))

# if not test_merge:
#     tests_merge = []

# failed = False
# for A, p, q, r in tests_merge:
#     student = A[:]
#     merge(student, p, q, r)
#     if not verify_merge(A, p, q, r, student):
#         if failed:
#             print("-"*50)

#         failed = True
#         print(f"""
# merge feilet for følgende instans:
# A: {A}
# p: {p}
# q: {q}
# r: {r}

# Ditt svar: {student}
# Riktig svar: {answer_merge(A, p, q, r)}
# """)


# if not failed and test_merge:
#     print("merge ga riktig svar for alle eksempeltestene")
# elif test_merge:
#     print("-"*50)


# # Hardkodete merge_sort tester på format: (A, p, r)
# tests_merge_sort = [
#     ([], 0, -1),
#     ([1], 0, 0),
#     ([1, 3, 2], 0, 1),
#     ([3, 1, 2], 0, 1),
#     ([1, 2, 1, 2], 0, 3),
#     ([1, 2, 1, 2], 0, 2),
#     ([1, 2, 1, 2], 1, 3),
#     ([1, 2, 1, 2], 1, 2),
#     ([3, 1, 0, 5], 0, 3),
#     ([1, 3, 1, 3, 1, 2, 4, 3], 2, 6),
#     ([99, 2, 3, 4, 5, 6, 7, 8, 7], 0, 5),
#     ([1, 0, 5], 7, 6),
#     ([1, 0, 5], 7, 7),
#     ([1, 0, 5], 1, 1),
# ]


# # Genererer tilfeldige tester for merge_sort
# def generate_merge_sort_tests(k, nl, nu):
#     for _ in range(k):
#         n = random.randint(nl, nu)
#         p = random.randint(0, n - 2)
#         r = p + random.randint(0, n - p - 1)

#         yield [random.randint(0, 99) for _ in range(n)], p, r


# if generate_random_tests_merge_sort:
#     tests_merge_sort.extend(generate_merge_sort_tests(random_tests, n_lower, n_upper))

# if not test_merge_sort:
#     tests_merge_sort = []

# failed = False
# for A, p, r in tests_merge_sort:
#     student = A[:]
#     merge_sort(student, p, r)
#     ans = A[:p] + sorted(A[p:r + 1]) + A[r + 1:]
#     if student != ans:
#         if failed:
#             print("-"*50)

#         failed = True

#         print(f"""
# merge_sort feilet for følgende instans:
# A: {A}
# p: {p}
# r: {r}

# Ditt svar: {student}
# Riktig svar: {ans}
# """)

# if not failed and test_merge_sort:
#     print("merge_sort ga riktig svar for alle eksempeltestene")



# ============================================================
#                          Oppgave 11
# ============================================================
# def find_maximum(x):
#     if len(x) == 1:
#         return x[0]
#     venstre = 0
#     høyre = len(x) - 1

#     while venstre < høyre:
#         midt = (venstre + høyre) // 2

#         if x[midt] < x[midt + 1]:
#             # Vi er på den stigende siden
#             venstre = midt + 1
#         else:
#             # Vi er på toppen eller den synkende siden
#             høyre = midt

#     return x[venstre]



def find_maximum(x):
    n = len(x)
    if n == 1:
        return x[0]

    # Rotasjonen kan gjøre at selve toppen havner helt i kant
    if x[0] > x[1] and x[0] > x[n - 1]:
        return x[0]
    if x[n - 1] > x[n - 2] and x[n - 1] > x[0]:
        return x[n - 1]

    venstre, høyre = 0, n - 1

    if x[0] < x[1]:
        # Mønster: stigende - synkende - (evt. stigende hale)
        referanse = x[0]
        while venstre < høyre:
            midt = (venstre + høyre) // 2
            if x[midt] < x[midt + 1]:
                if x[midt] >= referanse:
                    venstre = midt + 1   # ekte stigende del mot toppen
                else:
                    høyre = midt         # den "falske" halen
            else:
                høyre = midt             # synkende -> toppen er her eller til venstre
    else:
        # Mønster: synkende - stigende - (evt. synkende hale)
        referanse = x[n - 1]
        while venstre < høyre:
            midt = (venstre + høyre) // 2
            if x[midt] > x[midt + 1]:
                if x[midt] >= referanse:
                    høyre = midt         # ekte synkende del, kommer fra toppen
                else:
                    venstre = midt + 1   # den "falske" innledende delen
            else:
                venstre = midt + 1       # stigende -> toppen er til høyre

    return x[venstre]



# ----------------------- Tests -----------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


# Hardkodete tester på format: (x, svar)
tests = [
    ([1], 1),
    ([1, 3], 3),
    ([3, 1], 3),
    ([1, 2, 1], 2),
    ([1, 0, 2], 2),
    ([2, 0, 1], 2),
    ([0, 2, 1], 2),
    ([0, 1, 2], 2),
    ([2, 1, 0], 2),
    ([2, 3, 1, 0], 3),
    ([2, 3, 4, 1], 4),
    ([2, 1, 3, 4], 4),
    ([4, 2, 1, 3], 4),
]

# En liste som ikke kan skrives til
class List:
    def __init__(self, li):
        self.__internal_list = li

    def __getitem__(self, key):
        return self.__internal_list[key]

    def __len__(self):
        return len(self.__internal_list)

    def __setitem__(self):
        raise NotImplementedError(
            "Du skal ikke trenge å skrive til listen"
        )

# Genererer tilfeldige instanser med svar
def generate_examples(k, nl, nu):
    for _ in range(k):
        n = random.randint(nl, nu)
        x = random.sample(range(5*n), k=n)
        answer = max(x)
        t = x.index(answer)
        x = sorted(x[:t]) + [answer] + sorted(x[t + 1:], reverse=True)
        t = random.randint(0, n)
        x = x[t:] + x[:t]
        yield x, answer


if generate_random_tests:
    if seed:
        random.seed(seed)

    tests.extend(generate_examples(random_tests, n_lower, n_upper))


failed = False
for x, answer in tests:
    x_ro = List(x[:])
    student = find_maximum(x_ro)
    if student != answer:
        if failed:
            print("-"*50)

        failed = True

        print(f"""
Koden ga feil svar for følgende instans:
x: {x}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")