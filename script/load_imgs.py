import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import cv2
from tqdm import tqdm
import os
import pprint
import time
import urllib.error
import urllib.request
import time

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)



def load_and_save(root):
    save_dir = os.path.join(root, 'imgs')
    os.makedirs(save_dir, exist_ok=True)
    df = pd.read_csv(os.path.join(root, "data.csv"))
    for url in tqdm(df['image_url'].values):
        file = url.split("/")[-1]
        path = os.path.join(save_dir, file)
        download_file(url, path)
        time.sleep(0.1)

if __name__=='__main__':
    data_root = "/workdir/scrayping/script/weed_spider/data"
    load_and_save(data_root)