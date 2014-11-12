import os


class Brightness(object):

    def __init__(self, folder="/sys/class/backlight/intel_backlight"):
        self.folder = folder

        with open(os.path.join(folder, "max_brightness")) as f:
            self.max_brightness = int(f.read())

    @property
    def brightness(self):
        with open(self._brightness_file()) as f:
            return int(f.read())

    @brightness.setter
    def brightness(self, number):
        if not (0 <= number <= self.max_brightness):
            raise ValueError("Brightness must be between 0 and {}"
                             .format(self.max_brightness))
        with open(self._brightness_file(), 'w') as f:
            f.write(str(number))

    def _brightness_file(self):
        return os.path.join(self.folder, "brightness")

    def __str__(self):
        return str(self.brightness)

    @property
    def percent_brightness(self):
        return (self.brightness*100)//self.max_brightness

    @percent_brightness.setter
    def percent_brightness(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("Percent_brightness must be between 0 and 100")
        self.brightness = (percent*self.max_brightness)//100

    def set_max(self):
        self.percent_brightness = 100
