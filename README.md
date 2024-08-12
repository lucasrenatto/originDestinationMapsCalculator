This Python project calculates the distance and travel time between locations using data from an Excel file containing origin and destination addresses. 
Leveraging the Google Maps API, the script reads the data from the Excel file, performs the distance and travel time calculations, and then saves the results to a new Excel file. 
This tool is useful for automating distance calculations in logistics projects, route planning, or geographic data analysis.

Example XLSX:

<table border="1">
    <thead>
        <tr>
            <th>City</th>
            <th>State</th>
            <th>Address</th>
            <th>Distance</th>
            <th>Time</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>New York</td>
            <td>NY</td>
            <td>350 5th Ave, New York</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Los Angeles</td>
            <td>CA</td>
            <td>200 Santa Monica Blvd</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Chicago</td>
            <td>IL</td>
            <td>233 S Wacker Dr</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Houston</td>
            <td>TX</td>
            <td>1600 Smith St</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Miami</td>
            <td>FL</td>
            <td>1101 Brickell Ave</td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>
