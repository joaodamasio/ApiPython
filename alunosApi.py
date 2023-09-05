from fastapi import FastAPI
from alunoBD import BancoAluno


app = FastAPI()
bancoDados = BancoAluno()

@app.get("/alunos")
def getAluno():
    return bancoDados.db.all()

@app.get("/procurarId")
def getByName(id):
    return bancoDados.db.search(bancoDados.query.id == id)

@app.post("/cadastroAlunos")
def postAluno(id, nome):
    return bancoDados.db.insert({"id": id, "nome": nome}) 

@app.delete("/deletarAluno")
def deleteAluno(id):
    return bancoDados.db.remove(bancoDados.query.id == id)