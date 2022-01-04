import csv

from cv2 import norm
from getData import get_data

data = get_data()
header = ['class' , 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
with open('data.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(header) 
    
    # right  
    for right_data in data['right'] : 
        count = 1
        myrow = []
        myrow.append('right')
        for data_once in right_data :
            print(count ) 
            count +=1 
            print(data_once[0])
            print('-------------')
            myrow.append(data_once[0])
        writer.writerow(myrow)

        # left 
    for left_data in data['left'] : 
        count = 1
        myrow = []
        myrow.append('left')
        for data_once in left_data :
            print(count ) 
            count +=1 
            print(data_once[0])
            print('-------------')
            myrow.append(data_once[0])
        writer.writerow(myrow)

        # up 
    for up_data in data['up'] : 
        count = 1
        myrow = []
        myrow.append('up')
        for data_once in up_data :
            print(count ) 
            count +=1 
            print(data_once[0])
            print('-------------')
            myrow.append(data_once[0])
        writer.writerow(myrow)

        # down 
    for down_data in data['down'] : 
        count = 1
        myrow = []
        myrow.append('down')
        for data_once in down_data :
            print(count ) 
            count +=1 
            print(data_once[0])
            print('-------------')
            myrow.append(data_once[0])
        writer.writerow(myrow)

        # click 
    for click_data in data['click'] : 
        count = 1
        myrow = []
        myrow.append('click')
        for data_once in click_data :
            print(count ) 
            count +=1 
            print(data_once[0])
            print('-------------')
            myrow.append(data_once[0])
        writer.writerow(myrow)

        # normal 
    for normal_data in data['normal'] : 
        count = 1
        myrow = []
        myrow.append('normal')
        for data_once in normal_data :
            print(count ) 
            count +=1 
            print(data_once[0])
            print('-------------')
            myrow.append(data_once[0])
        writer.writerow(myrow)
                


