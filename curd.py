def addData():
    pass


data_list = []
id_list = []
while True:
    print("--------- CRUD OPERATIONSS IN PYTHON---------")
    print("1.ADD DATA")
    print("2.REMOVE DATA")
    print("3.UPDATE DATA")
    print("4.LIST DATA")
    print("5.EXIT")
    choice = input("----------------SELECT-----------")
    if choice == '1':
        while True:

                name = input("ENTER YOUR NAME")
                if name.isalpha():
                    break

                print("Your name  should be a string!!!!!!")
        while True:

                id = input("ENTER YOUR ID")
                if id.isdigit():
                    break

                print("Your id  should be a digit!!!!!!")

        #id = int(input("ENTER YOUR ID"))


        data = {}
        data["name"] = name
        data["id"] = id
        print("data : ", data)
        data_list.append(data)
        input("added successfully, press enter to continue")
        print("Items are : ", data_list)

    elif choice == '2':
        print("1.REMOVE ALL DATA")
        print("2.REMOVE SINGLE DATA")
        print("3.BACK")
        choice = input("Enter your choice")
        while True:
            if choice == '1':
                data_list.clear()
                print(data_list)
                print("REMOVE ALL DATAS")
                break
            elif choice == '2':
                id = input("enter id")
                #id = int(input("Enter id"))
                flag = 0
                for item in data_list:
                    if id == item['id']:
                        data_list.remove(item)
                        flag = 1
                        print("Item deleted")
                        print("Data : ", data_list)
                        input("Press enter to continue...")

                        break
                if flag == 1:
                    print("Item deleted")
                    print("Data : ", data_list)
                else:
                    print("Item not found")
                print(id_list)
                break
            elif choice == '3':
                print("BACK TO CRUD OPERATION")

                break

    elif choice == '3':
        id = input("enter your id")
        #id = int(input("enter your id"))
        for item in data_list:
            print(f"item id {item['id']} and its type {type(item['id'])} ")
            print(f"receved id {id} and its type {type(id)} ")
            if id == item['id']:
                print("item updating")
                item['name'] = input("Enter name to update : ")
                print("item updated")
                print("Data : ", data_list)

                break
            elif id != item['id']:
                print("no matching result")
                break
            else:
                print("invalid input")
        else:
            print("Item is empty")
        input("Press enter to continue...")

    elif choice == '4':
        print("1.LIST ALL DATA")
        print("2.LIST BY ID")
        choice = input("enter your choice")
        while True:
            if choice == '1':
                print("data: ", data_list)
                input("Press enter to continue...")
                break

            if choice == '2':
                id = input("enter id")
                #id = int(input("Enter id"))
                flag = 0
                for item in data_list:

                    if item["id"] == id:
                        print("Item is ", item)
                        flag = 1
                        input("Press enter to continue...")

                        break

                #break
                if flag == 0:
                    print("NO MATCHING RESULT FOUND")
                    break
                break

            else:
                input("Press enter to continue...")
                break







    elif choice == '5':
         print("............YOU ARE EXITED........")
         input("press enter to continue....")
