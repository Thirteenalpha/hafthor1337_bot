import praw
from praw.models import Message
import time 
import schedule



reddit = praw.Reddit(client_id = 'ka8DlGn756NaTA',
client_secret = 'vASC5cmoEaqg1Kl2-e9R7yeUZoMCEg',
user_agent = 'console: message_bot 1.2',
username = '13alpha36',
password = '7371+10270')

subreddits = ['CheckthisVin','carfax','whatcarshouldIbuy']



whatcarshouldIbuy_count = 0
def whatcarshouldIbuy_count_reset():
        global whatcarshouldIbuy_count
        whatcarshouldIbuy_count = 0

schedule.every().day.at("00:00").do(whatcarshouldIbuy_count_reset)

def check_author(author):
    
    file_read = open("Message_list.txt",'r+')
    
    for line in file_read.readlines():
        
        if line == (author + '\n'):
            file_read.close()
            
            return 1
    file_read.close()
    
    return 0




i = 50
print("Initiating bot")
time.sleep(60)
while (i>0):
        message_list = open("Message_list.txt",'a+')
        for topic in subreddits:
                
                subreddit = reddit.subreddit(topic)
                for submission in subreddit.new(limit = 5):
                        
                        author = str(submission.author)
                        
                        if check_author(author) == 1 :
                        
                                continue
                        if (topic == 'whatcarshouldIbuy') and (whatcarshouldIbuy_count < 5):
                                try :
                                        reddit.redditor(author).message('Cheap Carfax','Get your $5 carfax here: https://carsimulcast.com/')
                                        whatcarshouldIbuy_count += 1
                                        message_list.write('\n' + author)
                                        message_list.write('\n' + author)
                                        continue
                                except praw.exceptions.APIException as e:
                                        if e.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
                                                print("Lol this user has a whitelist, there is no way to message them, giving up")

                        try :       
                                reddit.redditor(author).message('Cheap Carfax','Get your $5 carfax here: https://carsimulcast.com/')
                                message_list.write('\n'+ author)
                                message_list.write('\n' + author)
                                print("Message sent.")
                                print(author)
                        except praw.exceptions.APIException as e:
                                if e.error_type == 'NOT_WHITELISTED_BY_USER_MESSAGE':
                                        print("Lol this user has a whitelist, ther is no way to message them, giving up")
        message_list.close()
        print("Online")
        time.sleep(540)       