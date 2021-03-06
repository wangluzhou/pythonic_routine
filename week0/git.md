# git踩坑之路
在环境踩坑之旅中，git一定会占据一个很重要的位置。不要回避，参考[廖雪峰的教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013745374151782eb658c5a5ca454eaa451661275886c6000)，我们一步一步地来。
## git名词解释

### 工作区\(working directory\)

就是你的.git所在那个文件夹下

### 版本库\(Repository\)

即`.git`文件夹

### git status

查看你当前的库的状态

```
lukes-MacBook:Py101-004 luke$ git status
On branch master
Your branch and 'origin/master' have diverged,
and have 2 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)
nothing to commit, working tree clean
```

## git问题汇总

### git 删除已经track的文件

[参考文章](http://www.pfeng.org/archives/840)

在git中如果想忽略掉某个文件，不让这个文件提交到版本库中，可以使用修改根目录中 .gitignore 文件的方法（如无，则需自己手工建立此文件）。这个文件每一行保存了一个匹配的规则例如：

```
# 此为注释 – 将被 Git 忽略

*.a       # 忽略所有 .a 结尾的文件
!lib.a    # 但 lib.a 除外
/TODO     # 仅仅忽略项目根目录下的 TODO 文件，不包括 subdir/TODO
build/    # 忽略 build/ 目录下的所有文件
doc/*.txt # 会忽略 doc/notes.txt 但不包括 doc/server/arch.txt
```

规则很简单，不做过多解释，但是有时候在项目开发过程中，突然心血来潮想把某些目录或文件加入忽略规则，按照上述方法定义后发现并未生效，原因是.gitignore只能忽略那些原来没有被track的文件，**如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的**。那么解决方法就是先把本地缓存删除（改变成未track状态），然后再提交：

```
git rm -r --cached .
git add .
git commit -m 'update .gitignore'
```

# 关于git无法忽视\_book的最终原因

好吧，是我把.gitignore写成.gitigorne了

# git切换分支

```
git branch -a 查看所有分支
git branch 查看当前分支
git checkout master 切换到master分支
```

## 关于git无法识别.gitignore的原因



