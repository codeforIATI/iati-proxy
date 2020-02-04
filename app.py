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
    r = requests.get(url, headers={'user-agent': USER_AGENT})
    resp = Response(r.content, headers={
        'access-control-allow-origin': '*'})
    return resp