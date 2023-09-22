import urllib

if __name__ == '__main__':
    # Data download from url
    urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt",
                               filename="./data/dataset/ratings_train.txt")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt",
                               filename="./data/dataset/ratings_test.txt")