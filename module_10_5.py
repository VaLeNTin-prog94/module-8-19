from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for readline in file:
            all_data += [readline]


if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)]
    time_start = datetime.now()
    for s in filenames:
        read_info(s)
    time_end = datetime.now()
    print(time_end - time_start)
    with multiprocessing.Pool(processes=4) as pool:
        time_start = datetime.now()
        pool.map(read_info, filenames)
    time_end = datetime.now()
    print(time_end - time_start)
