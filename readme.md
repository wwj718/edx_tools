#edx tools
在本地管理和调试远程edx服务器

#Install 
```bash
pip install fabric
git clone https://github.com/wwj718/edx_tools.git
cd edx_tools
```

#setting
在settings.py里填写服务器的账户和密码

#Usage
###查看所有可用指令
`fab -f edx.py -l`

###查看服务器状态
`fab -f edx.py status`

###重启edxapp
`fab -f edx.py restart_edxapp`

###查看日志
*  查看最新10条lms日志：`fab -f edx.py tailLog 10,lms`
*  查看最新50条cms日志：`fab -f edx.py tailLog 50,cms`

###进入lms shell
`fab -f edx.py shell`

###启用调试模式
`fab -f edx.py devstack`

###编译静态文件
*  编译lms：`fab -f edx.py update_assets:lms`
*  编译cms：`fab -f edx.py update_assets:cms`

###生成map文件（用于调试scss）
`fab -f edx.py create_scss_maps`

###实时编译scss
`fab -f edx.py watch_assets`
    
###edxapp.pip
*  查看环境中有安装了哪些依赖库：`fab -f edx.py edxapp_pip`
