import json

str1="office"
mydic={}

for n in str1:
    if (mydic.__contains__(n)):
        mydic[n] += 1
    else:
        mydic[n] = 1

print((str(mydic)).replace(" ",''))
print(json.dumps(mydic))