

def create_file(file_name):


    # Creating an empty file
    with open(file_name, 'w'):
        pass  # 'pass' statement means do nothing, so the file is created but remains empty



file_name = 'panet_arcnet_2017_clinical_data.tsv'

# Read the content of the file and display the first column of each row
with open(file_name, 'r') as file:
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



