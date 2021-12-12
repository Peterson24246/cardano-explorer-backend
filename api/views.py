from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from blockfrost import BlockFrostApi, ApiError

# Load api key from .env file
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
api_key = os.environ.get('API_KEY')
# Create your views here.

def index(request):
    api = BlockFrostApi(
        project_id=api_key
    )

    try:
        health = api.health(return_type='json')
    except ApiError as e:
        health = { 'error' : e }

    return JsonResponse(health)
