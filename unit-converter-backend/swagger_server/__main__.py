#!/usr/bin/env python3

import connexion
from flask import render_template

from swagger_server import encoder


def index():
    return render_template('index.html')


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Unit Converter'}, pythonic_params=True)
    app.add_url_rule('/', 'index', index)
    app.run(port=8080)


if __name__ == '__main__':
    main()
