def main():
    yell("this", "is", "cs50", "course", "finished")
    
def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)
    
if __name__ == '__main__':
    main()