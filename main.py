import requests
import logging
from Client import Client



def main():
    client = Client("https://api.onboarddata.io/")
    client.check()

if __name__ == "__main__":
    main()
