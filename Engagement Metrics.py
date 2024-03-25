def calculate_engagement_metrics(data):
    # Calculate engagement metrics (e.g., likes, comments, shares)
    likes = data.get("likes", 0)
    comments = data.get("comments", 0)
    shares = data.get("shares", 0)
    engagement_rate = (likes + comments + shares) / data.get("followers", 1)
    return engagement_rate

engagement_rate = calculate_engagement_metrics(social_media_data)
print("Engagement Rate:", engagement_rate)
