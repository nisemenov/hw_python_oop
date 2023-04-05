# Money and Calories Calculator
### Task description
Create two calculators: for counting money and calories. You don't need to write the user interface, write only the logic - a separate class for each of the calculators.

#### Money calculator should be able to:

1. Save a new expense record using the `add_record()` method
2. Calculate how much money has been spent today using the `get_today_stats()` method
3. Determine how much money is left to spend today in rubles, dollars, or euros using the `get_today_cash_remained(currency)` method
4. Calculate how much money has been spent in the last 7 days using the `get_week_stats()` method

#### Calorie calculator should be able to:

1. Save a new food intake record using the `add_record()` method
2. Calculate how many calories have been consumed today using the `get_today_stats()` method
3. Determine how many more calories can/should be consumed today using the `get_calories_remained()` method
4. Calculate how many calories have been consumed in the last 7 days using the `get_week_stats()` method

There are many overlapping functions in the calculators: they must be able to store some records (about food or money, but essentially - all numbers and dates), know the daily limit (how much money or how many calories can be spent/received per day), and sum up the records for specific dates. Include all this common functionality in the parent class **Calculator**, and inherit the **CaloriesCalculator** and **CashCalculator** classes from it.

The **Calculator** class constructor should take one argument - the number `limit` (the user-specified daily spending/calorie limit). In the constructor, create an empty list that will later store the records (call it `records`).

To make it more convenient to create records, create a separate class for them, **Record**. In it, save:

- the number `amount` (the amount of money or the number of kilocalories),
- the date of creation of the record `date` (passed explicitly in the constructor or assigned a default value - the current date),
- a `comment` explaining where the money was spent or where the calories came from.

#### Examples of such records:

```python
# for CashCalculator  
r1 = Record(amount=145, comment="Unrestrained shopping", date="08.03.2019")  
r2 = Record(amount=1568, comment="Filling the consumer basket", date="09.03.2019") 
r3 = Record(amount=691, comment="Taxi ride", date="08.03.2019")  

# for CaloriesCalculator  
r4 = Record(amount=1186, comment="Piece of cake. And another one.", date="24.02.2019")  
r5 = Record(amount=84, comment="Yogurt.", date="23.02.2019")  
r6 = Record(amount=1140, comment="Can of chips.", date="24.02.2019")  
```

## About the output format

1. The `get_calories_remained()` method of the **calorie calculator** should return the following response:
   - "*You can eat something else today, but your total calorie intake should not exceed N kcal*", if the `limit` has not been reached.
   - "*Enough is enough!*" if the limit has been reached or exceeded.
2. The `get_today_cash_remained(currency)` method of the **money calculator** should accept the currency code as input, one of the strings `"rub"`, `"usd"`, or `"eur"`.
    
It returns a message about the daily balance in this currency, rounding the amount to two decimal places (to the hundredths):

   - "*You have N rub/USD/Euro left for today*" - in case the `limit` has not been reached,
   - or "*You are broke, hold on tight*" if the limit has been reached,
   - or "*You are broke, and your debt is N rub/USD/Euro*" if the limit has been exceeded.

Please specify the currency rates as constants **USD_RATE** and **EURO_RATE** directly in the **CashCalculator** class.


# Калькулятор денег и калорий
### Условие задачи
Создайте два калькулятора: для подсчёта денег и калорий. Пользовательскую часть калькуляторов, их «лицо», писать не нужно, напишите только логику — отдельный класс для каждого из калькуляторов.

#### Калькулятор денег должен уметь:

1. Сохранять новую запись о расходах методом `add_record()`
2. Считать, сколько денег потрачено сегодня методом `get_today_stats()`
3. Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод `get_today_cash_remained(currency)`
4. Считать, сколько денег потрачено за последние 7 дней — метод `get_week_stats()`

#### Калькулятор калорий должен уметь:

1. Сохранять новую запись о приёме пищи — метод `add_record()`
2. Считать, сколько калорий уже съедено сегодня — метод `get_today_stats()`
3. Определять, сколько ещё калорий можно/нужно получить сегодня — метод `get_calories_remained()`
4. Считать, сколько калорий получено за последние 7 дней — метод `get_week_stats()`

У калькуляторов много пересекающихся функций: они должны уметь хранить какие-то записи (о еде или деньгах, но по сути - всё числа и даты), знать дневной лимит (сколько в день можно истратить денег или сколько калорий можно получить) и суммировать записи за конкретные даты. Всю эту общую функциональность заложите в родительский класс **Calculator**, а от него унаследуйте классы **CaloriesCalculator** и **CashCalculator**.

Конструктор класса **Calculator** должен принимать один аргумент --- число `limit` (дневной лимит трат/калорий, который задал пользователь). В конструкторе создайте пустой список, в котором потом будут храниться записи (назовите его `records`).

Чтобы было удобнее создавать записи, создайте для них отдельный класс **Record**. В нём сохраните:

- число `amount` (денежная сумма или количество килокалорий),
- дату создания записи `date` (передаётся в явном виде в конструктор, либо присваивается значение по умолчанию — текущая дата),
- комментарий `comment`, поясняющий, на что потрачены деньги или откуда взялись калории.

#### Примеры таких записей:

```python
# для CashCalculator  
r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")  
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019") 
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")  

# для CaloriesCalculator  
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")  
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")  
r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")  
```

#### Подробнее о формате вывода

1. Метод `get_calories_remained()` **калькулятора калорий** должен возвращать ответ
    - *«Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более N кКал»*, если лимит `limit` не достигнут,
    - или *«Хватит есть!»*, если лимит достигнут или превышен.
2. Метод `get_today_cash_remained(currency)` **денежного калькулятора** должен принимать на вход код валюты: одну из строк `"rub"`, `"usd"` или `"eur"`.

Возвращает он сообщение о состоянии дневного баланса в этой валюте, округляя сумму до двух знаков после запятой (до сотых):

- *«На сегодня осталось N руб/USD/Euro»* — в случае, если лимит `limit` не достигнут,
- или *«Денег нет, держись»*, если лимит достигнут,
- или *«Денег нет, держись: твой долг - N руб/USD/Euro»*, если лимит превышен.

Курс валют укажите константами **USD_RATE** и **EURO_RATE**, прямо в теле класса **CashCalculator**.
