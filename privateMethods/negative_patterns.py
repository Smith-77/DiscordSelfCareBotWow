from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

# This message formulates and returns a message to a user message containing a depression pattern
def get_depression_response():
    intro = "Hey! Are you okay? If you're struggling with anything, you're not alone and help is available. Here are some resources:"
    resource1 = "  -  National Suicide Prevention Lifeline: call 800-273-8255 or visit https://suicidepreventionlifeline.org/"
    resource2 = "  -  If you want to talk to people, check out this Discord: https://discord.gg/9g98gZ9H" 
    resource3 = "  -  One more resource"
    return "{intro}\n\n{resource1}\n{resource2}\n{resource3}".format(intro = intro, resource1 = resource1, resource2 = resource2, resource3 = resource3)

# This method determines if a message could contain a negative pattern of depression or anxiety
# It uses a combination of keywords and sentiment analysis
def contains_depression_traces(message_content):
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_analyzer.polarity_scores(message_content)
    negative_sentiment = sentiment_dict['neg']
    positive_sentiment = sentiment_dict['pos']
    message_is_depressing = negative_sentiment > .75 or (negative_sentiment > .5 and positive_sentiment < .5)
    overall_sentiment = message_content
    depression_keywords = ['end my life','depression','anxiety','anxious','depressed','I want to die','self harm','cut myself',"I don't wnat to live",'sad','mental health','suicide','kill myself']
    for word in depression_keywords:
        if word in message_content :
            print(negative_sentiment)
            return message_is_depressing
    return False