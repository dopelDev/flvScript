from wget import download
from csv import reader
from os import chdir, mkdir, path
from urllib.request import urlopen
from sys import exit
from urllib.error import HTTPError


def flvScript():

    print('name anime')
    directoryName = input()

    if directoryName is '' or not path.exists(directoryName + '.csv'):
        return exit()

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

        print(tmp, '\n')

        dumpName = directoryName + ' - ' + str(url + 1)
        secondPass = path.exists(dumpName)
        print(dumpName, '\n')

        if secondPass is False:
            try:
                response = urlopen(tmp)
                response = response.getcode()
                print(response)
            except HTTPError as e:
                print(e)
                continue

            if response is 200:
                download(tmp, dumpName)
                print('\n')
        else:
            continue

if __name__ == '__main__':
    flvScript()
