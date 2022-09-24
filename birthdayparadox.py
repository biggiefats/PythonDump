import datetime
import random


def getBirthdays(numberOfBirthdays):
    # Returns a list of number random date objects for birthdays

    birthdays = []

    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)

        # datetime.date creates an imaginary date in the form YYYY/MM/DD
        # using the datetime module

        # In the case of this simulation of the phenomena,
        # the year does not matter as long
        # as birthdays have the same year

        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))

        # datetime.timedelta used for manipulation of dates
        # and finding the difference in dates

        # Get a random day into the year

        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    # Returns the date object of a birthday that
    # occurs more than once in the birthdays list

    if len(birthdays) == len(set(birthdays)):
        return None

    # All birthdays are unique, so return None

    # That's if the length of birthdays
    # is the same length as
    # the length of the birthdays in a set

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday

    # The enumerate() method adds a counter to an iterable (meaning loop)
    # and returns it (the enumerate object).

    # Turns something like ('Cool'), ('Not Cool')
    # into (0, 'Cool') , (1, 'Not Cool')


print(''' The Birthday Paradox shows us that in a group of N people, the odds
 that two of them have matching birthdays is surprisingly large.
 This program does a Monte Carlo simulation (that is, repeated random
 simulations) to explore this concept.
 
 (It's not actually a paradox, it's just a surprising result.)
  ''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (1 - 100)')

    # Asks user for No. of birthdays that shall be generated

    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        #  If the response is not a decimal value
        #  and if the response is bigger than 0
        #  but less than or equal to 100,

        numBDays = int(response)
        break

        # Since the user has entered a valid amount,
        # we can break out of the loop

print()

print('Here are {} birthdays: '.format(numBDays))
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):

    if i != 0:
        print(',', end='')

        # Display a comma after each birthday
        # After the first birthday

    monthName = MONTHS[birthday.month - 1]

    # -1 keeps tuple index in range
    # so that no IndexError occurs

    dateText = '{} {}'.format(monthName, birthday.day)

    # Formats dates like: 'Jan 17' or 'Aug 23'

    print(dateText, end='')
print()
print()

match = getMatch(birthdays)
# Determine if there are two birthdays that match

print('In this simulation, ', end='')

if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)

    # Shows that multiple people have the same
    # birthday in this unusual phenomena

else:
    print('there are no matching birthdays.')

print()
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')
print('Let\'s run another 100,000 simulations.')

# Backslash allow an apostrophe to be used
# within quotation marks

simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')

        # Reports to user per every 10,000 simulations on the progress

    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1

    # If two birthdays are the same,
    # record that statistic in the variable 'simMatch',
    # adding 1 to it per match

print('All 100,000 simulations run.')

probability = round(simMatch/100_000 * 100, 2)

# Calculates the percentage of matched birthdays to birthdays
# in this specific simulation

# The '2' that is separated from the calculation
# of the probability (variable) allows
# a decimal to be represented to 2dp

print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
