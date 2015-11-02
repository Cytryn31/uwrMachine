import urllib.request
import json

X = []
Y = []
wordsArray = []
opinionArray = []
maxWord = 25939
Xcnt = 0

url = "http://naos-software.com/dataprocessing/rest-api/resultDocuments"
response = urllib.request.urlopen(url)
content = response.read()
data = json.loads(content.decode("utf8"))

Page = data['page']
totalPages = Page['totalPages']

for p in range(0, totalPages):
    url = "http://naos-software.com/dataprocessing/rest-api/resultDocuments?page="+str(p)
    response = urllib.request.urlopen(url)
    content = response.read()
    data = json.loads(content.decode("utf8"))

    content = data['_embedded']
    resultDocuments = content['resultDocuments']

    for document in resultDocuments:
        tmpArr = document['result'].split(" ")
        Y.append(tmpArr[0])
        X.append(['0'])
        countWords = 1
        for i in range(1, len(tmpArr)):
            word = tmpArr[i].split(":")
            stop = 0
            while (stop == 0):
                if(int(word[0]) != countWords):
                    X[Xcnt].append('0')
                else:
                    X[Xcnt].append(word[1])
                    stop = 1
                countWords += 1

        while countWords < maxWord:
             X[Xcnt].append('0')
             countWords += 1

        Xcnt +=1





