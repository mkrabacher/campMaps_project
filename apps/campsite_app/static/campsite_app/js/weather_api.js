
var target_string = 'https://api.darksky.net/forecast/6f2ceccdc4c5425df7336b58b16618bd/' + site_lat + ',' + site_lon
$.ajax({
    url: target_string,
    success: function(serverResponse) {
        weatherGather(serverResponse)
    }
})

function weatherGather(serverData) {
    var daily_forecast = serverData['daily']
    var day_int = new Date().getDay()
    var week_arr = ['Sun','Mon','Tue','Wed','Thur','Fri','Sat']
    for (var i=0; i < 5; i++) {
        if(daily_forecast['data'][i]['icon'] == 'partly-cloudy-night' || daily_forecast['data'][i]['icon'] == 'partly-cloudy-day') {
            var desc = 'cloudy'
        } else {
            desc = daily_forecast['data'][i]['icon']
        }
        icon = daily_forecast['data'][i]['icon']
        $('#weatherdiv').append('<div><h4>' + week_arr[day_int] + '</h4><img src="/static/campsite_app/images/' + daily_forecast['data'][i]['icon'] + '.png" alt="' + daily_forecast['data'][i]['icon'] + '"><p>' + desc + '</p></div>')
        day_int++
        if (day_int > 6) {
            day_int = 0;
        }
    }
}