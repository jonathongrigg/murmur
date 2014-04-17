var latitude = 0;
var longitude = 0;

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function deletePost(postId, postTitle) {
    if (confirm("Are you sure you want to delete " + postTitle + "?")) {
        // TODO: delete by pinging the server
    }
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
            $('.post h1').html(data['title']);
            $('.post h2').html("By ^" + data['author'] + " on " + data['date_created']);
            $('.post article').html(data['content']);
            if (data['cover']) {
                $('#headerwrap').css('background-image', 'url(' + data['cover'] + ')');
                $('#headerwrap').css('background-position', 'center center');
            }
        }
    })
};

var displayUnsplashImages = function(images, ids) {
    $('#cover').empty();
    for (var i = 0; i < images.length; i++) {
        //console.log(images[i]);
        $('#cover').append('<option data-img-src="' + images[i] + '" value="' + ids[i] + '"></option>');
    }
    $('select').imagepicker();
}

var getUnsplashImages = function(numberOfImages) {
    // Gets a random assortment of numberOfImages images from Unsplash
    if (numberOfImages > 20) {
        return false;
    }
    var imageArray = [];
    var idArray = [];
    $.ajax({
        type: 'GET',
        url: 'http://api.tumblr.com/v2/blog/unsplash.tumblr.com/posts/photo/',
        dataType: 'jsonp',
        data: {
            api_key: 'xjrPrK1xq3oZiU0DXfPm8HcpjkBr1aTfE2JdjgESQ0n8XeqZiH'
        },
        success: function(data) {
            total_images = data.response.total_posts;
            //console.log(data);
            //console.log(total_images);
            $.ajax({
                type: 'GET',
                url: 'http://api.tumblr.com/v2/blog/unsplash.tumblr.com/posts/photo/',
                dataType: 'jsonp',
                data: {
                    api_key: 'xjrPrK1xq3oZiU0DXfPm8HcpjkBr1aTfE2JdjgESQ0n8XeqZiH',
                    offset: getRandomInt(0, total_images-20)
                },
                success: function(data) {
                    //console.log(data);
                    while (imageArray.length != numberOfImages) {
                        var rand = getRandomInt(0, 19);
                        image = data.response.posts[rand].photos[0].alt_sizes[1].url;
                        id = data.response.posts[rand].id;
                        if ($.inArray(image, imageArray) === -1) {  // haven't seen this image yet
                            idArray[imageArray.length] = id;
                            imageArray[imageArray.length] = image;
                        }
                    }
                    displayUnsplashImages(imageArray, idArray);
                }
            })
        }
    })
}

$(document).ready(function() {
    $('#content').wysihtml5();
    $('select').imagepicker();
    // Get location data
    if (Modernizr.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            latitude = position.coords.latitude;
            longitude = position.coords.longitude;
            if (window.location.pathname === '/') {
                getPost(latitude, longitude);
            }
        });
    } else {
        $.ajax({
            url: 'http://freegeoip.net/json/',
            dataType: 'json',
            success: function(data) {
                latitude = data.latitude;
                longitude = data.longitude;
                if (window.location.pathname === '/') {
                    getPost(latitude, longitude);
                }
            }
        });
    }

    if (window.location.pathname === '/share') {
        getUnsplashImages(5);
    }

    $('#view_posts').click(function() {
        getPost(latitude, longitude);
    });

    $('#add_post').click(function() {
        var submit = function() {
            requestData = JSON.stringify({
                "title": $('#title').val(),
                "content": $('#content').val(),
                "cover_id": $('select').val(),
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

    $('#view_more_cover').click(function() {
        getUnsplashImages(5);
    });
});
