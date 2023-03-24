import Wallapop

def get_products(keywords):
    
    wallapop_search = Wallapop.get_itemsWallapop(keywords)

    return wallapop_search


