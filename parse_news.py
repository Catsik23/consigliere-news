import json, sys, xml.etree.ElementTree as ET

kw = ["дивиденд","байбэк","buyback","выкуп акций","отчёт","отчетность","МСФО","РСБУ","собрание акционеров","совет директоров"]

try:
    tree = ET.parse("raw.xml")
    root = tree.getroot()
except:
    print("[]")
    sys.exit(0)

news = []
for item in root.iter("item"):
    t = item.find("title")
    d = item.find("description")
    if t is None:
        continue
    text = ((t.text or "") + " " + (d.text or "")).lower()
    if any(k in text for k in kw):
        news.append({
            "title": t.text or "",
            "desc": (d.text or "")[:300],
            "link": item.find("link").text if item.find("link") is not None else ""
        })

print(json.dumps(news, ensure_ascii=False, indent=2))
