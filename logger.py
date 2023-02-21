import json
import datetime


def add_log(data):
    with open('log.json', 'a') as log_writing:
        dt = str(datetime.datetime.now())
        log_writing.write('-'*6+ dt + '\n')
        json.dump(data, log_writing, indent=4)
        log_writing.write('-'*6+ '\n')


def read_log():
    with open('log.json', 'a') as log_reading:
        print(*log_reading.readlines)
