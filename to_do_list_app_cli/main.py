from todo import get_tasks, add_task, remove_task  # 引入任務管理函式

def show_menu():
    # 列印出主選單，提示使用者可執行的動作
    print("\nTo-Do List Menu")
    print("1. View Tasks")    # 查看任務列表
    print("2. Add Task")      # 新增任務
    print("3. Remove Task")   # 刪除任務
    print("4. Exit")          # 離開程式

def main():
    # 程式主要執行流程，持續顯示選單並等待使用者輸入
    while True:
        show_menu()  # 顯示功能選單

        choice = input("Choose an option (1-4): ")  # 讀取使用者選擇

        if choice == "1":  # 使用者選擇查看任務
            tasks = get_tasks()  # 讀取任務清單
            if not tasks:  # 如果清單為空
                print("No tasks found.")  # 顯示無任務訊息
            else:
                print("\nYour Tasks:")  # 印出任務標題
                # 以編號搭配任務內容逐行顯示
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":  # 使用者選擇新增任務
            task = input("Enter a new task: ")  # 讀取任務內容
            if add_task(task):  # 嘗試加入任務，成功回傳True
                print("Task added.")  # 新增成功提示
            else:
                print("Empty task not added.")  # 空任務不加入提示

        elif choice == "3":  # 使用者選擇刪除任務
            tasks = get_tasks()  # 讀取目前任務
            if not tasks:  # 沒有任務時
                print("No tasks to remove.")  # 提示沒有可刪除任務
                continue  # 回到迴圈開始

            try:
                index = int(input("Enter the task number to remove: "))  # 輸入要刪除的任務編號
                removed = remove_task(index)  # 嘗試刪除該任務
                if removed:  # 刪除成功
                    print(f"Removed: {removed}")  # 顯示被刪除的任務內容
                else:
                    print("Invalid task number.")  # 輸入序號不合法的錯誤提示
            except ValueError:
                # 輸入非整數時，提醒使用者輸入正確格式
                print("Please enter a valid number.")

        elif choice == "4":  # 使用者選擇離開
            print("Goodbye!")  # 道別訊息
            break  # 跳出無限迴圈結束程式

        else:
            # 輸入不在1-4之間的錯誤處理提示
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()  # 只有被當作主程式執行時才啟動main函式
