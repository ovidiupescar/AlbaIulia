import pandas as pd

template = """
	<Placemark id="{{id}}732403ED2467EBFE02">
		<name>{{id}}</name>
		<LookAt>
			<longitude>{{long}}</longitude>
			<latitude>{{lat}}</latitude>
			<altitude>0</altitude>
			<heading>0</heading>
			<tilt>0</tilt>
			<gx:fovy>35</gx:fovy>
			<range>706.114966373874</range>
			<altitudeMode>relativeToGround</altitudeMode>
		</LookAt>
		<styleUrl>#__managed_style_0E877E96DE2467ECD080</styleUrl>
		<Point>
			<altitudeMode>relativeToGround</altitudeMode>
			<coordinates>{{long}},{{lat}},0</coordinates>
		</Point>
	</Placemark>
"""


def new_placemark(id, lat, long):
    print(f'lat {lat} -> long {long}')
    return template.replace("{{id}}", id).replace("{{lat}}", lat).replace("{{long}}", long)

STATII = "statii.csv"

statii = []

with open(STATII, "r") as fis:
    lines = fis.readlines()
    for line in lines:
        row = [item.strip() for item in line.split(';')]
        new_row = []
        for i in range(0, len(row)):
            if i == 2:
                coordinates = [item.strip() for item in row[i].split(',')]
                new_row.append(coordinates[0])
                new_row.append(coordinates[1])
            else:
                new_row.append(row[i])
        statii.append(new_row)
    
st = pd.DataFrame(statii,columns=["Statie", "Nume", "Lat", "Long", "Tema"])
print(st)

placemarks = ""
for index, row in st.iterrows():
    placemarks += new_placemark(row["Statie"], row["Lat"], row["Long"])

with open("AlbaIulia.kml", 'r') as f:
    contents = f.read().replace('{{Placemarks}}', placemarks)

    with open("AlbaIulia_statii.kml", "w") as out:
        out.write(contents)

st.to_excel("statii.xlsx")
