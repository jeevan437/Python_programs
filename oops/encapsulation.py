# class Hello:
#     def __init__(self):
#         self.a = 10
#         self._b = 20
#         self.__c = 30
#
# obj = Hello()
# print(obj.a)

class Hello:
    def __init__(self):
        self.__version  = 10

    def get_version(self):
        print(self.__version)

    def set_version(self,a):
        self.__version = a



obj = Hello()
obj.get_version()
obj.set_version(20)
obj.get_version()

