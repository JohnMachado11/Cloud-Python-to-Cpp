from utils.num_generator import number_generator
from gcp.bq import dataframe_creation


def main(request):
    
    number = number_generator()
    dataframe_creation(number)

    print("Done")

    return "Success", 201
