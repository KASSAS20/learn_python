from datetime import datetime


TASKS = list()
class Task:
    def __init__(self, name: str, destriction: str, end_date: datetime, level: int) -> None:
        self.name = name
        self.destriction = destriction
        self.end_date = end_date
        self.level = level
        TASKS.append(self)

class Meta:
    def get_falshe_tasks():
        result = list()
        for task in TASKS:
            if task.end_date < datetime.now():
                result.append(task)
        return result
    
        

Task('1','1',datetime(2023, 12, 20, 20, 20, 0), 2)
Task('2','2',datetime(2022, 12, 20, 20, 20, 0), 3)
Task('3','3',datetime.now(), 1)

for i in Meta.get_falshe_tasks():
    print(i.name)

    

