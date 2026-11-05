import shutil
import os
import tkinter
from tkinter import filedialog

# auther: ChatGPT-4 & RedSun
# level: 0.01
# 功能: 根据规则文件夹删除目标文件夹内重复文件，或根据规则文件夹复制源文件夹内缺失文件到目标文件夹
# 以及删除wallpaper因更新慢导致的残留文件


# 冗余代码
# # 调用生成器
# gen = get_directory("/path/to/root")
# # 获取深度为1的目录内容
# folders, files = next(gen)

def Recycle_Bin():
    #检测当前目录下是否有回收站文件夹
    recycle_bin_path = os.path.join('.', 'Recycle_Bin')
    if not os.path.exists(recycle_bin_path):
        os.makedirs(recycle_bin_path)
    return recycle_bin_path

def select_folder():
    # 创建隐藏的根窗口
    root = tkinter.Tk()
    root.withdraw()
    
    # 打开文件夹选择对话框
    folder_path = filedialog.askdirectory(
        title="选择文件夹",
        initialdir="."  # / 或 .
    )
    return folder_path


def get_directory(root_dir):
    for dirpath, dirnames, files_ in os.walk(root_dir, topdown=True):
        # 计算当前目录的深度（root_dir为深度0）
        current_depth = dirpath[len(root_dir):].count(os.sep)
        if current_depth == 0:
            # 创建存储文件夹和文件的列表
            folders = []
            file_list = []
            
            # 处理文件夹
            for d in dirnames:
                # folder_path = os.path.join(dirpath, d)
                # folders.append((d, folder_path))  # (文件夹名, 完整路径)
                folders.append(d)
            
            # 处理文件
            for f in files_:
                file_list.append(f)
            
            # 返回结果并停止后续遍历
            # yield folders, file_list, dirpath
            yield folders, file_list
            dirnames[:] = []  # 阻止继续遍历子目录
            return  # 结束生成器
            
        if current_depth > 2:
            # 如果当前深度大于2，则不继续遍历子目录
            dirnames[:] = []
            continue

def Delete_Files(rules_folder, target_folder, recycle_bin):

    rules_ = get_directory(rules_folder)
    rules_folders, rules_files = next(rules_)

    target_ = get_directory(target_folder)
    target_folders, target_files = next(target_)

    # 删除目标文件夹中与规则文件夹重复的文件
    for temp_target_folders in target_folders:
        if temp_target_folders in rules_folders:
                # 移动到回收站
                target_file_path = os.path.join(target_folder, temp_target_folders)
                os.rename(target_file_path, os.path.join(recycle_bin, temp_target_folders))
                print(f"已删除: {target_file_path} 并移动到回收站")
    for temp_target_files in target_files:
        if temp_target_files in rules_files:
                # 移动到回收站
                target_file_path = os.path.join(target_folder, temp_target_files)
                os.rename(target_file_path, os.path.join(recycle_bin, temp_target_files))
                print(f"已删除: {target_file_path} 并移动到回收站")


def Copy_Files(rules_folder, target_folder, source_folder):

    rules_ = get_directory(rules_folder)
    rules_folders, rules_files = next(rules_)

    source_ = get_directory(source_folder)
    source_folders, source_files = next(source_)

    for temp_source_folders in source_folders:
        if temp_source_folders not in rules_folders:
            source_file_path = os.path.join(source_folder, temp_source_folders)
            target_file_path = os.path.join(target_folder, temp_source_folders)
            if not os.path.exists(target_file_path) and os.path.exists(source_file_path):
                # 复制文件夹和其目录下所有内容
                shutil.copytree(source_file_path, target_file_path)
                print(f"已复制: {source_file_path} 到 {target_file_path}")
    for temp_source_files in source_files:
        if temp_source_files in rules_files:
            source_file_path = os.path.join(source_folder, temp_source_files)
            target_file_path = os.path.join(target_folder, temp_source_files)
            if not os.path.exists(target_file_path) and os.path.exists(source_file_path):
                # 复制文件
                shutil.copy2(source_file_path, target_file_path)
                print(f"已复制: {source_file_path} 到 {target_file_path}")


def Delete_Wallpaper_Residue(target_folder, recycle_bin):
    directory_ = get_directory(target_folder)
    target_folders, target_files = next(directory_)
    HasJson = []
    #目标文件夹存在文件，抛出可能不是wallpaper目录的警告
    if target_files:
        print("警告: 目标文件夹中存在文件，可能不是wallpaper目录")
    for temp_target_folders in target_folders:
        #获取下一级目录内容
        temp_target_folders_path = os.path.join(target_folder, temp_target_folders)
        directory2 = get_directory(temp_target_folders_path)
        sub_folders, sub_files = next(directory2)
        #匹配有无.json文件
        json_found = False
        for f in sub_files:
            if f.endswith('.json'):
                json_found = True
                break
        total_items = len(sub_folders) + len(sub_files)
        if not json_found:
            #计算sub_folders和sub_files的总数
            if total_items >= 2:
                print(f"警告: 目录 {temp_target_folders_path} 下无.json文件，但超过预期文件夹和文件数目，可能不是残留文件，请前往回收站文件夹查看")
            #elif total_items <= 1:
            else:
                print(f"已移除 {temp_target_folders_path}")
            #移动到回收站
            os.rename(temp_target_folders_path, os.path.join(recycle_bin, os.path.basename(temp_target_folders)))
        else:
            if total_items <= 2:
                print(f"警告: 目录 {temp_target_folders_path} 下有.json文件，但文件夹和文件数目过少，可能存在残留文件，请前往查看")
                HasJson.append(temp_target_folders + "\n")
    if HasJson:
        with open("./WarningJson.txt", "w", encoding='utf-8') as f:
            f.writelines(HasJson)
        exit(0)

# 使用示例
if __name__ == "__main__":
    print("欢迎使用“规则复制”")
    print("本脚本功能:1.删除目标文件夹内与规则文件夹重复的文件 2.根据规则文件夹内没有的文件将源文件夹复制到目标文件夹")
    print("3.删除wallpaper因更新慢导致的残留文件")
    recycle_bin = Recycle_Bin()
    #目标文件夹选择
    print("请选择目标文件夹:")
    target_folder = select_folder()
    print("选择的目标文件夹是:", target_folder)
    #操作选择
    print("选择的操作是:\n1(删除模式)\n2(复制模式)\n3(清理wallpaper残留ini文件)")
    mode = input("")
    if mode == "3":
        print("进入wallpaper残留ini文件清理模式")
        #调用删除函数
        Delete_Wallpaper_Residue(target_folder, recycle_bin)
    else: 
        #规则文件夹选择
        print("请选择规则文件夹:")
        rules_folder = select_folder()
        print("选择的规则文件夹是:", rules_folder)
        if mode == "2":
            print("进入复制模式")
            #源文件夹选择
            print("请选择源文件夹:")
            source_folder = select_folder()
            print("选择的源文件夹是:", source_folder)
            #调用复制函数
            Copy_Files(rules_folder, target_folder, source_folder)
        elif mode == "1":
            print("进入删除模式")
            #wallpaper残留删除模式
            Delete_Files(rules_folder, target_folder, recycle_bin)
        else:
            print("无效的操作模式")
    print("回收站:", recycle_bin)
    print("具有删除性质的模式中，请确认回收站内文件无误后再手动删除，按任意键键退出程序")
    input()