if __name__ == '__main__':
    n = int(input())
    farr = list(set(map(int, input().split())))
    """farr.sort(reverse=True)
    print(farr[1])"""

    farr.remove(max(farr))
    print(max(farr))