"""
从 crt.sh 证书透明度日志拉取子域名
纯被动收集，不直接与目标交互
"""
import json
import sys
import ssl
import urllib.request

def fetch_crtsh(domain):
    """从 crt.sh 获取证书透明度记录"""
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    ctx = ssl.create_default_context()
    
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (research)"
    })
    
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return set()
    
    # 提取所有 name_value，拆分多域名证书
    names = set()
    for entry in data:
        for name in entry.get("name_value", "").split("\n"):
            name = name.strip().lower().lstrip("*.")
            if name and domain in name:
                names.add(name)
    
    return names


domains = ["health.pingan.com", "pingan.com.cn"]
all_subdomains = set()

for domain in domains:
    print(f"\n=== 查询: {domain} ===", file=sys.stderr)
    subs = fetch_crtsh(domain)
    print(f"找到 {len(subs)} 个子域名", file=sys.stderr)
    all_subdomains.update(subs)

# 只输出与 health 或 ehis 相关的
relevant = sorted([s for s in all_subdomains if "health" in s or "ehis" in s])

print(f"\n=== 总计 {len(relevant)} 条相关子域名 ===")
for s in relevant:
    print(s)
