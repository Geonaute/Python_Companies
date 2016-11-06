def testmakeypscompanies():
        SearchesSource = open('SearchList.csv', 'rt')
        Companies = makeypscompanies(SearchesSource)
        print(str(len(Companies)) + ' Companies created')
        return Companies

def makeypscompanies(SearchesSource):
    from csv import reader
    #from time import sleep
    companies = {}
    
    reader = reader(SearchesSource)
    for row in reader:
        x = makeypcompanies(row[0],row[1],row[2])
        companies = {**x, **companies}
        #sleep(1)
    return companies

def makeypcompanies(Search, City, State):
    from cCompany import Company
    from fSoupIt import soupit
    companies = {}
    try:
        source = soupit('http://www.yellowpages.com/search?search_terms=' + Search + '&geo_location_terms=' + City + '+%2C+' + State)
    except:
        return companies
        print('No companies were found')
    

    #x = source.findAll('span', {'class' : 'street-address' })
    x = source.findAll('div', {'class' : 'info'})
    for c in x:
        company = Company(c.find('a', {'class' : 'business-name'}).string)
        try:
                company.address = c.find('span', {'itemprop' : 'streetAddress'}).string
        except:
                continue
        if c.find('div', {'itemprop' : 'telephone'}):
            company.phone = c.find('div', {'itemprop' : 'telephone'}).string
        company.subcategory = Search
        company.city = City
        company.state = State
        company.details = c
        companies[company.name] = company
    return companies
    
    #source = soupit("http://www.yellowpages.com/search?search_terms=Computer&geo_location_terms=Seattle+%2C+WA")
    #x = source.findAll('a', {'class' : 'business-name'})
    #x = source.findAll('a' , {'itemprop' : 'name'})
    #itemprop are labels for each property of a company
    #x = source.findAll('div', {'class' : 'info'})
    #companies = makeypcompanies('Computer', 'Seattle', 'WA')
    #print(str(c.name) + ' ' + str(c.address) + ' ' + str(c.phone))
    #x = testmakeypscompanies()
#with open('CompanyList.csv', 'rb') as csvfile:
#	fieldnames = ['Category','Subcategory','City','Name','Address','Phone','Email']
#	wr = csv.DictWriter(csvfile, fieldnames=fieldnames)
#	wr.writeheader()
#	for c in x:
#		wr.writerow({'Category': x[c].category, 'Subcategory': x[c].subcategory, 'City': x[c].city, 'Name': x[c].name, 'Address': x[c].address, 'Phone': x[c].phone, 'Email': x[c].email})
