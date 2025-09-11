# c = EmptyClass()
# print(dir(c))

# Exceptions Are an Exception

# class AnError(Exception):
#     pass

# raise AnError()
# output an error 


class AnError(Exception):
    pass

try:
    raise AnError("Oops!")
except AnError as e:
    print("Caught an error:", e)
