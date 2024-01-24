import requests
SHEETY_ENDPOINT = "https://api.sheety.co/1ed6c7c7fe694123f859f854d236c67d/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data_destination = {}

    def get_data_destination(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.data_destination = data['prices']
        return self.data_destination

    def update_data(self):
        for city in self.data_destination:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)
