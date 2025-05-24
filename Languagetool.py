# Import the Translator class from the googletrans library
from googletrans import Translator

# Define the main function
def main():
    # Create a translator object
    translator = Translator()

    # Print a list of common language codes for the user
    print("Language Codes:")
    print("English - en")
    print("French - fr")
    print("Spanish - es")
    print("German - de")
    print("Hindi - hi")
    print("Chinese - zh-cn")
    print("Arabic - ar")
    print("Japanese - ja")
    print("Korean - ko")
    print("Russian - ru")
    print("Portuguese - pt")
    print("Italian - it")
    print("----------------------------------")

    # Ask the user to enter text to translate
    text = input("Enter text to translate: ")

    # Ask the user for the target language code from the list
    target_lang = input("Enter target language code from the list above: ")

    # Try to translate the text
    try:
        # Translate the text using the chosen language code
        translated = translator.translate(text, dest=target_lang)

        # Show the original and translated text
        print("\nOriginal: " + text)
        print("Translated (" + target_lang + "): " + translated.text)

    # Show an error message if something goes wrong
    except:
        print("Something went wrong. Please check the language code or your internet connection.")

# Run the main function
main()
