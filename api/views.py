from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from blockfrost import BlockFrostApi, ApiError, ApiUrls

# Create your views here.

def index(request):
    api = BlockFrostApi(
        project_id='mainnetD7HZO64X2Jd4gbQGFfvEr4C5ysOe8xc4'
    )

    try:
        health = api.health(return_type='json')
    except ApiError as e:
        health = { 'error' : e }

    print(health)
    return JsonResponse(health)
