from flask import Flask, request
import logging
from werkzeug.routing import Rule

# don't want requests logged
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask('kaikki')

# accept all methods
def accept_everything(rule, **kwargs):
    kwargs['methods'] = None
    return Rule(rule, **kwargs)
app.url_rule_class = accept_everything

@app.route('/', defaults={'url': ''}, methods=[])
@app.route('/<path:url>')
def serve(url):
    print("Method: " + request.method)
    print("Path: " + request.path)
    query = request.query_string.decode('utf-8')
    if query:
        print("Query: " + query)
    print("\nHeaders\n----------")
    print(request.headers)
    print()
    print(request.data)
    print()
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
