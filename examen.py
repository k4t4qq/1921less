import inspect
import os

import colorama
import urllib
import datetime

choicelibrary = input("Hello\nWhat library you want to do introspection with? Libraries accessible for introspection: colorama, urllib, datetime\n")

#____________________________________________________________________

if choicelibrary == "colorama":
    print("\nLibrary colorama is module?", inspect.ismodule(colorama))
    print("Library colorama is callable?", callable(colorama))
    for method in dir(colorama):
        print("\n", method)

    while True:
        choicemethod = input("\nWhat method you want to do introspection with?\nIf you want to see all colorama methods, write print_again\nIf you want to clear console, write clear\n")

        if choicemethod == "AnsiToWin32":
            print("\nMethod AnsiToWin32 is class?", inspect.isclass(colorama.AnsiToWin32))
            print("\nMethod AnsiToWin32 is callable?", callable(colorama.AnsiToWin32))
            for method in dir(colorama.AnsiToWin32):
                print("\n", method)

        elif choicemethod == "Back":
            print("\nMethod Back is class?", inspect.isclass(colorama.Back))
            print("\nMethod Back is callable?", callable(colorama.Back))
            for method in dir(colorama.Back):
                print("\n", method)

        elif choicemethod == "Cursor":
            print("\nMethod Cursor is class?", inspect.isclass(colorama.Cursor))
            print("\nMethod Cursor is callable?", callable(colorama.Cursor))
            for method in dir(colorama.Cursor):
                print("\n", method)

        elif choicemethod == "Fore":
            print("\nMethod Fore is class?", inspect.isclass(colorama.Fore))
            print("\nMethod Fore is callable?", callable(colorama.Fore))
            for method in dir(colorama.Fore):
                print("\n", method)

        elif choicemethod == "Style":
            print("\nMethod Style is class?", inspect.isclass(colorama.Style))
            print("\nMethod Style is callable?", callable(colorama.Style))
            for method in dir(colorama.Style):
                print("\n", method)

        elif choicemethod == "__builtins__":
            print("\nMethod __builtins__ is class?", inspect.isclass(colorama.__builtins__))
            print("\nMethod __builtins__ is callable?", callable(colorama.__builtins__))
            for method in dir(colorama.__builtins__):
                print("\n", method)

        elif choicemethod == "__cached__":
            print("\nMethod __cached__ is class?", inspect.isclass(colorama.__cached__))
            print("\nMethod __cached__ is callable?", callable(colorama.__cached__))
            for method in dir(colorama.__cached__):
                print("\n", method)

        elif choicemethod == "__doc__":
            print("\nMethod __doc__ is class?", inspect.isclass(colorama.__doc__))
            print("\nMethod __doc__ is callable?", callable(colorama.__doc__))
            for method in dir(colorama.__doc__):
                print("\n", method)

        elif choicemethod == "__file__":
            print("\nMethod __file__ is class?", inspect.isclass(colorama.__file__))
            print("\nMethod __file__ is callable?", callable(colorama.__file__))
            for method in dir(colorama.__file__):
                print("\n", method)

        elif choicemethod == "__loader__":
            print("\nMethod __loader__ is class?", inspect.isclass(colorama.__loader__))
            print("\nMethod __loader__ is callable?", callable(colorama.__loader__))
            for method in dir(colorama.__loader__):
                print("\n", method)

        elif choicemethod == "__name__":
            print("\nMethod __name__ is class?", inspect.isclass(colorama.__name__))
            print("\nMethod __name__ is callable?", callable(colorama.__name__))
            for method in dir(colorama.__name__):
                print("\n", method)

        elif choicemethod == "__package__":
            print("\nMethod __package__ is class?", inspect.isclass(colorama.__package__))
            print("\nMethod __package__ is callable?", callable(colorama.__package__))
            for method in dir(colorama.__package__):
                print("\n", method)

        elif choicemethod == "__path__":
            print("\nMethod __path__ is class?", inspect.isclass(colorama.__path__))
            print("\nMethod __path__ is callable?", callable(colorama.__path__))
            for method in dir(colorama.__path__):
                print("\n", method)

        elif choicemethod == "__spec__":
            print("\nMethod __spec__ is class?", inspect.isclass(colorama.__spec__))
            print("\nMethod __spec__ is callable?", callable(colorama.__spec__))
            for method in dir(colorama.__spec__):
                print("\n", method)

        elif choicemethod == "__version__":
            print("\nMethod __version__ is class?", inspect.isclass(colorama.__version__))
            print("\nMethod __version__ is callable?", callable(colorama.__version__))
            for method in dir(colorama.__version__):
                print("\n", method)

        elif choicemethod == "ansi":
            print("\nMethod ansi is class?", inspect.isclass(colorama.ansi))
            print("\nMethod ansi is callable?", callable(colorama.ansi))
            for method in dir(colorama.ansi):
                print("\n", method)

        elif choicemethod == "ansitowin32":
            print("\nMethod ansitowin32 is class?", inspect.isclass(colorama.ansitowin32))
            print("\nMethod ansitowin32 is callable?", callable(colorama.ansitowin32))
            for method in dir(colorama.ansitowin32):
                print("\n", method)

        elif choicemethod == "colorama_text":
            print("\nMethod colorama_text is class?", inspect.isclass(colorama.colorama_text))
            print("\nMethod colorama_text is callable?", callable(colorama.colorama_text))
            for method in dir(colorama.colorama_text):
                print("\n", method)

        elif choicemethod == "deinit":
            print("\nMethod deinit is class?", inspect.isclass(colorama.deinit))
            print("\nMethod deinit is callable?", callable(colorama.deinit))
            for method in dir(colorama.deinit):
                print("\n", method)

        elif choicemethod == "init":
            print("\nMethod init is class?", inspect.isclass(colorama.init))
            print("\nMethod init is callable?", callable(colorama.init))
            for method in dir(colorama.init):
                print("\n", method)

        elif choicemethod == "initialise":
            print("\nMethod initialise is class?", inspect.isclass(colorama.initialise))
            print("\nMethod initialise is callable?", callable(colorama.initialise))
            for method in dir(colorama.initialise):
                print("\n", method)

        elif choicemethod == "reinit":
            print("\nMethod reinit is class?", inspect.isclass(colorama.reinit))
            print("\nMethod reinit is callable?", callable(colorama.reinit))
            for method in dir(colorama.reinit):
                print("\n", method)

        elif choicemethod == "win32":
            print("\nMethod win32 is class?", inspect.isclass(colorama.win32))
            print("\nMethod win32 is callable?", callable(colorama.win32))
            for method in dir(colorama.win32):
                print("\n", method)

        elif choicemethod == "winterm":
            print("\nMethod winterm is class?", inspect.isclass(colorama.winterm))
            print("\nMethod winterm is callable?", callable(colorama.winterm))
            for method in dir(colorama.winterm):
                print("\n", method)

        elif choicemethod == "clear":
            os.system("cls")

        elif choicemethod == "print_again":
            for method in dir(colorama):
                print("\n", method)

        else:
            print("This method in library colorama doesn't exist")
else:
    print("This library can't introspecting")

#____________________________________________________________________

if choicelibrary == "urllib":
    print("\nLibrary urllib is module?", inspect.ismodule(urllib))
    print("Library urllib is callable?", callable(urllib))
    for method in dir(urllib):
        print("\n", method)

    while True:
        choicemethod = input("\nWhat method you want to do introspection with?\nIf you want to see all urllib methods, write print_again\nIf you want to clear console, write clear\n")

        if choicemethod == "__builtins__":
            print("\nMethod __builtins__ is class?", inspect.isclass(urllib.__builtins__))
            print("\nMethod __builtins__ is callable?", callable(urllib.__builtins__))
            for method in dir(urllib.__builtins__):
                print("\n", method)

        elif choicemethod == "__cached__":
            print("\nMethod __cached__ is class?", inspect.isclass(urllib.__cached__))
            print("\nMethod __cached__ is callable?", callable(urllib.__cached__))
            for method in dir(urllib.__cached__):
                print("\n", method)

        elif choicemethod == "__doc__":
            print("\nMethod __doc__ is class?", inspect.isclass(urllib.__doc__))
            print("\nMethod __doc__ is callable?", callable(urllib.__doc__))
            for method in dir(urllib.__doc__):
                print("\n", method)

        elif choicemethod == "__file__":
            print("\nMethod __file__ is class?", inspect.isclass(urllib.__file__))
            print("\nMethod __file__ is callable?", callable(urllib.__file__))
            for method in dir(urllib.__file__):
                print("\n", method)

        elif choicemethod == "__loader__":
            print("\nMethod __loader__ is class?", inspect.isclass(urllib.__loader__))
            print("\nMethod __loader__ is callable?", callable(urllib.__loader__))
            for method in dir(urllib.__loader__):
                print("\n", method)

        elif choicemethod == "__name__":
            print("\nMethod __name__ is class?", inspect.isclass(urllib.__name__))
            print("\nMethod __name__ is callable?", callable(urllib.__name__))
            for method in dir(urllib.__name__):
                print("\n", method)

        elif choicemethod == "__package__":
            print("\nMethod __package__ is class?", inspect.isclass(urllib.__package__))
            print("\nMethod __package__ is callable?", callable(urllib.__package__))
            for method in dir(urllib.__package__):
                print("\n", method)

        elif choicemethod == "__path__":
            print("\nMethod __path__ is class?", inspect.isclass(urllib.__path__))
            print("\nMethod __path__ is callable?", callable(urllib.__path__))
            for method in dir(urllib.__path__):
                print("\n", method)

        elif choicemethod == "__spec__":
            print("\nMethod __spec__ is class?", inspect.isclass(urllib.__spec__))
            print("\nMethod __spec__ is callable?", callable(urllib.__spec__))
            for method in dir(urllib.__spec__):
                print("\n", method)

        elif choicemethod == "clear":
            os.system("cls")

        elif choicemethod == "print_again":
            for method in dir(urllib):
                print("\n", method)

        else:
            print("This method in library colorama doesn't exist")
else:
    print("This library can't introspecting")

#____________________________________________________________________

if choicelibrary == "datetime":
    print("\nLibrary datetime is module?", inspect.ismodule(datetime))
    print("Library datetime is callable?", callable(datetime))
    for method in dir(datetime):
        print("\n", datetime)

    while True:
        choicemethod = input("\nWhat method you want to do introspection with?\nIf you want to see again all datetime methods, write print_again\nIf you want to clear console, write clear\n")

        if choicemethod == "MAXYEAR":
            print("\nMethod MAXYEAR is class?", inspect.isclass(datetime.MAXYEAR))
            print("\nMethod MAXYEAR is callable?", callable(datetime.MAXYEAR))
            for method in dir(datetime.MAXYEAR):
                print("\n", method)

        elif choicemethod == "MINYEAR":
            print("\nMethod MINYEAR is class?", inspect.isclass(datetime.MINYEAR))
            print("\nMethod MINYEAR is callable?", callable(datetime.MINYEAR))
            for method in dir(datetime.MINYEAR):
                print("\n", method)

        elif choicemethod == "__all__":
            print("\nMethod __all__ is class?", inspect.isclass(datetime.__all__))
            print("\nMethod __all__ is callable?", callable(datetime.__all__))
            for method in dir(datetime.__all__):
                print("\n", method)

        elif choicemethod == "__builtins__":
            print("\nMethod __builtins__ is class?", inspect.isclass(datetime.__builtins__))
            print("\nMethod __builtins__ is callable?", callable(datetime.__builtins__))
            for method in dir(datetime.__builtins__):
                print("\n", method)

        elif choicemethod == "__cached__":
            print("\nMethod __cached__ is class?", inspect.isclass(datetime.__cached__))
            print("\nMethod __cached__ is callable?", callable(datetime.__cached__))
            for method in dir(datetime.__cached__):
                print("\n", method)

        elif choicemethod == "__doc__":
            print("\nMethod __doc__ is class?", inspect.isclass(datetime.__doc__))
            print("\nMethod __doc__ is callable?", callable(datetime.__doc__))
            for method in dir(datetime.__doc__):
                print("\n", method)

        elif choicemethod == "__file__":
            print("\nMethod __file__ is class?", inspect.isclass(datetime.__doc__))
            print("\nMethod __file__ is callable?", callable(datetime.__doc__))
            for method in dir(datetime.__doc__):
                print("\n", method)

        elif choicemethod == "__loader__":
            print("\nMethod __loader__ is class?", inspect.isclass(datetime.__loader__))
            print("\nMethod __loader__ is callable?", callable(datetime.__loader__))
            for method in dir(datetime.__loader__):
                print("\n", method)

        elif choicemethod == "__name__":
            print("\nMethod __name__ is class?", inspect.isclass(datetime.__name__))
            print("\nMethod __name__ is callable?", callable(datetime.__name__))
            for method in dir(datetime.__name__):
                print("\n", method)

        elif choicemethod == "__package__":
            print("\nMethod __package__ is class?", inspect.isclass(datetime.__package__))
            print("\nMethod __package__ is callable?", callable(datetime.__package__))
            for method in dir(datetime.__package__):
                print("\n", method)

        elif choicemethod == "__spec__":
            print("\nMethod __spec__ is class?", inspect.isclass(datetime.__spec__))
            print("\nMethod __spec__ is callable?", callable(datetime.__spec__))
            for method in dir(datetime.__spec__):
                print("\n", method)

        elif choicemethod == "date":
            print("\nMethod date is class?", inspect.isclass(datetime.date))
            print("\nMethod date is callable?", callable(datetime.date))
            for method in dir(datetime.date):
                print("\n", method)

        elif choicemethod == "datetime":
            print("\nMethod datetime is class?", inspect.isclass(datetime.datetime))
            print("\nMethod datetime is callable?", callable(datetime.datetime))
            for method in dir(datetime.datetime):
                print("\n", method)

        elif choicemethod == "datetime_CAPI":
            print("\nMethod datetime_CAPI is class?", inspect.isclass(datetime.datetime_CAPI))
            print("\nMethod datetime_CAPI is callable?", callable(datetime.datetime_CAPI))
            for method in dir(datetime.datetime_CAPI):
                print("\n", method)

        elif choicemethod == "sys":
            print("\nMethod sys is class?", inspect.isclass(datetime.sys))
            print("\nMethod sys is callable?", callable(datetime.sys))
            for method in dir(datetime.sys):
                print("\n", method)

        elif choicemethod == "time":
            print("\nMethod time is class?", inspect.isclass(datetime.time))
            print("\nMethod time is callable?", callable(datetime.time))
            for method in dir(datetime.time):
                print("\n", method)

        elif choicemethod == "timedelta":
            print("\nMethod timedelta is class?", inspect.isclass(datetime.timedelta))
            print("\nMethod timedelta is callable?", callable(datetime.timedelta))
            for method in dir(datetime.timedelta):
                print("\n", method)

        elif choicemethod == "timezone":
            print("\nMethod timezone is class?", inspect.isclass(datetime.timezone))
            print("\nMethod timezone is callable?", callable(datetime.timezone))
            for method in dir(datetime.timezone):
                print("\n", method)

        elif choicemethod == "timezone":
            print("\nMethod timezone is class?", inspect.isclass(datetime.timezone))
            print("\nMethod timezone is callable?", callable(datetime.timezone))
            for method in dir(datetime.timezone):
                print("\n", method)

        elif choicemethod == "timezone":
            print("\nMethod timezone is class?", inspect.isclass(datetime.timezone))
            print("\nMethod timezone is callable?", callable(datetime.timezone))
            for method in dir(datetime.timezone):
                print("\n", method)

        elif choicemethod == "clear":
            os.system("os")

        elif choicemethod == "print_again":
            for method in dir(datetime):
                print("\n", method)

        else:
            print("This method in library colorama doesn't exist")
else:
    print("This library can't introspecting")
#____________________________________________________________________
