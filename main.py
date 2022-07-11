from operator import index


print("hello")
question_list = ["How are you doing?"]
answer_list = ["I am good"]

query = input("You: ")
if query in question_list:
    print(answer_list[question_list.index(query)])

else:
    print("NO!!")
