
import sys
from lib.accepts import accept
from lib.requests import request

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) >1:
        argument = arguments[1]
        if argument == "accept":
            accept()
        elif argument == 'request':
            search = arguments[2]
            request(search)
        elif argument == "-h":
            print("Options and arguments:")
            print("")
            print("accept     :  accept all the available request")
            print("request     :  send request")
            print("to request you need to provide name or designation")
            print("***** python linkedin.py request programmer *****")
            print("add number of person you want to send request (optional) default(first page)")
            print("***** python linkedin.py request programmer 5 *****")

        else:
            print("Unknown option: ", argument)
            print("Try `python linkedin.py -h' for more information.: ")
    else:
        print("Try `python linkedin.py -h' for more information.: ")
        sys.exit()



