$(document).ready(function () {

    var lat = $("#site_latitude").val();
    var lon = $("#site_longitude").val();

    $.getJSON('api.openweathermap.org/data/2.5/forecast?' + lat + '=35&lon=' + lon, function (data) {

        var city = data.location.name;
        var region = data.location.region;
        var country = data.location.country;
        var localtime = data.location.localtime

        var temp_f = data.current.temp_f + " ";
        var temp_c = data.current.temp_c + " ";
        var icon = data.current.condition.icon;
        var weather = data.current.condition.text;
        var updated = data.current.last_updated;
        var id = 0;

        var info =
            "<div><br><strong>Current Weather</strong>: " + weather +
            "<br><strong>Last Updated</strong>: " + updated + "<br>" +
            "<br><strong>City</strong>: " + city + ", " + region + ", " + country +
            "<br><strong>Local Date and Time</strong>: " + localtime +
            "<br><strong>Latitude</strong>: " + lat +
            "<br><strong>Longitutde</strong>: " + lon;

        info += "</div><br>";
        $("#temp").text(temp_f)
        $("#weather_icon").attr("src", icon)
        $("#weather_text").text(weather)
        $("#city").append(city + ", " + region + ", " + country)
        $("#localtime").append(localtime)
        $("#lat").append(lat)
        $("#lon").append(lon)

        $("#metric").on("click", function () {
            if (id === 0) {
                $("#temp").text(temp_c)
                $("#metric").text("C")
                id = 1;
            } else if (id === 1) {
                $("#temp").text(temp_f)
                $("#metric").text("F")
                id = 0;
            }
        });

    });



});