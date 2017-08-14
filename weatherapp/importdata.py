import urllib.request


def readData():
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = "http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/AirFrost/ranked/UK.txt"
    headers={'User-Agent':user_agent,} 
    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    raw = response.readlines()
    
    """Extract the header level data from the file"""
    for line in raw:
        if line in ['\n', '\r\n']:
            break
        count=+1
    header = raw[:count]
    print(type(header))
    print(header)   
    print("===========================================================================")
    
    #Logic to extract month data into a list
    month = raw[count+1]
    for line in month:
        month = line.decode('utf8').split('Year')
    monthdata = [line.strip(' ') for line in month] 
    print(monthdata)
    print("============================================================================")
    
    #Logic to extract Coloumn data from the file
    columndata=raw[count+2:]
    for line in columndata:
        columndata = line.decode('utf8').split()
        print(columndata[0])
    
if __name__ == '__main__':
   readData()
