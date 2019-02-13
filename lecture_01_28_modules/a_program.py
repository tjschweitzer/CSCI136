# import with rename for syntactic convenience
import lecture_01_28_modules.some_lib as foo

# alternate "from" syntax
from lecture_01_28_modules.some_lib import a_library_fn


def main():
    foo.a_library_fn()
    a_library_fn()


# only run code directly when this is the file that was invoked
if __name__ == '__main__':
    print("I'm in main!")
    main()
