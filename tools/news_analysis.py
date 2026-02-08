from textblob import TextBlob

def sentiment_analysis(news_list):
    if not news_list:
        return "No recent news available."

    polarity_scores = []
    for article in news_list[:5]:
        blob = TextBlob(article.get("title", ""))
        polarity_scores.append(blob.sentiment.polarity)

    avg_score = sum(polarity_scores) / len(polarity_scores)

    if avg_score > 0:
        return "Positive sentiment"
    elif avg_score < 0:
        return "Negative sentiment"
    else:
        return "Neutral sentiment"
