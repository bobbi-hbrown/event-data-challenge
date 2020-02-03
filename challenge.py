import os, base64, json, re

challenge_file = os.path.abspath(os.getcwd()) + '/event_data.txt'


def to_json(challenge_file):
    events_json = {}
    regex = re.compile(r'[\n\\\"]')

    with open(challenge_file) as f:
        event_data = f.readlines()

        for line in event_data:
            event_data_split = line.split(' ')

            for k in range(0, len(event_data_split) - 1, 2):

                val = re.sub(regex, '', str(event_data_split[k+1]))
                events_json[event_data_split[k].strip(':')] = val

    print(events_json)
    return events_json

def decode_hint(json_data):

    decoded_data = base64.b64decode(json_data['hint'])
    print(decoded_data)

def xor_value(val):

    bitwise_comparison = int(val, 16) ^ 0x17F
    print(bitwise_comparison)

json_data = to_json(challenge_file)
decode_hint(json_data)
xor_value(json_data['one'])
xor_value(json_data['two'])
xor_value(json_data['three'])
xor_value(json_data['four'])