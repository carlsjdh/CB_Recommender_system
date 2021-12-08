from recommender import Recommender_CB
import argparse

parser = argparse.ArgumentParser(description="Recomendador por contenido")
parser.add_argument("-t", "--text", type=str, help="Texto", required=True)
parser.add_argument("-f", "--file", type=str, help="Fichero de salida")
parser.add_argument("-m", "--mode", type=str, choices=["table", "cosine", "all"] , help="Informacion a mostrar")

args = parser.parse_args()

text = open(args.text, "r")

recom = Recommender_CB(text)

if( args.file ):
    if ( args.mode == "table"):
        recom.write_table(args.file)
    elif ( args.mode == "cosine"):
        recom.write_cosine(args.file)
    else:
        recom.write_all(args.file)
else:
    if ( args.mode == "table"):
        recom.print_table()
    elif ( args.mode == "cosine"):
        recom.print_cosine()
    else:
        recom.print_all()