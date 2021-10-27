import random
import string
import datetime

domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]


def get_one_random_domain(domains):
    return domains[random.randint(0, len(domains) - 1)]


def get_one_random_name(letters):
    email_name = ""
    for i in range(7):
        email_name = email_name + letters[random.randint(0, 11)]
    return email_name


def generate_random_email():
    one_name = str(get_one_random_name(letters))
    one_domain = str(get_one_random_domain(domains))
    return one_name + "@" + one_domain


def printingLowercase():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))


def printingUppercase():
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(10))


def printingLetters():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(10))


def printingDigits():
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(10))


def printingPunctuation():
    letters = string.punctuation
    return ''.join(random.choice(letters) for i in range(10))


def getGender():
    lst = ["Male", "Female"]
    return random.choice(lst)


def getDob():
    start_date = datetime.date(1950, 1, 1)
    end_date = datetime.date(2003, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%m/%d/%Y")


def getNewsletter():
    lst = ["Your store name", "Test store 2"]
    return random.choice(lst)
