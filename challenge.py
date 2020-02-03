import os, base64, json, re

challenge_file = os.path.abspath(os.getcwd()) + '/event_data.txt'

# Converts our event_data into JSON format in order to parse
def to_json(challenge_file):

    # Create a new dict to populate with our event_data
    events_json = {}
    # Regex to remove the extra newlines, backslashes and extra quotation marks
    regex = re.compile(r'[\n\\\"]')

    with open(challenge_file) as f:
        event_data = f.readlines()

        for line in event_data:
            # Split this string into a list using whitespace as the delimiter
            event_data_split = line.split(' ')

            # Iterate through each item in our list, stepping over every 2nd item to turn pairs of items into key-value pairs
            for k in range(0, len(event_data_split) - 1, 2):

                # Sub out unwanted characters using our regex pattern, and set this as our value
                val = re.sub(regex, '', str(event_data_split[k+1]))
                # Remove colon characters from keys, then use this value as the key name
                events_json[event_data_split[k].strip(':')] = val

    print('Challenge json data: ' + str(events_json))
    return events_json

# base64 decode the value of key 'hint'
def decode_hint(json_data):

    decoded_data = base64.b64decode(json_data['hint'])
    print('B64 decoded hint: ' + str(decoded_data))

    return decoded_data

# Find the the bitwise XOR comparison with 0x175
def xor_value(val):

    # Make sure our value is interpreted as hexadecimal
    bitwise_comparison = int(val, 16) ^ 0x17F
    print('int value of our xor comparison ' + str(val) + ' with 0x17F: ' + str(bitwise_comparison))
    print('hex value of our xor comparison ' + str(val) + ' with 0x17F: ' + str(hex(bitwise_comparison)))

    return bitwise_comparison



json_data = to_json(challenge_file)
decode_hint(json_data)
xor_value(json_data['one'])
xor_value(json_data['two'])
xor_value(json_data['three'])
xor_value(json_data['four'])