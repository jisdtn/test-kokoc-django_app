import logging

from django.utils import timezone
import requests
from .models import Currency

logger = logging.getLogger(__name__)

def get_rates_cron_job():
    """Gets the currency rate data and save it to DB"""
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    logging.debug('запрос ушел')
    data = response.json()
    logging.debug('данные получены')
    for currency_code, currency_data in data['Valute'].items():
        charcode = currency_data['CharCode']
        date = timezone.now().date()
        rate = currency_data['Value']
        logging.debug('данные преобразованы')

        currency_rate, created = Currency.objects.update_or_create(
            charcode=charcode,
            date=date,
            defaults={'rate': rate}
        )
        logging.debug('данные сохранены')

        if created:
            print(f'Created new currency rate for {charcode} on {date}')
        else:
            print(f'Updated currency rate for {charcode} on {date}')
