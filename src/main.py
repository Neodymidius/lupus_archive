import requests


def main():
    session = requests.Session()
    with open("../resources/password", "r") as f:
        password = f.read()
    print(password)
    session.auth = ("admin", password)

    auth = session.post('http://' + hostname)
    response = session.get('http://' + hostname + '/rest/applications')


if __name__ == '__main__':
    main()