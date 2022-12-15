import webbrowser
import os

filename = ''

for file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    if file.endswith(".html"):
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)

webbrowser.open('file://' + filename, new=2)
