# downloadXkcd.py - Downloads every single XKCD comic.

"""
Steps:

[ ] 1: Download pages with request module
[ ] 2: Find URL of comic image using Beautiful Soup
[ ] 3: Download & save comic image to hard drive with requests.iter_content()
[ ] 4: Find the URL of Previous Comic link, and repeat

"""

import requests, os, bs4

url = 'http://xkcd.com'				# starting url
os.makedirs('xkcd', exist_ok=True)	# store comics in ./xkcd
while not url.endswith('#'):
	# TODO: Download page
	print("Downloading page %s..." % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, features='lxml')

	# TODO: Find URL of comic image
	comicElem = soup.select("#comic img")
	if (comicElem == []):
		print("Could not fine comic image.")
	else:
		try:
			comic_URL = "http:" + comicElem[0].get('src')

			# TODO: Download image
			print("Downloading image %s..." % (comic_URL))
			res = requests.get(comic_URL)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			# skip this comic
			prevLink = soup.select("a[rel='prev']")[0]
			url = 'http://xkcd.com' + prevLink.get("href")
			continue

		# TODO: Save image to ./ directory
		image_file = open(os.path.join('xkcd', os.path.basename(comic_URL)), 'wb')
		for chunk in res.iter_content(100000):
			image_file.write(chunk)

		image_file.close()

		# TODO: Get previous button's url and repeat
		prevLink = soup.select("a[rel='prev']")[0]
		url = 'http://xkcd.com' + prevLink.get("href")


print("Images successfully downloaded.")



