from main.models import Review, Service

def add_service_record_urls(request):

    review = Review()
    service = Service()
    return {"Review":review.get_absolute_url(),"Service":service.get_absolute_url_landing()}