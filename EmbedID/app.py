from flask import Flask, render_template, request
from ciphers_manager import embed, verify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/embed', methods=['POST'])
def embed_signature():
    file = request.files['file']
    method = request.form['method']
    signature = request.form['signature']
    content = file.read().decode('utf-8')
    embedded = embed(method, signature, content)
    return render_template('result.html', result=embedded)

@app.route('/verify', methods=['POST'])
def verify_signature():
    file = request.files['file']
    method = request.form['method']
    signature = request.form['signature']
    content = file.read().decode('utf-8')
    is_valid = verify(method, signature, content)
    return render_template('result.html', result=f"Signature valid: {is_valid}")

if __name__ == '__main__':
    app.run(debug=True)
