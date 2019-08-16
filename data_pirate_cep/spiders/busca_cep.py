# -*- coding: utf-8 -*-
# External imoprts
from lxml import html
import scrapy

# Personal imports
from data_pirate_cep.items import DataPirateCepItem

# Built-in imports

QTD_ROWS = '50'
class BuscaCepSpider(scrapy.Spider):
    name = 'busca_cep'
    allowed_domains = ['buscacep.correios.com.br']
    url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
    addresses = {}

    def start_requests(self):
        for uf in self.addresses.keys():
            form_data = {'UF': uf, 'Localidade': ''}
            yield scrapy.http.FormRequest(url=self.url, callback=self.parse_page, formdata=form_data, meta={'current_page': 1, 'UF': uf})

    def parse_page(self, response):
        current_page, uf = response.meta['current_page'], response.meta['UF']
        cep_rows = response.xpath("//table[not(contains(@style, 'width'))]/tr/td/parent::tr").extract()
        for cep_row in cep_rows:
            yield self.parse_cep(cep_row, uf)

        next_page_link = response.xpath("//div[@style]/a[contains(text(), 'Próxima')]").extract_first()
        if next_page_link:
            pag_ini = str(current_page*int(QTD_ROWS)+1)
            pag_fim = str(int(pag_ini) + int(QTD_ROWS) - 1)
            form_data = {'UF': uf, 'Localidade': '**', 'Bairro': '', 'qtdrow': QTD_ROWS, 'pagini': pag_ini, 'pagfim': pag_fim}
            yield scrapy.FormRequest(url=self.url, callback=self.parse_page, formdata=form_data, meta={'current_page': current_page+1, 'UF': uf})

    def parse_cep(self, cep_row, uf):
        item = DataPirateCepItem()
        cep_html = html.fromstring(cep_row)
        item['uf'] = uf
        item['address'] = cep_html.xpath("//td/text()")[0]
        item['range_cep'] = cep_html.xpath("//td/text()")[1]
        return item