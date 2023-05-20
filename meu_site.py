from flask import Flask, render_template

app = Flask(__name__)

#Criar a primeira página do site
#Route -> Qual link vai ficar a página
#Função -> O que você quer exibir, naquela página
#Template
#Decorator (Linha de código tem o objetivo de atribuir uma nova funcionalidade)
@app.route("/") #Decorator atribui uma nova funcionalidade para a função na sequência
def homepage():
    return render_template("homepage.html")

@app.route("/escola")
def escola():
    return render_template("escola.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)
@app.route('/professor')
def professor():
    return render_template('professor.html')

@app.route('/disciplina')
def disciplina():
    return render_template('disciplina.html')

@app.route('/turma')
def turma():
    return render_template('turma.html')

@app.route('/grade')
def grade():
    return render_template('grade.html')

@app.route('/visualizador')
def visualizador():
    return render_template('visualizador.html')

#Colocar o site no ar
if __name__=="__main__":
    app.run(debug=True)

# servidor do heroku
# Criar um arquivo em txt para incluir a documentação / Procfile

# Criar o file Procfile
# Para criar a documentação pip install requirements.txt
# heroku login
# git init
#git config --global user.email "brunalopescorreia@gmail.com"
#git config --global user.name "Brumcr"
#git init
#heroku git:remote -a siteestudantesunivesp
#================================ PARA ATUALIZAR PRECISA
#$ heroku login
#$ git add .
#$ git commit -am "maio 3"
#$ git push heroku master



