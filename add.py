class Tools(object):
    """
    工具，
    一个工具
    """

    # 我增加一行
    def __init__(self):
        super().__init__()
        self.say_hi()
        self.HELLO = "Hello"    # 插入一行

    def say_hello(self, one):
        if one:
            print(f'{self.HELLO},{one}')

    # 开发的注释1
    def say_hi(self, one):
        if one:
            print('我在这里插入一行')
            print(f'Hi~{one}')
            print('后面也插入一行')
