from gcp.bq import does_table_exist, records_from_table


def main(request):

    print("Compute_Func Cloud Function Called!\n")

    result = does_table_exist()

    if result is True:
        numbers = records_from_table()
        nums_as_str = f"{numbers}"

        print(f"5 most recent table records: \n{nums_as_str}")

        return nums_as_str
    else:
        return "No Data Found", 404
