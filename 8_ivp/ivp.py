#!/usr/bin/env python3
import numpy as np

def show_step(t, h, R, counter, y):
    print("%6f\t%6f\t%6e\t%d\t%s\t" % (t, h, R, counter[0], '\t'.join('%6f' % y_i for y_i in y)))

def extract_function(code_str):
    mini_namespace = {'np': np}
    initial_keys = set(mini_namespace.keys())
    initial_keys.add('__builtins__')
    exec(code_str, mini_namespace)
    new_keys = set(mini_namespace.keys()) - initial_keys
    if len(new_keys) == 1:
        new_key = new_keys.pop()
        if callable(mini_namespace[new_key]):
            return mini_namespace[new_key]

def read_input():
    t_0 = float(input())
    T = float(input())
    h_0 = float(input())
    N_x = int(input())
    eps = float(input())
    n = int(input())
    code_with_func = "\n".join([input() for i in range(n + 3)])
    foo = extract_function(code_with_func)
    initial_conditions = np.array(list(map(float, input().split())))
    if h_0 <= 0 or eps <= 0 or T <= t_0:
        raise ValueError("Invalid input values: ensure h_0 > 0, eps > 0, and T > t_0")
    if len(initial_conditions) != n:
        raise ValueError("Number of initial conditions does not match the number of equations")
    return t_0, T, h_0, N_x, eps, foo, initial_conditions

def heun_step(f, y, t, h, counter, k1=None):
    k1 = f(t, y, counter) if k1 is None else k1
    y_predictor = y + h * k1
    k2 = f(t+h, y_predictor, counter)
    y_corrected = y + h/2 * (k1 + k2)
    return y_corrected, k1, k2



def solve_ode(method, t_0, T, h_0, N_x, eps, rhs, y_0, THETA=2.0, ostream=True):
    t = t_0
    y = y_0
    h = h_0
    kounter = [0]
    R = 0.0

    cached_k01 = None
    history_counter = [kounter[0]]
    history_h = [h]
    history_t = [t]
    history_R = [R]
    ostream and show_step(t, h, R, kounter, y)
    while t+h/2 < T:
        if kounter[0] >= N_x:
            print(f"Maximum number of function calls ({N_x}) reached.")
            break
        h2 = h/2

        y1, k01,k02 = method(rhs,y,  t   ,h, kounter,k1=cached_k01)
        y21,k11,k12 = method(rhs,y,  t   ,h2,kounter,k1=k01)
        y22,k21,k22 = method(rhs,y21,t+h2,h2,kounter,k1=k12)

        R = THETA * np.linalg.norm(y1 - y22, 2)
        if R >= eps:
            cached_k01 = k11
            h = h2
        elif R < eps / 64:
            h = 2*h
            cached_k01 = k11
        else:
            cached_k01 = k02
            t = t+h
            y = y22
            ostream and show_step(t, h, R, kounter, y)
            history_counter.append(kounter[0])
            history_h.append(h)
            history_t.append(t)
            history_R.append(R)
    return y, history_counter, history_h, history_t, history_R

def main():
    t_0, T, h_0, N_x, eps, rhs, y_0 = read_input()
    heun = solve_ode(heun_step, t_0, T, h_0, N_x, eps, rhs, y_0)

if __name__ == "__main__":
    main()
