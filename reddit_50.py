import praw
from praw.models import Message
import time 
import schedule



reddit = praw.Reddit(client_id = 'pJ8rbRTJAwVrog',
client_secret = 'UYGBff9tCdtuWCljjHswRI-_e-Vk6w',
user_agent = 'console: message_bot 1.3',
username = 'Dopedude4712',
password = '7371+10270')

subreddits = ['carfax','CheckthisVIn','whatcarshouldIbuy']



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
        
        for topic in subreddits:
                
                subreddit = reddit.subreddit(topic)
                for submission in subreddit.new(limit = 3):
                        message_list = open("Message_list.txt",'a+')
                        author = str(submission.author)
                        
                        if check_author(author) == 1 :
                        
                                continue
                        if (topic == 'whatcarshouldIbuy') and (whatcarshouldIbuy_count < 5):
                                try :
                                        reddit.redditor(author).message('Cheap Carfax', "Hello, how's it going. I saw your submission on whatcarshouldibuy. if you are interested, you could check out cheap carfax here : carsimulcast . com . This helped me, so I thought to help you. Cheers and have a nice day")
                                        whatcarshouldIbuy_count += 1
                                        message_list.write('\n' + author)
                                        message_list.write('\n' + author)
                                        message_list.close()
                                        continue
                                except praw.exceptions.APIException as e:
                                        if e.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
                                                print("Lol this user has a whitelist, there is no way to message them, giving up")
                                                message_list.close()
                        elif (topic == 'carfax'):

                                try :       
                                        reddit.redditor(author).message('Cheap Carfax',"Hello, how's it going. I saw your submission on carfax. if you are interested, you could check out cheap carfax here : carsimulcast . com . This helped me, so I thought to help you. Cheers and have a nice day")
                                        message_list.write('\n'+ author)
                                        message_list.write('\n' + author)
                                        print("Message sent.")
                                        message_list.close()
                                        print(author)
                                except praw.exceptions.APIException as e:
                                        if e.error_type == 'NOT_WHITELISTED_BY_USER_MESSAGE':
                                                print("Lol this user has a whitelist, ther is no way to message them, giving up")
                                                message_list.close()
                        elif (topic == 'CheckthisVin'):
                                try :       
                                        reddit.redditor(author).message('Cheap Carfax',"Hello, how's it going. I saw your submission on CheckthisVin. if you are interested, you could check out cheap carfax here : carsimulcast . com . This helped me, so I thought to help you. Cheers and have a nice day")
                                        message_list.write('\n'+ author)
                                        message_list.write('\n' + author)
                                        print("Message sent.")
                                        message_list.close()
                                        print(author)
                                except praw.exceptions.APIException as e:
                                        if e.error_type == 'NOT_WHITELISTED_BY_USER_MESSAGE':
                                                print("Lol this user has a whitelist, ther is no way to message them, giving up")
                                                message_list.close()
        
        print("Online")
        time.sleep(540)       