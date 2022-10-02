# data we would have pre-surveyed and added to a database:
# the below data is an example
# the number of clusters of people in each room will be found using computer vision as shown in CV_clustering.ipynb
room_names = {1001: "TR +27", 1002: "TR +28", 1003: "TR +29", 1004: "TR +30", 1005: "TR +31"}
data_columns = {"Tables": 0, "Clusters": 1, "booked": 2}
data = {1001: [5, 4, 0], 1002: [3, 2, 0], 1003: [7, 2, 1], 1004: [4, 4, 0], 1005: [6, 5, 0]}
room_ids = [1001, 1002, 1003, 1004, 1005]

crowd_data = {}
for room in room_ids:
    effective_tables = 0
    clusters = data[room][data_columns["Clusters"]]
    booked = data[room][data_columns["booked"]]
    tables = data[room][data_columns["Tables"]]
    if booked:
        effective_tables = -1
    else:
        effective_tables = tables - clusters

    crowd_data[room] = effective_tables

best_id = 0
most_tables = -1

for id, crowd in crowd_data.items():
    if crowd > most_tables:
        best_id = id
        most_tables = crowd

if best_id == 0 and most_tables == -1:
    print("None of the rooms have any free tables :(")
else:
    print("Go to", room_names[best_id] + ". It has", most_tables, "tables free")