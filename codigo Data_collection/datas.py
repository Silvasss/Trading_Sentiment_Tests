import calendar
import datetime
import pandas as pd


def unixTimestampToDate(data):
    # Calculando o número de milissegundos para data
    # Entrada = 1653497700000 --- Saida = 2022-05-25 16:55:00
    return pd.to_datetime(data, unit= 'ms')


def dateToUnixTimestamp(data):
    # Datetime para Unix Timestamp
    return calendar.timegm(data.timetuple()) * 1000


def listaDatas():
    # Data de 30 dias atrás
    dataStart = datetime.datetime.now().date() - datetime.timedelta(days=29)

    return pd.date_range(dataStart, periods=30).to_list()
