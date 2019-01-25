import requests

url = "http://www.txt80.com/e/DownSys/doaction.php"

querystring = {"enews":"DownSoft","classid":"1","id":"9777","pathid":"0","pass":"0119ac5498928a0957863eee3cc26df6","p":"::::::"}

headers = {
    'Cookie': "UM_distinctid=16883c294e5605-05877eae4a78f5-162a1c0b-15f900-16883c294e64f1; CNZZDATA1263014046=663340662-1548397110-null%7C1548397110",
    'Cache-Control': "no-cache",
    'Postman-Token': "41bfbab1-2eac-4aa5-9572-e96bedf08e9d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)