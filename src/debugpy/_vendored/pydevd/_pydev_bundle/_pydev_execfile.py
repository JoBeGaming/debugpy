# We must redefine it in Py3k if it's not already there
def execfile(file, globalns=None, localns=None):
    if globalns is None:
        import sys

        globalns = sys._getframe().f_back.f_globals
    if localns is None:
        localns = globalns

    import tokenize

    with tokenize.open(file) as stream:
        contents = stream.read()

    # execute the script (note: it's important to compile first to have the filename set in debug mode)
    exec(compile(contents + "\n", file, "exec"), globalns, localns)
