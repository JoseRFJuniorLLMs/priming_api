from fastapi import FastAPI

from crud import crud_router
from logger import config_log

# Configurando o log
config_log()

# Criando a instância do aplicativo FastAPI
app = FastAPI()

# Incluindo as rotas CRUD
app.include_router(crud_router)

# Esta é apenas uma demonstração de como você pode configurar o log antes de iniciar o servidor.
# Se você tem outras configurações a serem feitas, certifique-se de realizá-las antes de iniciar o servidor.

# Se houver outras configurações ou inicializações necessárias, elas devem ser feitas aqui antes de iniciar o servidor.
# ...

# Iniciando o servidor FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
