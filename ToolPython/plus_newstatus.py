from menu import UI
from json import load, dump
from time import sleep
from color import color
import time
from version import version

ui = UI()
elsa = '''\
███████╗██╗     ███████╗ █████╗                                                           
██╔════╝██║     ██╔════╝██╔══██╗                                                          
█████╗  ██║     ███████╗███████║                                                          
██╔══╝  ██║     ╚════██║██╔══██║                                                          
███████╗███████╗███████║██║  ██║                                                          
╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝                                                          

 ██████╗ ██╗    ██╗ ██████╗     ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
██╔═══██╗██║    ██║██╔═══██╗    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
██║   ██║██║ █╗ ██║██║   ██║    ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
██║   ██║██║███╗██║██║   ██║    ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
╚██████╔╝╚███╔███╔╝╚██████╔╝    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
 ╚═════╝  ╚══╝╚══╝  ╚═════╝     ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
'''


# [0] Exit And Save"
# [1] Change Status"


def main():
    with open("..\src\statussetting.json", "r", encoding='utf-8') as f:
        data = load(f)
    print(f'{color.okcyan}{elsa}{color.reset}')
    print(f"                   {color.purple}Version: {version} {color.reset}")
    time.sleep(0.5)
    print()
    print(f"{color.warning}")
    ui.newstatus()
    print(f"{color.reset}")
    choice = input(f"{color.okcyan}Enter Your Choice:  {color.okgreen}")
    if choice == "0":
        print(f"{color.reset}")
        pass
    elif choice == "1":
        status(data, True)

    else:
        print(f"{color.fail}[INFO] {color.reset}Invalid Choice")


def status(data, all):
    print("")
    data['status']['number'] = input(f"{color.okcyan}How many line status do you want to change: {color.yellow}")
    if data['status']['number'].isdigit():
        data['status']['number'] = int(data['status']['number'])
        for i in range(data['status']['number']):
            index = i + 1
            StrJoin = ["status", str(index)]
            status_index = '_'.join(StrJoin)
            if index == 1:

                data['status'][status_index]['stt'] = input(f"{color.okcyan}Input your {index}st status: {color.warning}")
                data['status'][status_index]['time'] = input(f"{color.okcyan}Input time of {index}st status: {color.warning}")
            elif index == 2:
                data['status'][status_index]['stt'] = input(f"{color.okcyan}Input your {index}nd status: {color.warning}")
                data['status'][status_index]['time'] = input(f"{color.okcyan}Input time of {index}nd status: {color.warning}")
            elif index == 3:
                data['status'][status_index]['stt'] = input(f"{color.okcyan}Input your {index}th status: {color.warning}")
                data['status'][status_index]['time'] = input(f"{color.okcyan}Input time of {index}th status: {color.warning}")
            elif 3 < index < 11:
                data['status'][status_index]['stt'] = input(f"{color.okcyan}Input your {index}th status: {color.warning}")
                data['status'][status_index]['time'] = input(f"{color.okcyan}Input time of {index}th status: {color.warning}")
            else:
                print(f"{color.fail}Input only number from 01 to 10 {color.reset}")
            if data['status'][status_index]['time'].isdigit() :
                if int(data['status'][status_index]['time'])>0:
                    data['status'][status_index]['time'] = int(data['status'][status_index]['time'])
                else:
                    print(f"{color.fail}Input only number >0 {color.reset}")
            else:
                print(f"{color.fail}Input only number >0 {color.reset}")
    else:
        print(f'{color.fail}Wrong Input{color.reset}')
        status(data, all)
    file = open("..\src\statussetting.json", "w", encoding='utf-8')
    dump(data, file, indent=4,ensure_ascii=False)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


if __name__ == "__main__":
    main()
