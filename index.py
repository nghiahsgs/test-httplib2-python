import httplib2
import io

def write_file(ndung):
    f=io.open('code.html',mode='w',encoding='utf-8')
    f.write(ndung)
    f.close()

http = httplib2.Http()
content = http.request("https://batdongsan.com.vn/ban-dat-duong-cai-dam-phuong-bai-chay/can-ban-gap-lo-gia-re-khu-7-tp-ha-long-quang-ninh-pr26120859")[1]

ndung=content.decode()
# print(content.decode())
write_file(ndung)