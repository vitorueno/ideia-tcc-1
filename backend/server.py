from config import *
from contador import Contador
import sys


@app.route('/contador', methods=['post'])
def criar_contador():
    resposta = jsonify({'resultado': 'ok', 'detalhes': 'ok'})
    dados = request.get_json()

    try:
        nova = Contador(**dados)
        db.session.add(nova)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({'resultado': 'erro', 'detalhes': str(e)})

    resposta.headers.add('Access-Control-Allow-Origin', '*')
    return resposta


@app.route('/contador', methods=['get'])
def listar_contadores():
    contadores = db.session.query(Contador).all()
    contadores_em_json = [x.json() for x in contadores]
    return jsonify(contadores_em_json)


@app.route('/contador/<int:contador_id>', methods=['get'])
def listar_contador(contador_id):
    resposta = ''

    try:
        contador = Contador.query.get(contador_id)
        contador_em_json = contador.json()
        resposta = jsonify(contador_em_json)
    except Exception as e:
        resposta = jsonify({'resultado': 'erro', 'detalhes': str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route('/contador/<int:contador_id>', methods=['delete'])
def deletar_contador(contador_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Contador.query.filter(Contador.id == contador_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route('/contador/<int:contador_id>', methods=['put'])
def atualizar_contador(contador_id):
    resposta = jsonify({'resultado': 'ok', 'detalhes': 'ok'})
    dados = request.get_json()

    try:
        contador = Contador.query.get(contador_id)
        contador.contador = dados['contador']
        db.session.commit()

    except Exception as e:
        resposta = jsonify({'resultado': 'erro', 'detalhes': str(e)})

    resposta.headers.add('Access-Control-Allow-Origin', '*')
    return resposta


@app.route('/contador/<int:contador_id>/inc', methods=['get'])
def inc_contador(contador_id):
    resposta = ''

    try:
        cont = Contador.query.get(contador_id)
        cont.contador += 1
        db.session.commit()
        resposta = jsonify({'resultado': 'ok', 'detalhes': 'ok'})

    except Exception as e:
        resposta = jsonify({'resultado': 'erro', 'detalhes': str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route('/contador/<int:contador_id>/dec', methods=['get'])
def dec_contador(contador_id):
    resposta = ''

    try:
        cont = Contador.query.get(contador_id)
        cont.contador -= 1
        db.session.commit()
        resposta = jsonify({'resultado': 'ok', 'detalhes': 'ok'})

    except Exception as e:
        resposta = jsonify({'resultado': 'erro', 'detalhes': str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


if __name__ == '__main__':
    port = 5000
    if (len(sys.argv) > 1):
        port = sys.argv[1]

    app.run(debug=True, port=port)
