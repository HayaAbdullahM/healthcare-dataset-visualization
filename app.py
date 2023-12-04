from flask import Flask, render_template, json
from utils import genders, medical_condition, insurance_provider, blood_types, blood_medical

app = Flask(__name__)


@app.route('/')
def index():

    data = {
        'genders': genders(),
        'medical_conditions': medical_condition(),
        'insurance_providers': insurance_provider(),
        'blood_types': blood_types(),
        'blood_medical': blood_medical().to_dict(),
    }

    return render_template('index.html', data=json.dumps(data))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/students')
def students():
    return render_template('students.html')


if __name__ == '__main__':
    app.run()
