import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter - ')
print('1_Retrieving', url, type(url)) #class str
uh = urllib.request.urlopen(url)
print('2_uh', uh, type(uh)) #class 'http.client.HTTPResponse'
data = uh.read()
print("3_uh.read() or data", data, type(data)) #calss bytes
data = data.decode()
print("4_data decode", data, type(data)) #class str
tree = ET.fromstring(data)
print("5_tree", tree, type(tree)) #class 'xml.etree.ElementTree.Element'
count = tree.findall('.//count')
print("6_count", count, type(count), "len", len(count)) #class 'list

i = 0
i = int(i)
sumnum = list()

while True :
    try :
        countext = count[i].text
        countext = int(countext)
        sumnum.append(countext)
        print("7_count", countext, type(countext))
        i = i + 1
        continue
    except :
        break
    
print("sumnum", sum(sumnum), type(sumnum))