def is_peak_at(data, index, w):
    if len(data) > 1:
        if index < (len(data) - w) and index >= w:
            if data[index] > max(data[index - w:index]) and data[index] >= max(data[index:index + w + 1]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def find_moving_average(data, n):
    moving_averages = []
    for i in range(0, len(data) - n + 1):
        moving_averages.append(sum(data[i:i + n]) / n)
    return moving_averages


def get_only_peaks(data, w):
    peaks = []
    for index in range(len(data)):
        if is_peak_at(data, index, w):
            peaks.append(data[index])
    return peaks


def moving_average_of_peaks(data, n, w):
    peaks = get_only_peaks(data, w)
    moving_averages = find_moving_average(peaks, n)
    return moving_averages


def report_test(ans, expected):
    if ans == expected:
        print(" - correct:" + str(ans))
    else:
        print(" **INCORRECT** got " + str(ans) + " but expected " + str(expected))
        pass
    pass


def check_ma(data, n, expected):
    print("find_moving_average(" + str(data) + ", " + str(n) + ")")
    report_test(find_moving_average(data, n), expected)
    pass


def check_peaks(data, w, expected):
    print("get_only_peaks(" + str(data) + ", " + str(w) + ")")
    report_test(get_only_peaks(data, w), expected)
    pass


def check_ma_of_peaks(data, n, w, expected):
    print("moving_average_of_peaks(" + str(data) + ", " + str(n) + "," + str(w) + ")")
    report_test(moving_average_of_peaks(data, n, w), expected)
    pass


if __name__ == "__main__":
    data0 = [160, 161, 162, 161, 160, 161, 162, 163, 164, 163, 162]
    check_ma(data0, 4, [161, 161, 161, 161, 161.5, 162.5, 163, 163])
    check_peaks(data0, 2, [162, 164])
    check_ma_of_peaks(data0, 2, 2, [163])
    check_ma_of_peaks(data0, 3, 2, [])
    check_ma(data0, 1, data0)
    data1 = []
    check_ma(data1, 1, [])
    check_peaks(data1, 1, [])
    check_ma_of_peaks(data1, 1, 1, [])
    data2 = [100, 105, 110, 115, 120, 115, 110, 120, 125, 120, 125,
             120, 130, 135, 140, 135, 130]
    check_ma(data2, 5, [110, 113, 114, 116, 118, 118, 120, 122, 124,
                        126, 130, 132, 134])
    check_ma(data2, 10, [114, 116.5, 118, 120, 122, 124, 126, 128])
    check_peaks(data2, 1, [120, 125, 125, 140])
    check_peaks(data2, 2, [120, 125, 140])
    check_peaks(data2, 8, [])
    check_ma_of_peaks(data2, 2, 1, [122.5, 125, 132.5])
    check_ma_of_peaks(data2, 2, 2, [122.5, 132.5])
    pass




