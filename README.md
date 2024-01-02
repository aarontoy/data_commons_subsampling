# data_commons_subsampling
Data Commons datasets code to subsample.

For each dataset:
1. provide links to all the formats for each dataset eg. FASTQ format, CRAM format, VCF format
2. create code to download raw dataset or choose a publicly available dataset that is similar and rename
3. create code to subsample raw dataset or choose a publicly available dataset that is similar and rename
4. create code to process raw dataset or choose a publicly available dataset that is similar and rename
5. create README to point back to data portal and to this code



# 1. Public WGS - Pancreatic Neuroendocrine Tumors (Multi-Institute, Nature 2017) 

 
Scarpa et al and also Sean Grimmond from cBioPortal 

https://www.cbioportal.org/study/summary?id=panet_arcnet_2017 

This is a WGS with 98 samples/patients.  Accession EGAS00001001732 is here: - https://ega-archive.org/studies/EGAS00001001732?order=file_types&sort=asc - Please use the ICGC website for applying for access to the data: https://ega-archive.org/dacs/EGAC00001000010

It also has the non-identifiable clinical data available too. 

Need to subsample so that all 98 patients/samples take up about 500MB for all FASTQ, CRAM, and vcf files.


# 2. Private small WGS (even though it is WES) Pancreatic Neuroendocrine Tumors (Johns Hopkins University, Science 2011) 


https://www.cbioportal.org/study/summary?id=panet_jhu_2011 

Jiao et al from cBioPortal 

Ludwig Center for Cancer Genetics and Howard Hughes Medical Institutions, Johns Hopkins Kimmel Cancer Center, Baltimore, MD 21231, USA. 


This has 10 samples. 

Need to subsample so that all 10 patients/samples take up about 50MB for all FASTQ, CRAM, and vcf files.

# 3. Bulk RNASeq  

 

 
Need to subsample the dataset so that it takes up about 50MB for all FASTQ, CRAM, and count files.

# 4. Proteomics DIA-LFQ 

Need to subsample the dataset so that it takes up about 50MB for all raw, processed, and summary files.

# 5. Imaging (Lattice Light Sheet) 

 

 Need to subsample the dataset so that it takes up about 500MB for all raw, processed, and summary files.

 

 

# 6. Spatial Omics 


 Need to subsample the dataset so that it takes up about 500MB for all raw, processed, and summary files.
