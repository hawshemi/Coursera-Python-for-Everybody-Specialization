import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter - ')
print('1_Retrieving', url, type(url)) #class str
uh = urllib.request.urlopen(url)
print('2_uh', uh, type(uh)) #class 'http.client.HTTPResponse'
data = uh.read()
print("3_uh.read() or data", data, type(data)) #calss bytes
data = data.decode()
print("4_data decode", data, type(data)) #class str
info = json.loads(data)

print("5_info", info, type(info), '5_len_info', len(info)) #class dict
print('6_comments',info['comments'][2]['count']) # just as way to recover smth
print('7_comments type', type(info['comments']), '7_comments len', len(info['comments']))

x = 0

for item in (info['comments']) :
    print('count', item['count'], type(item['count']))
    x = x + item['count']

print(x)