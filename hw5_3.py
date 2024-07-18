import sys
from pathlib import Path


def parse_log_line(line: str) -> dict:
    date, time, level, *information = line.strip().split()
    return {"date":date, "time":time, "level":level, "information":" ".join(information)}
    
def load_logs(file_path: str) -> list:
    path = Path(file_path)
    log_list = []
    try:
        with open(path, encoding="utf-8") as fh:
            while True:
                try:
                    line = fh.readline()
                    if not line:
                        break
                    log_list.append(parse_log_line(line))
                except Exception as ex:
                    print(f"{ex} in load_logs")
    except Exception as e:
        print(f"{e}\nList was not formed")
        return []
    return log_list

def filter_logs_by_level(logs: list, level: str) -> list:
    log_level = level.upper()
    filtred_logs = filter(lambda x: x["level"] == log_level, logs)# фільтрація через порівняння з значенням з словника
    return filtred_logs

def count_logs_by_level(logs: list) -> dict:
    log_counter = dict()
    for log in logs:
        if log_counter.get(log["level"]) != None:
            log_counter[log["level"]] += 1 # підраховка "рівнів"
        else:
            log_counter[log["level"]] = 1 # створення "рівня"
    return log_counter


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість\n-----------------|----------")
    for key, value in counts.items():
        print(f"{key:<17}| {value}")
        

def main():
    length = len(sys.argv)
    if length < 2:
        print("Шлях не вказано")
    else:
        logs = load_logs(sys.argv[1])
        display_log_counts(count_logs_by_level(logs))
        if length >= 3:
            print(f"Деталі логів для рівня '{sys.argv[2].upper()}':")
            for log in filter_logs_by_level(logs, sys.argv[2]):
                print(f"{log.get("date")} {log.get("time")} {log.get("level")} {log.get("information")}")
        
    
if __name__=="__main__":
    main()