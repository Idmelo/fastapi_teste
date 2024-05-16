from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)


"""
"Usuário cadastrado"
{
  "nome": "Idmelo",
  "sobrenome": "Ivanilson Melo",
  "email": "ivanilson.melo@megaspo.com.br",
  "eh_admin": true,
  "senha": "@dmk1211"
}

{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzE2NDE4ODI0LCJpYXQiOjE3MTU4MTQwMjQsInN1YiI6IjcifQ.FQERSbIYHQVp81BaO9bVpgixRXsfopacdllHv4UjyyM",
  "token_type": "bearer"
}

"""