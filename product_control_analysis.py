reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "excellent", "bad", "poor", "average"]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]

def highlight_keywords(review, keywords):
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
        review = review.replace(keyword.capitalize(), keyword.upper())
for review in reviews:
    updated_review = highlight_keywords(review, keywords)
    print(updated_review)

keyword_counts = {key: 0 for key in keywords}
for review in reviews:
    for keyword in keywords:
        if keyword in review.lower():
            keyword_counts[keyword] += 1
            print("Keyword counts:[]")
for keyword, count in keyword_counts.items():
    print(f"{keyword.capitalize()}: {count}")

negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

positive_count = 0
negative_count = 0
for review in reviews:
    for word in review.lower().split():  
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

print(reviews)       
print("Sentiment Tally:")
print(f"Positive: {positive_count}")
print(f"Negative: {negative_count}")

def create_summary(review, length=100):
    return review[:length] + "..." if len(review) > length else review
for review in reviews:
    summary = create_summary(review)
    print(summary)