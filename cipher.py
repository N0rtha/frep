'''
Шифровка по Цезарю
Нет заглавных букв
Работает через файл с названием text.txt
Результат в файле caesar cipher.txt
'''
def ccipher(i):
    count=0
    countt=0
    f = open("text.txt")
    fi = open('caesar cipher.txt','w')
    for line in f:
        count+=1
    f = open("text.txt")
    for line in f:
        countt+=1
        if count!=countt:
            line=line[0:len(line)-1].lower()
        alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        index=0
        tindex=0
        text=''
        for a in line:
            if a!=" ":
                for b in alp:
                    if a!=b:
                        index+=1
                    else:
                        tindex=index+i
                        index=0
                        break
                if tindex>25:
                    tindex=tindex-26
                text=text+alp[tindex]
            else:
                text=text+a
        fi.write(text+"\n")

'''
'''
def crackc():
    i=-1
    fi = open("cracked caesar.txt","w")
    for cracking in range(26):
        i+=1
        count=0
        countt=0
        raz="---------------------------------------------------  "+str(i)
        f = open("cipher.txt")
        fi.write(raz+'\n')
        for line in f:
            count+=1
        f = open("cipher.txt")
        for line in f:
            countt+=1
            if count!=countt:
                line=line[0:len(line)-1]
            alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            index=0
            text=''
            for a in line:
                if a!=" ":
                    for b in alp:
                        if a!=b:
                            index+=1
                        else:
                            tindex=index+i
                            index=0
                            break
                    if tindex>25:
                        tindex=tindex-26
                    text=text+alp[tindex]
                else:
                    text=text+a
            fi.write(text+'\n')

'''
'''
def vcipher(key):
    alp = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
    #alp.get("h")
    f = open("text.txt")
    fi = open('Vigenere cipher.txt','w')
    for line in f:
        count+=1
    f = open("text.txt")
    for line in f:
        countt+=1
        if count!=countt:
            line=line[0:len(line)-1].lower()
        
        




