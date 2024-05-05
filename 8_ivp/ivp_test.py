from ivp_goodparts import *

def heun_step(rhs_func, t, y, h, counter):
    # Predictor
    k1 = rhs_func(t, y, counter)
    v_predictor = y + h * k1
    
    # Corrector
    k2 = rhs_func(t + h, v_predictor, counter)
    v_corrected = y + 0.5 * h * (k1 + k2)
    
    return v_corrected

def runge_estimate(rhs_func, t, y, h, counter):
    full_step = heun_step(rhs_func, t, y, h, counter)

    half_h = h/2
    half_step_1 = heun_step(rhs_func, t, y, half_h, counter)
    half_step_2 = heun_step(rhs_func, t + half_h, half_step_1, half_h, counter)
    
    R = np.linalg.norm(half_step_2 - full_step, 2) / 3.0
    return R, half_step_2

def solve_ode_heun(rhs_func, t_0, T, h_0, N_x, eps, initial_conditions):
    t = t_0
    y = initial_conditions
    h = h_0
    counter = [0]
    R = 0

    show_correct("t\t\th\t\tR\t\tN\ty1\t\ty2\t\ty3", Fore.BLUE)
    show_step(t, h, R, counter, y, Fore.RED)
    while t < T and counter[0] < N_x:

        R, y_next = runge_estimate(rhs_func, t, y, h, counter)

        if R < eps:
            show_correct(CORRECT.pop(), Fore.GREEN)
            print()
            
            t += h
            y = y_next
            show_step(t, h, R, counter, y, Fore.RED)
            if R < eps / 64:
                h = min(2 * h, T - t)
        else:
            h /= 2


def main():
    # t_0, T, h_0, N_x, eps, rhs_func, initial_conditions = read_input()

    t_0 = 1.5
    T = 2.5
    h_0 = 0.1
    N_x = 10000
    eps = 0.0001
    initial_conditions = np.array([1.0, 1.0, 2.0])
    
    def rhs_func(t, v, counter):
        A = np.array([[-0.4, 0.02, 0], [0, 0.8, -0.1], [0.003, 0, 1]])
        counter[0] += 1
        return np.dot(A, v)

    solve_ode_heun(rhs_func, t_0, T, h_0, N_x, eps, initial_conditions)


if __name__ == "__main__":
    main()
