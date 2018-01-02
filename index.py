import re
import os
from pyquery import PyQuery


PRODUCT_PATTERN = r"\/([0-9]+)_" # /と_に挟まれている数値
PRICE_PATTERN = r"[0-9,]+"

URL = os.environ["TARGET_URL"]

def main():
    pq = PyQuery(URL)

    for product in pq.find('div.js_productBox'):
        price_tag = PyQuery(product).find('.productPrice')
        price_str = re.findall(PRICE_PATTERN, price_tag.text())[0]
        price = int(float(price_str.replace(',', '')))
        product_img = PyQuery(product).find('.pImg img')
        img_url = product_img.attr('src')
        product_id = re.findall(PRODUCT_PATTERN, img_url)[0]
        print('product_id:{0} price:{1}'.format(product_id, price))

if __name__ == '__main__':
    main()
