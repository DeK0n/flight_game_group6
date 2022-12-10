class Map {
    defaultCoord = [50.901401519800004, 4.48443984985];

    constructor(airports, originalCoord) {
        this.originalCoord = originalCoord ? originalCoord : this.defaultCoord;
        this.currentLocationCoord = this.originalCoord;
        this.airports = airports;
        this.selectAirportLine = null;
        this.linePath = null;
        // Initiate map
        this.map = L.map('map', {tap: false, zoomControl: false});
        L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
            maxZoom: 5,
            minZoom: 4,
            subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
        }).addTo(this.map);
        this.refreshMap(this.originalCoord, this.airports);
        L.marker(this.originalCoord).addTo(this.map).bindPopup('Your staring city').openPopup();

    }
    refreshMap(nextDestinationCoord, airports) {
        this.map.setView(nextDestinationCoord, 4);
        for (let i = 0; i < airports.length; i++) {
            let coord = [airports[i].latitude, airports[i].longitude];
            let title = `${airports[i].city} - ${airports[i].distance}km`;
            let marker = L.marker(coord, {title: title, airport: airports[i]}).addTo(this.map)
            marker.on('click', (e) => {
                let selectedAirport = e.target.options.airport
                this.selectAirport(selectedAirport)
                let message = `${e.target.options.airport.city} is ${e.target.options.airport.distance}km away.`
                marker.bindPopup(message).openPopup();
            });
        }
    }

    selectAirport(airport) {
        if (this.selectAirportLine) this.map.removeLayer(this.selectAirportLine)
        this.selectAirportLine = L.polyline([this.currentLocationCoord, [airport.latitude, airport.longitude]]);
        this.selectAirportLine.addTo(this.map);

        let event = new CustomEvent("selectCity", {detail: airport});
        document.dispatchEvent(event);
    }

    flyTo (nextDestination, airports) {
        let nextDestinationCoord = [nextDestination.latitude, nextDestination.longitude];
        this.selectAirportLine = null;
        let linePath = L.polyline([this.currentLocationCoord, nextDestinationCoord]);
        this.currentLocationCoord = nextDestinationCoord;
        this.refreshMap(nextDestinationCoord, airports);
    }
}

export default Map