
import requests
from bs4 import BeautifulSoup

product_track = [
    {
        "URL": "https://www.flipkart.com/samsung-galaxy-m31-ocean-blue-64-gb/p/itm1268b57512fb8?pid=MOBFPNPS6GTGZHE4&lid=LSTMOBFPNPS6GTGZHE4MR8YKS&marketplace=FLIPKART&srno=s_1_1&otracker=AS_Query_HistoryAutoSuggest_1_3_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_3_na_na_na&fm=SEARCH&iid=7ed64fb0-2813-4eba-a188-31510a3200d9.MOBFPNPS6GTGZHE4.SEARCH&ppt=sp&ppn=sp&ssid=mfr9comyls0000001599722937598&qH=72c0d4f69be69bf9",
        "name": "Space Black 128GB",
        "target_price" : 16000
    },
    {
    "URL":"https://www.flipkart.com/samsung-galaxy-m31-space-black-128-gb/p/itmeb29fb2c00580?pid=MOBFPNPS6QGTKBQB&lid=LSTMOBFPNPS6QGTKBQBGM8FDO&marketplace=FLIPKART&q=Samsung+galaxy+M31&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=445315e9-a0ba-4ee9-9567-ff69ce2a4d85.MOBFPNPS6QGTKBQB.SEARCH&ppt=pp&ppn=pp&ssid=8xzz8tr8kg0000001632470807454&qH=15deaddbe2f10cac",
    "name": "Space Black 64GB",
     "target_price" : 16000
    },

    {
    "URL" : "https://www.flipkart.com/samsung-galaxy-m31-ocean-blue-128-gb/p/itm1e7ce328b07b6?pid=MOBFUYQTFBAYCFKG&lid=LSTMOBFUYQTFBAYCFKGTGCYDF&marketplace=FLIPKART&q=Samsung+galaxy+M31&store=tyy%2F4io&srno=s_1_5&otracker=search&otracker1=search&fm=SEARCH&iid=445315e9-a0ba-4ee9-9567-ff69ce2a4d85.MOBFUYQTFBAYCFKG.SEARCH&ppt=pp&ppn=pp&ssid=8xzz8tr8kg0000001632470807454&qH=15deaddbe2f10cac",
    "name" : "Iceberg Blue 128GB",
    "target_price" : 16000
    },

    {
    "URL" : "https://www.flipkart.com/samsung-galaxy-m31-space-black-64-gb/p/itme0c5a25c1e64a?pid=MOBFPNPSZWQ7YKGH&lid=LSTMOBFPNPSZWQ7YKGHGQDQLJ&marketplace=FLIPKART&q=Samsung+galaxy+M31&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=445315e9-a0ba-4ee9-9567-ff69ce2a4d85.MOBFPNPSZWQ7YKGH.SEARCH&ppt=pp&ppn=pp&ssid=8xzz8tr8kg0000001632470807454&qH=15deaddbe2f10cac",
    "name" : "Space Black 8GBRAM",
    "target_price" : 17000
    },
    {
    "URL" : "https://www.flipkart.com/samsung-galaxy-m31-ocean-blue-128-gb/p/itm1e7ce328b07b6?pid=MOBFUYQTFBAYCFKG&lid=LSTMOBFUYQTFBAYCFKGCDJE4J&marketplace=FLIPKART&q=Samsung+galaxy+M31&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=85a1c6d9-1e2f-45c0-8dbf-826ceb0d0d3e.MOBFUYQTFBAYCFKG.SEARCH&ppt=hp&ppn=homepage&ssid=l8u5ckevsg0000001632479258904&qH=15deaddbe2f10cac",
    "name" : "Ocean Blue 128GB",
    "target_price" : 18000
    }
]

def product_price (URL):
    headers = {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

 #   print(page)

    price3 = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
    return price3.string

result_file = open ('myresult_file_txt','w')

try:
    for every_product in product_track:
        price_returned = product_price(every_product.get("URL"))
        print(price_returned + " - " + every_product.get("name"))

        my_product_price = price_returned[1:]
        my_product_price = my_product_price.replace(",", "")
        my_product_price = int(my_product_price)
        print(my_product_price)

        if my_product_price < every_product.get("target_price"):
            print("available at required price")
            result_file.write(
                every_product.get("name") + " " + "Available at 17K" + "Current price - " + str(my_product_price)+ '\n')

        else:
            print("still at current price")

finally:
    result_file.close()




