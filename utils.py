import random
feet_in_mile = 5280.00
meters_in_kilometer = 1000
beatles = ["Jhon Lennon", "Paul McCartney"]


def get_file_ext(filename):
    return filename[filename.index(".")+1:]


def role_dice(num):
    return random.randint(1, num)
