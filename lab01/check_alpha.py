from PIL import Image

# Wczytanie obrazu z przezroczystością (np. PNG)

img = Image.open("logo.png")

# Wypisanie kanałów

print(img.getbands())

# Wynik w konsoli: ('R', 'G', 'B', 'A')


# OR
# Sprawdzenie trybu obrazu
img = Image.open("obraz.png")

if "A" in img.getbands():
    print("Obraz zawiera kanał alfa.")
else:
    print("Obraz nie zawiera kanału alfa.")