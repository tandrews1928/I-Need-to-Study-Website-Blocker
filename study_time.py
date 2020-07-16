import time

from datetime import datetime as dt

hosts_path = r"/etc/hosts"   # r is for raw string

hosts_temp = "hosts"

redirect = "0.0.0.0"

bad_web_sites = ["www.amazon.com", "amazon.com", "www.reddit.com", "reddit.com"]     

while True:
    print("Block Sites")
    with open(hosts_path, "r+") as file:
        content = file.read()
        for website in bad_web_sites:
            if website in content:
                pass
            else:
                file.write(redirect+" "+website+"\n")
    time.sleep(5)