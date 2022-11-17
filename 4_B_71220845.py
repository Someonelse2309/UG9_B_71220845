nama = input("Siapa Namamu : ")
print ("=======================================================================")
print
print ("<<<<< Petualangan ",nama," >>>>>")
print
print ("Welcome to the Adventure of ",nama,"!")
print
print ("Apa gendermu? [M/F]")
pro = input(">> ")
print
print
print
print
print ("Suatu hari hiduplah seorang bocil kematian bernama ",nama,", Dia hidup sebatang kara dengan ayahnya yang adalah seorang petani jagung")
print ("Suatu hari ",nama," diberikan pilihan untuk tidur atau membantu ayah")
print ("Apa yang akan ",nama," lakukan?")
print ("1. Tidur")
print ("2. Membantu Ayah")
pil1 = int(input(">> "))
if pil1 == 1:
    print ("Ayah pun memarahi ",nama," dan akhirnya ",nama," pun harus bangun dan bekerja")
else:
    if pil1 == 2:
        print ("Ayah pun memuji ",nama," dan akhirnya merekapun bekerja bersama")
    else:
        print ("Salah Input")
print("")
print("Di ladang cuaca sangat panas dan terik, Ayah pun membawakan sebuah apel. Apa yang akan ",nama," lakukan?")
print ("1. Makan apel itu sendiri")
print ("2. Membagi dua apel itu dan memakan bersama ayah")
pil2 = int(input(">> "))
if pil2 == 1 :
    print ("Ayah pun melihat ",nama," makan apel itu sendiri, dan ayah pun harus menahan lapar")
else :
    if pil2 == 2:
        print ("Ayah pun memuji ",nama," dan akhirnya merekapun makan bersama")
    else:
        print ("Salah Input")
print("")
print("Setelah makan, merekapun kembali bekerja, lalu ",nama," menemukan sebuah kotak di ladang. Apa yang akan ",nama," lakukan?")
print ("1. Membuka kotak itu")
print ("2. Menunggu ayah")
pil3 = int(input(">> "))
if pil3 == 1 :
    print ("Ayah pun melihat ",nama," membuka kotak itu sendiri, Namun ayah kecewa karena ",nama," tidak menunggu ayah")
else :
    if pil3 == 2:
        print ("Ayah pun memuji ",nama," karena mau menunggu dan akhirnya merekapun membuka kotak itu bersama")
    else:
        print ("Salah Input")
print("")
print("Setelah melihat kode itu pun merekapun kembali bekerja, lalu ",nama," ingat akan sebuah kotak di rumah yang memiliki kode yang sama.")
print (nama,"pun membuka kotak itu, isinya ada banyak emas. ",nama,"pun berfikir apakah ia perlu memberi tahu ayah, Apa yang akan ",nama," lakukan?")
print ("1. Memberi tahu ayah")
print ("2. Menyimpan semua emasnya sendiri")
pil4 = int(input(">> "))
if pil4 == 1 :
    print (nama,"pun menjadi kaya raya namun membiarkan ayahnya sendiri miskin")
else :
    if pil4 == 2:
        print ("Ayah pun sadar apa yang telah ",nama," lakukan, lalu ayah pun membunuh ",nama," karena menemukan uang untuk selingkuhan ayahnya di kota")
    else:
        print ("Salah Input")
print ("")
print ("THE END")

