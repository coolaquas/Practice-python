secret_word = "test"
guess = ""
count = 0
guess_limit = 3
out_of_guess = False
while guess != secret_word and not(out_of_guess):
    if count < guess_limit:
        guess = input("Enter A guess : ")
        count += 1
    else:
        out_of_guess = True
count = 0
if out_of_guess:
    print("Ohh! You are out of guess")
else:
    print("Wooh hoo! You have identified the word.")
out_of_guess = False
