[10:42 AM, 3/17/2022] Fatemeh Karampanah SRH: import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
from sklearn.metrics import accuracy_score, plot_confusion_matrix, confusion_matrix
from matplotlib import pyplot as plt
from sklearn.svm import SVC

df = pd.read_excel("D:/UNI/Big_data/project/labeled_data (1).xlsx")
X = df[['score_github', 'score_normalised_kaggle',
       'score_stack', 'score_twitter', 'weighted_score']]
Y = df.loc[:, 'role']
# scaler = MinMaxScaler()
# X = scaler.fit_transform(X)

ordinal = OrdinalEncoder()
Y = ordinal.fit_transform(Y.values.reshape(-1, 1))
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
# plt.hist(Y)
# plt.sho…
[10:42 AM, 3/17/2022] Sasha Behrouzi: بله
[10:43 AM, 3/17/2022] Fatemeh Karampanah SRH: in yeki SVM hast
[10:43 AM, 3/17/2022] Fatemeh Karampanah SRH: plz pak konid comment ha ro
[10:43 AM, 3/17/2022] Fatemeh Karampanah SRH: man kheili diram shode
[10:43 AM, 3/17/2022] Sasha Behrouzi: Ok
[10:44 AM, 3/17/2022] Fatemeh Karampanah SRH: import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
from sklearn.metrics import accuracy_score, plot_confusion_matrix, confusion_matrix
from matplotlib import pyplot as plt
from sklearn.svm import SVC

df = pd.read_excel("D:/UNI/Big_data/project/labeled_data (1).xlsx")
X = df[['score_github', 'score_normalised_kaggle',
       'score_stack', 'score_twitter', 'weighted_score']]
Y = df.loc[:, 'role']
# scaler = MinMaxScaler()
# X = scaler.fit_transform(X)

ordinal = OrdinalEncoder()
Y = ordinal.fit_transform(Y.values.reshape(-1, 1))
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
# plt.hist(Y)
# plt.sho…
[10:44 AM, 3/17/2022] Fatemeh Karampanah SRH: inam un shabake asabi
[10:44 AM, 3/17/2022] Fatemeh Karampanah SRH: in yeki akhari behtare
[3:40 PM, 3/17/2022] Fatemeh Karampanah SRH: Fatemeh Karampanah is inviting you to a scheduled Zoom meeting.

Topic: Fatemeh Karampanah's Personal Meeting Room

Join Zoom Meeting
https://us04web.zoom.us/j/6630431311?pwd=MFN4THdvUmQzM0M1Z1JucjljY044Zz09

Meeting ID: 663 043 1311
Passcode: 1wUDQm
[3:40 PM, 3/17/2022] Fatemeh Karampanah SRH: biaid inja
[3:48 PM, 3/17/2022] Fatemeh Karampanah SRH: import time
import sqlite3
from contextlib import contextmanager
import requests
from math import ceil
import pandas as pd
import csv
from sklearn import preprocessing
from scipy import stats


class Twitter:

    def _init_(self):
        self.n_request = 0
        self.max_request = 100
        self.requested_records = 300
        self.payload = {}
        self.headers = {
            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAOpkYQEAAAAA%2FdcO4z5xjLPEDa0xhXeV9PxZEk4%3DtmrRUaqTqI37tb86L5McUGNLb9EIzaAI56EMidJGDqLj7n9fCy',
            'Cookie': 'guest_id=v1%3A164278466592740761'
        }
        self.url_1 = "https://api.twitter.com/2/tweets/search/recent?expansions=author_id&max_results={}&tweet.fields=author_id,conversation_id,created_at,geo,id,lang,source,text&user.fields=created_at,description,entities,id,location,name,url,username&query={}"
        self.url_2 = "https://api.twitter.com/2/users?ids={}"
        self.url_3 = "https://api.twitter.com/2/tweets?ids={}&tweet.fields=public_metrics&expansions=attachments.media_keys&media.fields=public_metrics"

    def get_userid(self, tags, k):
        twitter_user_id = []
        twitter_tweet_id = []
        for tag in tags:
            for j in range(ceil(k / self.max_request)):
                if self.n_request == 300:
                    print("I am sleeping for 15 minutes")
                    time.sleep(900)
                    self.n_request = 0
                self.response_1 = requests.request("GET", self.url_1.format(min(self.max_request, k), tag),
                                                   headers=self.headers, data=self.payload)
                self.n_request += 1
                print(f"get tweets {self.n_request}")
                # self.response_2 = requests.request("GET", url_2, headers=headers, data=payload)
                for i in self.response_1.json()['data']:
                    twitter_user_id.append(i['author_id'])
                    twitter_tweet_id.append(i['id'])

        return twitter_user_id, twitter_tweet_id

    def get_user_name(self, twitter_user_ids: list):
        sz = 100
        tweeter_user_name_list = []
        for i in range(ceil(len(twitter_user_ids) / sz)):
            user_id_string = ",".join(twitter_user_ids[i * sz:(i + 1) * sz])
            response_2 = requests.request("GET", self.url_2.format(user_id_string), headers=self.headers,
                                          data=self.payload)
            for j in response_2.json()['data']:
                tweeter_user_name_list.append(j['username'])
        return tweeter_user_name_list

    def get_public_metric(self, twitter_tweet_ids: list):
        retweet_count_list = []
        like_count_list = []
        reply_count_list = []
        for tweet_id in twitter_tweet_ids:
            if self.n_request == 300:
                print("I am sleeping for 15 minutes")
                time.sleep(900)
                self.n_request = 0
            response_3 = requests.request("GET", self.url_3.format(tweet_id), headers=self.headers, data=self.payload)
            self.n_request += 1
            print(f"get public metrics {self.n_request}")
            retweet_count_list.append(response_3.json()['data'][0]['public_metrics']['retweet_count'])
            like_count_list.append(response_3.json()['data'][0]['public_metrics']['like_count'])
            reply_count_list.append(response_3.json()['data'][0]['public_metrics']['reply_count'])
        return retweet_count_list, like_count_list, reply_count_list

    def fetch(self, tags: list, k: int):
        tweets = []

        users_ids, tweets_ids = self.get_userid(tags, k)
        users_names = self.get_user_name(users_ids)
        retweet_count_list, like_count_list, reply_count_list = self.get_public_metric(tweets_ids)
        tag_list = []
        for tag in tags:
            for i in range(k):
                tag_list.append(tag)
        for tag, u_id, t_id, u_name, retweet, like, reply in zip(tag_list, users_ids, tweets_ids, users_names,
                                                                 retweet_count_list, like_count_list, reply_count_list):
            tweet = Tweet(tag, u_name, u_id, t_id, retweet, like, reply)
            tweets.append(tweet)

        with self.cursor_handler() as cur:
            # twitter_user_id,twitter_tweet_id = self.get_userid(tags,k)
            for tweet in tweets:
                tweet.insert(cur)
        return tweets


class Tweet:
    def _init_(self, tag, tweeter_user_name, twitter_user_id, twitter_tweet_id, like_count, retweet_count,
                 reply_count):
        self.tag = tag
        self.tweeter_user_name = tweeter_user_name
        self.twitter_user_id = twitter_user_id
        self.twitter_tweet_id = twitter_tweet_id
        self.like_count = like_count
        self.retweet_count = retweet_count
        self.reply_count = reply_count

    def _repr_(self):
        text = f"{self.tweeter_user_name} = tweeter_user_name \n {self.twitter_user_id} = twitter_user_id \n {self.twitter_tweet_id} = twitter_tweet_id \n {self.like_count} = like_count \n {self.retweet_count} = retweet_count \n {self.reply_count} = reply_count \n {self.tag}"
        return text

    def insert(self, cur):
        cur.execute("INSERT into tweeterTable VALUES (?,?,?,?,?,?,?)", (
            self.tweeter_user_name, self.twitter_user_id, self.twitter_tweet_id, self.like_count, self.retweet_count,
            self.reply_count, self.tag))
        print("inersted")

    @classmethod
    @contextmanager
    def cursor_handler(self):
        connection = sqlite3.connect('Programmers.db')
        cur = connection.cursor()
        yield cur
        connection.commit()
        cur.close()
        connection.close()

    @classmethod
    def select(cls, tag):
        with cls.cursor_handler() as cur:
            cur.execute(f"SELECT * FROM tweeterTable")
            rows = cur.fetchall()
            tweets = [Tweet(*row) for row in rows]
            # res = tuple(int(num) for num in rows.replace('(', '').replace(')', '').replace('...', '').split(', '))
            like_list = []
            reply_list = []
            retweet_list = []
            for i in range(len(rows[0])):
                like_list.append(int(rows[i][3]))
                reply_list.append(int(rows[i][4]))
                retweet_list.append(int(rows[i][4]))

        return like_list, reply_list, retweet_list

    @classmethod
    def get_max_min(cls, tag):
        pass


def get_user_score():
    connection = sqlite3.connect("Programmers.db")
    cur = connection.cursor()
    df2 = pd.read_sql_query("select * from Twitter_user", connection)
    x = df2.loc[:, ['TweetLikeNumber', 'RetweetNumber', 'TweetReplyNumber']].values  # returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df2['score'] = stats.hmean(x_scaled, axis=1)

    users = pd.read_sql_query("select * from NewtweeterUsers", connection)
    users = users.set_index('userID')
    scores = df2.groupby(by="authorID").score.mean().round(2)

    tbl = users.join(scores)
    tbl = tbl.reset_index()

    tbl.to_sql('finalTweeterUsers', connection, if_exists='replace', index=False)
    cur.execute("select * from finalTweeterUsers")
    return cur.fetchall()

    connection.commit()


twitter = Twitter()
tags = ['VimL','Ruby','Clojure','JavaScript','Objective-C','Python','Java','ColdFusion','Go','C++','HTML','Shell','CSS','Rust','Common' 'Lisp','Handlebars','PHP','Swift','Assembly','C#','C','OCaml','Perl','Lua','Haskell','TypeScript','Elixir','CoffeeScript','Makefile','TSQL','SCSS','Pascal','F#','AutoHotkey','Jupyter Notebook','Groovy','Scala','Racket','Kotlin','ActionScript','Vim script','MATLAB','PowerShell','Processing','CMake','TeX','PLpgSQL','ApacheConf','Dart','Crystal','Arduino','R','Objective-J','Prolog','ASP','Jinja','GCC Machine Description','Vue','RenderScript','Erlang','XSLT','SQF','Bison','Elm','Arc','Julia','AppleScript','D','xBase','Nu']
tweets = twitter.fetch(tags, 20000)
users = get_user_score()
# print(Tweet.select('python'))
# print(tweets[0].get_score())
# print(users)