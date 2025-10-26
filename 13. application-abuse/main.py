import sys
from pprint import pprint
import os

constraints = input()
params = dict()
for param in constraints.split(", "):
    key, value = param.split("=")
    value = int(value)
    params[key] = value

headers = input().split(", ")
orders = dict()
for i, header in enumerate(headers):
    orders[header] = i

entries = []
for line in sys.stdin:
    line = line.rstrip("\n")
    entries.append(line)

def parse_entry(entry):
    words = entry.split(" ")
    ranges = []
    start = -1
    for i,w in enumerate(words):
        if w.startswith('"'):
            start = i
        if w.endswith('"'):
            ranges.append((start, i, " ".join(words[start:i+1])))
            start = -1
    newline = []
    last_e = 0
    for s, e, b in ranges:
        newline += words[last_e:s]
        newline.append(b)
        last_e = e + 1
    newline += words[last_e:]
    registry = {
        "Host": newline[orders["Host"]],
        "Client IP": newline[orders["Client IP"]],
        "Id": newline[orders["Id"]],
        "Date": newline[orders["Date"]].strip('[]').split(":")[0],
        "Request": newline[orders["Request"]],
        "HTTP Status": newline[orders["HTTP Status"]],
        "User Agent": newline[orders["User Agent"]],
        "Session Cookie": newline[orders["Session Cookie"]],
    }

    return registry
    
entries = list(map(parse_entry, entries))

events = dict()
for entry in entries:
    if entry["HTTP Status"] != "200":
        continue
    if entry["Date"] not in events:
        events[entry["Date"]] = dict()
    if entry["Id"] not in events[entry["Date"]]:
        events[entry["Date"]][entry["Id"]] = {
            "agent": set(),
            "ip": set(),
            "pdf": [],
            "session": set(),
        }
    events[entry["Date"]][entry["Id"]]["agent"].add(entry["User Agent"])
    events[entry["Date"]][entry["Id"]]["ip"].add(entry["Client IP"])
    basename = os.path.basename(entry["Request"].split(" ")[1])
    if basename.endswith(".pdf"):
        events[entry["Date"]][entry["Id"]]["pdf"].append(int(basename.split(".")[0]))
    events[entry["Date"]][entry["Id"]]["session"].add(entry["Session Cookie"])

abuses = []
for date, entries in events.items():
    for id, summary in entries.items():
        if id == "-":
            continue
        if "agent" in params and len(summary["agent"]) >= params["agent"]:
            abuses.append(f"{id} agent={len(summary['agent'])}")
        if "ip" in params and len(summary["ip"]) >= params["ip"]:
            abuses.append(f"{id} ip={len(summary['ip'])}")
        if "pdf" in params and len(summary["pdf"]) >= params["pdf"]:
            abuses.append(f"{id} pdf={len(summary['pdf'])}")
        if "session" in params and len(summary["session"]) >= params["session"]:
            abuses.append(f"{id} session={len(summary['session'])}")
        if "crawl" in params:
            consectives = 1
            max_consecutives = 0
            for pdf in range(1, len(summary["pdf"])):
                if summary["pdf"][pdf] - summary["pdf"][pdf-1] != 1:
                    max_consecutives = max(max_consecutives, consectives)
                    consectives = 1
                else:
                    consectives += 1
            max_consecutives = max(max_consecutives, consectives)
            if max_consecutives >= params["crawl"]:
                abuses.append(f"{id} crawl={max_consecutives}")
if len(abuses) == 0:
    print("N/A")
else:
    for a in abuses:
        print(a)
        