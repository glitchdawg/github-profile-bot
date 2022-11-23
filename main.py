#importing requests lib
import requests
#importing the BeautifulSoup module from bs4
from bs4 import BeautifulSoup as bs

#taking user input

username=input('Enter github Username:')
url='https://github.com/'+username
r=requests.get(url)
soup=bs(r.content,'html.parser')
avatar=soup.find('img',{'alt':'Avatar'})['src']
print(avatar)


