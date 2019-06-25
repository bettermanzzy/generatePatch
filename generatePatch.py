import requests
import random
import os

if __name__ == '__main__':


    commitUrl = input("Please input your commit Url: \n")

    if commitUrl:

        commitArray = commitUrl.split(" ")
        commitNum = len(commitArray)-1
        patchString2 = ""
        patchFileName = ""

        for index in range(commitNum):

            urlArray = commitArray[index].split("/")
            userName = urlArray[3]
            reposName = urlArray[4]
            commitId = urlArray[6]

            url = "https://api.github.com/repos/" + userName + "/" + reposName +"/compare/" + commitId + "^..." + commitId
            patchFileName = patchFileName + reposName
            response = requests.get(url)

            html = response.json()
            patchString = ""
            for patchStr in html["files"]:
                patchName = "diff --git a/" + patchStr["filename"] + " b/" + patchStr["filename"] + "\n"
                patchAction = "--- b/" + patchStr["filename"] + "\n" + "+++ b/" + patchStr["filename"] + "\n"
                patchString = patchString + patchName + patchAction + patchStr["patch"] + "\n"

            patchString2 = patchString2 + patchString

        patchFileName = patchFileName + str(random.randint(1,100)) + ".patch"
        print(patchFileName)
        fh = open(patchFileName,"w")
        fh.write(patchString2)
        fh.close()
        os.system("pause")


