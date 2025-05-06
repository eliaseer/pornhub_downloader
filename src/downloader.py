import youtube_dl
import json
from concurrent.futures import ThreadPoolExecutor

def download(link):
    options = {
        'noplaylist': True,
        'format': 'best[ext=mp4]/best',
        'ignoreerrors': True
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([link])

def get_links():
    with open('./data/data.json', 'r') as file:
        links = json.load(file)['downloaded_links']
    return links

def start_download(links):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download, links)

if __name__ == "__main__":
    links = get_links(   "https://www.pornhub.com/view_video.php?viewkey=ph5f9f33677b74d")
    start_download(links)
