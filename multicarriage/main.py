class MultiCarriage:
    def __init__(self, txt: str, lineno: int, dropno: int = None, clearline=False, flushtxt=False):
        self.txt = txt
        self.lineno = lineno
        self.dropno = dropno
        self.clearline = clearline
        self.flushtxt = flushtxt
    def lineup(no):
        return "\x1b[{}A".format(no)
    def linedown(no):
        return "\x1b[{}B".format(no)
    def lineerase():
        return "\x1b[2K"
    def write(txt: str, lineno: int, dropno: int = None, clearline=False, flushtxt=False):
        if not isinstance(dropno, int) and dropno != None:
            raise ValueError("'dropno' must be type integer")
        if clearline:
            print(f"{MultiCarriage.lineup(lineno)}{MultiCarriage.lineerase()}\r", end='', flush=flushtxt)
        else:
            print(f"{MultiCarriage.lineup(lineno)}\r", end='', flush=flushtxt)
        print(txt, end='', flush=flushtxt)
        if dropno == None:
            print(f"{MultiCarriage.linedown(lineno)}{MultiCarriage.lineerase()}\r", end='', flush=flushtxt)
        else:
            print(f"{MultiCarriage.linedown(dropno)}{MultiCarriage.lineerase()}\r", end='', flush=flushtxt)
    def create_newline(no: int = 1):
        print("\n"*no, end='')
