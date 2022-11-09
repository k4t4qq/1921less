# ! logging
# import logging
#
# logging.basicConfig(level = logging.DEBUG,
# 		    filename = "logs.log",
# 		    filemode = "a",
# 		    format = "We have next logging message:%(asctime)s:%(levelname)s - %(message)s")
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")
# try:
#     print(10/10)
# except Exception:
#     logging.exception("Exception")
#
# 0.5! ASSERT
# assert 2+2==5,"ne rabotaet"
# assert func(), "func ne rabitea"
#
# !! DOCTEST
# """
# >>> 2+2
# 5
# """
# IF __name == "__main__":
#     import doctest
#     doctest.testmod()
#
#!!! unittest
def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result
