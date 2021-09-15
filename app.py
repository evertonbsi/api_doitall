from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return '''<h1>Rotas:</h1> 
            <li><a href='/usuarios'>/usuarios</a></li>
            <li><a href='/feedbacks'>/feedbacks</a></li>
            <li><a href='/servicos'>/servicos</a></li>
            <li><a href='/status_servicos'>/status_servicos</a></li>
         '''

@app.route('/usuarios')
def usuarios():
  usuario = [{'id':1, 'nome':'Maria R.', 'tipo':'Cliente', 'cpf':'12345678900', 'telefone':'82912345678','endereco':'-1.5052,-35.7111'},
              {'id':2, 'nome':'Joaquina S.', 'tipo':'Profissional', 'cpf':'12345678901', 'telefone':'82912345679','endereco':'-2.5021,-35.7321'},
              {'id':3, 'nome':'Antonia M.', 'tipo':'Cliente', 'cpf':'12345678000', 'telefone':'82912345678','endereco':'-3.5012,-35.7123'}]
  return jsonify(results=usuario)

@app.route('/feedbacks')
def feedback():
  feedback = [{'Joaquina S.':
                [{'id':1,'id_usuario':3, 'cliente':'Antonia M.','Servico':[{'id_servico':1}], 'comentários':'Excelente profissional, recomendo.', 'estrelas':'5'},
                 {'id':2,'id_usuario':1, 'cliente':'Maria R.', 'Servico':[{'id_servico':1}], 'comentários':'Ok.', 'estrelas':'4'}]
  }]

  return jsonify(result=feedback)

@app.route('/servicos')
def servicos():
  servico = [{'id':1, 'id_usuario':2,'nome_servico':'Salão Domicílio', 'valor':'150.00', 'docs_receber_pagamento':[{'PIX':[{'chave':'87SD98SDGHH34IJIJDK'}],'bnk':[{'conta':'12345','agencia':'1010'}]}]}]

  return jsonify(result=servico)

@app.route('/status_servicos')
def status():
  status = [{'id_servico:':1, 'status':'Aguardando confirmação de pagamento.', 'id_usuario_profissional':2, 'id_usuario_cliente':1,'forma_pagamento':'PIX'},
            {'id_servico:':1, 'status':'Pagamento Concluído.', 'id_usuario_profissional':2, 'id_usuario_cliente':3,'forma_pagamento':'PIX'}]
  return jsonify(result=status)

if __name__=='__main__':
  app.run(host='0.0.0.0')