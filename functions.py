import urllib.request

def ask_confirmation(prompt, retries = 4, reminder = "Please try again!"):
    while True:
        response = input(prompt + ' ')
        if response in ('y', 'ye', 'yes'):
            return True
        if response in ('n', 'no', 'nop'):
            return False
        retries -= 1
        if retries == 0:
            raise ValueError("Invalid user response.")
        print(reminder)

try:
    if ask_confirmation("Do you want to learn Python?"):
        print("Awesome! You'll love Python!")
    else:
        print("Oh, too bad...")
except ValueError:
    print("Error")

# What's new in Python 3.6
name, age = "Abner", 26
print(f"Your name is {name} and you are {age} years old.")

request = request('viacep.com.br/ws/01001000/json/')
try:
	response = urlopen(request)
	kittens = response.read()
	print(kittens[559:1000])
except URLError:
    print('No kittez. Got an error code:')