punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(str): #this function replaces every punctionation in the list strip_punctuation with ""
    for char in str:
        if char in punctuation_chars:
            str = str.replace(char,"")
    return str

def get_pos(tweet_str):
    count_pos = 0
    tweet_str = tweet_str.strip().lower()
    tweet_str = strip_punctuation(tweet_str)
    for t_word in tweet_str.split(" "):
        if t_word in positive_words:
            count_pos+=1
            
    return count_pos

def get_neg(tweet_string): 
    count_neg = 0
    tweet_string = tweet_string.strip().lower()
    tweet_string = strip_punctuation(tweet_string)
    for t_word in tweet_string.split(" "):
        if t_word in negative_words:
            count_neg+=1
            
    return count_neg

"""code to open this file - project_twitter_data.csv 
(the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet)"""

in_project_twitter = open("project_twitter_data.csv","r")
out_project_twitter = open("resulting_data.csv","rw")

lines = in_project_twitter.readlines()
print(lines[0])

header = "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n"
out_project_twitter.write(header)

for line in lines[1:]:
    line = line.replace("\n","")
    line = line.split(",")
    no_of_retweets = line[1]
    no_of_replies = line[2]
    line[0] = strip_punctuation(line[0])
    pos_score = get_pos(line[0]) 
    neg_score = get_neg(line[0])
    net_score = pos_score - neg_score
    abc = "{},{},{},{},{}\n".format(no_of_retweets,no_of_replies,pos_score,neg_score,net_score)
    out_project_twitter.write(abc)
    
print(out_project_twitter.readlines())

in_project_twitter.close()
out_project_twitter.close()
