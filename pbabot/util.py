import pickle

class Clock:
    """Countdown Clock

    This class maintains the state of a countdown clock. It also increases and decreases their value.

    Attributes:
        name -> String: Name of the clock
        time -> String: Time of the clock (defaults to 1200 on creation)
    """
    def __init__(self, name: str, time: str = '1200'):
        """Init"""
        self.name = name
        self.time = time

    def __str__(self):
        """String representation of a clock"""
        switch = {
            '1200': '□□□□ □□□□ □□□□ □ □ □',
            '1500': '■■■■ □□□□ □□□□ □ □ □',
            '1800': '■■■■ ■■■■ □□□□ □ □ □',
            '2100': '■■■■ ■■■■ ■■■■ □ □ □',
            '2200': '■■■■ ■■■■ ■■■■ ■ □ □',
            '2300': '■■■■ ■■■■ ■■■■ ■ ■ □',
            '0000': '■■■■ ■■■■ ■■■■ ■ ■ ■'
        }

        return f'{self.name}: {switch[self.time]}'

    def increase(self) -> str:
        """Increases the clock's time by one segment"""
        if self.time == "1200":
            self.time = "1500"
        elif self.time == "1500":
            self.time = "1800"
        elif self.time == "1800":
            self.time = "2100"
        elif self.time == "2100":
            self.time = "2200"
        elif self.time == "2200":
            self.time = "2300"
        elif self.time == "2300":
            self.time = "0000"
        elif self.time == "0000":
            return 'Clock is already at midnight.'

    def decrease(self) -> str:
        """Decreases the clock's time by one segment"""
        if self.time == "0000":
            self.time = "2300"
        elif self.time == "2300":
            self.time = "2200"
        elif self.time == "2200":
            self.time = "2100"
        elif self.time == "2100":
            self.time = "1800"
        elif self.time == "1800":
            self.time = "1500"
        elif self.time == "1500":
            self.time = "1200"
        elif self.time == "1200":
            return 'Clock is already at 1200.'


class Contact:
    """Contact

    Stores a contacts name and description.

    Attributes:
        name -> String: Name of the contact
        description -> String: Description of the contact
    """
    def __init__(self, name: str, description: str):
        """Init"""
        self.name = name
        self.description = description

    def __str__(self):
        """String representation of a Contact"""
        return f'{self.name}: {self.description}'


class FileManager:
    """FileManager

    Contains static functions that interact with files on disk.
    """
    @staticmethod
    def log(message, filename='log.txt'):
        """Writes the message to a log file"""
        with open(filename, 'a') as file:
            file.write(f'{message}\n')
            print(f'Log saved: {message}')

        return 'Log saved.'

    @staticmethod
    def save_data(data, filename):
        with open(filename, 'wb') as file:
            file.write(pickle.dumps(data))

    @staticmethod
    def load_data(filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.loads(file.read())
        except EOFError:
            print('No data in file.')
        except FileNotFoundError:
            print('No data file found.')
