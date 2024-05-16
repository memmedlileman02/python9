with open("cumle1.txt", "w") as f:
    f.write("have a good weekend \n Thank you very much \n See you later")


with open("cumle1.txt", "r") as f:
    ilk_setir = f.readline()
    boyukherfler = ilk_setir.upper()

with open("boyukherfler.txt", "w") as f:
    f.write(boyukherfler)


