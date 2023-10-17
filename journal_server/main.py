
logs = list()
class Log:
    def __init__(self, data) -> None:
        self.ip = data[0]
        self.date = data[1]
        self.time = data[2]
        self.url = data[3]
        self.status_server = data[4]
        self.size_response = data[5]

def pars_log(file):
    with open(f'{file}') as jornal:
        lines = jornal.readlines()
        for line in lines:
            list_line = line.replace('\n', '').split('|')
            logs.append(Log(list_line))

# pars_log('journal.txt')
