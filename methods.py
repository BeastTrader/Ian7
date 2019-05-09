from dateutil.relativedelta import relativedelta

def calculate_returns(stock):

    data = stock.historical_data
    data.sort_values(by='timestamp', inplace=True)
    start_price = data.iloc[0]['price']
    end_price = data.iloc[-1]['price']
    start_date = data.iloc[0]['timestamp']
    end_date = data.iloc[-1]['timestamp']
    n = relativedelta(end_date, start_date)
    n = n.years + n.months / 12 + n.days / 365
    perc_return = (end_price / start_price) ** (1 / n) - 1

    return perc_return