import urllib.request
import http.cookiejar

# 目标网址
url = 'http://baike.baidu.com/view/21087.htm'

print('第一种方法')
response = urllib.request.urlopen(url)
print(response.getcode())
print(len(response.read()))

print('第二种方法')
request = urllib.request.Request(url)
request.add_header("user-ageng", "Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print('第三种方法')
# 创建cookie容器
cookie = http.cookiejar.CookieJar
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(len(response3.read()))

