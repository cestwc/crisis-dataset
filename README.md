# crisis-dataset
Three datasets for topic modelling

### Usage
```
bash crisis-dataset/extract.sh >/dev/null
pip install tweet-preprocessor
```

```python
from crisisload import CrisisTweetsLoader
crisis = CrisisTweetsLoader()
tweets_labeled, tweets_unlabeled, wikitruth = crisis('C6')
```
