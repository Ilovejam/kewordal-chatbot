from operator import index
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from micro_service_chatbot import MicroServiceChatbot

app = Flask(__name__)
api = Api(app)
api.add_resource(MicroServiceChatbot, '/')

if __name__ == '__main__':
    app.run(debug=True)