# database

using mysql and sqlalchemy to store data to database

#### [object] weibo

* `id`(int) id,pk,auto_increment
* `weibo`(text) limited 140 words
* `user_id`(int) weibo_id
* `weibo_id`(char255)
* `url`(text)
* `images`(text)(urls)
* `time`

#### [object] comment

* `int` id
* `text` comment_content
* `weibo_id` id
* `user_id`
* `time` comment time
* `image`(supporting image in commit)

### [object] user
* id
* atavar
* user_id
* nickname
* is_fellow
* is_friend
* pv
* time_to_fellow
* time_to_know
