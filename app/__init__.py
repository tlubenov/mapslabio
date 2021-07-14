from flask import Flask

app = Flask(__name__)


@app.route('/')
def mapslabio_service():
    return {
        'service': 'mapslab.io',
        'version': 'v1',
        'last_update_date': '20210714'
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0')
