# input_handler.py

from color import Color

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

    @staticmethod
    def get_api_url_details():
        condition_met = False
        while not condition_met:
            details_api_url = input(f"Please enter the API Details URL: \n \t Example: "
                                    f"http://cent7spt21-01.akana.roguewave.com:9900/akanaportal/#/api/d55bd030-a64b-429e-931c-e19204a66851.akanaportal/versions/aad820ab-044c-454f-bfa5-25f8c5757165.akanaportal/specifics\n")
            print(f"\nAPI Details URL is: " + str(details_api_url))

            api_VersionId = details_api_url.split('versions/')[1].split('/')[0]
            print(f"\nThe API ApiVersionID is: " + Color.BLUE + str(api_VersionId) + Color.END)

            api_ApiId = details_api_url.split('api/')[1].split('/')[0]
            print(f"The API ID (APIID) is: " + Color.BLUE + str(api_ApiId) + Color.END)

            yesno_input = input("\nAre these details correct Y or N? ")
            if yesno_input.lower() == "y":
                condition_met = True
            else:
                print("Please try again.\n")

        return api_VersionId, api_ApiId