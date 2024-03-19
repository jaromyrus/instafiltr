from PIL import Image
#obrazek = Image.open("03388450_0.jpeg") váš libovolný obrázek
sirka, vyska = obrazek.size
x = 0
while x < sirka:
    y = 0
    while y < vyska:
        r, g, b = obrazek.getpixel((x,y))
        prumer = int((r+g+b)/3)
        obrazek.putpixel((x,y), (b , g, r))        
       # if prumer > 150:
        #    obrazek.putpixel((x,y), (90, 90, 25))
        #else:
         #   obrazek.putpixel((x,y), (230, 140, 60))
        y += 1
    x += 1
display(obrazek) #obrazek.show()