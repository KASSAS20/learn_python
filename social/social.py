class Cosial: #создание социальной сети
    def __init__(self, users: list = [], groups: list = []) -> None:
        self.users = users
        self.groups = groups

    def __str__(self) -> str:
        return f'cont users: {len(self.users)}\ncount groups: {len(self.groups)}'
    
    def searsh_group(self, name: str) -> list:
        res = list()
        for group in self.groups:
            if group.name == name:
                res.append(group)
        return res
    
    def searsh_users(self, name: str) -> list:
        res = list()
        for user in self.users:
            if user.name == name:
                res.append(user)
        return res



class User:
    def __init__(self, name: str, age: int = None, friends_list: list = [], subscriptions_group: list = [], subscriptions: list = [], subscribers: list = [], posts: list = [], secure: bool = True) -> None:
        self.name = name
        self.age = age
        self.friends_list = friends_list
        self.subscriptions_group = subscriptions_group
        self.subscriptions = subscriptions#подписки
        self.subscribers = subscribers#подписчики
        self.posts = posts
        self.secure = secure#тип профиля : True - открытый и наоборот

    def __str__(self) -> str:
        if self.secure == True:
            return f'name: {self.name}\nage: {self.age}\ncount frends: {len(self.friends_list)}\ncount subscriptions: {len(self.subscriptions)}\ncount subscribes: {len(self.subscribers)}'
        else:
            return f'Пользователь {self.name} ограничил доступ к своему профилю'

class Comment:# создание коментария
    def __init__(self, author: User = None, content: str = None, count_like: int = 0, count_preview: int = 0) -> None:
        self.author = author
        self.content = content
        self.count_like = count_like
        self.count_preview = count_preview
    def __str__(self) -> str:
        return f'author: {self.author}\ncontent: {self.content}\ncount like: {self.count_like}\ncount preview: {self.count_preview}'

class Post:#создание поста пользователя
    def __init__(self,author: User = None, content: str = None, count_like: int = 0,count_preview: int = 0, list_comment: list = [], secure: bool = True) -> None:
        self.author = author
        self.content = content
        self.count_like = count_like
        self.count_preview = count_preview
        self.list_comment = list_comment
        self.secure = secure

    def __str__(self) -> str:
        return f'author: {self.author}\ncontent: {self.content}\ncount like: {self.count_like}\ncount preview: {self.count_preview}\ncount_comment: {len(self.list_comment)}'

    def add_comment(self, comment: Comment) -> None:
        self.list_comment.append(comment)

class Post_Group:# создание поста группы
    def __init__(self, author = None, content: str = None, count_like: int = 0, count_preview: int = 0, list_comment: list = []) -> None:
        self.author = author
        self.content = content
        self.count_like = count_like
        self.count_preview = count_preview
        self.list_comment = list_comment
    
    def __str__(self) -> str:
        return f'author: {self.author}\ncontent: {self.content}\ncount like: {self.count_like}\ncount preview: {self.count_preview}\ncount_comment: {len(self.list_comment)}'

    def add_comment(self, comment: Comment) -> None:
        self.list_comment.append(comment)

class Group:#создание группы
    def __init__(self, admins: list, id: int, name: str, discription: str, posts: list = [], subscribers: list = []) -> None:
        self.id = id
        self.name = name
        self.admins = admins
        self.discription = discription
        self.posts = posts 
        self.subscribers = subscribers

    def __str__(self) -> str:
        return f'id: {self.id}\nname: {self.name}\ndiscription: {self.discription}\ncount subscribers: {len(self.subscribers)}\ncount posts: {len(self.posts)}'
    
    def add_member(self, member: User) -> None:
        self.subscribers.append(member)
    
    def remove_member(self, member: User) -> None:
        self.subscribers.remove(member)

    def create_post(self, post: Post_Group) -> None:
        if post.author in self.admins:
            self.posts.append(post)
    
    def view_post(self, user: User) -> list:
        if user in self.subscribers:
            return self.posts



class Profile_User: #создание профиля пользователя
    def __init__(self, id: int, user:User) -> None:
        self.id = id
        self.user = user
    
    def __str__(self) -> str:
        return f'id: {self.id}\nname: {self.user.name}'

    def add_frend(self, frend: User) -> None:
        if frend not in self.user.friends_list:
            self.user.friends_list.append(frend)

    def remove_friend(self, frend: User) -> None:
        if frend in self.user.friends_list:
            self.user.friends_list.remove(frend)
    
    def get_frends(self) -> list:
        return self.user.friends_list
    
    def create_post(self, post: Post) -> None:
        self.user.posts.append(post)
    
    def view_post(self, person: User) -> list:
        if (person.secure == True) or (person in self.user.friends_list):
            return person.posts
        
class Chat: #чат между двумя пользователями
    def __init__(self, user_1: User, user_2: User, messages: list = []) -> None:
        self.user_1 = user_1
        self.user_2 = user_2
        self.messages = messages
    
    def __str__(self) -> str:
        return f'Это чат пользователей {self.user_1} и {self.user_2}'
    
    def drop_message(self, droper:User, message: str) -> None:
        if droper in [self.user_1, self.user_2]:
            self.messages.append((droper, message))
    
