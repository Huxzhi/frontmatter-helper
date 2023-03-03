# coding: utf-8

import os,platform
import time

import frontmatter

def update_front_matter(file):

    with open(file, 'r', encoding='utf-8') as f:
       post = frontmatter.loads(f.read())
    
    is_write = False
      
    # 获取标题   
    if not post.metadata.get('title', None):  
        # 去掉 .md 后缀
        title=file.split('/')[-1][:-3]
        print('获取标题 '+title)
        post['title'] =title
        if not is_write:
            is_write = True


    if not post.metadata.get('date', None):
        
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


if __name__ == "__main__":
    # 默认忽略文件
    ignore_dirs = [".obsidian", "Write"]
    files = list_all_files('./', ignore_dirs=ignore_dirs)

    print("current dir: ", os.path.dirname(os.path.abspath(__file__)))
    for file in files:
        print(platform.system())    
        print("---------------------------------------------------------------")
        print('current file: ', file)
        update_front_matter(file)
        time.sleep(1)
