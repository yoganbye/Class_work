class Input:
    '''
    Один из классов который описывает тэг input,
    можно создать базовый класс для всех тэгов 
    и вынести туда какие-нибудь общие вещи, с ходу не придумал
    '''
    def __init__(self, type_attr, text_attr):
        '''
        тэг инпут должен иметь аттрибут type,
        на счет аттрибутов можешь не заморачиваться, 
        если не знаешь фронтенд
        '''
        self.type_attr = type_attr
        self.text_attr = text_attr
    
    def __str__(self):
        return f'<input type="{self.type_attr}"> {self.text_attr} </input>'

class TagFactory:
    '''
    этот класс должен реализовывать у тебя создание обьектов а не просто           
    возврат строчки
    '''
   
    def create_tag(self, name):
        '''
        этот метод должен реализовывать создание тэгов
        ты можешь создать несколько статических методов которые будут       
        создавать конкретные тэги
        '''
        if name == 'input':
            tag = self.create_input()
        # elif name == 'a':
        #     ........
            
        return tag
    
    @staticmethod
    def create_input(type_attr='button', text_attr='Кнопка'):
        tag = Input(type_attr, text_attr)
        return tag


'''
В итоге ты с помощью фабрики создаешь тэги
'''
tag_factory = TagFactory()

new_input = tag_factory.create_tag(name='input')
# new_input = tag_factory.create_tag(name='a')


print(new_input)