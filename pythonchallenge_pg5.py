import requests

link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + x
f = requests.get(link)

print(f.text)

