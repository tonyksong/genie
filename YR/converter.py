import pandas as pd
import json
import time
import numpy as np
import multiprocessing

class Converter:

    def __init__(self, dir='data', files = ['user.json', 'review.json', 'business.json']):
        self.dir = dir
        self.files = files

    def worker(self, directory, file_name):
        print("worker called for directory :: "+directory+" file :: "+file_name)
        jsonData = []
        with open(directory +'/'+ file_name, encoding="utf8") as file:
            for line in file:
                jsonData.append(json.loads(line.rstrip()))
        df = pd.DataFrame.from_dict(jsonData)
        csvFileName = file_name[:len(file_name) - 5] + '.csv'
        df.to_csv(csvFileName)

    def convert(self):
        jobs = []
        for file in self.files:
            p = multiprocessing.Process(target=self.worker, name=file, args=(self.dir, file))
            jobs.append(p)
            p.start()
        for job in jobs:
            job.join()
            print('Completed converting file :: '+job.name)

def main():
    converter = Converter('data', ['user.json', 'review.json', 'business.json'])
    start = time.time()
    converter.convert()
    end = time.time()
    print("Time taken for conversion :: "+str(end-start))

if __name__ == '__main__':
    main()

