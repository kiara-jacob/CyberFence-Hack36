import twint
import pandas as pd


# Configure
c = twint.Config()
c.Search = "bitch ass nigga OR nigger OR chink OR pussy OR"
c.Store_csv = True
c.Output = "/Users/kiarajacob/GitHubHack36/Hack36/data/tweets2.csv"
c.Lang = 'en'
c.Limit=6000

# Run
twint.run.Search(c)


data= pd.read_csv("/Users/kiarajacob/GitHubHack36/Hack36/data/tweets2.csv")
data=data.sample(n=6000)
data_final = data.drop(['place', 'mentions','urls','photos','replies_count','retweets_count','likes_count','hashtags','cashtags','retweet','quote_url','video','thumbnail','near','geo','source','user_rt_id','user_rt','retweet_id','retweet_date','translate','trans_src','trans_dest'], axis=1)
data_final.reset_index(drop=True)
data_final.to_csv('data_final_harassment.csv')