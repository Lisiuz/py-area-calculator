from rich import print
from tqdm import tqdm
import time

# modifica per testare github pull extension


def area_calc():
    lista_fig_geom = ["1", "2", "3", "4"]
    print("\n***************\nAREA CALCULATOR\n***************\n\nSelezione la figura geometrica\n")
    while True:
        fig_geom = input(
            "\n(1 - Cerchio, 2 - Quadrato, 3 - Rettangolo, 4 - Triangolo): ")
        if fig_geom in lista_fig_geom:
            break
        else:
            print("\nSelezione non valida. Inserisci un indice numerico valido:")
    if fig_geom == "1":
        print("\n*****************************\nCalcolo dell'area del cerchio\n")
        while True:
            raggio = input("Inserisci il raggio del cerchio: ")
            try:
                raggio = float(raggio)
                break
            except ValueError:
                print("Non hai inserito un numero valido. Inserisci il raggio: ")
        raggio = float(raggio)
        area = float((raggio*raggio) * 3.14)
        print(f"\nL'area del cerchio, avente raggio {raggio}, è: ", area)

    elif fig_geom == "3":
        print("\n********************************\nCalcolo dell'area del rettangolo\n")
        while True:
            base = input("Inserisci lunghezza della base: ")
            try:
                base = float(base)
                break
            except ValueError:
                print("Non hai inserito un numero. Inserisci la base: ")
        while True:
            altezza = input("Inserisci altezza: ")
            try:
                altezza = float(altezza)
                break
            except ValueError:
                print("Non hai inserito un numero. Inserisci l'altezza: ")
        altezza = float(altezza)
        area = float(base * altezza)
        print(
            f"\nL'area del rettangolo, avente base {base} ed altezza {altezza}, è: ", area)

    elif fig_geom == "2":
        print("\n******************************\nCalcolo dell'area del quadrato\n")
        while True:
            base = input("Inserisci lunghezza del lato: ")
            try:
                base = float(base)
                break
            except ValueError:
                print("Non hai inserito un numero. Inserisci lunghezza del lato:")
        base = float(base)
        area = float(base ** 2)
        print(
            f"\nL'area del quadrato, avente per lato {base}, è: ", area)

    elif fig_geom == "4":
        print("\n********************************\nCalcolo dell'area del triangolo\n")
        while True:
            base = input("Inserisci lunghezza della base: ")
            try:
                base = float(base)
                break
            except ValueError:
                print("Non hai inserito un numero. Inserisci la base:")
        while True:
            altezza = input("Inserisci altezza: ")
            try:
                altezza = float(altezza)
                break
            except ValueError:
                print("Non hai inserito un numero. Inserisci l'altezza:")
        altezza = float(altezza)
        area = float((base * altezza)/2)
        print(
            f"\nL'area del triangolo, avente per base {base} ed altezza {altezza}, è: ", area)

    yes_no = input("\nVuoi calcolare un'altra area? S(Si) or any key(Exit): ")
    if yes_no.lower() == "s":
        area_calc()
    else:
        exit()


print("AREA CALCULATOR - LizPy Project\n")
for i in tqdm(range(300), desc="LET'S GO!", ascii=False, ncols=75):
    time.sleep(0.003)
    # Loader. Because, why not?


area_calc()
