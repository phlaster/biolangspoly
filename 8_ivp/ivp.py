from ivp_goodparts import *

def heun_step(rhs_func, t, y, h, counter):
    k1 = rhs_func(t, y, counter)
    k2 = rhs_func(t + h, y + h * k1, counter)    
    return y + h/2 * (k1 + k2)


def solve_ode_heun(rhs_func, t_0, T, h_0, N_x, eps, initial_conditions):
    t = t_0
    y = initial_conditions
    h = h_0
    counter = [0]
    R = 0

    show_step(t, h, R, counter, y, Fore.RED)
    step_BUFFER = heun_step(rhs_func, t, y, h, counter)
    while t < T and counter[0] < N_x:
        full_step = step_BUFFER
        half_h = h/2
        half_step_1 = heun_step(rhs_func, t, y, half_h, counter)
        half_step_2 = heun_step(rhs_func, t + half_h, half_step_1, half_h, counter)

        R = np.linalg.norm(half_step_2 - full_step, ord=2) / 3
        if R < eps:
            t += h
            y = half_step_2
            show_step(t, h, R, counter, y, Fore.RED)
            if 64 * R < eps:
                h = min(2*h, T-t) # no more than remaining t
        else:
            h = max(h/2, 1e-15) # no less than reasonably small float
            step_BUFFER = half_step_1
    print(np.linalg.norm(y - np.array([0.693090,1.732764, 5.440465]), 2))


def main():
    t_0, T, h_0, N_x, eps, rhs_func, initial_conditions = read_input()
    solve_ode_heun(rhs_func, t_0, T, h_0, N_x, eps, initial_conditions)


if __name__ == "__main__":
    main()
