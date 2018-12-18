#asdfsdfasdfsdf

def m1(*args,**kwargs):
    print('the type of args is',type(args))
    print('the type of kwargs is', type(kwargs))
m1()

dic_inty={'name':'inty','age':'18 years od','height':'180cm','weight':'193b'}
def someone(dic_someone):

    for k,v in dic_someone.items():
         print(k,':',v)

someone(dic_inty)


def someone(**kwargs):
    for k,v in kwargs.items():
         print(k,':',v)
someone(name='xiao',age='18',height='192')

#aaaa