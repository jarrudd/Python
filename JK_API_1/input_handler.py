# input_handler.py
class InputHandler:
    @staticmethod
    def get_validated_url():
        condition_met = False
        while not condition_met:
            url_input = input(f"Please enter CM Login URL: \n \t Example: http://cent7spt21-01.akana.roguewave.com:9900\n")
            print(f"\nCM Login URL is: " + str(url_input))
            yesno_input = input("\nIs this URL correct Y or N? ")
            if yesno_input.lower() == "y":
                condition_met = True
            else:
                print("Please try again.\n")
        return url_input

    @staticmethod
    def get_validated_credentials():
        condition_met = False
        while not condition_met:
            user_input = input("\nWhat is your Username? ")
            pass_input = input("What is your Password? ")
            print(f"\nUsername is: {user_input}\nPassword is: {pass_input}")
            yesno_input = input("\nAre these credentials correct Y or N? ")
            if yesno_input.lower() == "y":
                condition_met = True
            else:
                print("Please try again.\n")
        return user_input, pass_input