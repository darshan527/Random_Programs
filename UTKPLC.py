def preference(orderList: list, offerList: list) -> None:
    for i in range(3):
        if orderList[i] == offerList[0] or orderList[i] == offerList[1]:
            print(orderList[i])
            break


if __name__ == "__main__":
    for T in range(int(input())):
        orderList = input().split()
        offerList = input().split()
        preference(orderList, offerList)
