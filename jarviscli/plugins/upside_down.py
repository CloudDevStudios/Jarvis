from plugin import plugin
from colorama import Fore


@plugin('upside down')
def generate_random_list(jarvis, str):
    user_input = jarvis.input("Enter string to be converted to upside-down (only english letters will be converted): ")
    result = convert_input(jarvis, user_input)
    jarvis.say(result, Fore.GREEN)


def convert_input(jarvis, u_input):
    upside_str = 'zʎxʍʌnʇsɹbdouɯןʞſıɥbɟǝpɔqɐ'
    normal_str = 'abcdefghijklmnopqrstuvwxyz'
    upside_str = upside_str[::-1]
    converter_dict = dict(zip(normal_str, upside_str))
    result = ''.join(
        converter_dict[letter]
        for letter in u_input
        if letter in converter_dict
    )
    return result[::-1]
