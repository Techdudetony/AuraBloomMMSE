# MMSE Self-Assessment Quiz

def main():
    print("Welcome to the Self-Assessment Quiz!")
    print("This quiz is inspired by the MMSE and is for educational purposes only.")
    print("It is not a diagnostic tool. If you have concerns, consult a professional.\n")

    score = 0  # Initialize score
    max_score = 30  # Total possible score

    # Orientation Section
    print("### Orientation Section ###")
    day_question = input("What day of the week is it? ").strip().lower()
    correct_day = "monday"  # Adjust to match the actual day when deployed
    if day_question == correct_day:
        print("Correct! You're aware of the day.")
        score += 1
    else:
        print("That's okay. Awareness of time can vary.")

    city_question = input("What city are you currently in? ").strip().lower()
    correct_city = "new york"  # Replace with appropriate location for the user
    if city_question == correct_city:
        print("Correct! You're aware of your location.")
        score += 1
    else:
        print("That's okay. Awareness of place can vary.\n")

    # Registration (Memory) Section
    print("### Registration Section ###")
    words_to_remember = ["apple", "car", "book"]
    print("Remember these three words: Apple, Car, Book.")
    input("Press Enter when you're ready to continue...\n")  # Pause to let the user memorize
    repeat_words = input("Please repeat the three words: ").strip().lower().split(", ")
    if repeat_words == words_to_remember:
        print("Excellent memory!")
        score += 3
    else:
        print("Good try! We'll revisit these words later.\n")

    # Attention and Calculation Section
    print("### Attention and Calculation Section ###")
    print("Start with 100 and subtract 7 repeatedly.")
    numbers = [100, 93, 86, 79, 72, 65]
    for i in range(len(numbers) - 1):
        user_number = int(input(f"What is {numbers[i]} - 7? ").strip())
        if user_number == numbers[i + 1]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {numbers[i + 1]}.")

    print("\nNow, spell the word 'WORLD' backward.")
    spell_word = input("Your answer: ").strip().lower()
    if spell_word == "dlrow":
        print("Great focus and problem-solving!")
        score += 1
    else:
        print("That's okay. Let's continue.\n")

    # Recall Section
    print("### Recall Section ###")
    recall_words = input("What were the three words I asked you to remember earlier? ").strip().lower().split(", ")
    recall_score = sum(1 for word in recall_words if word in words_to_remember)
    if recall_score > 0:
        print(f"You remembered {recall_score} word(s). Good effort!")
    else:
        print("No worries! Memory is something we can strengthen.")
    score += recall_score

    # Language Section
    print("### Language Section ###")
    print("Read and follow this instruction: 'Close your eyes.'")
    input_action = input("Type 'done' once you have completed the instruction: ").strip().lower()
    if input_action == "done":
        print("Good job! Your comprehension is strong.")
        score += 1
    else:
        print("That's okay. Let's move on.")

    print("What is this object called? (Hint: It's something you write with)")
    object_name = input("Your answer: ").strip().lower()
    if object_name == "pen":
        print("Correct!")
        score += 1
    else:
        print("That's okay. Let's continue.\n")

    # Final Score and Feedback
    print("### Final Score ###")
    print(f"Your final score is: {score}/{max_score}")
    if score >= 25:
        print("Great cognitive performance! Keep up the good work.")
    elif 20 <= score < 25:
        print("Good job! Some areas might need attention.")
    else:
        print("Consider reaching out to a professional for additional support.")

    # Replay Option
    retry = input("\nWould you like to try the quiz again? (yes/no): ").strip().lower()
    if retry == "yes":
        main()
    else:
        print("Thank you for taking the Self-Assessment Quiz! Remember, mental health matters.")

# Run the quiz
if __name__ == "__main__":
    main()
