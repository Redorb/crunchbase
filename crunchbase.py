import requests

class NetworkError(RuntimeError):
    def __init__(self, strerror):
        self.strerror = strerror


class crunchbase:
    def __init__(self):

        with open("crunchbase.key") as f:
            self.api_key = f.read()

    def loadJSON(self, query):
        baseURL = "http://api.crunchbase.com/v/2/"
        qURL = baseURL + query + "?user_key=" + self.api_key

        r = requests.get(qURL)
        if r.status_code == 200:
            return r.json
        else:
            s = "HTTP code " + str(r.status_code)
            raise NetworkError(s)

    def getAllOrganizations(self):
        '''Pulls a list of all the organizations in the crunchbase API

        '''
        queryString = "organizations"
        return self.loadJSON(queryString)

    def getOrganizationInfo(self, organizationName):
        '''Pulls the data of the requested organization.

        Keyword arguments:
        companyName -- The company's permalink string.
        '''
        organizationName = organizationName.replace('_', '-').replace(' ', '-')
        queryString = "organization/" + organizationName
        return self.loadJSON(queryString)

    def getAllPeople(self):
        '''Pulls a list of all the people in the crunchbase API

        '''
        queryString = "people"
        return self.loadJSON(queryString)

    def getPersonInfo(self, personName):
        '''Pulls the data of the requested person.

        Keyword arguments:
        personName -- The person's permalink string.
        '''
        personName = personName.replace('_', '-').replace(' ', '-')
        queryString = "person/" + personName
        return self.loadJSON(queryString)

    def getAllProducts(self):
        '''Pulls a list of all the products in the crunchbase API

        '''
        queryString = "products"
        return self.loadJSON(queryString)

    def getProductInfo(self, productName):
        '''Pulls the data of the requested product.

        Keyword arguments:
        productName -- The product's permalink string.
        '''
        productName = productName.replace('_', '-').replace(' ', '-')
        queryString = "product/" + productName
        return self.loadJSON(queryString)

    def getFundingRoundInfo(self, uuid):
        '''Pulls the data of the requested funding round.

        Keyword arguments:
        uuid -- The funding round's uuid string.
        '''
        queryString = "funding-round/" + uuid
        return self.loadJSON(queryString)

    def getAcquisitionInfo(self, uuid):
        '''Pulls the data of the requested acquisition.

        Keyword arguments:
        uuid -- The acquisition's permalink string.
        '''
        queryString = "acquisition/" + uuid
        return self.loadJSON(queryString)

    def getIPO(self, uuid):
        '''Pulls the data of the requested IPO.

        Keyword arguments:
        uuid -- The IPO's uuid string.
        '''
        queryString = "ipo/" + uuid
        return self.loadJSON(queryString)

    def getFundRaiseInfo(self, uuid):
        '''Pulls the data of the requested IPO.

        Keyword arguments:
        uuid -- The Fund Raise's uuid string.
        '''
        queryString = "fund-raise/" + uuid
        return self.loadJSON(queryString)
