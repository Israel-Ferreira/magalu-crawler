from dotenv import load_dotenv

import os
import services

if __name__ == "__main__":
    load_dotenv()
    print("Rodando o Crawler")

    magalu_url = os.getenv("MAGALU_URL")

    products = services.get_products(magalu_url)

    for product in products:
        print(product)

