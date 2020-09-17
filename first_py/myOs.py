#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding:utf-8
import os
import sys
# help(os)

print(sys.path)#获取python的环境变量,以list形式返回
#输出：['E:\\study\\Automantic\\jxz-code\\Course4']
print(os.listdir('./'))#获取指定目录下的文件及文件夹名称，以list形式返回
#输出：['access.log', 'b.txt', 'c.txt', 'course4作业.py', 'goods.txt', 'user_info.txt', '、', '函数.py']
print(os.getcwd())#获取当前目录
#输出：E:\study\Automantic\jxz-code\Course4
#print(os.chdir('E:\study\Automantic\jxz-code'))#更换当前目录
#print(os.rename('c.txt','a.txt'))#修改文件名称
print(os.mkdir('新目录'))#创建文件夹
print(os.rmdir('新目录'))#删除文件夹（只能删除空文件夹）
#print(os.makedirs('E:\\xixi\\haha'))#依次创建目录
#print(os.removedirs('E:\\xixi\\haha'))#依次删除非空目录
print(os.sep)#获取当前操作系统的路径分隔符
#输出：\
print(os.environ)#获取当前操作系统的环境变量
#输出：environ({'ALLUSERSPROFILE': 'C:\\ProgramData'})
print(os.pathsep)#获取当前系统的环境变量中每个路径的分隔符，linux是:，windows是;
#输出：;
print(os.path.abspath(__file__))#获取当前文件的绝对路径
#输出：E:\study\Automantic\jxz-code\Course4\函数.py
print(os.path.dirname(os.path.abspath(__file__)))#获取指定路径的父目录
#输出：E:\study\Automantic\jxz-code\Course4
print(os.path.isdir(os.path.abspath(__file__)))#判断指定路径是不是一个文件夹
#输出：False
print(os.path.isfile(os.path.abspath(__file__)))#判断指定路径是不是一个文件
#输出：True
print(os.path.join('一级','二级','三级','haha.txt'))#将内容以当前操作系统的路径分隔符拼接成一个路径
#输出：一级\二级\三级\haha.txt
print(os.path.split('E:\study\Automantic\jxz-code\Course4\函数.py'))#分割路径和文件名
#输出：('E:\\study\\Automantic\\jxz-code\\Course4', '函数.py')
print(os.path.exists('E:\study\Automantic\jxz-code\Course4\函数.py'))#判断目录或文件是否存在
#输出：True

print(os.name )                #获取操作系统平台
print(os.getcwd())             #获取现在的工作目录
print(os.listdir())            #获取某个目录下的所有文件名
#print(os.system() )            #用来运行shell命令
#print(os.remove())             #删除某个文件
#print(os.path.exists())        #检验给出的路径是否真地存在
#print(os.path.isfile())        #判断是否为文件;若是，返回值为真
#print(os.path.isdir())         #判断是否为文件夹;若是，返回值为真
print(os.path.abspath(""))   #获得绝对路径
#print(os.path.splitext())      #分离文件名与扩展名
#print(os.path.split())         #把一个路径拆分为目录+文件名的形式
#print(os.path.join(path,"")) #连接目录与文件名或目录
#print(os.path.basename(""))  #返回文件名
#print(os.path.dirname(""))   #返回文件路径 

'''
os.close(fd)                 #关闭文件描述符 fd
os.write(fd, str)            #写入字符串到文件描述符 fd中. 返回实际写入的字符串长度
os.getcwd()                  #返回当前工作目录
os.getcwdu()                 #返回一个当前工作目录的Unicode对象
os.open(file, flags[, mode]) #打开一个文件，并且设置需要的打开选项，mode参数是可选的
os.openpty()                 #打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
os.read(fd, n)               #从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
os.readlink(path)            #返回软链接所指向的文件
os.remove(path)              #删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
os.removedirs(path)          #递归删除目录。
os.rename(src, dst)          #重命名文件或目录，从 src 到 dst
os.renames(old, new)         #递归地对目录进行更名，也可以对文件进行更名。
os.rmdir(path)               #删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
os.lseek(fd, pos, how)       #设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效

os.access(path, mode)            检验权限模式
os.chdir(path)                   改变当前工作目录
os.chflags(path, flags)          设置路径的标记为数字标记。
  path -- 文件名路径或目录路径。
  flags -- 可以是以下值：
  stat.UF_NODUMP: 非转储文件
  stat.UF_IMMUTABLE: 文件是只读的
  stat.UF_APPEND: 文件只能追加内容
  stat.UF_NOUNLINK: 文件不可删除
  stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
  stat.SF_ARCHIVED: 可存档文件(超级用户可设)
  stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
  stat.SF_APPEND: 文件只能追加内容(超级用户可设)
  stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
  stat.SF_SNAPSHOT: 快照文件(超级用户可设)
os.chmod(path, mode)                       更改权限
  path -- 文件名路径或目录路径。
  stat.S_IXOTH: 其他用户有执行权0o001
  stat.S_IWOTH: 其他用户有写权限0o002
  stat.S_IROTH: 其他用户有读权限0o004
  stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
  stat.S_IXGRP: 组用户有执行权限0o010
  stat.S_IWGRP: 组用户有写权限0o020
  stat.S_IRGRP: 组用户有读权限0o040
  stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
  stat.S_IXUSR: 拥有者具有执行权限0o100
  stat.S_IWUSR: 拥有者具有写权限0o200
  stat.S_IRUSR: 拥有者具有读权限0o400
  stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
  stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
  stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
  stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
  stat.S_IREAD: windows下设为只读
  stat.S_IWRITE: windows下取消只读
os.chown(path, uid, gid)                                          # 更改文件所有者
os.chroot(path)                                                   # 改变当前进程的根目录
os.closerange(fd_low, fd_high)                                    # 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
os.dup(fd)                                                        # 复制文件描述符 fd
os.dup2(fd, fd2)                                                  # 将一个文件描述符 fd 复制到另一个 fd2
os.fchdir(fd)                                                     # 通过文件描述符改变当前工作目录
os.fchmod(fd, mode)                                               # 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
os.fchown(fd, uid, gid)                                           # 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
os.fdatasync(fd)                                                  # 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
os.fdopen(fd[, mode[, bufsize]])                                  # 通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
os.fpathconf(fd, name)                                            # 返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
os.fstat(fd)                                                      # 返回文件描述符fd的状态，像stat()。
os.fstatvfs(fd)                                                   # 返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
os.fsync(fd)                                                      # 强制将文件描述符为fd的文件写入硬盘。
os.ftruncate(fd, length)                                          # 裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
os.isatty(fd)                                                     # 如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
os.lchflags(path, flags)                                          # 设置路径的标记为数字标记，类似 chflags()，但是没有软链接
os.lchmod(path, mode)                                             # 修改连接文件权限
os.lchown(path, uid, gid)                                         # 更改文件所有者，类似 chown，但是不追踪链接。
os.link(src, dst)                                                 # 创建硬链接，名为参数 dst，指向参数 src
os.listdir(path)                                                  # 返回path指定的文件夹包含的文件或文件夹的名字的列表。
os.lstat(path)                                                    # 像stat(),但是没有软链接
os.major(device)                                                  # 从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
os.makedev(major, minor)                                          # 以major和minor设备号组成一个原始设备号
os.makedirs(path[, mode])                                         # 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
os.minor(device)                                                  # 从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
os.mkdir(path[, mode])                                            # 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
os.mkfifo(path[, mode])                                           # 创建命名管道，mode 为数字，默认为 0666 (八进制)
os.mknod(filename[, mode=0600, device])                           # 建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
os.pathconf(path, name)                                           # 返回相关文件的系统配置信息。
os.pipe()                                                         # 创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
os.popen(command[, mode[, bufsize]])                              # 从一个 command 打开一个管道
os.stat(path)                                                     # 获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
os.stat_float_times([newvalue])                                   # 定stat_result是否以float对象显示时间戳
os.statvfs(path)                                                  # 获取指定路径的文件系统统计信息
os.symlink(src, dst)                                              # 创建一个软链接
os.tcgetpgrp(fd)                                                  # 返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
os.tcsetpgrp(fd, pg)                                              # 设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
os.tempnam([dir[, prefix]])                                       # 返回唯一的路径名用于创建临时文件。
os.tmpfile()                                                      # 返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
os.tmpnam()                                                       # 为创建一个临时文件返回一个唯一的路径
os.ttyname(fd)                                                    # 返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
os.unlink(path)                                                   # 删除文件路径
os.utime(path, times)                                             # 返回指定的path文件的访问和修改的时间。
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]]) # 输出在文件夹中的文件名通过在树中游走，向上或者向下。
'''





