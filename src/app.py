import os
from flask import Flask, request, Response
from src.models import slack_commands
from src.models.fact_generator import FactGenerator
from src.configs import Configs


app = Flask(__name__)
config = Configs()
SLACK_WEBHOOK_SECRET = config.incoming_key


@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        if "puppy_fact" in text:
            #fact_generator = Fact_generator()
            slack_commands.send_message(channel,
                                        FactGenerator.puppy_fact_generator(),
                                        FactGenerator.puppy_fact_attachment())
            print(FactGenerator.puppy_fact_attachment())


@app.route('/', methods=['GET'])
def test():
	return Response('It works!')


if __name__ == "__main__":
	app.run(debug=True)