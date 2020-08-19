from main.models import Review, Service

def add_models(request):
    review = Review()
    return {"Review":review.get_absolute_url()}