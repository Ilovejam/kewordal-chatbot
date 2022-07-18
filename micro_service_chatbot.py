from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
import requests

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
        url = f"https://kewordal-backend.herokuapp.com/answers/getByQuestion?question={question}"
        headers = {
            "Authorization" : self.access_token,
            "Content-Type": "application/json"
        }
        response = requests.get(url=url,headers=headers)
        response = response.json()
        status = response["data"]["status"]
        answer = response["data"]["answer"]

        if status == "No":
            #TODO: there is no question like this in microservice. Search another place.
            print(status)
            return answer

        print(status)
        return answer