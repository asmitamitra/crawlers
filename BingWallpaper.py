import requests
from bs4 import BeautifulSoup
import os
import datetime
import sys
import subprocess


# Apple Script to set wallpaper
SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""



dt = datetime.datetime.now()
cd = str(dt.year)+'0'+str(dt.month)+str(dt.day)
while True:
	dt = datetime.datetime.now()
	if (dt.hour == 0 and dt.minute == 2 and dt.second == 0) or (dt.hour == 15 and dt.minute == 0 and dt.second == 0): 
		os.makedirs('Bing', exist_ok=True)
		url = "http://bingwallpaper.com/"
		sc = requests.get(url)
		soup = BeautifulSoup(sc.text, 'lxml') #check lxml?
		print (sc.text)
		image = soup.select('.cursor_zoom img')
		image_url = image[0].get('src')
		response = requests.get(image_url)

		with open(os.path.join('Bing', cd+'.jpg'), 'wb') as file:
			file.write(response.content)

		#change desktop background
		#os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/radioactive/Bing/'+cd+'.jpg')
		file_path = '/Users/asmita.mitra/PythonScripts/crawlers/Bing/' + cd+'.jpg'
		subprocess.Popen(SCRIPT%file_path, shell=True)
		print('Wallpaper set to ' + file_path)
		break

sys.exit()