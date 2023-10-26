class Tools(object):
    """
    工具，
    一个工具
    """

    def __init__(self):
        super().__init__()
        self.say_hi()

    def say_hi(self, one):
        if one:
            print(f'Hi~{one}')
