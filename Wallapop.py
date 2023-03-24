from models.data_model import Product
import requests

def get_itemsWallapop(keyword):
    products = []

    #formated_keyword = keyword.replace(' ', '+')

    request = requests.get(f"https://api.wallapop.com/api/v3/general/search?keywords={keyword}")
    json_data = request.json()['search_objects']

    for i in json_data:
        # Conseguir array de todas las imagenes originales
        images = []
        all_images = i['images']
        for image in all_images:
            images.append(image['original'])

        # Crear objetos Product y añadir al array de productos
        product = Product(id=i['id'],
                          title=i['title'],
                          description=i['description'],
                          images=images,
                          price=i['price'],
                          url=i['web_slug'],
                          vendor='Wallapop')
        products.append(product)

    return products

