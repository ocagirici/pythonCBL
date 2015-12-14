import sys
import re

# diag_selector = re.compile(".*")
diag_selector = re.compile("nothing")
diag_stream = sys.stdout

def diag_select(pattern):
    """Set regexp pattern to filter which messages are printed.""" 
    global diag_selector 
    diag_selector = re.compile(pattern)

def diag_direct(stream):
    """set stream to which messages are printed"""
    global diag_stream
    diag_stream = stream

def diag_print(str, code=''):
    global diag_selector
    global diag_stream
    if diag_selector.match(code):
        diag_stream.write(str)
        diag_stream.write("\n")


def _gen_messages():
    diag_print("Message 1")
    diag_print("Message 2", "group1")
    diag_print("Message 3", "group1")
    diag_print("Message 4", "group2")
    diag_print("Message 5", "gerror")


