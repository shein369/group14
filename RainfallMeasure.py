
class RainfallRecord:

    def __init__(self, season, month, rainfall):
        self.season = season
        self.month = month
        self.rainfall = rainfall

def read_data():
    file = open("rainfall2.txt", "r")
    lines = file.readlines()
    file.close()

    records = []

    for line in lines[1:]:
        parts = line.strip().split(",")

        if len(parts) == 3:
            season = parts[0]
            month = parts[1]
            rainfall = float(parts[2])

            record = RainfallRecord(season, month, rainfall)
            records.append(record)

    return records
def organise_seasons(records):
    seasons = {}

    for record in records:
        if record.season not in seasons:
            seasons[record.season] = []

        seasons[record.season].append(record)

    return seasons

def analyse(records):
    rainfall_values = list(map(lambda record: record.rainfall,records))

    total = sum(rainfall_values)
    average = total / len(records)

    highest = max(records, key=lambda record: record.rainfall)
    lowest = min(records, key=lambda record: record.rainfall)

    return total, average, highest, lowest

def drought_months(records, threshold):
    risky = list(filter(lambda record: record.rainfall < threshold,records))

    return [record.month for record in risky]

def display_report(name, records, threshold):
    total, average, highest, lowest = analyse(records)
    risky = drought_months(records, threshold)

    print("\nSeason:", name)
    print("Total rainfall:", total, "mm")
    print("Average rainfall:", round(average, 2), "mm")
    print("Highest rainfall:", highest.month, highest.rainfall, "mm")
    print("Lowest rainfall:", lowest.month, lowest.rainfall, "mm")
    print("Months below threshold:", risky)

records = read_data()

seasons = organise_seasons(records)
season_names = list(seasons.keys())

season1 = seasons[season_names[0]]
season2 = seasons[season_names[1]]

threshold = float(input("Enter drought threshold in mm: "))

total1, average1, highest1, lowest1 = analyse(season1)
total2, average2, highest2, lowest2 = analyse(season2)

display_report(season_names[0], season1, threshold)
display_report(season_names[1], season2, threshold)

if total1 > total2:
    comparison = season_names[0] + " was wetter."
elif total2 > total1:
    comparison = season_names[1] + " was wetter."
else:
    comparison = "Both seasons received equal rainfall."

print("\nSeason comparison:", comparison)

file = open("rainfall_report.txt", "w")

file.write("RAINFALL ANALYSIS REPORT\n\n")

for name in season_names:
    records = seasons[name]
    total, average, highest, lowest = analyse(records)
    risky = drought_months(records, threshold)

    file.write("Season: " + name + "\n")
    file.write("Total rainfall: " + str(total) + " mm\n")
    file.write("Average rainfall: " + str(round(average, 2)) + " mm\n")
    file.write("Highest rainfall: " + highest.month + "\n")
    file.write("Lowest rainfall: " + lowest.month + "\n")
    file.write("Months below threshold: " + str(risky) + "\n\n")

file.write("Season comparison: " + comparison)

file.close()

print("\nSummary report saved to rainfall_report.txt")