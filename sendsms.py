import requests

url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"5cK4qWZ4iQhuTO5nJTU3FwFMxh3u0QEfHSn43MoOvEV4N1SUhcqJIzrPil5x","sender_id":"FSTSMS","message":"This is test message","language":"english","route":"p","numbers":"9088029355"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)