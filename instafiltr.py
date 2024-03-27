
from PIL import Image
image_path = input("Zadejte cestu k obrázku: ")
obrazek = Image.open(image_path)
sirka, vyska = obrazek.size

def vlastnifiltr():
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y)) 
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (b , g, r))        
            y += 1
        x += 1
    obrazek.show()
def negativ():
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            obrazek.putpixel((x,y), (255-r, 255-g, 255-b))
            y += 1
        x += 1
    obrazek.show()

def cernobily():
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (prumer, prumer, prumer))
            y += 1
        x += 1
    obrazek.show()

print("Vítejte v mém editoru na fotky (ZATÍM POUZE NA FILTRY)!")
print("Máte na výběr ze 3 mých vlastních filtrů, vyberte si kterýkoliv chcete !")
volba = int(input(" 1. Fialový filtr (romantický)\n 2. Negativ\n 3. Černobílý\n V kódu si importujte obrázek dle vaší libosti!\n Vaše volba: "))

if volba == 1:
    vlastnifiltr()
    print("hodně romantické <3")

elif volba == 2:
    negativ()
    print("hodně negativní :(")

elif volba == 3:
    cernobily()
    print("hodně starý")
