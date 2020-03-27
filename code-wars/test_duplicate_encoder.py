def duplicate_encode(word):
    for i in range(len(word)):
        for j in range(i, len(word)-1):
            if word[i].lower() == word[j+1].lower():
                print(word[i], word[j+1], i)
                #print(word[j+1])

        #print("==")


#duplicate_encode("recede")
#duplicate_encode("Success")

a=1

def do(x):
    return(x+a)

print(do(1))