from histeq_gauss import histeq_gauss
from bwlabel import bwlabel
from imclose import imclose
from entropyfilt import entropyfilt
from utils import RGB_IMAGE, BINARY_IMAGE, MONO_IMAGE
from utils import process_image


def start():
    print("Wybierz obraz jaki chcesz przetworzyć")
    print("1. Monochromatyczny")
    print("2. RGB")
    print("3. Binarny")
    print("4. Zakończ program")
    typ = int(input("Wybór: "))
    return typ

def mono(img):
    print("Wybrany obraz to "+img)
    print("Wybierz akcje: ")
    print("1. Wyrównywanie histogramu obrazu do rozkładu Gaussa o zadanym odchyleniu")
    print("2. Filtracja entropii w zadanym oknie")
    print("3. Zamknięcie elementem linijnym o zadanej długości i nachyleniu")
    print("4. Zmień obrazek (upewnij się że znajduje się w katalogu images)")
    print("5. Powrót")
    typ = int(input("Wybór: "))
    if typ == 1:
        std = int(input("Podaj odchylenie standardowe: "))
        process_image(img, 'mono', histeq_gauss, std)
    elif typ == 2:
        window = int(input("Podaj wielkość okna: "))
        process_image(img, 'mono', entropyfilt, window)
    elif typ == 3:
        length = int(input("Podaj długość elementu: "))
        angle = int(input("Podaj kąt: "))
        process_image(img, 'mono', imclose, length, angle)
    elif typ == 4:
        new_name = input("Podaj nazwę obrazka: ")
        mono(new_name)
    elif typ == 5:
        return
    else:
        print("Źle wybrana akcja")

def rgb(img):
    print("Wybrany obraz to "+img)
    print("Wybierz akcje: ")
    print("1. Wyrównywanie histogramu obrazu do rozkładu Gaussa o zadanym odchyleniu")
    print("2. Filtracja entropii w zadanym oknie")
    print("3. Zmień obrazek (upewnij się że znajduje się w katalogu images)")
    print("4. Powrót")
    typ = int(input("Wybór: "))
    if typ == 1:
        std = int(input("Podaj odchylenie standardowe: "))
        process_image(img, 'rgb', histeq_gauss, std)
    elif typ == 2:
        window = int(input("Podaj wielkość okna: "))
        process_image(img, 'rgb', entropyfilt, window)
    elif typ == 3:
        new_name = input("Podaj nazwę obrazka: ")
        rgb(new_name)
    elif typ == 4:
        return
    else:
        print("Źle wybrana akcja")

def binary(img):
    print("Wybrany obraz to"+img)
    print("Wybierz akcje: ")
    print("1. Zamknięcie elementem linijnym o zadanej długości i nachyleniu")
    print("2. Etykietowanie")
    print("3. Zmień obrazek (upewnij się że znajduje się w katalogu images)")
    print("4. Powrót")
    typ = int(input("Wybór: "))
    if typ == 1:
        length = int(input("Podaj długość elementu: "))
        angle = int(input("Podaj kąt: "))
        process_image(img, 'binary', imclose, length, angle)
    elif typ == 2:
        process_image(img, 'binary', bwlabel)
    elif typ == 3:
        new_name = input("Podaj nazwę obrazka: ")
        rgb(new_name)
    elif typ == 3:
        return
    else:
        print("Źle wybrana akcja")


if __name__ == '__main__':
    while(1):
        typ = start()
        if typ == 1:
            mono(MONO_IMAGE)
        elif typ == 2:
            rgb(RGB_IMAGE)
        elif typ == 3:
            binary(BINARY_IMAGE)
        elif typ == 4:
            break
        else:
            print("Źle wybrana akcja")


