find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done;
find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done;
rm -rf tweets_labeled-C26; mkdir tweets_labeled-C26; cp crisis-dataset/C26\ Dataset/Crisis\ Tweets/*-tweets_labeled.csv tweets_labeled-C26/; cp crisis-dataset/C26\ Dataset/*.csv  tweets_labeled-C26/
rm -rf tweets_labeled-C6; mkdir tweets_labeled-C6; cp crisis-dataset/C6\ Dataset/Crisis\ Tweets\ C6/*.csv tweets_labeled-C6/; cp crisis-dataset/C6\ Dataset/*.csv  tweets_labeled-C6/
rm -rf tweets_labeled-C8; mkdir tweets_labeled-C8; cp crisis-dataset/C8\ Dataset/*.csv tweets_labeled-C8/