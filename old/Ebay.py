from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

# API key is set in .env file - create and save in same directory

API_KEY = 'PabloUga-apiThrif-PRD-008db439e-4ad5fd66'


class Ebay_Thrift3r(object):
    def __init__(self, API_KEY, st):
        self.api_key = API_KEY
        self.st = st

    def fetch(self):
        try:
            api = Connection(appid=self.api_key, config_file=None, siteid="EBAY-ES")
            response = api.execute('findItemsAdvanced', {'keywords': self.st})

            # The total number of items found that match the search criteria in your request
            print(f"Total items {response.reply.paginationOutput.totalEntries}\n")

            for item in response.reply.searchResult.item:
                print(f"Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}")
                print(f"Buy it now available : {item.listingInfo.buyItNowAvailable}")
                print(f"Country : {item.country}")
                print(f"End time :{item.listingInfo.endTime}")
                print(f"URL : {item.viewItemURL}")
                try:
                    print(f"Watchers : {item.listingInfo.watchCount}\n")
                except:
                    pass

        except ConnectionError as e:
            print(e)
            print(e.response.dict())

    def parse(self):
        pass
