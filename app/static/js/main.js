var latitude = 0;
var longitude = 0;

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
            $('.post h1').html(data['title']);
            $('.post h2').html("By ^" + data['author'] + " on " + data['date_created']);
            $('.post article').html(data['content']);
        }
    })
};

$(document).ready(function() {
    $('#content').wysihtml5();
    // Get location data
    if (Modernizr.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            latitude = position.coords.latitude;
            longitude = position.coords.longitude;
            getPost(latitude, longitude);
        });
    } else {
        $.ajax({
            url: 'http://freegeoip.net/json/',
            dataType: 'json',
            success: function(data) {
                latitude = data.latitude;
                longitude = data.longitude;
                getPost(latitude, longitude);
            }
        });
    }

    $('#view_posts').click(function() {
        getPost(latitude, longitude);
    });

    $('#add_post').click(function() {
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
                    $('#add_post').html(data.status);
                    $('#add_post').addClass('btn-info');
                    setTimeout(function() {
                        window.location.href='/';
                    }, 2000); // wait two seconds before reloading
                }
            })
        }
        submit();
    });
});
