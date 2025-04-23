import requests

class TFLApiWrapper:
    def __init__(self,api='https://api.tfl.gov.uk'):
        self.list_of_modes = '/Line/Meta/Modes'
        self.list_of_lines = '/Line/Mode/{mode}'
        self.list_of_stations = '/Line/{line}/StopPoints'
    def get_modes(self):
        return requests.get(self.list_of_modes)