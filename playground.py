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
            metrics = []
            for d in range(len(data['d_metric'])):
                if key in data['d_metric'][d].keys():
                    metrics = data['d_metric'][d][key]
            if len(metrics) > 0:
                d_metrics.append(sum(metrics) * 1.000 / len(metrics))
            else:
                d_metrics.append(0)
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
        moead_solutions_count = get_number_of_solutions_by_run_and_alg(i, 'moead')
        nsga2_solutions_count = get_number_of_solutions_by_run_and_alg(i, 'nsga2')
        with open('runs/' + str(i) + '-metrics.json') as json_file:
            data = json.load(json_file)
            # FIXME - I calculated this backwards
            nsga2_c_metrics.append(data['c_metric'][0]['moead'] / nsga2_solutions_count)
            moead_c_metrics.append(data['c_metric'][0]['nsga2'] / moead_solutions_count)
    return moead_c_metrics, nsga2_c_metrics


def get_number_of_solutions_by_run_and_alg(i, alg):
    with open('runs/' + str(i) + '-' + alg + '-solutions.json') as json_file:
        return len(json.load(json_file))


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
