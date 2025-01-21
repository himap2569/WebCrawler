import matplotlib.pyplot as plt
import pandas as pd

# Crawl statistics
total_urls = 1000
books_extracted = 965
duration_minutes = 20.52
pages_per_minute = 48.74

# Derived statistics
urls_remaining = total_urls - books_extracted
crawl_completion_ratio = books_extracted / total_urls * 100

# Data for plotting
time_intervals = list(range(1, int(duration_minutes) + 1))  # Simulating data for each minute
pages_crawled_per_minute = [pages_per_minute for _ in time_intervals]

# Visualization 1: Crawl Speed Over Time
plt.figure(figsize=(10, 6))
plt.plot(time_intervals, pages_crawled_per_minute, marker='o')
plt.title("Crawl Speed Over Time")
plt.xlabel("Time (Minutes)")
plt.ylabel("Pages Crawled Per Minute")
plt.grid()
plt.tight_layout()
plt.savefig("crawl_speed_over_time.png")
plt.show()

# Visualization 2: Ratio of URLs Crawled
labels = ["Books Extracted", "URLs Remaining"]
sizes = [books_extracted, urls_remaining]
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=["skyblue", "lightgray"])
plt.title("Ratio of URLs Crawled")
plt.tight_layout()
plt.savefig("ratio_of_urls_crawled.png")
plt.show()

# Visualization 3: Books Extracted vs. URLs Crawled
plt.figure(figsize=(10, 6))
plt.bar(["Total URLs Crawled", "Books Extracted"], [total_urls, books_extracted], color=["skyblue", "lightgreen"])
plt.title("Books Extracted vs. URLs Crawled")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("books_vs_urls_crawled.png")
plt.show()

# Visualization 4: Crawl Completion Percentage
df = pd.DataFrame({
    "Metric": ["Books Extracted", "Crawl Completion (%)"],
    "Value": [books_extracted, crawl_completion_ratio],
})

plt.figure(figsize=(10, 6))
plt.bar(df["Metric"], df["Value"], color="orange")
plt.title("Crawl Completion Percentage")
plt.ylabel("Value")
plt.tight_layout()
plt.savefig("crawl_completion_percentage.png")
plt.show()
