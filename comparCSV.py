import csv
num_rec = int(input("How many files are being compared ? "))
split_choice=(input("Chose split type, R:record or E:element?\n(All files will parsed this way) "))

files = {}
for i in range(0,num_rec):
    with open(input(f"{i+1}.CSV file name : ")+".csv",'r') as csv_file:
        csv_content = csv_file.read()
    if split_choice =="R":
        files[f'csv_list{i}'] = csv_content.split('\n')
    elif split_choice == "E":
        files[f'csv_list{i}'] = csv_content.replace('\n',',').split(',')

print('files len is :'+str(len(files)))

for i in range(len(files)-1):
    for j in files[f'csv_list{i}']:
        if j not in files[f'csv_list{i+1}']:
            print(f"The follwing recored(s) are in {i+1}.CSV  and not in {i+2}.CVS: ")
            print(j+'\n')
    for k in files[f'csv_list{i+1}']:
        if k not in files[f'csv_list{i}']:
            print(f"The follwing recored(s) are in {i+2}.CSV  and not in {i+1}.CVS: ")
            print(k+'\n')
        i+1
