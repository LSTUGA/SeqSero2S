import os, sys
from distutils.core import setup
from setuptools import find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='SeqSero2S',
    #version=open("version.py").readlines()[-1].split()[-1].strip("\"'"),
    version='1.1.4',
    description='Salmonella serotyping',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Linguistic',
        ],
    keywords='Salmonella serotyping bioinformatics WGS',
    url='https://github.com/denglab/SeqSero2S/',
    author='Shaokang Zhang, Hendrik C Den-Bakker and Xiangyu Deng',
    author_email='zskzsk@uga.edu, Hendrik.DenBakker@uga.edu, xdeng@uga.edu',
    license='GPLv2',
    scripts=["bin/deinterleave_fastq.sh","bin/Initial_Conditions_SS2S.py","bin/Initial_Conditions_SS2.py","bin/SeqSero2S.py","bin/SeqSero2_update_kmer_database.py"],
    packages=[""],
    include_package_data = True,
    install_requires=['biopython~=1.73'],
    data_files=[("seqsero2s_db",["seqsero2s_db/mlst.pickle","seqsero2s_db/antigens.pickle","seqsero2s_db/H_and_O_and_specific_genes.fasta","seqsero2s_db/invA_mers_dict","seqsero2s_db/special.pickle"]),("seqsero2s_db/kmer",["seqsero2s_db/kmer/salmonella_35.txt","seqsero2s_db/kmer/salmonella_config.txt","seqsero2s_db/kmer/salmonella_hemD.tfa","seqsero2s_db/kmer/salmonella.log","seqsero2s_db/kmer/salmonella_purE.tfa","seqsero2s_db/kmer/salmonella_thrA.tfa","seqsero2s_db/kmer/salmonella_aroC.tfa","seqsero2s_db/kmer/salmonella_dnaN.tfa","seqsero2s_db/kmer/salmonella_hisD.tfa","seqsero2s_db/kmer/salmonella_profile.txt","seqsero2s_db/kmer/salmonella_sucA.tfa","seqsero2s_db/kmer/salmonella_weight.txt"])],
    zip_safe=False,
)
