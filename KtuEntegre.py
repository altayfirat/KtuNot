print ("Ktu Bağıl Not Sistemi")
print ("Harf Notu için 1'e , Final Notu için 2'ye Basınız. Çıkmak için 0'a Basınız.")



while True:
 işlem = int(input("İşlem Seçiniz : "))
 if işlem == 0 :
     print("Güle Güle")

 elif işlem == 1 :


        vize = float(input("Vize Notunuzu Girin:"))
        final = float(input("Final Notunuzu Girin:"))
        sapma = float(input("Standart Sapmayı Girin:"))
        ort = float(input("Sınıf Ortalamasını Girin:"))
        gercek = ((((((vize + final) / 2) - ort) / sapma) * 10) + 50)


        if (80 <= ort <= 100) and 90 <= note <= 100:
         print("Harf Notunuz: AA")
        elif (80 <= ort <= 100) and 80 <= note <= 89:
         print("Harf Notunuz: BA")
        elif (80 <= ort <= 100) and 75 <= note <= 79:
         print("Harf Notunuz: BB")
        elif (80 <= ort <= 100) and 70 <= note <= 74:
         print("Harf Notunuz: CB")
        elif (80 <= ort <= 100) and 60 <= note <= 69:
         print("Harf Notunuz: CC")
        elif (80 <= ort <= 100) and 50 <= note <= 59:
         print("Harf Notunuz: DC")
        elif (80 <= ort <= 100) and 40 <= note <= 49:
         print("Harf Notunuz: DD")
        elif (80 <= ort <= 100) and 30 <= note <= 39:
         print("Harf Notunuz: FD")
        elif (80 <= ort <= 100) and 0 <= note <= 29:
         print("Harf Notunuz: FF")

        if (70 < ort < 80) and gercek < 24:
         print("Harf Notunuz: FF")
        elif (70 < ort < 80) and 24 < gercek < 28.99:
         print("Harf Notunuz: FD")
        elif (70 < ort < 80) and 29 < gercek < 33.99:
         print("Harf Notunuz: DD")
        elif (70 < ort < 80) and 34 < gercek < 38.99:
         print("Harf Notunuz: DC")
        elif (70 < ort < 80) and 39 < gercek < 43.99:
         print("Harf Notunuz: CC")
        elif (70 < ort < 80) and 44 < gercek < 48.99:
         print("Harf Notunuz: CB")
        elif (70 < ort < 80) and 49 < gercek < 53.99:
         print("Harf Notunuz: BB")
        elif (70 < ort < 80) and 54 < gercek < 58.99:
         print("Harf Notunuz: BA")
        elif (70 < ort < 80) and gercek >= 59:
         print("Harf Notunuz: AA")

        if (62.5 < ort <= 70) and gercek < 26:
         print("Harf Notunuz: FF")
        elif (62.5 < ort <= 70) and 26 < gercek < 30.99:
         print("Harf Notunuz: FD")
        elif (62.5 < ort <= 70) and 31 < gercek < 35.99:
         print("Harf Notunuz: DD")
        elif (62.5 < ort <= 70) and 36 < gercek < 40.99:
         print("Harf Notunuz: DC")
        elif (62.5 < ort <= 70) and 41 < gercek < 45.99:
         print("Harf Notunuz: CC")
        elif (62.5 < ort <= 70) and 46 < gercek < 50.99:
         print("Harf Notunuz: CB")
        elif (62.5 < ort <= 70) and 51 < gercek < 55.99:
         print("Harf Notunuz: BB")
        elif (62.5 < ort <= 70) and 56 < gercek < 60.99:
         print("Harf Notunuz: BA")
        elif (62.5 < ort <= 70) and gercek >= 61:
         print("Harf Notunuz: AA")

        if (57.5 < ort <= 62.5) and gercek < 28:
         print("Harf Notunuz: FF")
        elif (57.5 < ort <= 62.5) and 28 < gercek < 32.99:
         print("Harf Notunuz: FD")
        elif (57.5 < ort <= 62.5) and 33 < gercek < 37.99:
         print("Harf Notunuz: DD")
        elif (57.5 < ort <= 62.5) and 38 < gercek < 42.99:
         print("Harf Notunuz: DC")
        elif (57.5 < ort <= 62.5) and 43 < gercek < 47.99:
         print("Harf Notunuz: CC")
        elif (57.5 < ort <= 62.5) and 48 < gercek < 52.99:
         print("Harf Notunuz: CB")
        elif (57.5 < ort <= 62.5) and 53 < gercek < 57.99:
         print("Harf Notunuz: BB")
        elif (57.5 < ort <= 62.5) and 58 < gercek < 62.99:
         print("Harf Notunuz: BA")
        elif (57.5 < ort <= 62.5) and gercek >= 63:
         print("Harf Notunuz: AA")

        if (52.5 < ort <= 57.5) and gercek < 30:
         print("Harf Notunuz: FF")
        elif (52.5 < ort <= 57.5) and 30 <= gercek <= 34.99:
         print("Harf Notunuz: FD")
        elif (52.5 < ort <= 57.5) and 35 <= gercek <= 39.99:
         print("Harf Notunuz: DD")
        elif (52.5 < ort <= 57.5) and 40 <= gercek <= 44.99:
         print("Harf Notunuz: DC")
        elif (52.5 < ort <= 57.5) and 45 <= gercek <= 49.99:
         print("Harf Notunuz: CC")
        elif (52.5 < ort <= 57.5) and 50 <= gercek <= 54.99:
         print("Harf Notunuz: CB")
        elif (52.5 < ort <= 57.5) and 55 <= gercek <= 59.99:
         print("Harf Notunuz: BB")
        elif (52.5 < ort <= 57.5) and 60 <= gercek <= 64.99:
         print("Harf Notunuz: BA")
        elif (52.5 < ort <= 57.5) and gercek >= 65:
         print("Harf Notunuz: AA")

        if (47.5 < ort <= 52.5) and gercek < 32:
         print("Harf Notunuz: FF")
        elif (47.5 < ort <= 52.5) and 32 <= gercek <= 36.99:
         print("Harf Notunuz: FD")
        elif (47.5 < ort <= 52.5) and 37 <= gercek <= 41.99:
         print("Harf Notunuz: DD")
        elif (47.5 < ort <= 52.5) and 42 <= gercek <= 46.99:
         print("Harf Notunuz: DC")
        elif (47.5 < ort <= 52.5) and 47 <= gercek <= 51.99:
         print("Harf Notunuz: CC")
        elif (47.5 < ort <= 52.5) and 52 <= gercek <= 56.99:
         print("Harf Notunuz: CB")
        elif (47.5 < ort <= 52.5) and 57 <= gercek <= 61.99:
         print("Harf Notunuz: BB")
        elif (47.5 < ort <= 52.5) and 62 <= gercek <= 66.99:
         print("Harf Notunuz: BA")
        elif (47.5 < ort <= 52.5) and gercek >= 67:
         print("Harf Notunuz: AA")

        if (42.5 < ort <= 47.5) and gercek < 34:
         print("Harf Notunuz: FF")
        elif (42.5 < ort <= 47.5) and 34 <= gercek <= 38.99:
         print("Harf Notunuz: FD")
        elif (42.5 < ort <= 47.5) and 39 <= gercek <= 43.99:
         print("Harf Notunuz: DD")
        elif (42.5 < ort <= 47.5) and 44 <= gercek <= 48.99:
         print("Harf Notunuz: DC")
        elif (42.5 < ort <= 47.5) and 49 <= gercek <= 53.99:
         print("Harf Notunuz: CC")
        elif (42.5 < ort <= 47.5) and 54 <= gercek <= 58.99:
         print("Harf Notunuz: CB")
        elif (42.5 < ort <= 47.5) and 59 <= gercek <= 63.99:
         print("Harf Notunuz: BB")
        elif (42.5 < ort <= 47.5) and 64 <= gercek <= 68.99:
         print("Harf Notunuz: BA")
        elif (42.5 < ort <= 47.5) and gercek >= 69:
         print("Harf Notunuz: AA")

        if (ort <= 42.5) and gercek < 36:
         print("Harf Notunuz: FF")
        elif (ort <= 42.5) and 36 < gercek < 40.99:
         print("Harf Notunuz: FD")
        elif (ort <= 42.5) and 41 < gercek < 45.99:
         print("Harf Notunuz: DD")
        elif (ort <= 42.5) and 46 < gercek < 50.99:
         print("Harf Notunuz: DC")
        elif (ort <= 42.5) and 51 < gercek < 55.99:
         print("Harf Notunuz: CC")
        elif (ort <= 42.5) and 56 < gercek < 60.99:
         print("Harf Notunuz: CB")
        elif (ort <= 42.5) and 61 < gercek < 65.99:
         print("Harf Notunuz: BB")
        elif (ort <= 42.5) and 66 < gercek < 70.99:
         print("Harf Notunuz: BA")
        elif (ort <= 42.5) and gercek >= 71:
         print("Harf Notunuz: AA")








 elif işlem == 2 :


    vize = float(input("Vize Notunuzu Girin:"))
    s = float(input("Standart Sapmayı Girin:"))
    ort = float(input("Sınıf Ortalamasını Girin:"))

    if (80 <= ort <= 90):
        final = (2 * 90 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız AA ".format(final))

        final = (2 * 80 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BA ".format(final))

        final = (2 * 75 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BB ".format(final))

        final = (2 * 70 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CB ".format(final))

        final = (2 * 60 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CC ".format(final))

        final = (2 * 50 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DC ".format(final))

        final = (2 * 40 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DD ".format(final))

        final = (2 * 30 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız FD ".format(final))

    if (70 < ort < 80):
        final = (2 * 59 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız AA ".format(final))

        final = (2 * 54 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BA ".format(final))

        final = (2 * 49 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BB ".format(final))

        final = (2 * 44 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CB ".format(final))

        final = (2 * 39 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CC ".format(final))

        final = (2 * 34 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DC ".format(final))

        final = (2 * 29 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DD ".format(final))

        final = (2 * 24 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız FD ".format(final))

    if (62.5 < ort <= 70):
        final = (2 * 26 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız FD ".format(final))

        final = (2 * 31 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DD ".format(final))

        final = (2 * 36 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DC ".format(final))

        final = (2 * 41 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CC ".format(final))

        final = (2 * 46 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CB ".format(final))

        final = (2 * 51 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BB ".format(final))

        final = (2 * 56 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BA ".format(final))

        final = (2 * 61 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız AA ".format(final))

    if (57.5 < ort <= 62.5):
        final = (2 * 28 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız FD ".format(final))

        final = (2 * 33 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DD ".format(final))

        final = (2 * 38 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DC ".format(final))

        final = (2 * 43 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CC ".format(final))

        final = (2 * 48 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CB ".format(final))

        final = (2 * 53 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BB ".format(final))

        final = (2 * 58 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BA ".format(final))

        final = (2 * 63 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız AA ".format(final))

    if (52.5 < ort <= 57.5):
        final = (2 * 30 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız FD ".format(final))

        final = (2 * 35 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DD ".format(final))

        final = (2 * 40 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DC ".format(final))

        final = (2 * 45 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CC ".format(final))

        final = (2 * 50 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CB ".format(final))

        final = (2 * 55 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BB ".format(final))

        final = (2 * 60 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BA ".format(final))

        final = (2 * 65 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız AA ".format(final))

    if (47.5 < ort <= 52.5):
        final = (2 * 32 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız FD ".format(final))

        final = (2 * 37 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DD ".format(final))

        final = (2 * 42 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DC ".format(final))

        final = (2 * 47 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CC ".format(final))

        final = (2 * 52 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CB ".format(final))

        final = (2 * 57 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BB ".format(final))

        final = (2 * 62 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BA ".format(final))

        final = (2 * 67 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız AA ".format(final))

    if (42.5 < ort <= 47.5):
        final = (2 * 34 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız FD ".format(final))

        final = (2 * 39 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DD ".format(final))

        final = (2 * 44 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DC ".format(final))

        final = (2 * 49 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CC ".format(final))

        final = (2 * 54 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CB ".format(final))

        final = (2 * 59 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BB ".format(final))

        final = (2 * 64 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BA ".format(final))

        final = (2 * 69 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız AA ".format(final))

    if (ort <= 42.5):
        final = (2 * 36 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız FD ".format(final))

        final = (2 * 41 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DD ".format(final))

        final = (2 * 46 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız DC ".format(final))

        final = (2 * 51 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CC ".format(final))

        final = (2 * 56 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız CB ".format(final))

        final = (2 * 61 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BB ".format(final))

        final = (2 * 66 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız BA ".format(final))

        final = (2 * 71 * s - 10 * vize + 20 * ort - 100 * s) / 10
        print("{} Alırsanız AA ".format(final))


 continue