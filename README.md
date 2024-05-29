# 项目名称：个人课程设计

这是一个基于Python和PyQt6的登录和注册系统，同时包含了用户和武器的管理功能。

## 环境

- Python 3.8+
- PyQt6
- pandas
- json
- qfluentwidgets

## 文件说明

- `login_gui_system.py`：定义了登录和注册窗口的GUI，以及登录和注册的逻辑。
- `main.py`：主程序入口，包含了用户和武器的类定义，以及主窗口的定义。同时，还包含了从Excel文件和JSON文件中同步武器列表的函数。
- `gui.py`：定义了主窗口的GUI。
- `player_loader.py`：定义了用户加载器，用于从JSON文件中加载用户信息。
- `user_list.json`：存储用户信息的JSON文件。

## 使用说明

1. 运行`main.py`启动程序。
2. 在登录窗口中输入用户名和密码进行登录，或点击注册按钮进行注册。
3. 注册时，用户名和密码不能为空，密码长度必须至少为6位，且必须包含至少一个数字和一个字母。
4. 登录成功后，会打开主窗口。

## 注意事项

- 用户信息存储在`user_list.json`文件中，每个用户的信息包括用户名、密码、武器列表和用户类型。
- 武器信息存储在Excel文件中，每个武器的信息包括武器名称、伤害、弹药、剩余弹药、类型和射击模式。
- 程序启动时，会从Excel文件和`user_list.json`文件中同步武器列表。

## 项目目标

本项目旨在实践Python和PyQt6的使用，以及文件读写和JSON处理等技术。同时，通过实现登录和注册功能，以及用户和武器的管理功能，提高编程能力和解决实际问题的能力。

## 项目进度

1. 实现用户登录和注册功能。
2. 实现用户和武器的管理功能，包括添加、删除、修改用户信息和武器信息。
3. 实现Excel文件和JSON文件的读写功能。
4. 实现用户信息的加密存储。 
5. 实现用户信息的保存和加载功能。
6. 实现用户信息的校验功能，防止恶意攻击。
7. 实现用户信息的存储和加载功能。
8. 实现武器信息的存储和加载功能。
9. 实现武器信息的校验功能，防止恶意攻击。
10. 实现武器信息的搜索功能。
11. 实现武器信息的排序功能。
12. 实现武器信息的导出功能。
13. 实现武器信息的导入功能。
14. 实现用户信息的导出功能。
15. 实现用户信息的导入功能。
16. 实现用户信息的搜索功能。
17. 实现用户信息的排序功能。
18. 实现用户信息的统计功能。
19. 实现武器信息的删除功能。
20. 通过异常处理机制，完善程序的鲁棒性。