import tweepy

Access_token = "1047021808350846976-SDTRmBOkO6TElahYF8sspfKXsDqfzf"#Access token
Access_secret = "Q68fCY5cKXxk8JCePYLYvOeCWlAJQFE2FiXUseUAWdSCf"#Access secret token
Consumer_key = "gFagiXD9ZTDPTj9FXwK38ubfy"#API
Consumer_secret = "MZ2Fy2LX0SbutEB9t4WcmSqG2y9Y6GLzL5lABbss8i6UTmMgu7"#API secret


# OAuth認証
auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_secret)
api = tweepy.API(auth)

#ツイート取得
data = []

#最大2200件のツイートを取得するためのページ
pages = [1,2,3,4,5,6,7,8,9,10]

for page in pages:
    results = api.user_timeline(screen_name="realDonaldTrump", count=200, page=page)
    for r in results:
        #r.textで、投稿の本文のみ取得する
        data.append(r.text)

line = ''.join(data)
with open("TrumpTweets.txt", 'wt') as f:
    f.write(line)