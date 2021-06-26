cp crisis-dataset/crisisload.py ./
find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done;
find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done;
rm -rf tweets-C26; mkdir tweets-C26; cp crisis-dataset/C26\ Dataset/Crisis\ Tweets/*-tweets_labeled.csv tweets-C26/; cp crisis-dataset/C26\ Dataset/*.csv  tweets-C26/
rm -rf tweets-C6; mkdir tweets-C6; cp crisis-dataset/C6\ Dataset/Crisis\ Tweets\ C6/*.csv tweets-C6/; cp crisis-dataset/C6\ Dataset/*.csv  tweets-C6/
rm -rf tweets-C8; mkdir tweets-C8; cp crisis-dataset/C8\ Dataset/*.csv tweets-C8/
