<?php
// دریافت اطلاعات توئیت‌های ثبت شده از فایل tweets.json
$tweets = json_decode(file_get_contents('tweets.json'), true);

// دریافت اطلاعات توئیت جدید
$data = file_get_contents('php://input');
$new_tweet = json_decode($data, true);

// اضافه کردن توئیت جدید به ابتدای آرایه توئیت‌ها
array_unshift($tweets, $new_tweet);

// ذخیره توئیت‌های جدید در فایل tweets.json
file_put_contents('tweets.json', json_encode($tweets));

// بازگشت پاسخ به JavaScript
echo 'success';
?>
