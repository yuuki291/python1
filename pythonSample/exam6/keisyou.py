
class MyObj:
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return "<You: message='" + self.message + "'>"

    # プロパティ
    @property
    def message(self):
        return self.__message

    # プロパティの値の変更のための関数
    @message.setter
    def message(self, value):
        if value != '':
            self.__message = value

    ob = MyObj("hello1")
    print(ob.message)
    ob.message = ''
    print(ob)
    ob.message = 'Bye!'
    print(ob)
