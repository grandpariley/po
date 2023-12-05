import json
import matplotlib.pyplot as plt

from pkg.consts import Constants


def main():
    moead_times, nsga2_times = get_times()
    show_times(moead_times, nsga2_times)
    moead_c_metrics, nsga2_c_metrics = get_c_metrics()
    show_c_metrics(moead_c_metrics, nsga2_c_metrics)
    moead_d_metrics = get_d_metrics('moead')
    show_d_metrics(moead_d_metrics, 'ro')
    nsga2_d_metrics = get_d_metrics('nsga2')
    show_d_metrics(nsga2_d_metrics, 'ko')


def get_d_metrics(key):
    d_metrics = []
    for i in range(Constants.NUM_RUNS):
        with open('runs/' + str(i) + '-metrics.json') as json_file:
            data = json.load(json_file)
            d = data['d_metric'][key]
            d_metrics.append(sum(d) * 1.000 / len(d))
    return d_metrics


def show_d_metrics(d_metrics, colour):
    plt.plot([i for i in range(Constants.NUM_RUNS)], d_metrics, colour)
    plt.xlabel("Generation")
    plt.ylabel("Average euclidean distance from approximated Pareto front")
    plt.show()


def get_c_metrics():
    nsga2_c_metrics = []
    moead_c_metrics = []
    for i in range(Constants.NUM_RUNS):
        with open('runs/' + str(i) + '-metrics.json') as json_file:
            data = json.load(json_file)
            nsga2_c_metrics.append(data['c_metric']['nsga2'])
            moead_c_metrics.append(data['c_metric']['moead'])
    return moead_c_metrics, nsga2_c_metrics


def show_c_metrics(moead_c_metric, nsga2_c_metric):
    plt.plot([i for i in range(Constants.NUM_RUNS)], nsga2_c_metric, 'ko')
    plt.plot([i for i in range(Constants.NUM_RUNS)], moead_c_metric, 'ro')
    plt.xlabel("Generation")
    plt.ylabel("Number of dominated solutions")
    plt.show()


def show_times(moead_times, nsga2_times):
    plt.plot([i for i in range(Constants.NUM_RUNS)], nsga2_times, 'ko')
    plt.plot([i for i in range(Constants.NUM_RUNS)], moead_times, 'ro')
    plt.xlabel("Generation")
    plt.ylabel("Time (in ms)")
    plt.show()


def get_times():
    nsga2_times = []
    moead_times = []
    for i in range(Constants.NUM_RUNS):
        with open('runs/' + str(i) + '-times.json') as json_file:
            data = json.load(json_file)
            nsga2_times.append(data['nsga2'] / 1000000)
            moead_times.append(data['moead'] / 1000000)
    return moead_times, nsga2_times


if __name__ == '__main__':
    main()
