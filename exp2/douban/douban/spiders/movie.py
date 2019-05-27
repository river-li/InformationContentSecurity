# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath('//div[@class="item"]') 

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield scrapy.Request(next_url)

        for movie in movies:
            item["ranking"] = movie.xpath('.//em/text()').extract()[0]
            item["name"] = movie.xpath('.//span[@class="title"]/text()').extract()[0]
            item["score"] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item["description"] = movie.xpath('.//p[@class="quote"]/span[@class="inq"]/text()').extract()[0]
            item["score_num"] = movie.xpath('//div[@class="star"]//span/text()')[3].extract()[0]
            yield item


