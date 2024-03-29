import sys
import time


class Logger:
    def log(self, message):
        current_time = time.localtime()
        sys.stderr.write(
            f'{time.strftime("%Y-%b-%d %H:%M:%S", current_time)} '
            f'---> {message}\n'
        )


logger = Logger()
logger.log('An error was happened!')
