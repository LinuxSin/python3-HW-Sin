

# class HistEncoder:
#     @staticmethod
#     def encode(file_path):
#         raise NotImplementedError()

# Encoder interface
class HistEncoder:
    @staticmethod
    def encode(file_path):
        raise NotImplementedError("Encoder method must be implemented.")

    @staticmethod
    def decode(file_path):
        raise NotImplementedError("Decoder method must be implemented.")

# JSON format strategy
import json

class JsonHistEncoder(HistEncoder):
    @staticmethod
    def encode(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def decode(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

# CSV format strategy
import csv

class CsvHistEncoder(HistEncoder):
    @staticmethod
    def encode(file_path, data):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            for key, value in data.items():
                writer.writerow([key, value])

    @staticmethod
    def decode(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            return {rows[0]: int(rows[1]) for rows in reader}

# Context to use the strategy
class Histogram:
    def __init__(self, encoder_strategy: HistEncoder):
        self.encoder_strategy = encoder_strategy
        self.data = {}

    def add_data(self, key, value):
        if key in self.data:
            self.data[key] += value
        else:
            self.data[key] = value

    def save(self, file_path):
        self.encoder_strategy.encode(file_path, self.data)

    def load(self, file_path):
        self.data = self.encoder_strategy.decode(file_path)

# Example usage
if __name__ == "__main__":
    histogram = Histogram(JsonHistEncoder)
    histogram.add_data('A', 10)
    histogram.add_data('B', 20)
    histogram.save('histogram.json')

    histogram_csv = Histogram(CsvHistEncoder)
    histogram_csv.add_data('A', 10)
    histogram_csv.add_data('B', 20)
    histogram_csv.save('histogram.csv')

    # Loading data
    loaded_histogram = Histogram(JsonHistEncoder)
    loaded_histogram.load('histogram.json')
    print(loaded_histogram.data)
