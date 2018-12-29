class A:
    def __init__(self):
        self.global_attribute = 'haha'
        pass

    # def __getattribute__(self, name):
        # return self.__dict__[name]

# create obj a
a = A()
# This will call magic method __getattribute__
print(a.global_attribute)
# This will call magic method __setattr__ and set the 'global_attr' to 'hehe
a.global_attribute = 'hehe'
print(a.global_attribute)

#
# class B:
#     def __init__(self):
#         self.glbl_attr_of_B = 'new'
#
#     def __getattribute__(self, name):
#         return 123456
#
# b = B()
# # This should print 'new', but because we override the origin '__getattribute__', this will print '123456' instead.
# print(b.glbl_attr_of_B)

class B:
   def __init__(self):
       self.glbl_attr_of_B = 'new'

   # def __getattribute__(self, name):
   #     return 123456

   def __setattr__(self, name, value):
       if int(value) > 100:
           self.__dict__[name] = value
       else:
           pass

b = B()
b.glbl_attr_of_B = 99
print(b.glbl_attr_of_B)
