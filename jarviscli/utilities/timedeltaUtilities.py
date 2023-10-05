import datetime

class Timedelta_utilities:

    def format_time_delta(self) -> str:
        """
        Function takes timedelta and puts it into textual format
        """

        remaining_secs = self.seconds % 3600
        time_dict = {
            'days': self.days,
            'hours': int(self.seconds / 3600),
            'minutes': int(remaining_secs / 60),
            'seconds': remaining_secs % 60,
        }

        new_timedict = {}
        # create new dictionary with the keys being the right numeric textual value
        for element, value in time_dict.items():
            if value == 1:
                new_timedict[element[:-1]] = time_dict[element]
            else:
                new_timedict[element] = time_dict[element]

        # store keys and values in a list
        # for easier access
        measures = list(new_timedict.keys())
        values = list(new_timedict.values())

        timedelta = ''.join(f'{values[i]} {measures[i]}, ' for i in range(len(values)))
        # ignore the last 2 characters ', '
        return timedelta[:-2]