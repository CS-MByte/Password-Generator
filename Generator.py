import requests, json, time, os

white = '\033[37m'
red = '\033[31m'

def main():
    try:
        clearScreen()
        numPass = input(white + '\nHow Many Passwords Would You Like To Generate? ')
        url = 'https://www.passwordrandom.com/query?command=password&format=json&count=' + numPass
        get = requests.get(url)
        request = json.loads(get.content)
        clearScreen()

        print(white + '\nGenerated Passwords Are Below.')
        print(request['char'])

        doNext = input(white + '\nWould You Like To Run Again? (Y/N): ')

        if doNext.upper() == 'Y'.upper():
            main()
        else:
            clearScreen()
            print(red + '\nClosing' + white + '...')
            time.sleep(1)
            clearScreen()
            exit(0)

    except KeyboardInterrupt:
        clearScreen()
        print(red + '\nClosing' + white + '...')
        time.sleep(1)
        clearScreen()
        exit(0)

def clearScreen():
    os.system('cls')

if __name__ == '__main__':
    main()
