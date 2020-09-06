import scrapy 
class BrickSetSpider(scrapy.Spider):
    name ="bickset_spider"
    start_urls=['http://brickset.com/sets/year-2016']

    def parse(self, response):
        SET_SELECTOR ='.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1::text'
            PIECES_SELECOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }