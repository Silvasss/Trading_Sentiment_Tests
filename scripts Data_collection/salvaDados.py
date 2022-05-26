import json
import pandas as pd
import os.path


def converterArrayExtracao(array):
    # Convertendo para json e depois para dicionário
    dados = json.loads(json.dumps(array))

    if not os.path.exists("list.csv"):
        df = pd.DataFrame(dados, columns=["longShortRatio", "timestamp", "symbol", ])

        df.to_csv('list.csv', mode= "a", index=False)
    else:
        df = pd.DataFrame(dados, columns=["longShortRatio", "timestamp", "symbol", ])

        df.to_csv('list.csv', mode="a", index=False, header=False)

    pass
