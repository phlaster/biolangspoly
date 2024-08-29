from ivp_goodparts import *
import numpy as np
from scipy.integrate import solve_ivp

def reference_solution(t_0, T, h_0, N_x, eps, f, initial_conditions):
    def f_wrapper(t, y):
        kounter[0] += 1
        return f(t, y, kounter)

    kounter = [0]
    sol = solve_ivp(f_wrapper, (t_0, T), initial_conditions, method='RK45', atol=eps, rtol=eps).y[:, -1]
    show_step(T, 0, 0, kounter, sol, color=Fore.GREEN)
    return sol
#################################################################################
def rk4_step(f, t, y, h, kounter):
    k1 = h * f(t, y, kounter)
    k2 = h * f(t + h / 2, y + k1 / 2, kounter)
    k3 = h * f(t + h / 2, y + k2 / 2, kounter)
    k4 = h * f(t + h, y + k3, kounter)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
##############################################################################
def heun_step(f, t, y, h, counter):
    k1 = f(t, y, counter)
    v_predictor = y + h * k1
    k2 = f(t + h, v_predictor, counter)
    v_corrected = y + 0.5 * h * (k1 + k2)
    return v_corrected


def solve_ode(step_func, t_0, T, h_0, N_x, eps, rhs_func, initial_conditions, THETA, color=Fore.LIGHTRED_EX):
    t = t_0
    y = initial_conditions
    h = h_0
    kounter = [0]
    R = 0.0

    memo_h = None
    memo_h_12 = None
    show_step(t, h, R, kounter, y, color=color)
    while t < T:
        if kounter[0] >= N_x:
            print(f"Maximum number of function calls ({N_x}) reached.")
            break
        h2 = h / 2
        y_next    = step_func(rhs_func, t   , y,         h,  kounter) if memo_h    is None else memo_h
        y_next_12 = step_func(rhs_func, t   , y,         h2, kounter) if memo_h_12 is None else memo_h_12
        y_next_22 = step_func(rhs_func, t+h2, y_next_12, h2, kounter)

        R = THETA * np.linalg.norm(y_next - y_next_22, 2)
        if R > eps:
            h = h2
            memo_h = y_next_12
            memo_h_12 = None
        elif R < eps / 64:
            h *= 2
            memo_h_12 = y_next
            memo_h = None
        else:
            t += h
            y = y_next_22
            memo_h = None
            memo_h_12 = None
            show_step(t, h, R, kounter, y, color=color)
            if T-t < h:
                break
    return y

###################################################################################

# Example usage
t_0, T, h_0, N_x, eps, fs, initial_conditions = read_input()

show_correct("t\t\th\t\tR\t\tN\ty1\t\ty2\t\ty3", Fore.BLUE)
EXACT = reference_solution(t_0, T, h_0, N_x, 1e-15, fs, initial_conditions)
REF = reference_solution(t_0, T, h_0, N_x, eps, fs, initial_conditions)
print(f"err: {np.linalg.norm(REF - EXACT, 2)}")

rk4 = solve_ode(rk4_step, t_0, T, h_0, N_x, eps, fs, initial_conditions, THETA=8/7)
print(f"err: {np.linalg.norm(rk4 - EXACT, 2)}")

heun = solve_ode(heun_step, t_0, T, h_0, N_x, eps, fs, initial_conditions, THETA=6/3, color=Fore.BLUE)
print(f"err: {np.linalg.norm(heun - EXACT, 2)}")