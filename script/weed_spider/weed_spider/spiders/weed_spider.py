#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
import re
import os
from tqdm import tqdm
from weed_spider.items import Post

class WeedSpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["www.ikimono-tachi.jp"]
    start_urls = ["https://www.ikimono-tachi.jp/plndblist.php?tx=ALL"]


    
    def parse(self, response):
        names_list = response.css('.modal-title').getall()
        img_srcs_list = response.css(".modal-body>img.img-responsive::attr(src)").getall()
        print(response.css(".modal-body>img.img-responsive::attr(src)").getall())
        
        for names, img_src in tqdm(zip(names_list, img_srcs_list)):
            name = re.search(r'<h4 class="modal-title">(.*?)<small>', names).group(1)
            family = re.search(r'<small>（(.*?)）</small>', names).group((1))
            # items に定義した Post のオブジェクトを生成して次の処理へ渡す
            image_url = os.path.join('https://www.ikimono-tachi.jp/', img_src[2:])
            
            yield Post(
                name = name,
                family = family,
                image_url = image_url,
                # location = location,
            )
            # import ipdb;ipdb.set_trace(())

        data = response.css('a[title="次50件"]::attr(href)').getall()
        if len(data)<1:
            return
        next_link = os.path.join("https://www.ikimono-tachi.jp/", data[0][2:])
        
        yield response.follow(next_link, self.parse)