
function initMap() {
    myLatlng = { lat: -34.024, lng: 150.887 }

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: myLatlng
    });

    google.maps.event.addListener(map, 'click', function (event) {
        addMarker(event.latLng, map);
    });

    markers = setMarkers(map);
    // Add a marker clusterer to manage the markers.
    var markerCluster = new MarkerClusterer(map, markers,
        { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
}

// Adds a marker to the map.
function addMarker(location, map) {
    // Add the marker at the clicked location, and add the next-available label
    // from the array of alphabetical characters.
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
}


// Add some markers to the map.
function setMarkers(map) {
    // Origins, anchor positions and coordinates of the marker increase in the X
    // direction to the right and in the Y direction down.
    var image = {
        url: 'https://cdn1.iconfinder.com/data/icons/nature/32/tent-128.png',
        // This marker is 20 pixels wide by 32 pixels high.
        // The origin for this image is (0, 0).
        origin: new google.maps.Point(0, 0),
        // The anchor for this image is the base of the flagpole at (0, 32).
        anchor: new google.maps.Point(0, 0),
        scaledSize: new google.maps.Size(20, 20)
    };
    // Shapes define the clickable region of the icon. The type defines an HTML
    // <area> element 'poly' which traces out a polygon as a series of X,Y points.
    // The final coordinate closes the poly by connecting to the first coordinate.
    var shape = {
        coords: [1, 1, 1, 20, 18, 20, 18, 1],
        type: 'poly'
    };

    var prevWindow = new google.maps.InfoWindow({});

    //create list of map markers based off locations array
    var markers = locations.map(function (loc, i) {
        //create marker
        marker = new google.maps.Marker({
            position: { lat: loc[1], lng: loc[2] },
            map: map,
            icon: image,
            shape: shape,
            title: loc[0],
            zIndex: loc[3]
        });
        //add evenListener for actions when clicked
        marker.addListener('click', function () {
            // map.setZoom(12);
            // map.setCenter(markers[i].getPosition());
            infowindow = new google.maps.InfoWindow({
                content: loc[0],
                position: markers[i].getPosition()
            });
            prevWindow.close()
            prevWindow = infowindow
            infowindow.open(map)
        });
        return marker
    });

    return markers
};

var locations = [
    ['Bondi Beach', -33.890542, 151.274856, 4],
    ['Coogee Beach', -33.923036, 151.259052, 5],
    ['Cronulla Beach', -34.028249, 151.157507, 3],
    ['Manly Beach', -33.80010128657071, 151.28747820854187, 2],
    ['Maroubra Beach', -33.950198, 151.259302, 1]
]