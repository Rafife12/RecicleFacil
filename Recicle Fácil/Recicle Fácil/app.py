import numpy as np
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Modelo de Usuário
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    tipo_usuario = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "tipo_usuario": self.tipo_usuario,
        }

# Modelo de Resíduo
class Residuo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo_residuo = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(200))

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo_residuo": self.tipo_residuo,
            "quantidade": self.quantidade,
            "descricao": self.descricao,
        }

# Rota para carregar a página de login
@app.route('/')
def exibir_login():
    return render_template('login.html')

# Rota para processar o login
@app.route('/login', methods=['POST'])
def processar_login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    # Verifica se o usuário existe no banco de dados
    usuario = Usuario.query.filter_by(email=email).first()

    if usuario and usuario.senha == senha:  # Validação simples de senha
        session['user_id'] = usuario.id
        session['user_name'] = usuario.nome
        flash('Login realizado com sucesso!', 'success')
        return redirect(url_for('principal'))
    else:
        flash('E-mail ou senha inválidos.', 'danger')
        return redirect(url_for('exibir_login'))

# Rota para carregar a página de cadastro
@app.route('/cadastro', methods=['GET'])
def exibir_cadastro():
    return render_template('cadastro.html')

# Rota para processar o cadastro
@app.route('/cadastro', methods=['POST'])
def processar_cadastro():
    dados = request.form
    nome = dados.get('nome')
    email = dados.get('email')
    tipo_usuario = dados.get('tipo_usuario')
    senha = dados.get('senha')

    if Usuario.query.filter_by(email=email).first():
        flash("E-mail já cadastrado!", "danger")
        return redirect(url_for('exibir_cadastro'))

    novo_usuario = Usuario(nome=nome, email=email, tipo_usuario=tipo_usuario, senha=senha)
    db.session.add(novo_usuario)
    db.session.commit()

    flash("Usuário cadastrado com sucesso!", "success")
    return redirect(url_for('exibir_login'))

# Rota para a página principal
@app.route('/principal')
def principal():
    return render_template('tela_principal.html')

# Rota para a página de cadastro de resíduos
@app.route('/cadastrar_residuo', methods=['GET'])
def exibir_cadastrar_residuo():
    return render_template('cadastro_residuo.html')

# Rota para processar o cadastro de resíduos
@app.route('/cadastrar_residuo', methods=['POST'])
def processar_cadastrar_residuo():
    dados = request.form
    nome = dados.get('nome')
    tipo_residuo = dados.get('tipo_residuo')
    quantidade = int(dados.get('quantidade'))
    descricao = dados.get('descricao')

    novo_residuo = Residuo(nome=nome, tipo_residuo=tipo_residuo, quantidade=quantidade, descricao=descricao)
    db.session.add(novo_residuo)
    db.session.commit()

    flash("Resíduo cadastrado com sucesso!", "success")
    return redirect(url_for('principal'))

@app.route('/dashboards')
def dashboards():
    # Dados iniciais para o dashboard de pontos de coleta
    residuos = Residuo.query.all()
    dados_tabela = [
        {
            "Nome do Resíduo": residuo.nome,
            "Tipo de Resíduo": residuo.tipo_residuo,
            "Quantidade (kg)": residuo.quantidade,
            "Descrição": residuo.descricao or "Não especificada"
        }
        for residuo in residuos
    ]

    # Renderizar o template com os dados
    return render_template('dashboards.html', dados_tabela=dados_tabela)


# Rota para a página de dashboards
@app.route('/dashboards/pontos_coleta')
def dashboard_pontos_coleta():
    # Consultar os dados do banco de dados
    residuos = Residuo.query.all()

    # Preparar os dados em formato de lista de dicionários
    dados_tabela = [
        {
            "Nome do Resíduo": residuo.nome,
            "Tipo de Resíduo": residuo.tipo_residuo,
            "Quantidade (kg)": residuo.quantidade,
            "Descrição": residuo.descricao or "Não especificada"
        }
        for residuo in residuos
    ]

    # Renderizar o template passando os dados
    return render_template('dashboard_pontos_coleta.html', dados_tabela=dados_tabela)

@app.route('/dashboards/residuos_reciclados')
def dashboard_residuos_reciclados():
    # Simulação de dados para o dashboard
    bairros = ['Barra', 'Pituba', 'Ondina', 'Itapuã', 'Rio Vermelho', 'Brotas', 'Paralela', 'Iguatemi', 'Cajazeiras', 'Stella Maris']
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    # Simular resíduos reciclados em kg
    np.random.seed(42)  # Para consistência nos dados simulados
    dados = np.random.randint(500, 2000, size=(len(bairros), len(meses)))

    # Preparar os dados para exibição no template
    tabela = [
        {"Bairro": bairros[i], **{meses[j]: dados[i][j] for j in range(len(meses))}}
        for i in range(len(bairros))
    ]

    # Renderizar o template com os dados
    return render_template('dashboard_residuos_reciclados.html', tabela=tabela, meses=meses)

@app.route('/dashboards/reciclagem_anual')
def dashboard_reciclagem_anual():
    # Dados fictícios de resíduos reciclados em toneladas
    data = {
        "Tipo de Resíduo": ["Plástico", "Metal", "Vidro", "Papel/Papelão", "Orgânico"],
        "Janeiro": [12, 8, 6, 15, 3],
        "Fevereiro": [10, 7, 5, 13, 4],
        "Março": [14, 9, 7, 16, 5],
        "Abril": [13, 8, 6, 14, 4],
        "Maio": [15, 10, 8, 18, 6],
        "Junho": [16, 9, 7, 17, 5],
        "Julho": [18, 11, 9, 19, 6],
        "Agosto": [17, 10, 8, 18, 6],
        "Setembro": [19, 12, 10, 20, 7],
        "Outubro": [18, 11, 9, 19, 6],
        "Novembro": [20, 13, 11, 21, 7],
        "Dezembro": [21, 14, 12, 22, 8],
    }

    # Soma total por tipo de resíduo
    for tipo in data["Tipo de Resíduo"]:
        index = data["Tipo de Resíduo"].index(tipo)
        data["Total"] = [
            sum([data[mes][index] for mes in data if mes != "Tipo de Resíduo"])
            for index in range(len(data["Tipo de Resíduo"]))
        ]

    # Identificar o resíduo mais reciclado
    max_index = data["Total"].index(max(data["Total"]))
    residuo_mais_reciclado = data["Tipo de Resíduo"][max_index]

    # Preparar dados para exibição
    tabela = [
        {"Tipo de Resíduo": data["Tipo de Resíduo"][i], "Total": data["Total"][i]}
        for i in range(len(data["Tipo de Resíduo"]))
    ]

    # Renderizar o template
    return render_template(
        'dashboard_reciclagem_anual.html',
        tabela=tabela,
        residuo_mais_reciclado=residuo_mais_reciclado,
    )


# Configuração da chave secreta para sessões
app.secret_key = 'sua-chave-secreta'

# Inicialização do banco de dados
@app.before_request
def criar_banco():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
