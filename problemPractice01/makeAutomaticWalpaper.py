""" 
pROBLEM 

dOWNLOAD AND AUTO SETY BACKGROUND IMAGE

 """

# from urllib import request
import requests
import json
import PyWallpaper



api_url="https://api.nasa.gov/planetary/apod?api_key=UeIu04NbndCvyjma3rCAtgumRT0fuGdDhHebnJ9z"

response=requests.get(api_url)
content=response.content.decode('UTF-8')
# print(content)

#convert string to json
dict_content=json.loads(content)
# print(dict_content)

#get the image url
image_url=dict_content['url']
print(image_url)

#download the image
res=requests.get(image_url)
print(res)

#save the image
with open('apond.png','wb') as image:
    image.write(res.content)


# set as wallpaper
PyWallpaper.change_wallpaper('F:/PROGRAMMING/python-programming/apond.png')