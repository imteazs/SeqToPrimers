'''
Author: Imteaz Siddique
Description: Program to convert existing sequencing data to consenus fasta basis of the program can be found in this
link https://www.biostars.org/p/367626/
'''

from datetime import date
from pathlib import Path
import argparse
import pysam
from Bio import SeqIO

class BamtoFasta:
    def __init__(self, bamfile):
        self.bamfile = bamfile

    def runBamtoConsenus(self, bam):
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='get consensus sequences from bamfile')
    parser.add_argument('--bamfile', help='location of bamfile')
    args = parser.parse_args()
    bampath = Path(args.bamfile)

    bamObj = BamtoFasta(str(bampath))
