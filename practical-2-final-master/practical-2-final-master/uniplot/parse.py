import gzip
from Bio import SeqIO

def uniprot_seqrecords(file_location):
    """Parses a file and returns the list of records"""
    records = []

    handle = gzip.open(file_location)
    for record in SeqIO.parse(handle, "uniprot-xml"):
        records.append(record)

    return records
