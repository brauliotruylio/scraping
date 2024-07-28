import scrapy


class MercadolivretenisSpider(scrapy.Spider):
    name = "mercadolivretenis"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/calcados-roupas-bolsas/calcados/tenis/tenis-corrida-masculino_NoIndex_True#D[A:tenis%20corrida%20masculino,on]"]

    def parse(self, response):
        pass
