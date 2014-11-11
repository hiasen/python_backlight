import argparse
from backlight import *

def create_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("brightness", type=int)
    parser.add_argument("--percent", action="store_true", default=False)
    parser.add_argument("--keyboard", action="store_true", default=False)
    return parser

def main(args):
    parser = create_argument_parser()
    parsed = parser.parse_args(args)

    if parsed.keyboard:
        bb = Brightness(folder="/sys/devices/platform/asus-nb-wmi/leds/asus::kbd_backlight")
    else:
        bb = Brightness()

    if parsed.percent:
        bb.percent_brightness = parsed.brightness
    else:
        bb.brightness = parsed.brightness

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
