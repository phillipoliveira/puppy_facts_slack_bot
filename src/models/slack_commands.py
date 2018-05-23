from slackclient import SlackClient
from src.configs import Configs

config = Configs()
slack_client = SlackClient("xoxp-18873171831-63318799281-363547280834-5b242eb4a4ccb78212e2e28b38abf0ab")
slack_client.api_call("api.test")
slack_client.api_call("auth.test")

SLACK_TOKEN = "xoxp-18873171831-63318799281-363547280834-5b242eb4a4ccb78212e2e28b38abf0ab"
slack_client = SlackClient(SLACK_TOKEN)

def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call['ok']:
        return channels_call['channels']
    return None


def list_groups():
    groups_call = slack_client.api_call("groups.list")
    if groups_call['ok']:
        return groups_call['groups']
    return None


def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None


def print_channels():
    if __name__ == '__main__':
        channels = list_channels()
        if channels:
            print("Channels: ")
            for c in channels:
                print(c['name'] + " (" + c['id'] + ")")
                detailed_info = channel_info(c['id'])
                if detailed_info['purpose']['value']:
                    try:
                        print("\t"+(detailed_info['purpose']['value']))
                    except:
                        continue
        else:
            print("Unable to authenticate.")


def print_groups():
    if __name__ == '__main__':
        groups = list_groups()
        if groups:
            print("Groups: ")
            for g in groups:
                print(g['name'] + " (" + g['id'] + ")")
        else:
            print("Unable to authenticate.")


def send_message(channel_id, message, attachment):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='Puppy Facts Bot',
        icon_emoji=':dog:',
        attachments=attachment
    )


def return_group_id(name):
    groups_call = slack_client.api_call("groups.list")
    for g in groups_call['groups']:
        if g['name'] == name:
            return g['id']


def return_user_id(firstname):
    users = slack_client.api_call("users.list")
    l,results,count = [],[],0
    for i in users['members']:
        l.append(i['id'])
    while count < len(l):
        count+=1
        for i in users['members']:
            try:
                if i[u'profile']['first_name'].lower() == firstname.lower():
                    results.append(i[u'profile']['last_name'] + ": " + i['id'])
                else:
                    continue
            except:
                continue
    return set(results)


def print_users():
    users = slack_client.api_call("users.list")
    for i in users['members']:
        try:
            print(i[u'profile']['first_name'] +" "+ i[u'profile']['last_name'])
            print(i['id'])
        except:
            continue
