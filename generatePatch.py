import requests
import sys

if __name__ == '__main__':

    if sys.argv:

        commitNum = len(sys.argv) - 1
        patchString2 = ""

        for index in range(commitNum):

            urlArray = sys.argv[index+1].split("/")
            userName = urlArray[3]
            reposName = urlArray[4]
            commitId = urlArray[6]

            url = "https://api.github.com/repos/" + userName + "/" + reposName +"/compare/" + commitId + "^..." + commitId
            response = requests.get(url)

            html = response.json()
            patchString = ""
            for patchStr in html["files"]:
                patchName = "diff --git a/" + patchStr["filename"] + " b/" + patchStr["filename"] + "\n"
                patchAction = "--- b/" + patchStr["filename"] + "\n" + "+++ b/" + patchStr["filename"] + "\n"
                patchString = patchString + patchName + patchAction + patchStr["patch"] + "\n"

            patchString2 = patchString2 + patchString

        fh = open("CVE.patch","w")
        fh.write(patchString2)
        fh.close()


