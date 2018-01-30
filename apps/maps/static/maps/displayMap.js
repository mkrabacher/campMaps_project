
function initMap() {

    //if check to see if client is providing their current location
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            
            map.setCenter(pos);
        }, function () {
            handleLocationError(true, infoWindow, map.getCenter());
        });
        
        //createing a new map object
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 10,
            center: pos
        });
    } else {
        // Browser doesn't support Geolocation
        var pos = { lat: 46, lng: -100 }
        
        //createing a new map object
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 4,
            center: pos
        });
    }

    //coords for intial load location. change to my location 
    myLatlng = pos

    //Sets listener for clicking to add a marker
    google.maps.event.addListener(map, 'click', function (event) {
        addMarker(event.latLng, map);
        $("#LatLng").text("Latitude: " + event.latLng.lat() + " " + ", longitude: " + event.latLng.lng());
    });

    markers = setMarkers(map);
    // Add a marker clusterer to manage the markers.
    var markerCluster = new MarkerClusterer(map, markers,
        { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
};

// Adds a marker to the map.
function addMarker(location, map) {
    // Add the marker at the clicked location, delete and reset the prev.
    marker.setMap(null)
    marker = new google.maps.Marker({
        position: location,
        map: map
    });
};

// Add some markers to the map.
function setMarkers(map) {
    // Origins, anchor positions and coordinates of the marker increase in the X
    // direction to the right and in the Y direction down.
    var image = {
        url: 'https://cdn1.iconfinder.com/data/icons/nature/32/tent-128.png',
        origin: new google.maps.Point(0, 0),
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

    //tracks previous tool tip so that you can close it when a new one is opened
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
                position: markers[i].getPosition(),
                maxWidth: 200,
            });
            prevWindow.close()
            prevWindow = infowindow
            infowindow.open(map)
        });
        return marker
    });

    return markers
};

//array of test locations. to be replaced with campsites locations. Dicts? Tuples?
var locations = [
    ['Index Climbers Camp', 47.814826, -121.580629, 4],
    ['Ruby Chow Park. Free to camp there.', 47.546118, -122.314052, 5],
    ['Parking lot on Icicle Creek where you can camp.', 47.543728, -120.735529, 3],
    ['Parking lot on Icicle Creek where you can camp.', -33.80010128657071, -120.735529, 2],
    ['Maroubra Beach', -33.950198, 151.259302, 1]
]