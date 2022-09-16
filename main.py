import tool
while True:
    tool.welcometxt()
    action = input("请选择您的操作：")
    print("您选择的操作是[%s]" % action)
    if action == '1':
        tool.createcard()
    elif action == '2':
        tool.showcard()
    elif action == '3':
        tool.searchcard()
    elif action == '0':
        print("欢迎再次使用名片管理系统")
        break
    else:
        print("输入错误，请重新输入。")


