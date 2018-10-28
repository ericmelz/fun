from random import shuffle


numpicks = 20

excluded_mains = {3, 21, 45, 53, 56}

excluded_megas = {22}



def mains(max_number):
    nums = list(set(range(1, max_number + 1)) - excluded_mains)
    shuffle(nums)
    return ['%02d' % x for x in sorted(nums[:5])]


def mega(max_number):
    nums = list(set(range(1, max_number + 1)) - excluded_megas)
    shuffle(nums)
    return '%02d' % nums[0]


def print_picks(lotto_type):
    max_main, max_mega = -1, -1
    if lotto_type == 'powerball':
        max_main = 69
        max_mega = 26
    elif lotto_type == 'mega':
        max_main = 70
        max_mega = 25
    for _ in range(0, numpicks):
        print('%s   %s' % (' '.join(mains(max_main)), mega(max_mega)))


def powerball():
    print_picks('powerball')


def mega_millions():
    print_picks('mega')


powerball()
