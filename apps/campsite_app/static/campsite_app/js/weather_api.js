console.log("Hello from weather_api.js")
var target_string = 'https://api.darksky.net/forecast/6f2ceccdc4c5425df7336b58b16618bd/' + site_lat + ',' + site_lon
$.ajax({
    url: target_string,
    success: function(serverResponse) {
        weatherGather(serverResponse)
    }
})

function weatherGather(serverData) {
    console.log('weatherGather(serverData)')
    var daily_forecast = serverData['daily']
    console.dir(daily_forecast)
    var day_int = new Date().getDay()
    console.log(day_int)
    var week_arr = ['Sun','Mon','Tue','Wed','Thur','Fri','Sat']
    for (var i=0; i < 5; i++) {
        console.dir(daily_forecast['data'][i])
        icon = daily_forecast['data'][i]['icon']
        $('#weatherdiv').append('<div><p>' + week_arr[day_int] + '</p><img src="/static/campsite_app/images/' + daily_forecast['data'][i]['icon'] + '.png" alt="' + daily_forecast['data'][i]['icon'] + '"></div>')
        day_int++
        if (day_int > 6) {
            day_int = 0;
        }
    }
}