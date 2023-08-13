import os, requests
from dotenv import load_dotenv

load_dotenv()

class NasaAPI:
    def __init__(self):
        self.api_key = os.getenv("NASA_API_KEY")
        self.url =  "https://api.nasa.gov/planetary/apod"
        
    
    def get_image(self, birthday=''):
        final_url = f'{self.url}?api_key={self.api_key}&date={birthday}'
        response = requests.get(final_url)

        return response
        