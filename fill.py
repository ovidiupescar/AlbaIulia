template = """
	<Placemark id="{{id}}732403ED2467EBFE02">
		<name>{{id}}</name>
		<LookAt>
			<longitude>{{alt}}</longitude>
			<latitude>{{long}}</latitude>
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
			<coordinates>{{alt}},{{long}},0</coordinates>
		</Point>
	</Placemark>
"""


def new_placemark(id, alt, long):
    return template.replace("{{id}}", id).replace("{{alt}}", alt).replace("{{long}}", long)


placemark = new_placemark("03", "123.34", "64.33")

print(placemark)
