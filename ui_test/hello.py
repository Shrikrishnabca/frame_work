def attach_count(cls):
    cls.count = 0  # Demo.count = 0
    return cls  # return Demo


@attach_count  # Demo = attach_count(Demo)
class Demo:
    def spam(self):
        print("hello spam")
        Demo.count += 1
