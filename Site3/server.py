from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['POST', 'GET'])
def hello():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    word = first_name + last_name
    with open("test.txt", "w") as datafile:
        datafile.write(word)
    complete = word * 3
    return render_template('calc2.html', data = complete)




if __name__ == "__main__":
    app.run(debug=True)