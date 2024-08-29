import numpy as np
import matplotlib.pyplot as plt
from ivp import solve_ode, heun_step#, read_input
from scipy.integrate import solve_ivp

def reference_solution(t_0, T, h_0, N_x, eps, f, initial_conditions):
    def f_wrapper(t, y):
        kounter[0] += 1
        return f(t, y, kounter)

    kounter = [0]
    sol = solve_ivp(f_wrapper, (t_0, T), initial_conditions, rtol=eps).y[:, -1]
    return sol

def plot_results(eps_data, min_step_size_data, num_steps_data):
    plt.figure(figsize=(12, 8))

    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.plot(eps_data, num_steps_data, 'o-', color='blue', label='Number of Steps')
    ax1.set_xlabel('Specified Accuracy (eps)')
    ax1.set_ylabel('Number of Steps', color='blue')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_title('Dependence of Number of Steps and Minimum Step Size on Specified Accuracy')
    ax1.legend(loc='upper left')
    ax1.grid(True, which='major', linestyle='--', linewidth=0.5, color='blue', alpha=0.6)

    ax2.plot(eps_data, min_step_size_data, 's-', color='red', label='Minimum Step Size h')
    ax2.set_ylabel('Minimum Step Size h', color='red')
    ax2.set_yscale('log')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.legend(loc='upper right')
    ax2.grid(True, which='major', linestyle='--', linewidth=0.5, color='red', alpha=0.6)

    plt.tight_layout()
    plt.show()

def plot_running_h(history_t_list, history_h_list, epsilons):
    plt.figure(figsize=(12, 8))

    for i, eps in enumerate(epsilons):
        plt.plot(history_t_list[i], history_h_list[i], label=f'eps = {eps}')

    plt.xlabel('Time t')
    plt.ylabel('Step Size h')
    plt.title('Step Size h over Time t for Different Values of eps')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.gca().set_yscale('log')
    plt.axvline(x=min(min(history_t_list)), linestyle='--',  color='black', linewidth=2)
    plt.axvline(x=max(max(history_t_list)), linestyle='--',  color='black', linewidth=2)
    plt.tight_layout()
    plt.show()

def plot_errors(epsilons, errors, mean_Rs):
    plt.figure(figsize=(12, 8))

    ax = plt.gca()

    # Plot errors
    ax.plot(epsilons, errors, 'o-', color='red', label='Errors')
    ax.set_xlabel('Specified Accuracy (eps)')
    ax.set_ylabel('Errors / Mean Runge Estimates', color='black')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.tick_params(axis='y', labelcolor='black')
    ax.set_title('Dependence of Errors and Mean Runge Estimates on Specified Accuracy')
    ax.legend(loc='upper left')
    ax.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.6)

    # Plot mean Runge estimates
    ax.plot(epsilons, mean_Rs, 's-', color='blue', label='Mean Runge Estimates')
    ax.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

def main():
    t_0 = 1.5
    T = 2.5
    h_0 = 0.1
    N_x = 10_000
    epsilons = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9]
    THETA = 2.0
    def fs(t, v, kounter):
        A = np.array([
            [-0.4, 0.02, 0],
            [0, 0.8, -0.1],
            [0.003, 0, 1]
        ])
        kounter[0] += 1
        return np.dot(A, v)
    iconds = np.array([1., 1., 2.])
    solve_heun = lambda eps: solve_ode(heun_step, t_0, T, h_0, N_x, eps, fs, iconds, THETA, ostream=False)

    history_errors = []
    history_counters = []
    history_hs = []
    history_ts = []
    history_mean_Rs = []
    min_step_size_data = []
    num_steps_data = []

    ref = reference_solution(t_0, T, h_0, N_x, 1e-16, fs, iconds)
    for eps in epsilons:
        y, history_counter, history_h, history_t, history_R = solve_heun(eps)
        err = np.linalg.norm(y - ref, 2)
        history_errors.append(err)
        mean_R = np.mean(history_R)
        history_mean_Rs.append(mean_R)
        history_ts.append(history_t)
        history_hs.append(history_h)
        min_step_size_data.append(min(history_h))
        num_steps_data.append(len(history_t))


    # plot_running_h(history_ts[:6], history_hs[:6], epsilons[:6])
    # plot_results(epsilons, min_step_size_data, num_steps_data)
    plot_errors(epsilons, history_errors, history_mean_Rs)

if __name__ == "__main__":
    main()