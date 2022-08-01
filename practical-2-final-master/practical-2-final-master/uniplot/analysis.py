

def average_len(records):
    """Give the average length of records from the data"""
    total=0
    count=0
    for i in records:
        total=total+len(i)
        count=count+1
    average_records=total/count
    return average_records

def average_len_taxa(records):
    """Returns the average length for the top level taxa"""
    record_by_taxa = {}
    depth = int(input("Please select a level of taxonomy between -1 and 1: "))
    for r in records:
        taxa = r.annotations["taxonomy"][depth]
        record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}
