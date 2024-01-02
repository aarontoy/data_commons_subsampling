import sys
import os


def create_file(file_name):


    # Creating an empty file
    with open(file_name, 'w'):
        pass  # 'pass' statement means do nothing, so the file is created but remains empty




if len(sys.argv) < 2:
    print("Usage: python script_name.py file_path")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print("Error: not a valid file_path.")
    sys.exit(1)



# Read the content of the file and display the first column of each row
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove the first row
if lines:
    lines = lines[1:]

for line in lines:
    columns = line.strip().split('\t')  # Splitting columns by tab delimiter
    if columns:  # Check if there are columns in the row
        patient_id = columns[0]

        file_name = patient_id + '.bam' 
        create_file(file_name)
        
        file_name = patient_id + '.fastq' 
        create_file(file_name)

        file_name = patient_id + '.vcf' 
        create_file(file_name)



