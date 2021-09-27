# topTrendsApp: Consumindo a API do Twitter
# Desenvolvido por Ícaro Cazé Nunes

# 1. Importando os arquivos e bibliotecas:

# 1.1. Arquivos:

from src.services import getTrendsFromMongo, saveTrends, toCSV # topViews, getTweets, createDataFrame, preProcDF
from src.responses import TrendItem

# 1.2. Bibliotecas:

from typing import List
import uvicorn
from fastapi import FastAPI

# 2. Construindo a API:

app = FastAPI()

@app.get('/trends', response_model = List[TrendItem])

def getTrendsRoute():

    return getTrendsFromMongo()

if __name__ == '__main__':
    
    trends = getTrendsFromMongo()

    if not trends:

        saveTrends()

    uvicorn.run(app, host= '0.0.0.0', port = 8000)

# 3. Criando um arquivo (.csv) com os tweets das #topTrends:

exportCSV = toCSV()







