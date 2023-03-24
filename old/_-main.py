import webReactiveScraping
import Wallapop
import Ebay


def getUrl(keyword):
    url_wallapop = f"https://api.wallapop.com/api/v3/general/search?keywords=%s&filters_source=search_box&longitude" \
                   f"=-3.69196&latitude=40.41956", keyword
    url_milanuncios = f"https://www.milanuncios.com/anuncios/?s=%s&orden=relevance&fromSearch=1&fromSuggester=1" \
                      f"&suggestionUsed=0&hitOrigin=home_search ", keyword
    url_vinted = f"https://www.vinted.es/catalog?search_text=%s"


if __name__ == '__main__':
    API_KEY = 'PabloUga-apiThrif-PRD-008db439e-4ad5fd66'
    webReactiveScraping.selenium("https://www.vinted.es/catalog?search_text=air+force+1")
    ebay = Ebay.Ebay_Thrift3r(API_KEY, "raton logitech")
    ebay.fetch()
    ebay.parse()
    Wallapop.get_itemsWallapop("https://api.wallapop.com/api/v3/general/search?keywords=raton+logitech+mx+master")
    # La API de Amazon todavia no es funcional porque amazon nos tiene que aceptar la solicitud de desarollador
    # El Web Scraping en milanuncios hay que acabarlo de pulir
    # webReactiveScraping.selenium("https://www.milanuncios.com/anuncios/?s=libro&orden=relevance&fromSearch=1"
    # "&fromSuggester=1&suggestionUsed=0&hitOrigin=home_search")
