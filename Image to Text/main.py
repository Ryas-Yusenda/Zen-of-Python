import easyocr
import regex as re

reader = easyocr.Reader(["en"])
result = reader.readtext("download.jpeg")

for detection in result:
    text = detection[1]
    # regex only get alphanumeric
    text = re.sub(r"[^a-zA-Z0-9]+", "", text)
    print(text)
