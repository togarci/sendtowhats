import pandas

class ReadingCSV(object):
    def __init__(self):
        self.date = pandas.read_csv('contacts.csv', encoding='ISO-8859-1')

    def getNumbersPhones(self):
        numbers = self.date['Phone 1 - Value']
        list_number=[]
        for x in range(0, len(numbers)):
            string = str(numbers[x]).replace('-','')
            if len(string[-9::]) >= 9:
                list_number.append(string[-9::])                                                                    
                
        return list_number
            
teste = ReadingCSV()
list = teste.getNumbersPhones()
for x in list:
    print(x)
            


