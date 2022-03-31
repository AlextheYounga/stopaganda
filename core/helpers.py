import os
from tabulate import tabulate
import zipfile
import re
import json
from os import path
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS


def read_json_file(path):
    txtfile = open(path, "r")
    return json.loads(txtfile.read())


def create_wordcloud(text, output):
    currdir = path.dirname(__file__)
    mask = np.array(Image.open(path.join(currdir, "cloud.png")))

    stopwords = set(STOPWORDS)

    # create wordcloud object
    wc = WordCloud(background_color="white",
                   color_func=lambda *args, 
                   **kwargs: "black",
                   mask=mask,
                   stopwords=stopwords)

    wc.generate(text)

    # save wordcloud
    wc.to_file(path.join(currdir + '/clouds/', output))


def print_tabs(data, headers=[], tablefmt='simple'):
    """ 
    Parameters
    ----------
    data     :  list of lists
                first list must be list headers
    tablefmt : string
                see https://pypi.org/project/tabulate/ for supported text formats
    """
    tabdata = []
    if (type(data) == dict):
        for h, v in data.items():
            tabrow = [h, v]
            tabdata.append(tabrow)
        print(tabulate(tabdata, headers, tablefmt))
    if (type(data) == list):
        tabdata = data
        print(tabulate(tabdata, headers, tablefmt))


def zipfolder(path, filename, move=''):
    def zipdir(path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))

    def delete_old_export_files(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                os.remove(path + file)

    zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    zipdir(path, zipf)
    zipf.close()
    delete_old_export_files(path)
    if (move):
        os.rename(filename, f"{move+filename}.zip")
        return
    os.rename(filename, f"{path+filename}.zip")


def unzip_folder(directory, filepath):
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(directory)

def strip_urls_from_text(text):
    return re.sub(r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?', '', text, flags=re.MULTILINE)