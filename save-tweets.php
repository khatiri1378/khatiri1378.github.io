<?php
$tweets_json = file_get_contents("tweets.json");
$tweets = json_decode($tweets_json, true);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $author = $_POST["author"];
    $content = $_POST["content"];
    $date = date('Y-m-d H:i:s');
    
    $new_tweet = array(
        "author" => $author,
        "content" => $content,
        "date" => $date
    );
    
    array_push($tweets, $new_tweet);
    $new_tweets_json = json_encode($tweets);
    file_put_contents("tweets.json", $new_tweets_json);
    
    header('Content-Type: application/json');
    echo json_encode($new_tweet);
}
?>
