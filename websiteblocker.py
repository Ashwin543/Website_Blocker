from datetime import datetime

host_path="c:/Users/LENOVO/OneDrive/Documents/Ashwin/dupe_host"
redirect = "127.0.0.1"
# C:\Users\LENOVO\OneDrive\Documents\Ashwin

website_list=["facebook.com", "www.facebook.com", "www.instagram.com"]

start_date = datetime(2021, 9, 20)
end_date = datetime(2021, 10, 23)
today_date = datetime(datetime.now().year, datetime.now().month, datetime.now().day)

while True:
    if start_date <= today_date < end_date:
        with open(host_path, "r") as file:
            content = file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
        print("all sites are blocked")
        break
    else: # end_date < today_date
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)
            file.truncate()
        print("all sites unblocked")
        break