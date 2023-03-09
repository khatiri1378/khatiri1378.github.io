<?php
$tweets_json = file_get_contents("tweets.json");
$tweets = json_decode($tweets_json, true);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $tweet = json_decode(file_get_contents("php://input"), true);
  
  array_push($tweets, $tweet);

  $new_tweets_json = json_encode($tweets);
  file_put_contents("tweets.json", $new_tweets_json);
}
?>
