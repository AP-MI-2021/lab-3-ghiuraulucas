from math import *

def main():
    test_numai_patrate_perfecte()
    test_numai_numere_prime()
    test_numai_numere_doar_cu_cifre_prime()
    test_subsecventa_max_numere_patrate_perfecte()
    test_subsecventa_max_numai_numere_prime()
    test_subsecventa_max_numere_cu_cifre_prime()
    l=[]
    option = input ("""
    Alegeti una dintre optiunile de mai jos:
    1. Citirea unei liste.
    2. Determinarea celei mai lungi subsecvente din lista ce contine numai numere patrate perfecte.
    3. Determinarea celei mai lungi subsecvente din lista ce contine numai numere prime.
    4. Determinarea celei mai lungi subsecvente din lista ce contine numai numere formate doar din cifre prime.
    5. Iesire
    """)
    while True:
        if option == "1":
            l = citire_lista()
        elif option == "2":
            print(subsecventa_max_numere_patrate_perfecte(l))
        elif option == "3":
            print(subsecventa_max_numai_numere_prime(l))
        elif option == "4":
            print(subsecventa_max_numere_cu_cifre_prime(l))
        elif option == "5":
            break
        else:
            print("Optiune incorecta. Va rugam sa alegeti din nou: ")
        option = input("""
            Alegeti una dintre optiunile de mai jos:
            1. Citirea unei liste.
            2. Determinarea celei mai lungi subsecvente din lista ce contine numai numere patrate perfecte.
            3. Determinarea celei mai lungi subsecvente din lista ce contine numai numere prime.
            4. Determinarea celei mai lungi subsecvente din lista ce contine numai numere formate doar din cifre prime.
            5. Iesire
            """)


def citire_lista():
    l = []
    lista = input("Introduceti numerele din lista, separate prin virgula: ")
    variabila = lista.split(",")
    for x in variabila:
        l.append(int(x))
    return l


def numai_patrate_perfecte(l):
    '''
    Determina daca toate numerele dintr-o lista sunt patrate perfecte.
    :param l: lista de numere intregi.
    :return: True, daca toate numerele din lista sunt p.p.; False, in rest.
    '''
    for x in l:
        if (sqrt(x) * 10) % 10 != 0:
            return False
    return True

def test_numai_patrate_perfecte():
    assert numai_patrate_perfecte([4, 16, 25]) == True
    assert numai_patrate_perfecte([5, 2]) == False
    assert numai_patrate_perfecte([100]) == True


def numai_numere_prime(l):
    '''
    Verifica daca toate numerele dintr-o lista sunt prime
    :param l: lista de numere intregi
    :return: True, daca toate numerele dintr-o lista sunt prime; False, in rest.
    '''
    for x in l:
        if x < 2:
            return False
        for i in range (2, x//2+1):
            if x % i == 0:
                return False
    return True

def test_numai_numere_prime():
    assert numai_numere_prime([2, 3, 5, 7]) == True
    assert numai_numere_prime([1,2,3,4,5,56]) == False
    assert numai_numere_prime([17, 19]) == True

# Advice: puteam sa iau 2 functii - una care verifica daca un nr are doar cifre prime, a doua sa apeleze
# functia respectiva pentru fiecare element l dintr-o lista data. Keep in mind.

def numai_numere_doar_cu_cifre_prime(l):
    '''
    Determina daca intr-o lista toate numerele sunt formate doar idn cifre prime.
    :param l: lista de numere intregi.
    :return: True, daca conditia pusa e adevarata.
    '''
    m=0
    for x in l:
        q=0
        while x>0:
            a = x % 10
            if a < 2:
                q = q+1
            for i in range(2, a//2+1):
                if a % i == 0:
                    q = q + 1
            if q != 0:
                m = m + 1
            x = x // 10
    if m != 0:
        return False
    else:
        return True

def test_numai_numere_doar_cu_cifre_prime():
    assert numai_numere_doar_cu_cifre_prime([234, 78, 59]) == False
    assert numai_numere_doar_cu_cifre_prime([22, 33, 55, 77]) == True
    assert numai_numere_doar_cu_cifre_prime([2357, 5377, 2323]) == True

def subsecventa_max_numere_patrate_perfecte(l):
    '''
    Determina subsecventa maxima de numere patrate perfecte dintr-o lista
    :param l: lista de numere intregi.
    :return: Lista de numere intregi (patrate perfecte)
    '''
    secv_max = []
    for i in range (0, len(l)):
        for j in range (i, len(l)):
            if numai_patrate_perfecte(l[i: j+1]) == True and len(l[i: j+1]) > len(secv_max):
                secv_max = l[i: j+1]
    return secv_max

def test_subsecventa_max_numere_patrate_perfecte():
    assert subsecventa_max_numere_patrate_perfecte([4,9,16, 8]) == [4, 9, 16]
    assert subsecventa_max_numere_patrate_perfecte([64, 59, 1]) == [64]
    assert subsecventa_max_numere_patrate_perfecte([]) == []


def subsecventa_max_numai_numere_prime(l):
    '''
    Determina subsecventa maxima de numere prime dintr-o lista
    :param l: lista de numere intregi.
    :return: Lista de numere intregi (numere prime)
    '''
    secv_max = []
    for i in range (0, len(l)):
        for j in range (i, len(l)):
            if numai_numere_prime(l[i: j+1]) == True and len(l[i: j+1]) > len(secv_max):
                secv_max = l[i: j+1]
    return secv_max

def test_subsecventa_max_numai_numere_prime():
    assert subsecventa_max_numai_numere_prime([7, 8, 9, 20]) == [7]
    assert subsecventa_max_numai_numere_prime([2, 4, 56, 7, 17, 19]) == [7, 17, 19]
    assert subsecventa_max_numai_numere_prime([]) == []


def subsecventa_max_numere_cu_cifre_prime(l):
    '''
    Determina subsecventa maxima de numere ale caror cifre sunt numere prime dintr-o lista
    :param l: lista de numere intregi.
    :return: Lista de numere intregi (care sunt formate din cifre prime)
    '''
    secv_max = []
    for i in range(0, len(l)):
        for j in range(i, len(l)):
            if numai_numere_doar_cu_cifre_prime(l[i: j + 1]) == True and len(l[i: j + 1]) > len(secv_max):
                secv_max = l[i: j + 1]
    return secv_max

def test_subsecventa_max_numere_cu_cifre_prime():
    assert subsecventa_max_numere_cu_cifre_prime([235, 555, 77, 34]) == [235, 555, 77]
    assert subsecventa_max_numere_cu_cifre_prime([33, 45, 56]) == [33]
    assert subsecventa_max_numere_cu_cifre_prime([]) == []

main()