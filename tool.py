card_list = []
card_dict = {}
global name_search
def welcometxt():
    print('*' * 30)
    print('欢迎使用[名片管理系统]')
    print()
    print('1. 新建名片')
    print('2. 显示全部')
    print('3. 查询名片')
    print()
    print('0. 退出系统')
    print('*' * 30)
def createcard():
    print('-' * 30)
    name = input('请输入您的姓名:')
    age = input('请输入您的年龄: ')
    tel = input('请输入您的电话: ')
    card_dict = {"name": name, "age": age, "tel": tel}
    global card_list
    card_list.append(card_dict)
    print(card_list)
    print('添加 %s 名片成功' % name)
def showcard():
    print('-' * 30)
    print('显示所有名片')
    global card_list
    if len(card_list) == 0:
        return
    for head in ['姓名', '年龄', '电话']:
        print(head, end='\t\t')
    print("")
    print("=" * 30)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["age"], card_dict["tel"]))
def searchcard():
    global name_search
    global card_dict
    print('-' * 30)
    name_search = input("请输入您要查询的名片： ")
    for card_dict in card_list:
        if card_dict["name"] == name_search:
            for head in ['姓名', '年龄', '电话']:
                print(head, end='\t\t')
            print("")
            print("=" * 30)
            print("%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["age"], card_dict["tel"]))
            print()
            deal_dict(card_dict)
            break
    else:
        print("没有找到%s的名片" % name_search)
def deal_dict(card_dict):
    global name_search
    print("请选择您接下来的操作: ")
    print("1. 修改名片")
    print("2. 删除名片")
    print("")
    print("0. 返回上级菜单")
    print('*' * 30)
    action = input("请输入您的选择: ")
    while True:
        if action == '1':
            print("请输入您要修改的属性: ")
            print("")
            print("1. 姓名")
            print("2. 年龄")
            print("3. 电话")
            print("")
            print("0. 返回上级菜单")
            print("")
            while True:
                action = input("请输入您要修改的属性: ")
                if action == '1':
                    name_modify = input("请输入修改后的姓名: ")
                    card_dict["name"] = name_modify
                    break
                elif action == '2':
                    age_modify = input("请输入修改后的年龄: ")
                    card_dict["age"] = age_modify
                    break
                elif action == '3':
                    tel_modify = input("请输入修改后的电话: ")
                    card_dict["tel"] = tel_modify
                    break
                elif action == '0':
                    return
                else:
                    print("输入错误，请重新输入")
                    break
        elif action == '2':
            for card_dict in card_list:
                if card_dict["name"] == name_search:
                    card_list.remove(card_dict)
            return
        elif action == '0':
            return
        else:
            print("输入错误，请重新输入")
            break

