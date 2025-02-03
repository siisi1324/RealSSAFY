# 클래스가 사용해야 할 것 
# 클래스 메서드, 스태틱 메서드

# 인스턴스가 사용해야 할 것 
# 인스턴스 메서드

class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
# 클래스가 할 수 있는 것
print(MyClass.instance_method(instance))
print(MyClass.class_method())
print(MyClass.static_method())


# 인스턴스가 할 수 있는 것
print(instance.instance_method())
print(instance.class_method())
print(instance.static_method())

# 결론적으로 전부 다 가능하다. (구조적, 문법적으로 막지 않는다.)
# 하지만 알아서 제한해서 사용하도록
# 할 수 있다 != 써도 된다. 
# 패러다임이다. (규칙은 아니지만)