import csv
def find_min_demand_days(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        data = list(reader)

    min_demand = float('inf')
    min_days = []
    for row in data:
        day, demand = row
        demand = int(demand)
        
        if demand < min_demand:
            min_demand = demand
            min_days = [day]
        elif demand == min_demand:
            min_days.append(day)
    
    print(f"Мінімальний попит: {min_demand}")
    print(f"Дні з мінімальним попитом: {min_days}")
csv_file_path = 'data.csv'
find_min_demand_days(csv_file_path)