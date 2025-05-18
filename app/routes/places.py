from fastapi import APIRouter
from services.secret_service import SecretService
from services.places_service import PlacesService

router = APIRouter()

secret_service = SecretService()
api_key = secret_service.get("GOOGLE_PLACES_API_KEY")
places_service = PlacesService(api_key)

@router.get("/restaurants")
def get_restaurants(lat: float, lng: float, radius: int = 16000):
    return places_service.get_places(lat, lng, radius, "restaurant", places_service.normalize_cuisine)

@router.get("/vacation_spots")
def get_vacation_spots(lat: float, lng: float, radius: int = 16000):
    return places_service.get_places(lat, lng, radius, "tourist_attraction", places_service.normalize_vacation)

