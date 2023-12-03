import requests

proxies = open("proxies.txt").read().split("\n")
open("working.txt","w").write("")

for proxy in proxies:

    proxies = {
        "http": f"http://{proxy}/",
        "https": f"http://{proxy}/"
    }

    url = 'https://api.ipify.org'

    try:
        response = requests.get(url, proxies=proxies)
        print(proxy, " working. IP:", response.text)
        open("working.txt","a").write(proxy + "\n")
    except:
        print(proxy, " does not work.")
        
        
        
input("Working proxies saved into working.txt. Press enter to exit..")