from flask import Flask, jsonify, request
from flask_cors import CORS
from joblib import load

presence_classifier = load('presence_classifier.joblib')
presence_vect = load('presence_vectorizer.joblib')
category_classifier = load('category_classifier.joblib')
category_vect = load('category_vectorizer.joblib')

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        output = []
        data = request.get_json().get('tokens')

        for token in data:
            result = presence_classifier.predict(presence_vect.transform([token]))
            if result[0] == 'Dark':
                cat = category_classifier.predict(category_vect.transform([token]))
                # Converte explicitamente de numpy.str_ para string nativa do Python
                output.append(str(cat[0])) 
            else:
                output.append(str(result[0]))

        # Filtra os dark patterns apenas para o log/print no console do backend
        dark = [data[i] for i in range(len(output)) if output[i] != 'Not Dark']
        for d in dark:
            print(d)
        print(f"\nTotal Dark Patterns: {len(dark)}")

        # Cria um dicionário nativo e usa o jsonify corretamente
        response_dict = {'result': output}
        print(response_dict)

        return jsonify(response_dict)

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
