# main.py
from color import Color
from input_handler import InputHandler
from response_parser import ResponseParser
from post_login_api import APIClient

# Declare global variables
url_input = None
api_client = None
user_input = None
pass_input = None
response = None

set_cookie_header = None
auth_token = None
csrf_token = None

api_VersionId = None
api_ApiId = None


##########################################################################################################

def case1():
    print("1. Currently loaded variables. (Selection 1):")

    print(f"\nCM Login URL is: " + str(url_input))

    print(f"\nUsername is: " + Color.GREEN + str(user_input) + Color.END)
    print(f"Password is: " + Color.GREEN + str(pass_input) + Color.END + '\n')

    print('AtmoAuthToken_atmosphere:', Color.RED + str(auth_token) + Color.END)
    print('Csrf-Token_atmosphere:', Color.RED + str(csrf_token) + Color.END + '\n')

    print(f"The API version ID (ApiVersionID) is: " + Color.BLUE + str(api_VersionId) + Color.END)
    print(f"\tCM > API > Details > URL > between /version/ ... /specifics")
    print(f"The API ID (APIID) is: " + Color.BLUE + str(api_ApiId) + Color.END)
    print(f"\tCM > API > Details > URL > between /api/ ... /versions/\n")

def case2():
    global url_input, api_client, user_input, pass_input, response, set_cookie_header, auth_token, csrf_token

    print("2. To Execute login API (Selection 2):")

    if not (url_input or user_input or pass_input):
        if __name__ == "__main__":
            url_input = InputHandler.get_validated_url()
            api_client = APIClient()
            user_input, pass_input = InputHandler.get_validated_credentials()
            response = api_client.login(url_input, user_input, pass_input)

            if response.status_code == 200:
                print('POST request was successful.')
                set_cookie_header = response.headers.get('Set-Cookie')
                if set_cookie_header:
                    auth_token, csrf_token = ResponseParser.parse_set_cookie_header(set_cookie_header)
                    print('AtmoAuthToken_atmosphere:', Color.RED + auth_token + Color.END)
                    print('Csrf-Token_atmosphere:', Color.RED + csrf_token + Color.END + '\n')
                else:
                    print('Set-Cookie header not found in the response.')
            else:
                print('POST request failed with status code:', response.status_code)

            print('Response:', response.text)

    else:
        yesno_input = input("\nDo you need to re-input the User/pass and URL? Y or N? ")
        if yesno_input.lower() == "y":
            if __name__ == "__main__":
                url_input = InputHandler.get_validated_url()
                api_client = APIClient()
                user_input, pass_input = InputHandler.get_validated_credentials()
                response = api_client.login(url_input, user_input, pass_input)

                if response.status_code == 200:
                    print('POST request was successful.')
                    set_cookie_header = response.headers.get('Set-Cookie')
                    if set_cookie_header:
                        auth_token, csrf_token = ResponseParser.parse_set_cookie_header(set_cookie_header)
                        print('AtmoAuthToken_atmosphere:', Color.RED + auth_token + Color.END)
                        print('Csrf-Token_atmosphere:', Color.RED + csrf_token + Color.END + '\n')
                    else:
                        print('Set-Cookie header not found in the response.')
                else:
                    print('POST request failed with status code:', response.status_code)

                print('Response:', response.text)

        else:
            response = api_client.login(url_input, user_input, pass_input)

            if response.status_code == 200:
                print('POST request was successful.')
                set_cookie_header = response.headers.get('Set-Cookie')
                if set_cookie_header:
                    auth_token, csrf_token = ResponseParser.parse_set_cookie_header(set_cookie_header)
                    print('AtmoAuthToken_atmosphere:', Color.RED + auth_token + Color.END)
                    print('Csrf-Token_atmosphere:', Color.RED + csrf_token + Color.END + '\n')
                else:
                    print('Set-Cookie header not found in the response.')
            else:
                print('POST request failed with status code:', response.status_code)

            print('Response:', response.text)



def case3():

    global api_VersionId, api_ApiId

    print("3. To Add an API Details URL (Selection 3)")

    api_VersionId, api_ApiId = InputHandler.get_api_url_details()




def default_case():
    print("Invalid option. Please try again.")


# Define your switch cases as functions
cases = {
    '1': case1,
    '2': case2,
    '3': case3
}

# Main loop
while True:
    print("*" * 100 + '\n')

    print("Select an option:")
    print("1. To preview loaded variables, select 1:")
    print("2. To execute login API, select 2:")
    print("3. To Add Related API URL, select 3:")
    print("0. Exit")

    choice = input("Enter your choice: ")

    print("*" * 100 + '\n')

    if choice == '0':
        print("Exiting...")
        break

    # Execute the selected case function or the default case if the choice is not in the cases dictionary
    cases.get(choice, default_case)()

##########################################################################################################
