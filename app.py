import openai
from flask import Flask, render_template, request
from dotenv import dotenv_values
import json 

config = dotenv_values(".env");
openai.api_key = config['OPENAI_API_KEY']

app = Flask(__name__,
    template_folder='templates',
    static_url_path='',
    static_folder='static'
            )

@app.route("/")
def index():
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt='give me a motivation quote'
    )
    return response['choices'][0]['text']

if __name__ == "__main__":
    app.run(debug=True)

