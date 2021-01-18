from selenium import webdriver as wb
import time


def adiciona(lista, produtos):
    lista.append(produtos)


def pegaPreco():
    precoProd = wbD.find_elements_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div[2]/div[2]/span[2]/span')[
        0].text
    return precoProd


def pegaProduto(selector):
    produtos = wbD.find_element_by_css_selector(selector).get_attribute('href')
    return produtos


def novoLink(link):
    wbD.get(link)
    time.sleep(3)

link = "https://www.pichau.com.br/hardware/placa-de-video"

wbD = wb.Chrome('chromedriver.exe')
wbD.get(link)
listaDeFiltro = []
listaDeLinks = []
preco = []
listaPichau = ['#narrow-by-list > dd:nth-child(2) > form > ol > li:nth-child(5) > a',
               '#narrow-by-list > dd:nth-child(2) > form > ol > li:nth-child(11) > a',
               '#narrow-by-list > dd:nth-child(2) > form > ol > li:nth-child(12) > a',
               '#narrow-by-list > dd:nth-child(2) > form > ol > li:nth-child(13) > a',
               '#narrow-by-list > dd:nth-child(2) > form > ol > li:nth-child(14) > a',
               '#narrow-by-list > dd:nth-child(2) > form > ol > li:nth-child(41) > a',
               '#narrow-by-list > dd:nth-child(2) > form > ol > li:nth-child(45) > a',
               '#narrow-by-list > dd:nth-child(2) > form > ol > li:nth-child(51) > a',
               '#narrow-by-list > dd:nth-child(2) > form > ol > li:nth-child(53) > a']
time.sleep(3)

produtoInfoLista = wbD.find_elements_by_xpath('//div[@class="product details product-item-details"]')[0]
wbD.find_elements_by_xpath('//div/select[@id="sorter"]/option')[2].click()
teste = wbD.find_element_by_css_selector(
    '#narrow-by-list > dd:nth-child(2) > form > ol > li:nth-child(8) > a').get_attribute('href')
print(teste)
time.sleep(5)

for i in (listaPichau):
    adiciona(listaDeFiltro, pegaProduto(i))

for i in (listaDeFiltro):
    novoLink(i)
    adiciona(listaDeLinks, pegaProduto(
        '#amasty-shopby-product-list > div.products.wrapper.grid.products-grid > ol > li:nth-child(1) > div > div > strong > a'))

for i in listaDeLinks:
    novoLink(i)
    adiciona(preco, pegaPreco())

print(listaDeLinks, '\n preço', preco, '\n filtros', listaDeFiltro)