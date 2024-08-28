import numpy as np
from colorama import Fore, Style


CORRECT = list(reversed([
    "1.500000\t0.100000\t0\t\t0\t1.000000\t1.000000\t2.000000",
    "1.500781\t0.000781\t9.352e-05\t4\t0.999973\t1.000547\t2.001565",
    "1.502344\t0.000781\t3.98388e-11\t8\t0.999676\t1.001016\t2.003132",
    "1.505469\t0.001563\t3.18989e-10\t12\t0.999082\t1.001955\t2.006269",
    "1.511719\t0.003125\t2.55639e-09\t16\t0.997897\t1.003834\t2.012557",
    "1.524219\t0.006250\t2.0523e-08\t20\t0.995531\t1.007601\t2.025194",
    "1.549219\t0.012500\t1.65339e-07\t24\t0.990818\t1.015167\t2.050705",
    "1.599219\t0.025000\t1.3414e-06\t28\t0.981468\t1.030431\t2.102692",
    "1.649219\t0.050000\t1.10365e-05\t33\t0.963070\t1.061486\t2.210638",
    "1.699219\t0.050000\t1.16015e-05\t38\t0.945066\t1.093244\t2.324115",
    "1.749219\t0.050000\t1.21957e-05\t43\t0.927452\t1.125704\t2.443406",
    "1.799219\t0.050000\t1.28208e-05\t48\t0.910218\t1.158866\t2.568810",
    "1.849219\t0.050000\t1.34784e-05\t53\t0.893359\t1.192724\t2.700641",
    "1.899219\t0.050000\t1.417e-05\t58\t0.876868\t1.227276\t2.839228",
    "1.949219\t0.050000\t1.48975e-05\t63\t0.860737\t1.262512\t2.984916",
    "1.999219\t0.050000\t1.56628e-05\t68\t0.844961\t1.298425\t3.138071",
    "2.049219\t0.050000\t1.64678e-05\t73\t0.829534\t1.335002\t3.299076",
    "2.099219\t0.050000\t1.73145e-05\t78\t0.814449\t1.372230\t3.468331",
    "2.149219\t0.050000\t1.82052e-05\t83\t0.799699\t1.410093\t3.646262",
    "2.199219\t0.050000\t1.91421e-05\t88\t0.785279\t1.448570\t3.833312",
    "2.249219\t0.050000\t2.01276e-05\t93\t0.771183\t1.487639\t4.029949",
    "2.299219\t0.050000\t2.11643e-05\t98\t0.757406\t1.527274\t4.236665",
    "2.349219\t0.050000\t2.22547e-05\t103\t0.743940\t1.567446\t4.453976",
    "2.399219\t0.050000\t2.34018e-05\t108\t0.730782\t1.608121\t4.682426",
    "2.449219\t0.050000\t2.46084e-05\t113\t0.717924\t1.649261\t4.922586",
    "2.499219\t0.050000\t2.58776e-05\t118\t0.705362\t1.690825\t5.175055",
    "2.500000\t0.050000\t2.72127e-05\t123\t0.693090\t1.732764\t5.440465"
]))


def show_step(t, h, R, counter, y, color=Fore.YELLOW):
    print(color + "%6f\t%6f\t%6e\t%d\t%s\t" % (t, h, R, counter[0], '\t'.join('%6f' % y_i for y_i in y)))
    print(Style.RESET_ALL, end='')


def show_correct(S, color=Fore.GREEN):
    print(color + str(S) + Style.RESET_ALL)


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
    return None


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

    return t_0, T, h_0, N_x, eps, foo, initial_conditions