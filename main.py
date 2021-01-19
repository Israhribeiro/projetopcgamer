from selenium import webdriver as wb
import time


def adiciona(lista, produtos):
    lista.append(produtos)


def pegaPreco():
    try:
        wbD.find_element_by_css_selector(
            "#maincontent > div.columns > div > div.product-info-main > div.product-info-price > div.product-info-stock-sku > div.stock.available")
        precoProd = wbD.find_elements_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div[2]/div[2]/span[2]/span')[
            0].text

        preco = ""
        for i in precoProd:
            if i.isdigit():
                preco += i
            if i == ",":
                preco += "."

    except:
        preco = "Indisponível"
    return preco


def pegaProduto(selector):
    produtos = wbD.find_element_by_css_selector(selector).get_attribute('href')
    return produtos


def novoLink(link):
    wbD.get(link)
    time.sleep(3)


wbD = wb.Chrome('chromedriver.exe')
wbD.get('https://www.pichau.com.br/hardware/placa-de-video')
listaDeFiltro = []
listaDeLinks = []
preco = []
listaPichau = [5,11,12,13,14,41,45,51,53]
time.sleep(3)
produtoInfoLista = wbD.find_elements_by_xpath('//div[@class="product details product-item-details"]')[0]
wbD.find_elements_by_xpath('//div/select[@id="sorter"]/option')[2].click()
time.sleep(5)

for i in (listaPichau):
    adiciona(listaDeFiltro, pegaProduto(f'#narrow-by-list > dd:nth-child(2) > form > ol > li:nth-child({i}) > a'))

for i in (listaDeFiltro):
    novoLink(i)
    adiciona(listaDeLinks, pegaProduto(
        '#amasty-shopby-product-list > div.products.wrapper.grid.products-grid > ol > li:nth-child(1) > div > div > strong > a'))

for i in listaDeLinks:
    novoLink(i)
    adiciona(preco, pegaPreco())

print(listaDeLinks, '\n preço', preco, '\n filtros', listaDeFiltro)
