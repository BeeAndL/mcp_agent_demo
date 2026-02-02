import os
import platform
import socket

def get_host_info() -> str:
    """
    get host info of this pc
    return:
        host info
    """
    try:
        # 获取主机名
        hostname = socket.gethostname()
        # 获取IP地址
        ip_address = socket.gethostbyname(hostname)
        # 获取操作系统信息
        os_name = platform.system()
        os_version = platform.version()
        os_release = platform.release()
        # 获取处理器信息
        processor = platform.processor()
        # 获取Python版本
        python_version = platform.python_version()
        
        # 构建主机信息字符串
        host_info = f"主机名: {hostname}\n"
        host_info += f"IP地址: {ip_address}\n"
        host_info += f"操作系统: {os_name} {os_release} {os_version}\n"
        host_info += f"处理器: {processor}\n"
        host_info += f"Python版本: {python_version}\n"
        
        return host_info
    except Exception as e:
        return f"获取主机信息失败: {str(e)}"

