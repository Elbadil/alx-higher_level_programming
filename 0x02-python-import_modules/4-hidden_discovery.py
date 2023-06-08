#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names_hidden = dir(hidden_4)
    for names in names_hidden:
        if names[0] != '_':
            print("{}".format(names))
