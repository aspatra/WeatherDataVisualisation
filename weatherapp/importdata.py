import urllib.request
#import nltk,re
#from nltk import word_tokenize
#import numpy.ma as MA

def readData():
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = "http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/AirFrost/ranked/UK.txt"
    headers={'User-Agent':user_agent,} 
    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    raw = response.readlines()#.decode('utf8')
    
    """Extract the header level data from the file"""
    #header = raw.find("Last updated")
    for line in raw:
        if line in ['\n', '\r\n']:
            break
        count=+1
    header = raw[:count]# 529
    #decode('utf8')
    print(type(header))
    print(header)   
    print("===========================================================================")
    month = raw[count+1]#raw[530:765]
    #month = month.split('Year')
    for line in month:
        month = line.decode('utf8').split('Year')
    monthdata = [line.strip(' ') for line in month] 
    print(monthdata)
    print("============================================================================")
    columndata=raw[count+2:]
    for line in columndata:
        columndata = line.decode('utf8').split()
        print(columndata[0])
    #print(i.split('Year')[0] for i in month)
    
    """
    #f = open (file)
    for lines in f:
        month_value=lines.decode().split('Year')
        print(month_value)
    #f.close()
    
    data = []

    
    for col_name in col_names:
        #for line in data_block:
              print(data.append(col_name))
        #= MA.zeros(len(data_block), 'f',  
        #                    fill_value = -999.999)
        


    for (line_count, line) in enumerate(data_block): 
        items = line#.decode().split() 
        for (col_count, col_name) in enumerate(col_names): 
            value = items[col_count] 
            data[col_name][line_count] = checkValue(value) 
    return data """

if __name__ == '__main__':
   readData()
