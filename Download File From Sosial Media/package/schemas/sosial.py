from ..schemas.download import MediaDownloader

def downloadEntity(url):
    data = MediaDownloader(url)
    json = data.json()
    
    return json
