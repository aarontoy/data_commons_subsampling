# data_commons_subsampling
Data Commons datasets code to subsample based off [the Data Commons project](https://github.com/WEHI-ResearchComputing/data-commons/wiki).

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


Run this in public_wgs folder:  python create_placeholder_files.py panet_arcnet_2017_clinical_data.tsv

# 2. Private small WGS (even though it is WES) - Pancreatic Neuroendocrine Tumors (Johns Hopkins University, Science 2011) 


https://www.cbioportal.org/study/summary?id=panet_jhu_2011 

Jiao et al from cBioPortal 

Ludwig Center for Cancer Genetics and Howard Hughes Medical Institutions, Johns Hopkins Kimmel Cancer Center, Baltimore, MD 21231, USA. 


This has 10 samples. 

Need to subsample so that all 10 patients/samples take up about 50MB for all FASTQ, CRAM, and vcf files.

Run this in private_wgs folder: python ../public_wgs/create_placeholder_files.py panet_jhu_2011_clinical_data.tsv


# 3. Bulk RNASeq  

 

 
Need to subsample the dataset so that it takes up about 50MB for all FASTQ, CRAM, and count files.

# 4. Proteomics DIA-LFQ 

Need to subsample the dataset so that it takes up about 50MB for all raw, processed, and summary files.

# 5. Imaging (Lattice Light Sheet) 

 

Need to subsample the dataset so that it takes up about 500MB for all raw, processed, and summary files.

 

 

# 6. Spatial Omics - Integrating spatial gene expression and breast tumour morphology via deep learning


Need to subsample the dataset so that it takes up about 500MB for all raw, processed, and summary files.

Integrating spatial gene expression and breast tumour morphology via deep learning

https://www.nature.com/articles/s41551-020-0578-x

https://aquila.cheunglab.org/view/9ae7dd552df4fc33c918695e9e9f49cc

Follow information from this tutorial - https://pachterlab.github.io/voyager/articles/visium_10x.html

https://github.com/bryanhe/ST-Net

https://data.mendeley.com/datasets/29ntw7sh4r/5

Triplicates from 23 breast cancer patients with luminal a, luminal b, triple-negative, and HER2-positive subtypes. Please refer to metadata.csv for patient, replicate, and subtype associations.

Using space ranger - files needed for space ranger is explained here - https://www.10xgenomics.com/support/software/space-ranger/analysis/inputs/input-overview

Can use this dataset from 10x Genomics - but you do need to give them your email address: https://www.10xgenomics.com/datasets/pancreatic-cancer-with-xenium-human-multi-tissue-and-cancer-panel-1-standard


# 7. Spatial Omics - Visium CytAssist Gene Expression Libraries of Post-Xenium Human Colon Cancer (FFPE)

Spatial Omics raw data using Visium technology. This experiment analyses 4 tissue samples: two replicates of experimental samples and two replicates of control samples.

Each sample’s raw data consists of one of each: TIFF, JSON, BTF, CSV and FASTQS, which takes up about 10-20GB. 

Within the FASTQS file, contains four fastq files – four capture slides.


https://www.10xgenomics.com/datasets/visium-cytassist-gene-expression-libraries-of-post-xenium-human-colon-cancer-ffpe-using-the-human-whole-transcriptome-probe-set-2-standard  

	
Watch 10x genomic’s video on Visium Spatial Gene Expression Solution to understand how Visum works -  https://www.youtube.com/watch?v=VwNk4d-0RJc   



