import random

# List of words
words = ["python", "apple", "banana", "grapes", "orange"]
word = random.choice(words)

guessed_letters = []
tries = 6

# 🎁 Pick ONE random letter from the word as initial hint
hint_letter = random.choice(word)
guessed_letters.append(hint_letter)

print("🤣🎉 WELCOME TO HANGMAN 🎉🤣")
print(f"❤️ Lives: {tries}")

while tries > 0:
    display_word = ""

    # Build display with guessed letters (including the hint)
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "-"  # hidden letters

    print("\n🧩 Word:", display_word)  # only shows ---a--- style

    # Check if player has won
    if "-" not in display_word:
        print("🎉🎉 YOU WON!!! 🎉🎉")
        print("🕺 The hangman dances 💃")
        break

    # Ask for user guess
    guess = input("🔤 Guess a letter: ").lower()

    if len(guess) != 1:
        print("🤨 ONE letter only!")
        continue

    if guess in guessed_letters:
        print("😑 Already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("😎 Correct!")
    else:
        tries -= 1
        print("💀 WRONG!")
        print(f"❤️ Lives left: {tries}")

        if tries == 3:
            print("⚠️ He’s nervous 😰")
        elif tries == 1:
            print("🚨 LAST LIFE! 🔥")

# Lose condition
if tries == 0:
    print("\n💀💀 GAME OVER 💀💀")
    print(f"😭 The word was: {word}")
