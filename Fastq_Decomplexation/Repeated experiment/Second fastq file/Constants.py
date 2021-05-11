"""
Constants file contains all information about constant regions of this barcodes – including sample indexes.

Sample indexes here are defined by finding reverse complementary of corresponding region on reverse primers we use
to amplify the barcode regions.
"""

from Bio.Seq import Seq

__author__ = 'Tee Udomlumleart'
__maintainer__ = 'Tee Udomlumleart'
__email__ = ['teeu@mit.edu', 'salilg@mit.edu']
__status__ = 'Production'

# Constant regions of amplicons
constant_1 = 'AGCAGAGCTACGCACTCTATGCTAGTGCTAGAGATCGGAAGAGCACACGTCTGAACTCCAGTCAC'
constant_2 = 'ATCTCGTATGCCGTCTTCTGCTTG'

# All sample indices
sample_index_dict = {
    'sample_index_1':
    str(Seq('CAAGCAGAAGACGGCATACGAGATACGATCGTGAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_2':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCTAGATCGTGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_3':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGACTCGATCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_4':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTGACTAGCTCGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_5':
    str(Seq('CAAGCAGAAGACGGCATACGAGATATGCTCAGCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_6':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCGATCTGCATGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_7':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGATAGCTGACGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_8':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCAGCTACGTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_9':
    str(Seq('CAAGCAGAAGACGGCATACGAGATAGTACGCATGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_10':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCACGTCGATAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_11':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGTATCACGACGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_12':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCGCAGTACTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_13':
    str(Seq('CAAGCAGAAGACGGCATACGAGATAGCGTCTGATGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_14':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCAGCATGTCTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_15':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGTACTCATCGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_16':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCTGCAGCTAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_17':
    str(Seq('CAAGCAGAAGACGGCATACGAGATACTGTACTCGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_18':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCGACAGCTATGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_19':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGTCATGCGTAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_20':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTAGTCGCATGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_21':
    str(Seq('CAAGCAGAAGACGGCATACGAGATATCGATGACGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_22':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCGATAGTCGTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_23':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGAGCTGTATCGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_24':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCTGATCGCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_25':
    str(Seq('CAAGCAGAAGACGGCATACGAGATAGCATCGTCTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_26':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCTACGTCTAGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_27':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGCTAGATGCTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_28':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCGAGTGCATGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_29':
    str(Seq('CAAGCAGAAGACGGCATACGAGATACGCTGACATGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_30':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCATACAGTGCGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_31':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGAGCACTAGTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_32':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTGCATGTAGCGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_33':
    str(Seq('CAAGCAGAAGACGGCATACGAGATAGTGATCGACGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_34':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCTGACATGCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_35':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGTAGCAGATCGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_36':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCACTATGCGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_37':
    str(Seq('CAAGCAGAAGACGGCATACGAGATACTCGATACGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_38':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCGCATGATCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_39':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGCAGATCACTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_40':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCGACTAGTGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement())
}

all_sample_index_dict = {
    'sample_index_1':
    str(Seq('CAAGCAGAAGACGGCATACGAGATACGATCGTGAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_2':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCTAGATCGTGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_3':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGACTCGATCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_4':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTGACTAGCTCGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_5':
    str(Seq('CAAGCAGAAGACGGCATACGAGATATGCTCAGCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_6':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCGATCTGCATGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_7':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGATAGCTGACGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_8':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCAGCTACGTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_9':
    str(Seq('CAAGCAGAAGACGGCATACGAGATAGTACGCATGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_10':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCACGTCGATAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_11':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGTATCACGACGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_12':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCGCAGTACTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_13':
    str(Seq('CAAGCAGAAGACGGCATACGAGATAGCGTCTGATGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_14':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCAGCATGTCTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_15':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGTACTCATCGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_16':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCTGCAGCTAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_17':
    str(Seq('CAAGCAGAAGACGGCATACGAGATACTGTACTCGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_18':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCGACAGCTATGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_19':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGTCATGCGTAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_20':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTAGTCGCATGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_21':
    str(Seq('CAAGCAGAAGACGGCATACGAGATATCGATGACGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_22':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCGATAGTCGTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_23':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGAGCTGTATCGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_24':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCTGATCGCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_25':
    str(Seq('CAAGCAGAAGACGGCATACGAGATAGCATCGTCTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_26':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCTACGTCTAGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_27':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGCTAGATGCTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_28':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCGAGTGCATGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_29':
    str(Seq('CAAGCAGAAGACGGCATACGAGATACGCTGACATGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_30':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCATACAGTGCGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_31':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGAGCACTAGTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_32':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTGCATGTAGCGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_33':
    str(Seq('CAAGCAGAAGACGGCATACGAGATAGTGATCGACGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_34':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCTGACATGCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_35':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGTAGCAGATCGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_36':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCACTATGCGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_37':
    str(Seq('CAAGCAGAAGACGGCATACGAGATACTCGATACGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_38':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCGCATGATCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_39':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGCAGATCACTGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_40':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTCGACTAGTGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_41':
    str(Seq('CAAGCAGAAGACGGCATACGAGATATCAGCGATGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_42':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCTGTATGAGCGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_43':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGTGACTGTCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_44':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTACGCTGCATGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_45':
    str(Seq('CAAGCAGAAGACGGCATACGAGATAGCTGATGCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_46':
    str(Seq('CAAGCAGAAGACGGCATACGAGATCTATGCACTGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_47':
    str(Seq('CAAGCAGAAGACGGCATACGAGATGCTCATGTCAGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement()),
    'sample_index_48':
    str(Seq('CAAGCAGAAGACGGCATACGAGATTAGCGATCTGGTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTCTAGCACTAGCATAGAGTGCGTAGCT'[24:34]).\
    reverse_complement())
}

print()


