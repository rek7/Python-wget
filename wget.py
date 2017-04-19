from bs4 import BeautifulSoup
import urllib.request
site = ""
isrecursive = False;
dl_location = "/tmp/"
resp = urllib.request.urlopen(site)
if isrecursive == True:
    parse = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
    for link in parse.find_all('a', href=True):
        filename = link['href'][::-1].split("/")
        try:
            if filename[0]=="/" or filename[0]=="":
                filename[0] = "index"[::-1]
            print("Downloading: " + filename[0][::-1])
            urllib.request.urlretrieve(link['href'], dl_location + filename[0][::-1])
            print("Finished Downloading: " + filename[0][::-1])
        except Exception as e:
            print(str(e))
            continue
else:
    try:
        filename = site[::-1].split("/")
        if filename[0]=="/" or filename[0]=="":
            filename[0] = "index"[::-1]
        print("Downloading To: " + filename[0][::-1])
        urllib.request.urlretrieve(site, dl_location + filename[0][::-1])
        print("Finished Downloading: " + filename[0][::-1])
    except Exception as e:
        print(str(e))
