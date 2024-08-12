import csv

class parse_vehicle_data:
    def __init__(self):
        pass

    def parse_vehicle_data(file_path):
        with open(file_path) as f:
            reader = csv.reader
            data = []
            for row in reader:
                data.append(
                    {
                        "model" : row[0],
                        "make" : row[1],
                        "year" : int(row[2]),
                        "price" : int(row[3])
                    }
                )
            return data