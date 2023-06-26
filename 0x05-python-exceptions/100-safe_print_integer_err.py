#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise Exception

    except Exception:
        print("Exception: Unknown format code 'd' for object\
 of type 'str'", file=sys.stderr)
        return False
