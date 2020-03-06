from wget import download
from csv import reader
from os import chdir, mkdir


def flvScript():

    print('name anime')
    directoryName = input()
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
        download(tmp, directoryName + ' - ' + str(url + 1))


flvScript()
