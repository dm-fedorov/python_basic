#!/usr/bin/env python
# coding: utf-8

# ## Обработка ошибок в Python

# In[1]:


def try_div(x):
    if x:
        return 5 / x 
    # else: return None


# In[2]:


print(try_div(5))
print(try_div(0)) # функция вернет None


# In[3]:


a = 5
result = try_div(a)
if result is not None:
    print(result)


# In[ ]:





# In[4]:


def my_function_1(x):
    import math
    result = try_div(x)
    if result is not None: 
        return result * math.pi


# In[5]:


print(my_function_1(5))
print(my_function_1(0)) 


# In[ ]:





# In[6]:


def my_function_2(x):
    result = my_function_1(x)
    if result is not None:
        return result ** 3


# In[7]:


print(my_function_2(5))
print(my_function_2(0))


# In[ ]:





# In[8]:


def try_div_raise(x):
    if x:
        return 5 / x
    else:
        # генерируем исключение:
        raise ZeroDivisionError 


# In[ ]:





# In[9]:


def my_function_1(x):
    import math
    return try_div_raise(x) * math.pi


# In[ ]:





# In[10]:


def my_function_2(x):
    return my_function_1(x) ** 3


# In[11]:


print(my_function_2(0))


# In[ ]:





# In[12]:


try:
    print(my_function_2(0))
except ZeroDivisionError:
    print("Ошибка деления на ноль!")


# In[ ]:





# In[13]:


4/0


# In[ ]:





# In[14]:


def my_function_1(x):
    import math
    return 5/x * math.pi


# In[15]:


def my_function_2(x):
    return my_function_1(x) ** 3


# In[16]:


try:
    print(my_function_2(0))
except ZeroDivisionError:
    print("Ошибка деления на ноль!")


# In[ ]:





# In[17]:


int("r")


# In[ ]:





# In[ ]:





# In[18]:


try:
    x = int(input("Введите число: "))
    print(5/x)
except ZeroDivisionError:
    print("Ошибка деления на ноль!!!")
except ValueError:
    print("Ошибка преобразования типа!!!")


# In[ ]:





# In[19]:


try:
    x = int(input("Введите число: "))
    print(5/x)
except:
    print("Какая-то ошибка")


# In[ ]:





# In[20]:


try:
    x = int(input("Введите число: "))
    print(5/x)
except Exception as err:
    #print(type(err))
    print(err) 


# In[ ]:





# In[21]:


def get_int(msg):
    while True:
        try:
            x = int(input(msg))
            return x
        except ValueError:
            print("Ошибка преобразования типов")


# In[22]:


get_int("Введите целое число: ")


# In[ ]:





# In[23]:


x = (1, 2, 3)
assert len(x) > 5, 'len(x) not > 5'


# In[ ]:





# In[ ]:





# In[ ]:




