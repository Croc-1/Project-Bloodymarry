"""
script file for the logging of the program
"""

import os
import string
import secrets
import time
import json


def logit(message=''):
    """

    :param message: message to pass by the programmer stored in the
    log file

    :return: log_data
    """
    if os.path.exists('log') is False:
        # making the log directory
        os.mkdir('log')
        # changing the current working directory to another
        os.chdir('log')

        # creating the log file in the log directory
        with open('logfile.log', 'x') as _:
            pass
    else:
        os.chdir('log')
        number_id = ' '.join(secrets.choice(string.digits) for _ in range(5))
        log_data = [time.asctime(time.localtime()), number_id, message]
        with open('logfile.log', 'a') as log_file:
            json.dump(log_data, log_file)
            log_file.write('\n')
        os.chdir('..')
        return number_id
