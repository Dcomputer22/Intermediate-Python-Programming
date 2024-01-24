#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_data_destination()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for data in sheet_data:
        data["iataCode"] = flight_search.get_destination_code(data["city"])
    print(f"sheet data:\n {sheet_data}")

    data_manager.data_destination = sheet_data
    data_manager.update_data()
