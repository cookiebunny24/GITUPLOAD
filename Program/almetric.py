

def stopclosing(text,k):
    text_trim=list()
    text_trim=text.split()
    print(text_trim)
    mydic=dict()
    for i in text_trim:
        if mydic.__contains__(i):
            mydic[i]+=1
        else:
            mydic[i]=1

    for x,y in mydic.items():
        if y>=k:
            return  str(x), y


input = "The brown dog was so awsome brown"
print(stopclosing(input,k=2))