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
[[todo]]
```