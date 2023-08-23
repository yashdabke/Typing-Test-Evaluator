import time
import random

# List of phrases for typing test
# Add more complex phrases to the list for better results
phrases = [
    "The quick brown fox jumps over the lazy dog",
    "To be or not to be, that is the question",
    "In the middle of difficulty lies opportunity",
    "Coding is the language of the future",
    "Success is walking from failure to failure with no loss of enthusiasm"
]

def create_box():
    # Display the test title and instructions
    print("+--------------------------------------------------------+")
    print("|                  Typing Speed Test                     |")
    print("+--------------------------------------------------------+")
    print()
    print("Enter the following phrase as fast as possible and with accuracy:")

def calculate_accuracy(input_words, correct_words):
    # Calculate accuracy based on correct words in the input
    if not input_words:
        return 0
    return len(correct_words) / len(input_words)

def display_result(words_typed, time_taken, accuracy):
    # Show the user's results: words typed, time, and accuracy
    print("\nResults:")
    print("Total words typed:", words_typed)
    print("Time taken:", round(time_taken, 2), "seconds")
    print("Accuracy:", round(accuracy * 100, 2), "%")

def main():
    while True:
        phrase = random.choice(phrases)
        create_box()
        print(phrase, "\n")

        input("Press Enter to start...")  # Wait for user input
        start_time = time.time()
        user_input = input()  # Get user's typed input
        end_time = time.time()

        input_words = user_input.split()
        correct_words = [w for w in input_words if w in phrase]

        accuracy = calculate_accuracy(input_words, correct_words)
        time_taken = end_time - start_time
        words_per_minute = (len(input_words) / 5) / (time_taken / 60)

        display_result(len(input_words), time_taken, accuracy)
        print("Speed:", round(words_per_minute, 2), "words per minute")

        if accuracy > 0.8:
            score = int(words_per_minute * accuracy)
            print("Congratulations! Your score:", score)
        else:
            print("Keep practicing for better accuracy!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            time.sleep(1.5)
            break

if __name__ == "__main__":
    main()
