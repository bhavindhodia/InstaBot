import json
from numpy.random import choice
from helper import TextWrap
from configVars import FONT,QUOTE_WRAP_SIZE
from requests import get,exceptions

class Quote:

    def __init__(self):
        pass

    def getData(self,url):

        """ Get JSON data from URL   """

        try:
            req = get(url)
            print("\n #### Response Status #### \n",req.status_code)
            return req.json()
        except exceptions.Timeout:
            print("\n #### Server Timeout #### \n")

        except exceptions.TooManyRedirects:
            print("\n #### Bad URL #### \n")
        except exceptions.RequestException as e:
            print("\n #### I Quit  #### \n")
            raise SystemExit(e)


    def getZenQuote(self):

        """ Fetch Data from ZEN QUOTES  """

        print("\n ****** FETCHING ZEN DATA ******")
        req_url = "https://zenquotes.io/api/random"
        data = self.getData(req_url)
        print("QUOTE IS => {0} \n ".format(data[0]['q']))
        return data[0]['q']

    def getForismatic(self):

        """ Fetch Data from FORISMATIC QUOTES  """

        print("\n ****** FETCHING FORISMATIC DATA ******")
        req_url = "http://api.forismatic.com/api/1.0/?lang=en&method=getQuote&format=json"
        data = self.getData(req_url)
        print("QUOTE IS => {0} \n ".format(data['quoteText']))
        return data['quoteText']

    def getRandomQuote(self):
        
        """ Make a Random choice to get data from websites  """

        allquotes = [self.getZenQuote,self.getForismatic]

        # Define Porbabilty to fetch more data from FORISMATIC
        randomQuote = choice(allquotes,p=(.9,.1))

        return randomQuote()

    def quoteLines(self):

        txt = self.getRandomQuote()
        quoteWrap =  TextWrap(txt,FONT,QUOTE_WRAP_SIZE)
        # print('quoteWrap',quoteWrap,"  = >",len(quoteWrap[0]))
        # If Legth of Quote Greater than 8 lines Fetch Again
        while (len(quoteWrap[0]) >= 8):
            print("\n ******** REFETCHING ******** \n  " )
            txt = self.getRandomQuote()
            quoteWrap = TextWrap(txt,FONT,QUOTE_WRAP_SIZE)

        
        return quoteWrap