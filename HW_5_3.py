def parse_log_line(line: str) -> dict:
    log_dict = {}
    parts = line.split()
    log_dict.update({"data": parts[0], "time": parts[1], \
                     "level": parts[2], "msg":" ".join(parts[3:])})
    return log_dict


def load_logs(file_path: str) -> list:
    with open(file_path, "r") as fh:
        new_list = []
        while True:
            line = fh.readline()
            if not line:
                break
            new_list.append(parse_log_line(line))
        return new_list


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = [log for log in logs if log.get("level")==level]
    return filtered_logs


def count_logs_by_level(logs: list) -> dict:
    log_count = {}
    for log in logs:
        log_level = log.get("level")
        if log_level in log_count:
            log_count[log_level] += 1
        else:
            log_count[log_level] =1
    return log_count

# print(count_logs_by_level(load_logs("log_file.log")))

def display_log_counts(counts: dict):
    print(f"Рівень логування | Кількість\
          \n----------------------------")
    for key, val in counts.items():
        print(f"{key:<17}| {val}")




display_log_counts(count_logs_by_level(load_logs("log_file.log")))
#print(filter_logs_by_level(load_logs("log_file.log"), "ERROR"))