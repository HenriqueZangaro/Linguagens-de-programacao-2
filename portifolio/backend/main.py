from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/perfil")
def get_perfil():
    return {
        "nome": "Henrique Zangaro",
        "idade": 20,
        "email": "henrique.eng.prog@gmail.com",
        "celular": "4002-8922",
        "formacao": [
            "Engenharia Elétrica (2023 - 2025)",
            "Engenharia da Computação (2025 - )"
        ],
        "habilidades": [
            {"nome": "Python", "nivel": 70},
            {"nome": "C/C++", "nivel": 50}
        ],
        "experiencias": [
            {
                "titulo": "Estágio em Automação Industrial",
                "empresa": "Empresa XYZ",
                "periodo": "2023 - 2024",
                "descricao": "Desenvolvimento de painéis elétricos e programação de CLPs."
            },
            {
                "titulo": "Monitor de Circuitos Elétricos",
                "empresa": "Universidade",
                "periodo": "2024",
                "descricao": "Auxílio a alunos em atividades práticas de laboratório."
            },
            {
                "titulo": "Freelancer em Desenvolvimento Web",
                "empresa": "Autônomo",
                "periodo": "2024 - ",
                "descricao": "Criação de sites e landing pages para pequenos negócios."
            },
            {
                "titulo": "Iniciação Científica",
                "empresa": "Universidade",
                "periodo": "2025 - ",
                "descricao": "Pesquisa em sistemas embarcados e IoT aplicados à eficiência energética."
            }
        ],
        "projetos": [
            {
                "titulo": "Site de Portfólio",
                "descricao": "Portfólio pessoal com HTML e CSS puro."
            },
            {
                "titulo": "Sistema de Automação Residencial",
                "descricao": "Projeto com Arduino e sensores para controle de iluminação."
            },
            {
                "titulo": "Monitoramento de Energia com IoT",
                "descricao": "Coleta de dados de consumo elétrico via ESP32 e dashboard em Python."
            },
            {
                "titulo": "Braço Robótico com Arduino",
                "descricao": "Controle de servomotores via interface serial."
            }
        ]
    }