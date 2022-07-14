from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource


class MicroServiceChatbot(Resource):
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjEiLCJuYmYiOjE2MzMwOTAyNjIsImV4cCI6MTY5NjE2MjI2MiwiaWF0IjoxNjMzMDkwMjYyfQ.VIuUiGRjO7VrUmImKeXG7dFBp8GMcQzUUE-Eo405YOM"

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('question', type=str, required=True, help='Question cannot be null')
        parser.add_argument('Authorization', type=str, required=True, help='Unauthorized', location = "headers")
        args = parser.parse_args()

        access_tok = args["Authorization"]
        question = args["question"]

        if access_tok != self.access_token:
            return jsonify(self.responseHelper(False, "Unauthorized"))

        answer = self.chatbot_connector(question)
        return jsonify(self.responseHelper(True, answer))

    def responseHelper(self, success, data):
        if (success == False):
            return {
                "success": False,
                "data": "",
                "errorMessage": data
            }

        return {
            "success": True,
            "data": data,
            "errorMessage": ""
        }

    def chatbot_connector(self,question):
        question_list = ["How are you doing?"]
        answer_list = ["I am good"]

        query = question
        if query in question_list:
            return answer_list[question_list.index(query)]

        else:
            return "NO!!"