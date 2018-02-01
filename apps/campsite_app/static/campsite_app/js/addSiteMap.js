
var map
//turns the map div in the html into a map.
function initMap() {

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            map.setCenter(pos);
        });
        //createing a new map object
        map = new google.maps.Map(document.getElementById('map'), {
            zoom: 10,
            center: pos
        });

    } else {
        // if browser doesn't support Geolocation
        // this is currently not working. not neccessarily the below code but something to do with this if statement and how the google maps object works.
        var pos = { lat: 46.0, lng: -100.0 }

        map.setCenter(pos);
        //createing a new map object
        map = new google.maps.Map(document.getElementById('map'), {
            center: { lat: -34.397, lng: 150.644 },
            zoom: 4,
        });
    }


    //Sets listener for clicking to add a marker
    google.maps.event.addListener(map, 'click', function (event) {
        // addMarker(event.latLng, map);
        currentLatLng = {'lat':event.latLng.lat(), 'lng':event.latLng.lng()}
        $("#add-latitude").val(currentLatLng.lat);
        $("#add-longitude").val(currentLatLng.lng);
        addMarker(currentLatLng, map)
    });

    // var markers
    $.ajax({
        url: '/sites.json',
        success: function(serverResponse) {
            ajax_location_build(serverResponse)
        }
    })
    // Add a marker clusterer to manage the markers.
    // console.log('markers')
    // console.dir(markers)
    setTimeout(() => {
        var markerCluster = new MarkerClusterer(map, markers,
            { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
    }, 200);
    // console.log('markers')
    // console.dir(markers)
};
// Builds the location array and calls addMarker
function ajax_location_build(arr) {
    for (var i=0; i<arr.length; i++) {
        fields = arr[i]['fields']
        var push_arr = []
        push_arr.push(fields['name'])
        push_arr.push(parseFloat(fields['latitude']))
        push_arr.push(parseFloat(fields['longitude']))
        address_string = ""
        for (var j=0; j<fields['address'].length;j++) {
            if (fields['address'].charAt(j) != ';') {
                address_string = address_string + fields['address'].charAt(j)
            } else {
                address_string += '<br>'
            }
        }
        push_arr.push(address_string)
        push_arr.push(arr[i]['pk'])
        locations.push(push_arr)
    }
    markers = setMarkers(map);
}
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
        url: '/static/images/campIcon.png',
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(13, 1),
        scaledSize: new google.maps.Size(25, 25)
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
            title: loc[0]
        });
        //add evenListener for actions when clicked
        marker.addListener('click', function () {
            var myLat, myLng
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (position) {
                    myLat = position.coords.latitude,
                        myLng = position.coords.longitude
                });
                setTimeout(() => {
                    contentString = '<div><b><a href="/site/' + loc[4] + '">' + loc[0] + '</a></b></div><div>' + loc[3] + '</div><div><a target="blank_" href="https://www.google.com/maps/dir/?api=1&origin=' + myLat + ',' + myLng + '&destination=' + loc[1] + ',' + loc[2] + '&z=10&t=h&hl=en-US&gl=US&mapclient=apiv3">Get Directions</a>'

                    infowindow = new google.maps.InfoWindow({
                        content: contentString,
                        position: markers[i].getPosition(),
                        maxWidth: 200,
                    });
                    prevWindow.close()
                    prevWindow = infowindow
                    infowindow.open(map)
                }, 200);
            };
        });
        return marker
    });

    return markers
};

//array of test locations. to be replaced with campsites locations. Dicts? Tuples?
var locations = []