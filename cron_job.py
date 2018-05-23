from src.models import slack_commands
from src.models.fact_generator import FactGenerator
import time


def cron_job():
    #users = ["G5GB3E2UQ", "G2ENPNCTT", "G8N9KU65A", "U0JS84517"]
    users = ['C0JS385LP']
    while True:
        if all([(time.localtime().tm_hour == 9), (time.localtime().tm_min == 55)]):
            print("sending...")
            for user in users:
                slack_commands.send_message(user,
                                            FactGenerator.puppy_fact_generator(),
                                            FactGenerator.puppy_fact_attachment())
            time.sleep(120)
        else:
            time.sleep(50)

cron_job()