var getRandomInt = function(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

var getPost = function(latitude, longitude) {
    requestData = JSON.stringify({
        "latitude": latitude,
        "longitude": longitude,
    });
    console.log(requestData);
    $.ajax({
        url: '/get_post',
        dataType: 'json',
        contentType: 'application/json; charset=UTF-8',
        data: requestData,
        type: 'POST',
        success: function(data) {
            console.log(data);
            number = getRandomInt(0, data.posts.length - 1);
            console.log(number);
            $('#post h1').html(data.posts[number]['title']);
            $('#post h2').html("By ^" + data.posts[number]['author'] + " at " + data.posts[number]['date_created']);
            $('#post article').html(data.posts[number]['content']);
        }
    })
};

$(document).ready(function() {
    $('#ip_location').click(function() {
        $.ajax({
            url: 'http://freegeoip.net/json/',
            dataType: 'json',
            success: function(data) {
                getPost(data.latitude, data.longitude);
            }
        });
    });

    $('#geo_location').click(function() {
        if (Modernizr.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                getPost(position.coords.latitude, position.coords.longitude);
            });
        } else {
            // no native support; maybe try a fallback?
        }
    });

    $('#add_post').click(function() {
        var latitude = 0;
        var longitude = 0;
        var submit = function() {
            requestData = JSON.stringify({
                "title": $('#title').val(),
                "content": $('#content').val(),
                "latitude": latitude,
                "longitude": longitude
            });
            console.log(requestData);
            $.ajax({
                url: '/add_post',
                dataType: 'json',
                contentType: 'application/json; charset=UTF-8',
                data: requestData,
                type: 'POST',
                success: function(data) {
                    console.log(data);
                }
            })
        }
        if (Modernizr.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                latitude = position.coords.latitude;
                longitude = position.coords.longitude;
                submit();
            });
        } else {
            $.ajax({
                url: 'http://freegeoip.net/json/',
                dataType: 'json',
                success: function(data) {
                    latitude = data.latitude;
                    longitude = data.longitude;
                    submit();
                }
            });
        }
    });
});
