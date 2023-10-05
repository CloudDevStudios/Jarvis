from colorama import Fore
import re
import random
from utilities.textParser import parse_number
from plugin import plugin


@plugin('roll')
class Roll():
    """
    Roll a dice
    -- Example:
        Roll a dice
        Roll four dices with 16 edges
        Roll 5 dices five times
    """

    def __call__(self, jarvis, s):
        config = self._dice_parse(s)

        if error := self._dice_is_error_in_config(config):
            jarvis.say(error, Fore.RED)
            return

        for roll in self._dice_roll(config):
            result = "|" + "| |".join(roll) + "|"
            border = re.sub(r"\S", "-", result)

            jarvis.say(border, Fore.BLUE)
            jarvis.say(result, Fore.BLUE)
            jarvis.say(border + '\n', Fore.BLUE)

    def _dice_parse(self, s):
        repeat = 1
        howmany = 1
        edges = 6

        prefix = ""
        prefix_length = 0
        prefix_number = -1

        # Iterate string.
        # Search for number before keywords (edges, times, dices)
        for word_current in s.split():
            parse_result = parse_number(prefix)

            # make sure, prefix still contains only number-characters
            if parse_result[0] != prefix_length:
                # last token not part of number -> reset prefix
                prefix = word_current
                prefix_length = 1
                continue
            prefix_number = parse_result[1]

            if word_current in ["edge", "edges"]:
                edges = prefix_number

            if word_current == "dices":
                howmany = prefix_number

            elif word_current == "times":
                repeat = prefix_number

            prefix += " "
            prefix += word_current
            prefix_length += 1

        return {"repeat": repeat, "howmany": howmany, "edges": edges}

    def _dice_is_error_in_config(self, config):
        assert isinstance(config["edges"], int)
        assert isinstance(config["howmany"], int)
        assert isinstance(config["repeat"], int)

        if config["howmany"] == 0:
            return "No dice to roll?"
        if config["howmany"] < 0:
            return f'Rolling {config["howmany"]} dices does not really make sense ;).'
        if config["repeat"] == 0:
            return "Roll 0 howmany? Finish!"
        if config["repeat"] < 0:
            return f'Doing something {config["repeat"]} does not really make sense ;).'
        if config["edges"] <= 1:
            return f'A dice with {config["edges"]} edges does not really make sense ;).'

        return False

    def _dice_roll(self, config):
        for _ in range(config["repeat"]):
            yield [str(random.randint(1, config["edges"])) for _ in range(config["howmany"])]
