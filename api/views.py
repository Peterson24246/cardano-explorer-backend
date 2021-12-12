from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from blockfrost import BlockFrostApi, ApiError

# Load api key from .env file
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
api_key = os.environ.get('API_KEY')
api = BlockFrostApi(
        project_id=api_key
)
# Create your views here.

# View returning json of network status
def index(request):
    try:
        health = api.health(return_type='json')
    except ApiError as e:
        health = { 'error' : e }

    return JsonResponse(health)

def block_latest(request):
    try:
        latest_block = api.block_latest(return_type="json")
    except ApiError as e:
        latest_block = {'error' : e }
    
    return JsonResponse(latest_block)
