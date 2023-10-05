import os
from plugin import plugin, require


@require(native='wmctrl')
@plugin("go to")
def go_to(jarvis, s):
    os.system(f"wmctrl -a {s}")


@require(native='wmctrl')
@plugin("workspace")
def workspace(jarvis, s):
    if s == 'one':
        s = 1
    num = str(int(s) - 1)
    os.system(f"wmctrl -s {num}")


@plugin("run")
def run(jarvis, s):
    """
    Run commands in terminal(use shell)
    e.g. run echo hello
    """
    os.system(s)
