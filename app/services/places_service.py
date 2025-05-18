import requests
from collections import defaultdict

class PlacesService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_places(self, lat: float, lng: float, radius: int, place_type: str, normalizer) -> dict:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            "location": f"{lat},{lng}",
            "radius": radius,
            "type": place_type,
            "key": self.api_key
        }
        r = requests.get(url, params=params)
        results = r.json().get("results", [])
        grouped = defaultdict(list)
        for place in results:
            types = place.get("types", [])
            matched = False
            for tag in types:
                category = normalizer(tag)
                if category:
                    grouped[category].append(place)
                    matched = True
                    break
            if not matched:
                grouped["other"].append(place)
        return grouped

    def normalize_cuisine(self, tag):
        return {
            "indian_restaurant": "indian",
            "mexican_restaurant": "mexican",
            "chinese_restaurant": "chinese",
            "italian_restaurant": "italian",
            "japanese_restaurant": "japanese",
            "thai_restaurant": "thai",
            "pizza_place": "pizza",
            "korean_restaurant": "korean",
        }.get(tag)

    def normalize_vacation(self, tag):
        return {
            "park": "parks",
            "museum": "museums",
            "tourist_attraction": "landmarks",
            "zoo": "zoos",
            "art_gallery": "galleries",
        }.get(tag)
