import argparse
from . import parse
from . import analysis
from . import plot

LOC="uniprot_receptor.xml.gz"

def dump(args, LOC):
    """Passes the data and displays the full set of data"""
    for record in parse.uniprot_seqrecords(LOC):
        print(record)


def names(args, LOC):
    """Passes the data and displays the names of the proteins in the data"""
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)

def average(args, LOC):
    """Passes the data and gives the average length of the protein"""
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(LOC))))

def plot_average_by_taxa(args, LOC):
    """Passes the data through to create a bar chart plot.py"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC))
    plot.plot_bar_show(av)

def plot_pie_chart(args, LOC):
    """Passes the data through to create a pie chart in plot.py"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC))
    plot.plot_pie_show(av)


def cli(LOC):
    """Sets all the arguments and how they are called"""
    ## Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help='''List of commands: \n
    dump - Gives full file \n
    list - lists out all proteins \n 
    average - Gives average length of the proteins \n
    graph - Gives a graph of the different types of protein \n
    pie - Gives a pie chart of different types of protein
    ''')

    ## Add subparsers
    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)
    subparsers.add_parser("graph").set_defaults(func=plot_average_by_taxa)
    subparsers.add_parser("pie").set_defaults(func=plot_pie_chart)

    ## Parse the command line
    args = parser.parse_args()

    ## Take the func argument, which points to our function and call it.
    args.func(args, LOC)
