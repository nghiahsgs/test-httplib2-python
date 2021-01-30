import httplib2
import urllib
 
http = httplib2.Http()
 
url = "http://global.longmandictionaries.com/dict_search/entry_for_alpha_key/lcdt/"
cookie = "_ga=GA1.2.593997455.1608592969; _gid=GA1.2.1576812044.1612036872; ci_session=a%3A10%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22ae8ddc64539a01bf64b1ee3b66e97acc%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A12%3A%2242.118.55.78%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F87.0.4280.141+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1612036981%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A5%3A%22email%22%3Bs%3A25%3A%22futuregoten1997%40gmail.com%22%3Bs%3A2%3A%22id%22%3Bs%3A6%3A%22108806%22%3Bs%3A7%3A%22user_id%22%3Bs%3A6%3A%22108806%22%3Bs%3A8%3A%22group_id%22%3Bs%3A1%3A%222%22%3Bs%3A5%3A%22group%22%3Bs%3A7%3A%22members%22%3B%7D895b7995d1e361b3c07b6124eb6f87f25d83f111; _gat=1; dict_lcdt=learn"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Referer":"http://global.longmandictionaries.com/lcdt/collocations",
    "Cookie":cookie,
    "Accept-Language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
}
raw_data = 'alpha_key=beautiful&name='
 
content = http.request(url, 
                       method="POST", 
                       headers=headers,
                    #    body=urllib.parse.urlencode(body) )[1]
                       body=raw_data )[1]
 
print(content.decode()
