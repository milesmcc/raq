# RAQ — General Documentation
**The mediasphere is complex. RAQ cuts through the noise.**

RAQ takes a topic—just a string of text, like `Elizabeth Warren`—and scans the media to understand the role of that topic within the greater media sphere.

### How to Use
First, clone the repository. Then, make sure that `secrets.txt` (in the project root directory) has valid API keys in it. The `secrets.txt` file has valid secret keys in it. In order, the keys are:
```
Wolfram Alpha Key
Word Extractor API Key (http://keywordextraction.net/keyword-extraction-api-document)
Microsoft Azure API Key 1
Microsoft Azure API Key 2
```

Simply import the `Manager` and pass it a string of the topic you'd like to understand.

You'll get data that looks like this in response:
```
[
  {
    "elements": {
      "RelatedTopics": [
        "testimony",
        "air force",
        "pacific command",
        "briefing",
        "trump",
        "rene boucher",
        "rand paul",
        "bowling green",
      ],
      "Popularity": {
        "popularity": 48
      },
      "Sentiment": {
        "sentiment": -0.9879,
        "individual_sentiments": [
          0.5297,
          0.307,
          -0.9528
        ]
      },
      "RelatedArticles": {
        "top_articles": [
          {
            "headline": "Did Sessions mislead Congress about his interactions with Russia?",
            "url": "https://www.cbsnews.com/news/did-sessions-mislead-congress-about-his-interactions-with-russia/",
            "thumbnail": "https://www.bing.com/th?id=ON.7486CC918722A70321BBD371496F30A2&pid=News"
          },
          {
            "headline": "Trump Stops in Hawaii En Route to Asia",
            "url": "https://www.voanews.com/a/trump-hawaii-pearl-harbor-asia-trip/4099705.html",
            "thumbnail": "https://www.bing.com/th?id=ON.CCCA5F42648032139E3CE60CD622E660&pid=News"
          },
          {
            "headline": "Sen. Rand Paul Allegedly Assaulted at His Kentucky Home, Suspect Arrested",
            "url": "https://www.nbcnews.com/news/us-news/sen-rand-paul-assaulted-his-kentucky-home-suspect-arrested-n817591",
            "thumbnail": "https://www.bing.com/th?id=ON.C230C821D79BB6AF5BF11B8105C6CF0E&pid=News"
          }
        ]
      }
    },
    "connected": [],
    "name": "Jeff Sessions"
  },
  {
    "elements": {
      "RelatedTopics": [
        "conaway told cnn",
        "sessions",
        "testimony",
        "met",
        "air force",
        "pacific command",
        "briefing",
        "trump",
        "president",
        "rene boucher",
        "rand paul",
        "minor injury",
        "bowling green",
        "paul"
      ],
      "Popularity": {
        "popularity": 48
      },
      "Sentiment": {
        "sentiment": -0.9879,
        "individual_sentiments": [
          0.5297,
          0.307,
          -0.9528
        ]
      },
      "RelatedArticles": {
        "top_articles": [
          {
            "headline": "Did Sessions mislead Congress about his interactions with Russia?",
            "url": "https://www.cbsnews.com/news/did-sessions-mislead-congress-about-his-interactions-with-russia/",
            "thumbnail": "https://www.bing.com/th?id=ON.7486CC918722A70321BBD371496F30A2&pid=News"
          },
          {
            "headline": "Trump Stops in Hawaii En Route to Asia",
            "url": "https://www.voanews.com/a/trump-hawaii-pearl-harbor-asia-trip/4099705.html",
            "thumbnail": "https://www.bing.com/th?id=ON.CCCA5F42648032139E3CE60CD622E660&pid=News"
          },
          {
            "headline": "Sen. Rand Paul Allegedly Assaulted at His Kentucky Home, Suspect Arrested",
            "url": "https://www.nbcnews.com/news/us-news/sen-rand-paul-assaulted-his-kentucky-home-suspect-arrested-n817591",
            "thumbnail": "https://www.bing.com/th?id=ON.C230C821D79BB6AF5BF11B8105C6CF0E&pid=News"
          }
        ]
      }
    },
    "connected": [
      "conaway told cnn"
    ],
    "name": "conaway told cnn"
  },
  {
    "elements": {
      "RelatedTopics": [
        "conaway told cnn",
        "sessions",
        "testimony",
        "met",
        "air force",
        "pacific command",
        "briefing",
        "trump",
        "president",
        "rene boucher",
        "rand paul",
        "minor injury",
        "bowling green",
        "paul"
      ],
      "Popularity": {
        "popularity": 48
      },
      "Sentiment": {
        "sentiment": -0.9879,
        "individual_sentiments": [
          0.5297,
          0.307,
          -0.9528
        ]
      },
      "RelatedArticles": {
        "top_articles": [
          {
            "headline": "Did Sessions mislead Congress about his interactions with Russia?",
            "url": "https://www.cbsnews.com/news/did-sessions-mislead-congress-about-his-interactions-with-russia/",
            "thumbnail": "https://www.bing.com/th?id=ON.7486CC918722A70321BBD371496F30A2&pid=News"
          },
          {
            "headline": "Trump Stops in Hawaii En Route to Asia",
            "url": "https://www.voanews.com/a/trump-hawaii-pearl-harbor-asia-trip/4099705.html",
            "thumbnail": "https://www.bing.com/th?id=ON.CCCA5F42648032139E3CE60CD622E660&pid=News"
          },
          {
            "headline": "Sen. Rand Paul Allegedly Assaulted at His Kentucky Home, Suspect Arrested",
            "url": "https://www.nbcnews.com/news/us-news/sen-rand-paul-assaulted-his-kentucky-home-suspect-arrested-n817591",
            "thumbnail": "https://www.bing.com/th?id=ON.C230C821D79BB6AF5BF11B8105C6CF0E&pid=News"
          }
        ]
      }
    },
    "connected": [
      "conaway told cnn"
    ],
    "name": "conaway told cnn"
  },
  {
    "elements": {
      "RelatedTopics": [
        "conaway told cnn",
        "sessions",
        "testimony",
        "met",
        "air force",
        "pacific command",
        "briefing",
        "trump",
        "president",
        "rene boucher",
        "rand paul",
        "minor injury",
        "bowling green",
        "paul"
      ],
      "Popularity": {
        "popularity": 48
      },
      "Sentiment": {
        "sentiment": -0.9879,
        "individual_sentiments": [
          0.5297,
          0.307,
          -0.9528
        ]
      },
      "RelatedArticles": {
        "top_articles": [
          {
            "headline": "Did Sessions mislead Congress about his interactions with Russia?",
            "url": "https://www.cbsnews.com/news/did-sessions-mislead-congress-about-his-interactions-with-russia/",
            "thumbnail": "https://www.bing.com/th?id=ON.7486CC918722A70321BBD371496F30A2&pid=News"
          },
          {
            "headline": "Trump Stops in Hawaii En Route to Asia",
            "url": "https://www.voanews.com/a/trump-hawaii-pearl-harbor-asia-trip/4099705.html",
            "thumbnail": "https://www.bing.com/th?id=ON.CCCA5F42648032139E3CE60CD622E660&pid=News"
          },
          {
            "headline": "Sen. Rand Paul Allegedly Assaulted at His Kentucky Home, Suspect Arrested",
            "url": "https://www.nbcnews.com/news/us-news/sen-rand-paul-assaulted-his-kentucky-home-suspect-arrested-n817591",
            "thumbnail": "https://www.bing.com/th?id=ON.C230C821D79BB6AF5BF11B8105C6CF0E&pid=News"
          }
        ]
      }
    },
    "connected": [
      "conaway told cnn"
    ],
    "name": "conaway told cnn"
  },
  {
    "elements": {
      "RelatedTopics": [
        "conaway told cnn",
        "sessions",
        "testimony",
        "met",
        "air force",
        "pacific command",
        "briefing",
        "trump",
        "president",
        "rene boucher",
        "rand paul",
        "minor injury",
        "bowling green",
        "paul"
      ],
      "Popularity": {
        "popularity": 48
      },
      "Sentiment": {
        "sentiment": -0.9879,
        "individual_sentiments": [
          0.5297,
          0.307,
          -0.9528
        ]
      },
      "RelatedArticles": {
        "top_articles": [
          {
            "headline": "Did Sessions mislead Congress about his interactions with Russia?",
            "url": "https://www.cbsnews.com/news/did-sessions-mislead-congress-about-his-interactions-with-russia/",
            "thumbnail": "https://www.bing.com/th?id=ON.7486CC918722A70321BBD371496F30A2&pid=News"
          },
          {
            "headline": "Trump Stops in Hawaii En Route to Asia",
            "url": "https://www.voanews.com/a/trump-hawaii-pearl-harbor-asia-trip/4099705.html",
            "thumbnail": "https://www.bing.com/th?id=ON.CCCA5F42648032139E3CE60CD622E660&pid=News"
          },
          {
            "headline": "Sen. Rand Paul Allegedly Assaulted at His Kentucky Home, Suspect Arrested",
            "url": "https://www.nbcnews.com/news/us-news/sen-rand-paul-assaulted-his-kentucky-home-suspect-arrested-n817591",
            "thumbnail": "https://www.bing.com/th?id=ON.C230C821D79BB6AF5BF11B8105C6CF0E&pid=News"
          }
        ]
      }
    },
    "connected": [
      "conaway told cnn",
    ],
    "name": "conaway told cnn"
  }
]
```