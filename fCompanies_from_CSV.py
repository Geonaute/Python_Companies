def makecompanies(SourceCSV):
        #              Assumed Field Order                #
        #Category,Subcategory,City,Name,Address,Phone,Email

        from cCompany import Company
        from csv import reader
        Companies = set() #ouput

        reader = reader(SourceCSV)
        for rows in reader:
                x = Company(rows[3])
                x.category = rows[0]
                x.subcategory = rows[1] 
                x.city = rows[2]
                x.address = rows[4]
                x.phone = rows[5]
                x.email = rows[6]
                Companies.add(x)
        return Companies
        
        
#for c in Companies:
#	if c.email.strip() and i < 10:
#		print(c.email)
#		i = i + 1

def testmakecompanies():
        CompanySource = open('CompanyList.csv', 'rt')
        Companies = makecompanies(CompanySource)
        print(str(len(Companies)) + ' Companies created')
        return Companies

def usermakecompanies():
        from tkinter.filedialog import askopenfilename
        print("Please select a CSV with a list of companies to add. Assumed field order: Category,Subcategory,City,Name,Address,Phone,Email")
        filename = askopenfilename()
        CompaniesSource = open(filename, 'rt')
        Companies = makecompanies(CompaniesSource)
        return Companies
