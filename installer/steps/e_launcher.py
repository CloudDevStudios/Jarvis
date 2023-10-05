from helper import *
from os.path import expanduser, exists
import unix_windows

# TODO Windows Install options?
if unix_windows.IS_WIN:
    fw = open('jarvis.bat', 'w')
    fw.write("""\
@ECHO off
CALL "{JARVISPATH}\\env\\Scripts\\activate.bat"
python "{JARVISPATH}\\jarviscli" %*
    """.format(JARVISPATH=os.getcwd()))
    section("FINISH")

    printlog("Installation Successful! Use 'jarvis' in cmd to start Jarvis!")
else:

    section("Write Jarvis starter")

    JARVIS_MACRO = """\
#!/bin/bash
source "{PATH}/env/bin/activate"
python "{PATH}/jarviscli" "$@"
    """

    with open('jarvis', 'w') as fw:
        fw.write(JARVIS_MACRO.format(PATH=os.getcwd()))
    shell('chmod +x jarvis').should_not_fail()
    # get the SHELL of the current user
    user_shell = get_default_shell()
    _do_nothing_str = "Do nothing (Call Jarvis by full path)"
    install_options = [("Install jarvis /usr/local/bin starter (requires root)", 0), ]
    if user_shell in SUPPORTED_SHELLS:
        install_options += [
            (f"Add {os.getcwd()} to $PATH (.{user_shell}rc)", 1),
            (_do_nothing_str, 2),
        ]
    else:
        install_options += [
            (_do_nothing_str, 1)
        ]
    selection = user_input(install_options)

    if selection == 0:
        os.system('sudo cp jarvis /usr/local/bin')
    elif selection == 1 and user_shell in SUPPORTED_SHELLS:
        line_to_add = f'export PATH="$PATH:{os.getcwd()}"'
        shell_rc = f'{expanduser("~")}/.{user_shell}rc'

        if not os.path.exists(shell_rc):
            print(f"NO .{user_shell}rc found!")
        else:
            line_already_exists = False

            fr = open(shell_rc)
            for line in fr:
                if line.startswith(line_to_add):
                    line_already_exists = True

            if line_already_exists:
                print(f"Jarvis path already added to $PATH in .{user_shell}rc!")
            else:
                with open(shell_rc, 'a') as fw:
                    fw.write(line_to_add)
                    fw.write('\n')
    printlog('\n\nInstallation complete. Try using Jarvis!')
    if selection == 0 or (selection == 1 and user_shell in SUPPORTED_SHELLS):
        printlog('$ jarvis')
    else:
        printlog(f'$ {os.getcwd()}/jarvis')
