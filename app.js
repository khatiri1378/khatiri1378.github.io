function showTweets() {
    $.getJSON("tweets.json", function(data) {
        var tweets = "";
        $.each(data, function(key, tweet) {
            tweets += "<li>" + tweet.author + ": " + tweet.content + "</li>";
        });
        $("#tweet-list").html(tweets);
    });
}

$("#add-tweet-form").submit(function(event) {
    event.preventDefault();
    var form = $(this);
    
    $.ajax({
        type: "POST",
        url: "save-tweets.php",
        data: form.serialize(),
        success: function(new_tweet) {
            var tweet_html = "<li>" + new_tweet.author + ": " + new_tweet.content + "</li>";
            $("#tweet-list").append(tweet_html);
        },
        dataType: "json"
    });
});

showTweets();
setInterval(showTweets, 5000);
