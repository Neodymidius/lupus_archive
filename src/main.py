import requests


def main():
    session = requests.Session()
    with open("../resources/password", "r") as f:
        password = f.read()
    print(password)
    session.auth = ("admin", password)

    auth = session.post('http://' + '192.168.178.57')
    response = session.get('http://' + '192.168.178.57' + '/html/recordPlanConfig.htm')
    print(response.text)

if __name__ == '__main__':
    main()