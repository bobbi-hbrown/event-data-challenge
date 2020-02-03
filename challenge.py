import os

challenge_file = os.path.abspath(os.getcwd()) + '/event_data.txt'
with open(challenge_file) as f:
    print(f.readlines())
