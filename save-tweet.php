<?php

// Get the JSON-encoded tweet data from the request body
$tweet = json_decode(file_get_contents("php://input"), true);

// Check if the tweet data is valid
if (!is_array($tweet) || empty($tweet['text'])) {
  http_response_code(400);
  echo "Invalid tweet data";
  exit;
}

// Save the tweet to a file or database
$file = 'tweets.json';
$tweets = json_decode(file_get_contents($file), true);
$tweets[] = $tweet;
file_put_contents($file, json_encode($tweets));

// Return a response indicating success
http_response_code(200);
echo "Tweet saved successfully";
exit;

?>
