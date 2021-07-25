import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And ' \
            'this is a second message","timestamp":"2021-06-04 16:41:01"}]} '
obj = json.loads(json_text)
key = "messages"
message2 = (obj[key][1])
key2 = "message"
print(message2[key2])


