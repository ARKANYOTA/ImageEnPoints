from PIL import Image
def ImgToChr4(file):
    img = Image.open(file)
    lar, hau = img.size
    newimg = Image.new("RGB", (((lar//2)*2)+1, (hau//3)*3))
    for l in range(hau):
        for c in range(lar-1):
            pix = img.getpixel((c, l))
            gris = int((pix[0]+pix[1]+pix[2])/96)

            try:
                newimg.putpixel((c, l),(gris*64, gris*64, gris*64))
            except:
                pass

    newimg.show()
    data = list(newimg.getdata())
    k = 0
    l = ""
    for i in data:
        k+=1
        if k%lar==0:
            l+= ";"
        l+=str(i).replace("(0, 0, 0)", "v").replace("(1, 1, 1)", ";").replace("(64, 64, 64)", "#").replace("(128, 128, 128)", "!").replace("(192, 192, 192)", ".").replace("(255, 255, 255)", " ")
    #with open("data.txt", "w") as fichier:
     #   fichier.write(l.replace(";", "\n"))
    print(l.replace(";", "\n"))
def ImgToChr4inFile(file, ToFile="data.txt"):
    img = Image.open(file)
    lar, hau = img.size
    newimg = Image.new("RGB", (((lar//2)*2)+1, (hau//3)*3))
    for l in range(hau):
        for c in range(lar-1):
            pix = img.getpixel((c, l))
            gris = int((pix[0]+pix[1]+pix[2])/96)

            try:
                newimg.putpixel((c, l),(gris*64, gris*64, gris*64))
            except:
                pass

    newimg.show()
    data = list(newimg.getdata())
    k = 0
    l = ""
    for i in data:
        k+=1
        if k%lar==0:
            l+= ";"
        l+=str(i).replace("(0, 0, 0)", "v").replace("(1, 1, 1)", ";").replace("(64, 64, 64)", "#").replace("(128, 128, 128)", "!").replace("(192, 192, 192)", ".").replace("(255, 255, 255)", " ")
    with open(ToFile, "w") as fichier:
        fichier.write(l.replace(";", "\n"))
