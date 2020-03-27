from math import *


def res_util_rate_messsage(res_util_rate):
    if res_util_rate > 1:
        return "Overspending of materials (v_v)"
    elif res_util_rate < 1:
        return "Resource saving (^_^)"
    else:
        return "Exactly according to plan (>_<)" 


def product_creation(plan_resources, fact_resources, result):
    material_consumption = round(result / fact_resources, 2)
    product_per_unit = round(fact_resources / result, 2)
    res_util_rate = round(fact_resources / plan_resources, 2)

    print("Material consumption:", material_consumption)
    print("Product per unit:", product_per_unit)
    print("Resource utilization rate:", res_util_rate, "-", res_util_rate_messsage(res_util_rate))




