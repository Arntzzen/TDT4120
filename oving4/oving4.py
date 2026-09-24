# ====================================================
#                     Oppgave 1
# ====================================================
# Før:
# Ikke stødig på noe egentlig, ergo; usikker på det meste.
# Kommer til å få bedre forståelse generelt.

# Etter:
# Mye jeg fortsatt sliter med å forstå. Alt av programmeringsoppgaver klarer jeg ikke helt alene. Induktive bevis er jeg også dårlig på.


# ====================================================
#                     Oppgave 11
# ====================================================

def counting_sort(A, n):
    if not A:
        return []
    max_val = max(A)
    cnt_ls = [0] * (max_val + 1)
    for i in A:
        cnt_ls[i] += 1
    for i in range(1, max_val + 1):
        cnt_ls[i] += cnt_ls[i - 1]
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        ans[cnt_ls[A[i]] - 1] = A[i]
        cnt_ls[A[i]] -= 1
    return ans


# ------------------ Tests ------------------
# #!/usr/bin/python3
# # coding=utf-8
# import random

# # Testsettet på serveren er større og mer omfattende enn dette.
# # Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# # er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# # De lokale testene består av to deler. Et sett med hardkodete
# # instanser som kan ses lengre nedre, og muligheten for å generere
# # tilfeldige instanser. Genereringen av de tilfeldige instansene
# # kontrolleres ved å justere på verdiene under.

# # Kontrollerer om det genereres tilfeldige instanser.
# generate_random_tests = False
# # Antall tilfeldige tester som genereres.
# random_tests = 10
# # Laveste mulige antall tall i generert instans.
# numbers_lower = 3
# # Høyest mulig antall tall i generert instans.
# numbers_upper = 8
# # Om denne verdien er 0 vil det genereres nye instanser hver gang.
# # Om den er satt til et annet tall vil de samme instansene genereres
# # hver gang, om verdiene over ikke endres.
# seed = 0



# # Hardkodete tester
# tests = [
#     [],
#     [1],
#     [1, 2, 3, 4],
#     [4, 3, 2, 1],
#     [1, 1, 2, 1],
#     [1281, 1, 2],
#     [0, 2047, 0, 2047],
#     [995, 334, 709, 999, 502, 303, 274, 488, 997, 568, 546, 756],
#     [648, 298, 568, 681, 795, 356, 603, 772, 373, 50, 253, 116],
# ]

# def gen_examples(k, lower, upper):
#     for _ in range(k):
#         yield [
#                 random.randint(0, 2047)
#                 for _ in range(random.randint(lower, upper))
#             ]


# if generate_random_tests:
#     if seed:
#         random.seed(seed)
#     tests += list(gen_examples(
#         random_tests,
#         numbers_lower,
#         numbers_upper,
#     ))

# failed = False
# for A in tests:
#     answer = sorted(A)
#     student = counting_sort(A[:], len(A))
#     if student != answer:
#         if failed:
#             print("-"*50)
#         failed = True
#         print(f"""
# Koden feilet for følgende instans:
# A: {A}
# n: {len(A)}

# Ditt svar: {student}
# Riktig svar: {answer}
# """)

# if not failed:
#     print("Koden ga riktig svar for alle eksempeltestene")




# ====================================================
#                     Oppgave 17
# ====================================================

def k_largest(A, n, k):
    if k == 0:
        return []
    pivot = A[n // 2]
    greater = []
    equal = []
    smaller = []
    for x in A:
        if x > pivot:
            greater.append(x)
            continue
        if x == pivot:
            equal.append(x)
            continue
        else:
            smaller.append(x)
    if len(greater) > k:
        if len(greater) == k:
            return greater
        return k_largest(greater, len(greater), k)
    if len(greater) + len(equal) >= k:
        return greater + equal[:k - len(greater)]
    else:
        return greater + equal + k_largest(smaller, len(smaller), k - len(greater) - len(equal))

# ------------------- Tests -------------------
# #!/usr/bin/python3
# # coding=utf-8
# import random

# # Testsettet på serveren er større og mer omfattende enn dette.
# # Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# # er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# # De lokale testene består av to deler. Et sett med hardkodete
# # instanser som kan ses lengre nedre, og muligheten for å generere
# # tilfeldige instanser. Genereringen av de tilfeldige instansene
# # kontrolleres ved å justere på verdiene under.

# # Kontrollerer om det genereres tilfeldige instanser.
# generate_random_tests = False
# # Antall tilfeldige tester som genereres.
# random_tests = 10
# # Laveste mulige antall tall i generert instans.
# numbers_lower = 3
# # Høyest mulig antall tall i generert instans.
# numbers_upper = 8
# # Om denne verdien er 0 vil det genereres nye instanser hver gang.
# # Om den er satt til et annet tall vil de samme instansene genereres
# # hver gang, om verdiene over ikke endres.
# seed = 0



# # Sett med hardkodete tester på format: (A, k)
# tests = [
#     ([], 0),
#     ([1], 0),
#     ([1], 1),
#     ([1, 2], 1),
#     ([-1, -2], 1),
#     ([-1, -2, 3], 2),
#     ([1, 2, 3], 2),
#     ([3, 2, 1], 2),
#     ([3, 3, 3, 3], 2),
#     ([4, 1, 3, 2, 3], 2),
#     ([4, 5, 1, 3, 2, 3], 4),
#     ([9, 3, 6, 1, 7, 3, 4, 5], 4),
# ]

# def gen_examples(k, lower, upper):
#     for _ in range(k):
#         A = [
#                 random.randint(-50, 50)
#                 for _ in range(random.randint(lower, upper))
#             ]
#         yield A, random.randint(0, len(A))


# if generate_random_tests:
#     if seed:
#         random.seed(seed)
#     tests += list(gen_examples(
#         random_tests,
#         numbers_lower,
#         numbers_upper,
#     ))

# failed = False
# for A, k in tests:
#     answer = sorted(A, reverse=True)[:k][::-1]
#     student = k_largest(A[:], len(A), k)

#     if type(student) != list:
#         if failed:
#             print("-"*50)
#         failed = True
#         print(f"""
# Koden feilet for følgende instans:
# A: {A}
# n: {len(A)}
# k: {k}

# Metoden må returnere en liste
# Ditt svar: {student}
# """)
#     else:
#         student.sort()
#         if student != answer:
#             if failed:
#                 print("-"*50)
#             failed = True
#             print(f"""
# Koden feilet for følgende instans:
# A: {A}
# n: {len(A)}
# k: {k}

# Ditt svar: {student}
# Riktig svar: {answer}
# """)

# if not failed:
#     print("Koden ga riktig svar for alle eksempeltestene")


# ====================================================
#                     Oppgave 19
# ====================================================

def countSort_help(A, n, d):
    chr_ls = []
    names = ["a", "b", "ab", "aab"]
    d = 2
    digit = [0] * d
    for i in range(d):
        digit[i] += [char_to_int(name[i]) for name in names if i < len(name)]
    return digit




def flexradix(A, n, d):
    exp = 1
    while d / exp >= 1:
        counting_sort(A, exp)
        exp *= 10
    return A


# -------------------- Tests --------------------
# #!/usr/bin/python3
# # coding=utf-8
# import random
# from string import ascii_lowercase

# # Testsettet på serveren er større og mer omfattende enn dette.
# # Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# # er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# # De lokale testene består av to deler. Et sett med hardkodete
# # instanser som kan ses lengre nedre, og muligheten for å generere
# # tilfeldige instanser. Genereringen av de tilfeldige instansene
# # kontrolleres ved å justere på verdiene under.

# # Kontrollerer om det genereres tilfeldige instanser.
# generate_random_tests = False
# # Antall tilfeldige tester som genereres.
# random_tests = 10
# # Laveste mulige antall strenger i generert instans.
# n_strings_lower = 3
# # Høyest mulig antall strenger i generert instans.
# n_strings_upper = 8
# # Laveste mulige antall tegn i hver streng i generert instans.
# n_chars_lower = 3
# # Høyest mulig antall tegn i hver streng i generert instans.
# n_chars_upper = 15
# # Antall forskjellige bokstaver som kan brukes i strengene. Må være mellom 1 og
# # 26. Plukker de første `n_diff_chars` bokstavene i alfabetet.
# n_diff_chars = 5
# # Om denne verdien er 0 vil det genereres nye instanser hver gang.
# # Om den er satt til et annet tall vil de samme instansene genereres
# # hver gang, om verdiene over ikke endres.
# seed = 0

def char_to_int(char):
    return ord(char) - 97


# # Hardkodete instanser på format: (A, d)
# tests = [
#     ([], 1),
#     (["a"], 1),
#     (["a", "b"], 1),
#     (["b", "a"], 1),
#     (["a", "z"], 1),
#     (["z", "a"], 1),
#     (["ba", "ab"], 2),
#     (["b", "ab"], 2),
#     (["ab", "a"], 2),
#     (["zb", "za"], 2),
#     (["abc", "b"], 3),
#     (["xyz", "y"], 3),
#     (["abc", "b"], 4),
#     (["xyz", "y"], 4),
#     (["zyxy", "yxz"], 4),
#     (["ab", "aaa"], 3),
#     (["abc", "b", "bbbb"], 4),
#     (["abcd", "abcd", "bbbb"], 4),
#     (["abcd", "wxyz", "bbbb"], 4),
#     (["abcd", "wxyz", "bazy"], 4),
#     (["ab", "aab", "aaab", "aaaab", "aaaaab"], 6),
#     (["a", "b", "c", "babcbababa"], 10),
#     (["a", "b", "c", "babcbababa"], 10),
#     (["w", "x", "y", "xxyzxyzxyz"], 10),
#     (["b", "a", "y", "xxyzxyzxyz"], 10),
#     (["jfiqdopvak", "nzvoquirej", "jfibopvmcq"], 10),
# ]

# def gen_examples(k, nsl, nsu, ncl, ncu):
#     for _ in range(k):
#         strings = [
#             "".join(random.choices(
#                 ascii_lowercase,
#                 k=random.randint(ncl, ncu)
#             )) for _ in range(random.randint(nsl, nsu))
#         ]
#         yield (strings, max(map(len, strings)))


# if generate_random_tests:
#     ascii_lowercase = ascii_lowercase[:n_diff_chars]
#     if seed:
#         random.seed(seed)
#     tests += list(gen_examples(
#         random_tests,
#         n_strings_lower,
#         n_strings_upper,
#         n_chars_lower,
#         n_chars_upper,
#     ))

# failed = False
# for A, d in tests:
#     answer = sorted(A)
#     student = flexradix(A[:], len(A), d)
#     if student != answer:
#         if failed:
#             print("-"*50)
#         failed = True

#         print(f"""
# Koden feilet for følgende instans:
# A: {A}
# n: {len(A)}
# d: {d}

# Ditt svar: {student}
# Riktig svar: {answer}
# """)

# if not failed:
#     print("Koden ga riktig svar for alle eksempeltestene")


print(countSort_help(None, None, None))