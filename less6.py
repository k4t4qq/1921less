# list = [1, 2, 3]
# iterator = iter(list)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))
# for elem in iterator:
#     print(elem)
#
# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#     def kvadrat(number, max_degree):
#         i = 0
#         for _ in range(max_degree):
#             yield number**i
#             i += 1
#     res = kvadrat(666, 7)
#     print(res)
#     for _ in res:
#         print(_)
#

#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
# count = Counter(5)
# for elem in count:
#     print(elem)

# def kvadrat(number):
#     i = 0
#     while True:
#         result = number**i
#         yield result
#         if result > 10**20:
#             return
#         i += 1
# res = kvadrat(666)
# print(res)
# for _ in res:
#     print(_)

# def helper(work):
#     work_in_memory = work
#     def helper(work):
#         return f"I will help you with {work_in_memory}. Posle pomogu s {work}"
#     return helper
# helper = helper("homework")
# print(helper("cliningi"))
# print(helper("drivingi"))

def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"Problema s {exc}")
        else:
            print(f"No problemo. Result - {result}")
    return checker

@checker
def calculate(expression):
    return eval(expression)
calculate("2+2")
