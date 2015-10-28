import urllib.request
import json

X = [[]]
Y = []

# for n in range(1, 3) - '3' zmieniamy na liczbe postow. obecnie 2772 i lecimy po wszystkich
for n in range(1, 3):
    url = "http://naos-software.com/dataprocessing/rest-api/resultDocuments/"+str(n)
    response = urllib.request.urlopen(url)
    content = response.read()
    data = json.loads(content.decode("utf8"))

    arrayResult = data['result'].split(" ")
    l = len(arrayResult)

    for i in range(1, l):
        tmp = arrayResult[i].split(":")
        if(tmp[0] == str(i)):
            X[n-1].append(tmp[1])
        else:
            X[n-1].append('0')

    Y.append(arrayResult[0])
    X.append([])

print (X)
print (Y)

