from flask import Flask, request, Response
import requests


app = Flask(__name__)


USER_AGENT = 'Mozilla/5.0 (compatible; iati-proxy.herokuapp.com)'


@app.route('/raw')
def proxy():
    dataset = request.args.get('dataset')
    if not dataset:
        return '', 404
    j = requests.get(f'https://iatiregistry.org/api/3/action/' +
                     f'package_show?id={dataset}',
                     headers={'user-agent': USER_AGENT}).json()
    url = j.get('result', {}).get('resources', [{}])[0].get('url')
    if not url:
        return '', 404
    with requests.get(url,
                      headers={'user-agent': USER_AGENT},
                      stream=True) as r:
        resp = Response(r.content, headers={
            'content-type': r.headers.get('Content-Type', 'text/xml'),
            'access-control-allow-origin': '*'})
        return resp
