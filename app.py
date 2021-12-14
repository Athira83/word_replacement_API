from chalice import Chalice
import json
app = Chalice(app_name='testpipeline')


@app.route('/')
def index():
    return {'hello': 'world'}

import json

def process_string(text):
    import re
    keywords=['Deliotte','Oracle','Google','Microsoft','Amazon']                # List of words which has to be replaced
    response_text=''                                                            # Creating an empty response text
    text=text.split(' ')                                                        # Splitting the string by spaces
    for word in text:                                                           # Recreating the text with new words
        if word in keywords:                                                
            word=word+'©'
        else:
            pass
        response_text+=word+' '
    return response_text
    
# text='Hello I am from Microsoft'
process_string(text)
    
# def lambda_handler(event, context):
#     """ THe lambda function will take a text as input from the user and add the copyrighted symbol after the given 
#     keywords. 
#     Eg : Google : Google©
#          Oracle : Oracle©
#          Amazon : Amazon©
#          Deloitte: Deloitte©
#          Microsoft: Microsoft©
#     """
#     print(event['text'])
#     user_input=event["text"]                                                    # To get text input from the event handler
#     user_output=process_string(user_input)
   
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'headers': {'Content-Type': 'application/json'},
#         'body': json.dumps(user_output)
#     }



# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
