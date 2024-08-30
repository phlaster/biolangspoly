#!/usr/bin/env python3
import numpy as np
import sys
import matplotlib.pyplot as plt
from ivp import solve_ode, heun_step, read_input
from scipy.integrate import solve_ivp

def reference_solution(t_0, T, h_0, N_x, eps, f, initial_conditions):
    def f_wrapper(t, y):
        kounter[0] += 1
        return f(t, y, kounter)

    kounter = [0]
    max_step_size = (T - t_0) / N_x
    sol = solve_ivp(f_wrapper, (t_0, T), initial_conditions, rtol=eps, max_step=max_step_size).y[:, -1]
    return sol

def plot_results(eps_data, min_step_size_data, num_steps_data):
    plt.figure(figsize=(12, 8))

    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.plot(eps_data, num_steps_data, 'o-', color='blue')
    ax1.set_xlabel('Заданная точность (eps)')
    ax1.set_ylabel('Количество шагов', color='blue')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_title('Зависимость количества шагов и минимального размера шага от заданной точности')
    ax1.grid(True, which='major', linestyle='--', linewidth=0.5, color='blue', alpha=0.6)

    ax2.plot(eps_data, min_step_size_data, 's-', color='red')
    ax2.set_ylabel('Минимальный размер шага h', color='red')
    ax2.set_yscale('log')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.grid(True, which='major', linestyle='--', linewidth=0.5, color='red', alpha=0.6)

    plt.tight_layout()
    plt.show()

def plot_running_h(history_t_list, history_h_list, epsilons):
    plt.figure(figsize=(12, 8))

    for i, eps in enumerate(epsilons):
        plt.plot(history_t_list[i], history_h_list[i], label=f'eps = {eps}')

    plt.xlabel('Время t')
    plt.ylabel('Размер шага h')
    plt.title('Размер шага h в зависимости от времени t для разных значений eps')
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

    ax.plot(epsilons, errors, 'o-', color='red', label='Фактическая ошибка')
    ax.set_xlabel('Заданная точность (eps)')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.tick_params(axis='y', labelcolor='black')
    ax.set_title('Оценки Рунге и фактические ошибки в зависимости от выбранной точности')
    ax.legend(loc='upper left')
    ax.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.6)

    ax.plot(epsilons, mean_Rs, 's-', color='blue', label='Средняя оценка Рунге на интервале')
    ax.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

def automatic_trial():
    t_0 = 1.5
    T = 2.5
    h_0 = 0.1
    N_x = 10_000
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
    ref = reference_solution(t_0, T, h_0, N_x, 1e-13, fs, iconds)
    return lambda eps: solve_ode(heun_step, t_0, T, h_0, N_x, eps, fs, iconds, THETA, ostream=False), ref

def main():
    manual = False
    for arg in sys.argv[1:]:
        if arg == '-m':
            manual = True
        else:
            print(f"Error: Unknown flag '{arg}'")
            sys.exit(1)

    epsilons = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9]
    if manual:
        t_0, T, h_0, N_x, eps, fs, iconds = read_input()
        solve_heun = lambda eps: solve_ode(heun_step, t_0, T, h_0, N_x, eps, fs, iconds, 2.0, ostream=False)
        ref = reference_solution(t_0, T, h_0, N_x, 1e-13, fs, iconds)
    else:
        solve_heun, ref = automatic_trial()

    history_errors = []
    history_counters = []
    history_hs = []
    history_ts = []
    history_mean_Rs = []
    min_step_size_data = []
    num_steps_data = []

    
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


    plot_running_h(history_ts[:6], history_hs[:6], epsilons[:6])
    plot_results(epsilons, min_step_size_data, num_steps_data)
    plot_errors(epsilons, history_errors, history_mean_Rs)

if __name__ == "__main__":
    main()