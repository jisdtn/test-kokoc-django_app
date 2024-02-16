from django.http import JsonResponse
from .models import Currency

def get_rate(request):
    """Display the json response for rate parameters"""
    if request.method == 'GET':
        charcode = request.GET.get('charcode')
        date = request.GET.get('date')

        try:
            rate = Currency.objects.get(charcode=charcode, date=date)
            data = {
                'charcode': rate.charcode,
                'date': rate.date,
                'rate': rate.rate
            }
            return JsonResponse(data)
        except Currency.DoesNotExist:
            return JsonResponse({'error': 'Data not found'}, status=404)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
