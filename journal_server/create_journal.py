from random import randint, choice
from faker import Faker


class work_of_path:
    def __init__(self, path) -> None:
        self.path = path

    def create_journal(self) -> None:
        fake = Faker()
        
        lines = list()
        http_status = [200, 200, 200, 200, 200, 200, 200,
                        200, 200, 200, 200, 200, 200, 200,
                        200, 200, 200, 200, 200, 200, 201,
                        204, 400, 401, 403, 404, 500, 502, 503]
        list_url = list()
        list_date = list()

        for _ in range(20):
            list_url.append(fake.url())
            for _ in range(3):
                list_date.append(fake.date_this_century())
                
        with open(self.path, 'w') as journal:
            for _ in range(1000):
                ip = fake.ipv4()
                date = choice(list_date)
                time = fake.time()
                url = choice(list_url)
                status_server = choice(http_status)
                size_response = randint(5, 10_240)
                journal.write(f'{ip}|{date}|{time}|{url}|{status_server}|{size_response}\n')
        
        with open(self.path, 'r+') as journal:
            for line in journal:
                lines.append(line)

            count = 0
            while count != -1:
                for i in range(999):
                    line_konstrukt_1 = int("".join(lines[i].split('|')[1:3]).replace('-', '').replace(':', ''))
                    line_konstrukt_2 = int("".join(lines[i+1].split('|')[1:3]).replace('-', '').replace(':', ''))
                    if line_konstrukt_1 > line_konstrukt_2:
                        save = lines[i]
                        lines[i] = lines[i+1]
                        lines[i+1] = save
                        count+=1

                if count == 0:
                    count = -1
                else:
                    res = count
                    count = 0
                
        with open(self.path, 'w') as journal:
            for line in lines:
                journal.write(line)


def make(name):
    work_of_path(f'{name}.txt').create_journal()

# make('journal')
