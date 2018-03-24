def displayMenu():
    print("-"*30)
    print("名片管理系统     v8.1")
    print("1:添加名片")
    print("2:删除名片")
    print("3:修改名片")
    print("4:查询名片")
    print("5:获取所有名片信息")
    print("6:退出系统")
    print("-" * 30)
namelist = []
i = 0
while i<1:
    displayMenu()
    def getChoice():
        selectedKey = input("请输入要执行操作的序号：")
        return int(selectedKey)
    key = getChoice()
    def addname():
        newname = input("请输入姓名：")
        namelist.append(newname)
    if key == 1:
        addname()
    elif key == 2:
        oldname = input("请输入姓名：")
        namelist.remove(oldname)
    elif key == 3:
        name = input("请要输入要修改姓名：")
        name1 = input("请要输入修改后姓名：")
        namelist[namelist.index(name)] = name1
    elif key == 4:
        name2 = input("请要输入要查询姓名：")
        if name2 not in namelist:
            print("不存在")
        else:
            print(name2)
    elif key ==5:
        for j in namelist:
            print(j)

    elif key ==6:
        exit()


