import imp
import random
import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
numbers = "0123456789"
symbols = "}{][\"'\|=+-_)(!':;@#$%^`~.,"

all = lower_case + upper_case + numbers + symbols
length = 14
password = "".join(random.sample(all, length))
print(password)
