T= int(input("enter number of inputs:\n"))
for aditi in range(T):
    N = int(input("enter length of string:\n"))
    wrd = input("enter string:\n")
    wrd1 = ''
    primeAlpha = {67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113}
    listPrimeAlpha = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    for char in wrd:
        ascii = ord(char)
        if ascii in primeAlpha:
            wrd1 += char
        else:
            if ascii > 113:
                wrd1 += chr(113)
                continue
            listPrimeAlpha1 = listPrimeAlpha[:]
            listPrimeAlpha1.append(ascii)
            listPrimeAlpha1.sort()
            i = listPrimeAlpha1.index(ascii)
            b, a = listPrimeAlpha1[i-1], listPrimeAlpha1[i+1]
            bd = abs(ascii - b)
            ad = abs(a - ascii)
            if bd < ad:
                ascii = b
            elif bd > ad:
                ascii = a
            else:
                ascii = min(b, a)
            wrd1 += chr(ascii)
    print("Panda's Magical Word:\n",wrd1)
