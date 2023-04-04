import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = float(amount)
        self.date = dt.date.today()
        if date:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = int(limit)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        return sum(i.amount for i in self.records
                   if i.date == dt.date.today())

    def get_week_stats(self):
        week_ago = dt.date.today() - dt.timedelta(days=7)
        return sum(i.amount for i in self.records
                   if week_ago < i.date <= dt.date.today())


class CashCalculator(Calculator):
    USD_RATE = 77.24
    EURO_RATE = 82.53

    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            currency_rate = 1
            currency_name = 'руб'
        elif currency == 'usd':
            currency_rate = self.USD_RATE
            currency_name = 'USD'
        elif currency == 'eur':
            currency_rate = self.EURO_RATE
            currency_name = 'Euro'
        else:
            raise ValueError('Currency is not defined!')
        cash = (self.limit - self.get_today_stats()) / currency_rate
        if cash > 0:
            return f'На сегодня осталось {cash:.2f} {currency_name}'
        elif cash == 0:
            return f'Денег нет, держись'
        cash = abs(cash)
        return f'Денег нет, держись: твой долг - {cash:.2f} {currency_name}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.get_today_stats() < self.limit:
            n = int(self.limit - self.get_today_stats())
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {n} кКал')
        return f'Хватит есть!'
