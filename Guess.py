secret_word = "giraffe"
guess = ""
tries = 0
tries_limit = 3
out_of_tries = False

while guess != secret_word and not (out_of_tries):
    if tries < tries_limit:
        guess = input("Guess the secret word: ")
        tries += 1
    else:
        out_of_tries = True

if out_of_tries:
    print("You're out of tries bucko.")
else:
    print("YOU WIN BUCKO!")
       
   
    

