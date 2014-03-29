$(document).ready(function() {
    $('#ip_location').click(function() {
        $.ajax({
            url: 'http://freegeoip.net/json/',
            dataType: 'json',
            success: function(data) {
                window.location.href = '/near?latitude=' + data.latitude + '&longitude=' + data.longitude;
            }
        });
    });

    $('#geo_location').click(function() {
        if (Modernizr.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                window.location.href = '/near?latitude=' + position.coords.latitude + '&longitude=' + position.coords.longitude;
            });
        } else {
            // no native support; maybe try a fallback?
        }
    });
});
