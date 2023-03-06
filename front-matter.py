# coding: utf-8

import os,platform,sys
import time

import frontmatter

# 获取标题和文件创建日期
def update_front_matter(file,is_force=False):

    with open(file, 'r', encoding='utf-8') as f:
       post = frontmatter.loads(f.read())
    
    is_write = False
      
    # 获取标题   
    if (not post.metadata.get('title', None)) or is_force:  
        # 去掉 .md 后缀
        title=file.split('/')[-1][:-3]
        print('获取标题 '+title)
        post['title'] =title
        if not is_write:
            is_write = True


    if (not post.metadata.get('date', None)) or is_force:
        
        # macOS
        if platform.system() =='Darwin':
            timeArray = time.localtime(os.stat(file).st_birthtime)
        # Window下 os.path(file).getctime()
        else:
            timeArray = time.localtime(os.path(file).getctime())
        createTime = time.strftime("%Y-%m-%d %H:%M", timeArray)
        print('获取创建时间 '+createTime)
        post['date'] = createTime
        if not is_write:
            is_write = True

    if is_write:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
  
# 添加 front matter 属性
def add_property(file,attribute,value):
    with open(file, 'r', encoding='utf-8') as f:
        post = frontmatter.loads(f.read())
    is_write = False

    if not post.metadata.get(attribute, None):
        post[attribute] = value
        is_write = True

    if is_write:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))


# 递归获取提供目录下所有文件
def list_all_files(root_path, ignore_dirs=[]):
    files = []
    default_dirs = [".git", ".obsidian", ".config"]
    ignore_dirs.extend(default_dirs)

    for parent, dirs, filenames in os.walk(root_path):
        dirs[:] = [d for d in dirs if not d in ignore_dirs]
        filenames = [f for f in filenames if not f[0] == '.']
        for file in filenames:
            if file.endswith(".md"):
                files.append(os.path.join(parent, file))
    return files

class Things():
    def __init__(self, username='nobody'):
        self.username = username

    def add_titleAndDate(self):
        for file in files:    
            print("---------------------------------------------------------------")
            print('current file: ', file)
            update_front_matter(file)
            time.sleep(1)
        print("添加标题和日期完成!")

    def add_titleAndDate_force(self):
        for file in files:    
            print("---------------------------------------------------------------")
            print('current file: ', file)
            update_front_matter(file,True)
            time.sleep(1)
        print("(强制)添加标题和日期完成!")


    def get_tag(self):
        print("未施工 ... ...")
        time.sleep(1)
        print("done!")

    def add_pros(self):
        attribute=input('请输入属性名（比如 category）：')
        value=input('请输入属性值：')
        for file in files:    
            print("---------------------------------------------------------------")
            print('current file: ', file)
            add_property(file,attribute,value)
            time.sleep(1)
        print("批量添加 yaml 属性名和属性值 完成!")


class Menu():
    def __init__(self):
        self.thing = Things()
        self.choices = {
            "1": self.thing.add_titleAndDate,
            "1f": self.thing.add_titleAndDate_force,
            "2": self.thing.get_tag,
            "3": self.thing.add_pros,
            "4": self.quit
        }

    def display_menu(self):
        print("current dir: ", os.path.dirname(os.path.abspath(__file__)))
        print("""
    请选择操作：
    1. 添加标题和日期，如果存在则不操作 （1f，强制覆盖）
    2. 识别标签(未完工)
    3. 批量添加 yaml 属性名和属性值
    4. quit
""")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = input("Enter an option: ")
            except Exception as e:
                print("Please input a valid option!");continue

            choice = str(choice).strip()
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def quit(self):
        print("\nThank you for using this script!\n")
        sys.exit(0)


if __name__ == '__main__':
    # 默认忽略文件
    ignore_dirs = [".obsidian", "Write"]
    files = list_all_files('./', ignore_dirs=ignore_dirs)
    Menu().run()




   
