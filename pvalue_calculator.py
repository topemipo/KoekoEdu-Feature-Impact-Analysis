# t_stat, z_score are the results of test statistis, the former for t-tests (data with unknown standard deviation) 
# and the latter is for z-tests (data with known standard deviations)

# df is the degrees of freedoms for t-tests
# dp is the number of decimal places you want your pvalue to have

from scipy import stats

# 1. Two-Sided t-Test
def two_sided_t_test(t_stat, df, dp):
    p_value = 2 * stats.t.cdf(-abs(t_stat), df)
    return round(p_value, dp)

# 2. Right-Tailed t-Test
def right_tailed_t_test(t_stat, df, dp):
    p_value = 1 - stats.t.cdf(t_stat, df)
    return round(p_value, dp)

# 3. Left-Tailed t-Test
def left_tailed_t_test(t_stat, df, dp):
    p_value = stats.t.cdf(t_stat, df)
    return round(p_value, dp)

# 4. Two-Sided z-Test
def two_sided_z_test(z_score, dp):
    p_value = 2 * stats.norm.cdf(-abs(z_score))
    return round(p_value, dp)

# 5. Right-Tailed z-Test
def right_tailed_z_test(z_score, dp):
    p_value = 1 - stats.norm.cdf(z_score)
    return round(p_value, dp)

# 6. Left-Tailed z-Test
def left_tailed_z_test(z_score, dp):
    p_value = stats.norm.cdf(z_score)
    return round(p_value, dp)