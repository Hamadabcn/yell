# Map in Python is a function that works as an iterator to return a result after applying a function 
# to every item of an iterable (tuple, lists, etc.)
def main():
    yell("this", "is", "cs50", "course", "finished")
    
def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)
    
if __name__ == '__main__':
    main()