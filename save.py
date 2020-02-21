import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["nick", "id", "contents", "date"])
    
    for job in jobs:
        writer.writerow(list(job.values()))
    
    return