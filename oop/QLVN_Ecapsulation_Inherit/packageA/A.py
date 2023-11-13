class A:
    def __init__(self,a :int,b,c)->None:
        self._a=a
        self.__b=b
        self.c=c

    def _methodA(self):
        print('Phướng thức _a(): Protected')

    def __methodB(self):
        print('Phướng thức __b(): Private')

    def methodC(self):
        print('Phướng thức c(): Public')

    def test_internal_class(self):
        print(self._a,self.__b,self.c)
        self._methodA()
        self.__methodB()
        self.methodC()


class C(A):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d=d

    def test(self):
        print(self._a,self.c,self.d)
        super()._methodA()
        super().__methodB()
        super().methodC()
if __name__ == '__main__':
    a_obj =A(1,2,3)

    c_obj = C(4,5,6,7)
    # c_obj.test()
