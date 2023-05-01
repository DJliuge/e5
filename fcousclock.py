import time

focus_time = 25 * 60  # 设置专注时长为25分钟
rest_time = 5 * 60  # 设置休息时长为5分钟

focus_count = 0  # 记录专注次数
while True:
    print("开始专注...")
    time.sleep(focus_time)  # 等待专注时长
    print("专注结束。")

    focus_count += 1
    if focus_count % 4 == 0:  # 每完成四次专注休息会更长
        print("你已经完成了四次专注。现在休息20分钟。")
        time.sleep(20 * 60)
    else:
        print("休息一下, 休息5分钟。")
        time.sleep(rest_time)
