"""Jermaine"""
def main():
    get_password = input('Please enter your password:')
    get_password = list(get_password)
    display_password = '*' * len(get_password)
    print(display_password)
main()