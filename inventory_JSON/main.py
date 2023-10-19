import json

class json_setting:
    def __init__(self, file:str) -> None:
        self.file = file

    def loging(self, massage) -> None:
        with open('history.txt', 'a+') as file:
            file.write(f'{massage}\n')

    def get_json(self) -> dict:
        with open(f"{self.file}", "r+") as json_file:
            return json.load(json_file)
    
    def post_json(self, products: dict) -> None:
        with open(f"{self.file}", "w") as json_file:
            json_file.write(json.dumps(products, indent=4))
    
    def edit_json(self, products:dict): #передать то что надо изменить
        file = self.get_json()
        for product in products:
            file[product] = products[product]
        self.post_json(file)

    def search_by_name(self, name: str) -> list:
        res = list()
        file = self.get_json()
        for product in file:
            product = product.lower()
            name = name.lower()
            if name in product:
                res.append(product)
        return res
    
    def search_by_price(self, min: int, max: int) -> list:
        res = list()
        file = self.get_json()
        for product in file:
            price = int(file[product]['price'])
            if price >= min and price <= max:
                res.append(product)
        return(res)
    
    def buy_product(self, product: str, count: int = 1) -> None: #пополнение это отрицательный COUNT
        file = self.get_json()
        if file[product]['count'] >= count:
            file[product]['count'] -= count
            self.edit_json(products=file)
            if count > 0:
                self.loging(
                f"Проданно {count} {product} на сумму {count*file[product]['price']}")
            else:
                self.loging(
                f"Пополнение {abs(count)} {product} на сумму {abs(count)*file[product]['price']}")
        else:
            print('ERROR: LOW COUNT')

        
    

file = json_setting('inventory.json')
# d = file.get_json()
# q = {"Zapravka59": {'id': 10, 'distriction': 'apple', 'price': 400, 'count': 23}}
file.buy_product('Zapravka59', count=-5)
        
