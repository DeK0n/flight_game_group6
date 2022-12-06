class Map {
    defaultCoord = [50.901401519800004, 4.48443984985];

    constructor(airports, originalCoord) {
        this.originalCoord = originalCoord ? originalCoord : this.defaultCoord;
        this.currentLocationCoord = this.originalCoord;
        this.airports = airports;
        this.selectAirportLine = null;
        // Initiate map
        this.map = L.map('map', {tap: false});
        L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
            maxZoom: 20,
            subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
        }).addTo(this.map);
        this.map.setView(this.originalCoord, 7);
        //Adding markers for cities
        L.marker(this.originalCoord).addTo(this.map).bindPopup('Your staring city').openPopup();
        for (let i = 0; i < this.airports.length; i++) {
            let coord = [this.airports[i].latitude, this.airports[i].longitude];
            let title = `${this.airports[i].city} - ${this.airports[i].distance}km`;
            let marker = L.marker(coord, {title: title, airport: this.airports[i]}).addTo(this.map)
            marker.on('click', (e) => {
                this.selectAirport(e.target.options.airport);
                let message = `${e.target.options.airport.city} is ${e.target.options.airport.distance}km away from your current city.`
                marker.bindPopup(message).openPopup();
            });
            marker.on('mouseover', (e) => {

            })
        }
    }

    refreshAirportList(airports) {
        this.airports = airports;
    }

    getDistance(airport) {
        return this.airports[this.airports.indexOf(airport)].distance;
    }

    selectAirport(airport) {
        if(this.selectAirportLine) this.map.removeLayer(this.selectAirportLine)
        this.selectAirportLine = L.polyline([this.currentLocationCoord, [airport.latitude, airport.longitude]]);
        this.selectAirportLine.addTo(this.map);
    }
}

export default Map