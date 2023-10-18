logs = list()
class Log:
    def __init__(self, data) -> None:
        self.ip = data[0]
        self.date = data[1]
        self.time = data[2]
        self.url = data[3]
        self.status_server = data[4]
        self.size_response = data[5]

class DataCalculation:
    def __init__(self, logs = logs) -> None:
        self.logs = logs
        self.ip = list()
        self.date = list()
        self.time = list()
        self.urls = list()
        self.status_server = list()
        self.size_response = list()
        for log in logs:
            self.ip.append(log.ip)
            self.date.append(log.date)
            self.time.append(log.time)
            self.urls.append(log.url)
            self.status_server.append(log.status_server)
            self.size_response.append(log.size_response)
    
    def top_urls(self) -> dict:
        dict_urls = dict()
        for url in self.urls:
            dict_urls[url] = self.urls.count(url)
        sorted_dict = dict(
                sorted(dict_urls.items(), key=lambda item: item[1], reverse=True))
        return sorted_dict
    
    def averege_response_size(self) -> str:
        res = 0
        for size in self.size_response:
            res+= int(size)
        res /= len(self.size_response)
        return f'{res}kb'
    
    def count_status(self, status) -> list:
        return self.status_server.count(str(status))
    
    def count_day_requests(self) -> dict:
        dict_date = dict()
        for date in self.date:
            dict_date[date] = self.date.count(date)
        sort_dict = dict(sorted(dict_date.items(), key = lambda item: item[1], reverse=True))
        first_key = next(iter(sort_dict))
        url_list_day = list()
        for log in logs:
            if log.date == first_key:
                url_list_day.append(log.url)

        dict_url = dict()
        for url in url_list_day:
            dict_url[url] = url_list_day.count(url)
        sort_dict_url = dict(sorted(dict_url.items(), key = lambda item: item[1], reverse=True))
        return sort_dict_url

def pars_log(file) -> None:
    with open(f'{file}') as jornal:
        lines = jornal.readlines()
        for line in lines:
            list_line = line.replace('\n', '').split('|')
            logs.append(Log(list_line))

# pars_log('journal.txt')
# print(DataCalculation(logs).count_day_requests())
