import requests
import datas
import salvaDados


def requestApi():
    # Lista com as datas passadas
    arrayDatas = datas.listaDatas()

    for i in range(len(arrayDatas)):
        if i + 1 < 30:
            salvaDados.converterArrayExtracao(baseURL(datas.dateToUnixTimestamp(arrayDatas[i]),
                                                      datas.dateToUnixTimestamp(arrayDatas[i + 1])))
        else:
            salvaDados.converterArrayExtracao(baseUrlNow())


def baseURL(data, data2):
    baseApi = f"https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=5m&startTime={data}&endTime={data2}&limit=288"

    resposta = requests.get(baseApi)

    return resposta.json()


def baseUrlNow():
    # Dados do dia atual
    baseApi = "https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=5m&limit=288"

    resposta = requests.get(baseApi)

    return resposta.json()
