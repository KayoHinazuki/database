# database

```
assets/
    users/
        id_name/
            avatar_timestamp.png

guinsoo: //用户
    id:string
    nick_name:string
    avatar: string
    is_fellow:
    is_friend:
    gender:
    location:
    description:
    fellowing:[id] // 关注的人
    fellowers:[id] //粉丝
    numberof: // 微博数
    time_to_recode:

assets/
    weibo/
        id_name/
            [image_1-9].png


daedalus // weibo
id : (‘string’)
content:(string) 
is_retweet:(boolean)
images:(url)
device: //设备
prev_id:id
post_time: //发微博的时间
star_number:
comment:[comment_id]
retweet:[userid]
time_to_recode:timestamp

comment：//weibo
    id：
    content:
    post_time：
    time_to_record:
    star_number:
    user_id:
    weibo_id:

```