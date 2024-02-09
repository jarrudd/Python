# response_parser.py
class ResponseParser:
    @staticmethod
    def parse_set_cookie_header(set_cookie_header):
        auth_token_atmosphere = set_cookie_header.split('AtmoAuthToken_atmosphere=')[1].split(';')[0]
        csrf_token_atmosphere = set_cookie_header.split('Csrf-Token_atmosphere=')[1].split(';')[0]
        return auth_token_atmosphere, csrf_token_atmosphere