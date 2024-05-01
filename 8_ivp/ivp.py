from ivp_goodparts import *

def heun_step(fn, t, v, h, counter):
    # Predictor step
    k1 = fn(t, v, counter)
    v_predictor = v + h * k1
    
    # Corrector step
    k2 = fn(t + h, v_predictor, counter)
    v_corrected = v + 0.5 * h * (k1 + k2)
    
    return v_corrected

def runge_estimate(rhs_func, t, v, h, counter):
    full_step = heun_step(rhs_func, t, v, h, counter)

    half_step_1 = heun_step(rhs_func, t, v, h / 2, counter)
    half_step_2 = heun_step(rhs_func, t + h / 2, half_step_1, h / 2, counter)
    
    R = np.linalg.norm(half_step_2 - full_step, np.inf) / 3.0  # factor due to Heun method order
    return R, half_step_2

def solve_ode_heun(rhs_func, t_0, T, h_0, N_x, eps, initial_conditions):
    t = t_0
    v = initial_conditions
    h = h_0
    counter = [0]
    
    while t < T:
        if counter[0] >= N_x:
            break

        R, v_next = runge_estimate(rhs_func, t, v, h, counter)
        if R < eps:
            print("%6f\t%6f\t%6e\t%d\t%s\t" % (t, h, R, counter[0], '\t'.join('%6f' % vi for vi in v)))
            t += h
            v = v_next
            if R < eps / 64:
                h = min(2 * h, T - t)
        else:
            h /= 2


def main():
    t_0, T, h_0, N_x, eps, rhs_f, initial_conditions = read_input()
    solve_ode_heun(rhs_f, t_0, T, h_0, N_x, eps, initial_conditions)


if __name__ == "__main__":
    main()
