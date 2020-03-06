from wget import download
from csv import reader
from os import chdir, mkdir, path
from urllib.request import urlopen


def flvScript():

    print('name anime')
    directoryName = input()

    if not path.exists(directoryName):

        mkdir(directoryName)

    csvFile = open(directoryName + '.csv', 'r')
    readerOfUrl = reader(csvFile, delimiter=' ')
    listOfUrl = []
    chdir(directoryName)
    for url in readerOfUrl:
        listOfUrl.append(url)

    for url in range(len(listOfUrl)):
        tmp = str(listOfUrl[url])
        tmp = tmp.replace("['", '')
        tmp = tmp.replace("']", '')

        print(tmp)
        response = urlopen(tmp)
        response = response.getcode()
        print(response)
        dumpName = directoryName + ' - ' + str(url + 1)
        secondPass = path.exists(dumpName)

        if response is 200 and secondPass is False:

            download(tmp, dumpName)


flvScript()
