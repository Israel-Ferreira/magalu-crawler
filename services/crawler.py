from models import Product

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webelement import WebElement

from typing import List



def extract_id_from_url(product_url: str) -> str:
    product_id_substring = product_url.find("/p/") + 3
    product_id_endsubstr =  product_url.find("/te")

    return product_url[product_id_substring:product_id_endsubstr]




def extract_product_info(web_elem: WebElement) -> Product:
    product_link = web_elem.find_element(By.CSS_SELECTOR, 'a').get_attribute("href")
    product_name =  web_elem.find_element(By.CSS_SELECTOR,'div[data-testid~="product-card-content"]>h2').text

    product_price_str = web_elem.find_element(By.CSS_SELECTOR, 'p[data-testid~="price-value"]').text

    product_price =  float(product_price_str.split("R$ ")[1].replace(".", "").replace(",", "."))

    product_id = extract_id_from_url(product_link)


    return Product(product_id, product_name, product_link, product_price)


def get_products(url: str) -> List[Product]:
    """
    get_products retorna uma lista de produtos presentes no magazineluiza

    Attributes

    url: str

    """

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")

    with webdriver.Firefox(options=options) as driver:

        driver.get(url)
        driver.implicitly_wait(20.0)


        items =  driver.find_elements(By.CSS_SELECTOR, 'div[data-testid~="product-list"]>ul>li')

        products = [extract_product_info(item) for item in items]

        return products



    







    



        


    