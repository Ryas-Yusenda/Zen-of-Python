from bs4 import BeautifulSoup
from requests import get

base_url = 'https://www.antaranews.com'

class Script:

    def query(self, url):
        print(url)
        datas = get(url)
        soup = BeautifulSoup(datas.text, 'html.parser')
        tag = soup.find_all(
            'article', attrs={'class': 'simple-post simple-big clearfix'})
        print(len(tag))
      #   print((tag))
        data = []

        for i in tag[0:29]:
            try:
                title = i.find('a')['title'].strip()
                link = i.find('a')['href'].strip()
                gambar = i.find('source')['data-srcset'].strip()
                tipe = i.find('p', attrs={'class': 'simple-share'})
                tipe = tipe.find('a')['title'].strip()
                data.append({
                    "judul": title,
                    "link": link,
                    "poster": gambar,
                    "tipe": tipe,
                })
            except:
                pass

        return data

    def index(self):
        return self.query('{}/'.format(base_url))

    def search(self, q):
        return self.query('{}/search?q={}'.format(base_url, q))


if __name__ != '__main__':
    Code = Script()
