from django.utils import timezone
import requests
from .models import Currency


def get_rates_cron_job(self, *args, **kwargs):
    self.stdout.write(self.style.SUCCESS(f'Started request'))
    """Gets the currency rate data and save it to DB"""
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    self.stdout.write(self.style.SUCCESS(f'Finished request {response.status_code}'))
    data = response.json()
    for currency_code, currency_data in data['Valute'].items():
        charcode = currency_data['CharCode']
        date = timezone.now().date()
        rate = currency_data['Value']

        currency_rate, created = Currency.objects.update_or_create(
            charcode=charcode,
            date=date,
            defaults={'rate': rate}
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Created new currency rate for {charcode} on {date}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Updated currency rate for {charcode} on {date}'))
