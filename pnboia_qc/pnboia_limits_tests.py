import numpy as np



# SPOTTERS
spotters = dict(
range_limits = {
    'wspd': [0,30],
    'wdir': [0,360],
    'swvht': [0,19.9],
    'sst': [0,30],
    'tp': [0,20],
    'mean_tp': [0,15],
    'pk_dir': [0,360],
    'wvdir': [0,360],
    }
,
mis_value_limits = {
    'wspd': -999,
    'wdir': -999,
    'sst': -999,
    'swvht': -999,
    'tp': -999,
    'mean_tp': -999,
    'pk_dir': -999,
    'wvdir': -999,
}
,
sigma_limits = {
    "swvht": 6,
    "wspd": 25,
    "sst": 8.6,
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
stuck_limits = 7
,
continuity_limits = 3
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}


)


# GENERAL
general = dict(
range_limits = {
                "swvht": [0.1, 19.9],
                "mxwvht": [0.1, 19.9],
                "tp": [1.7, 30],
                "wvdir": [0, 360],
                "wspd1": [0.1, 59],
                "wdir1": [0, 360],
                "gust1": [0.1, 59],
                "wspd2": [0.1, 59],
                "wdir2": [0, 360],
                "gust2": [0.1, 59],
                "atmp": [-39, 59],
                "pres": [501, 1099],
                "dewpt": [-29, 39],
                "sst": [-3, 39],
                "rh": [25, 102],
                "cspd1": [-4990, 4990],
                "cdir1": [0, 360],
                "cspd2": [-4990, 4990],
                "cdir2": [0, 360],
                "cspd3": [-4990, 4990],
                "cdir3": [0, 360],
                "tp": [1.7, 30],
                }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd1": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht": [20.47, -9999, np.nan],
    "mxwvht": [20.47, -9999, np.nan],
    "tp": [25.5, -9999, np.nan],
    "wvdir": [381, -9999, np.nan],
    "wvspread": [381, -9999, np.nan]
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)


# CABOFRIO
cabofrio = dict(
range_limits = {
    "swvht": [0.1, 19.9],
    "mxwvht": [0.1, 19.9],
    "tp": [1.7, 30],
    "wvdir": [0, 360],
    "wspd1": [0.1, 59],
    "wdir1": [0, 360],
    "gust1": [0.1, 59],
    "wspd2": [0.1, 59],
    "wdir2": [0, 360],
    "gust2": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "rh": [25, 102],
    "cspd1": [-4990, 4990],
    "cdir1": [0, 360],
    "cspd2": [-4990, 4990],
    "cdir2": [0, 360],
    "cspd3": [-4990, 4990],
    "cdir3": [0, 360],
    "tp": [1.7, 30],
    }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd1": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht": [20.47, -9999, np.nan],
    "mxwvht": [20.47, -9999, np.nan],
    "tp": [25.5, -9999, np.nan],
    "wvdir": [381, -9999, np.nan],
    "wvspread": [381, -9999, np.nan]
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)


# FORTALEZA
fortaleza = dict(
range_limits = {
    "swvht": [0.1, 19.9],
    "mxwvht": [0.1, 19.9],
    "tp": [1.7, 30],
    "wvdir": [0, 360],
    "wspd1": [0.1, 59],
    "wdir1": [0, 360],
    "gust1": [0.1, 59],
    "wspd2": [0.1, 59],
    "wdir2": [0, 360],
    "gust2": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "rh": [25, 102],
    "cspd1": [-4990, 4990],
    "cdir1": [0, 360],
    "cspd2": [-4990, 4990],
    "cdir2": [0, 360],
    "cspd3": [-4990, 4990],
    "cdir3": [0, 360],
    "tp": [1.7, 30],
    }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd1": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht": [20.47, -9999, np.nan],
    "mxwvht": [20.47, -9999, np.nan],
    "tp": [25.5, -9999, np.nan],
    "wvdir": [381, -9999, np.nan],
    "wvspread": [381, -9999, np.nan]
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)


# ITAGUAI
itaguai = dict(
range_limits = {
    "swvht": [0.1, 19.9],
    "mxwvht": [0.1, 19.9],
    "tp": [1.7, 30],
    "wvdir": [0, 360],
    "wspd1": [0.1, 59],
    "wdir1": [0, 360],
    "gust1": [0.1, 59],
    "wspd2": [0.1, 59],
    "wdir2": [0, 360],
    "gust2": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "rh": [25, 102],
    "cspd1": [-4990, 4990],
    "cdir1": [0, 360],
    "cspd2": [-4990, 4990],
    "cdir2": [0, 360],
    "cspd3": [-4990, 4990],
    "cdir3": [0, 360],
    "tp": [1.7, 30],
    }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd1": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht": [20.47, -9999, np.nan],
    "mxwvht": [20.47, -9999, np.nan],
    "tp": [25.5, -9999, np.nan],
    "wvdir": [381, -9999, np.nan],
    "wvspread": [381, -9999, np.nan]
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)


# ITAJAÍ
itajai = dict(
range_limits = {
    "swvht": [0.1, 19.9],
    "mxwvht": [0.1, 19.9],
    "tp": [1.7, 30],
    "wvdir": [0, 360],
    "wspd1": [0.1, 59],
    "wdir1": [0, 360],
    "gust1": [0.1, 59],
    "wspd2": [0.1, 59],
    "wdir2": [0, 360],
    "gust2": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "rh": [25, 102],
    "cspd1": [-4990, 4990],
    "cdir1": [0, 360],
    "cspd2": [-4990, 4990],
    "cdir2": [0, 360],
    "cspd3": [-4990, 4990],
    "cdir3": [0, 360],
    "tp": [1.7, 30],
    }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd1": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht": [20.47, -9999, np.nan],
    "mxwvht": [20.47, -9999, np.nan],
    "tp": [25.5, -9999, np.nan],
    "wvdir": [381, -9999, np.nan],
    "wvspread": [381, -9999, np.nan]
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)


# ITAOCA
itaoca = dict(
range_limits = {
    "swvht": [0.1, 19.9],
    "mxwvht": [0.1, 19.9],
    "tp": [1.7, 30],
    "wvdir": [0, 360],
    "wspd1": [0.1, 59],
    "wdir1": [0, 360],
    "gust1": [0.1, 59],
    "wspd2": [0.1, 59],
    "wdir2": [0, 360],
    "gust2": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "rh": [25, 102],
    "cspd1": [-4990, 4990],
    "cdir1": [0, 360],
    "cspd2": [-4990, 4990],
    "cdir2": [0, 360],
    "cspd3": [-4990, 4990],
    "cdir3": [0, 360],
    "tp": [1.7, 30],
    }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd1": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht": [20.47, -9999, np.nan],
    "mxwvht": [20.47, -9999, np.nan],
    "tp": [25.5, -9999, np.nan],
    "wvdir": [381, -9999, np.nan],
    "wvspread": [381, -9999, np.nan]
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)


# NITEROI
niteroi = dict(
range_limits = {
    "swvht": [0.1, 19.9],
    "mxwvht": [0.1, 19.9],
    "tp": [1.7, 30],
    "wvdir": [0, 360],
    "wspd1": [0.1, 59],
    "wdir1": [0, 360],
    "gust1": [0.1, 59],
    "wspd2": [0.1, 59],
    "wdir2": [0, 360],
    "gust2": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "rh": [25, 102],
    "cspd1": [-4990, 4990],
    "cdir1": [0, 360],
    "cspd2": [-4990, 4990],
    "cdir2": [0, 360],
    "cspd3": [-4990, 4990],
    "cdir3": [0, 360],
    "tp": [1.7, 30],
    }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd1": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht": [20.47, -9999, np.nan],
    "mxwvht": [20.47, -9999, np.nan],
    "tp": [25.5, -9999, np.nan],
    "wvdir": [381, -9999, np.nan],
    "wvspread": [381, -9999, np.nan]
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)


# PORTTO SEGURO
porto_seguro = dict(
range_limits = {
    "swvht": [0.1, 19.9],
    "mxwvht": [0.1, 19.9],
    "tp": [1.7, 30],
    "wvdir": [0, 360],
    "wspd1": [0.1, 59],
    "wdir1": [0, 360],
    "gust1": [0.1, 59],
    "wspd2": [0.1, 59],
    "wdir2": [0, 360],
    "gust2": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "rh": [25, 102],
    "cspd1": [-4990, 4990],
    "cdir1": [0, 360],
    "cspd2": [-4990, 4990],
    "cdir2": [0, 360],
    "cspd3": [-4990, 4990],
    "cdir3": [0, 360],
    "tp": [1.7, 30],
    }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd1": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht": [20.47, -9999, np.nan],
    "mxwvht": [20.47, -9999, np.nan],
    "tp": [25.5, -9999, np.nan],
    "wvdir": [381, -9999, np.nan],
    "wvspread": [381, -9999, np.nan]
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)


# RECIFE
recife = dict(
range_limits = {
    "swvht": [0.1, 19.9],
    "mxwvht": [0.1, 19.9],
    "tp": [1.7, 30],
    "wvdir": [0, 360],
    "wspd1": [0.1, 59],
    "wdir1": [0, 360],
    "gust1": [0.1, 59],
    "wspd2": [0.1, 59],
    "wdir2": [0, 360],
    "gust2": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "rh": [25, 102],
    "cspd1": [-4990, 4990],
    "cdir1": [0, 360],
    "cspd2": [-4990, 4990],
    "cdir2": [0, 360],
    "cspd3": [-4990, 4990],
    "cdir3": [0, 360],
    "tp": [1.7, 30],
    }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd1": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht": [20.47, -9999, np.nan],
    "mxwvht": [20.47, -9999, np.nan],
    "tp": [25.5, -9999, np.nan],
    "wvdir": [381, -9999, np.nan],
    "wvspread": [381, -9999, np.nan]
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)


# RIO GRANDE
rio_grande = dict(
range_limits = {
    "swvht": [0.1, 19.9],
    "mxwvht": [0.1, 19.9],
    "tp": [1.7, 30],
    "wvdir": [0, 360],
    "wspd1": [0.1, 59],
    "wdir1": [0, 360],
    "gust1": [0.1, 59],
    "wspd2": [0.1, 59],
    "wdir2": [0, 360],
    "gust2": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "rh": [25, 102],
    "cspd1": [-4990, 4990],
    "cdir1": [0, 360],
    "cspd2": [-4990, 4990],
    "cdir2": [0, 360],
    "cspd3": [-4990, 4990],
    "cdir3": [0, 360],
    "tp": [1.7, 30],
    }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd1": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht": [20.47, -9999, np.nan],
    "mxwvht": [20.47, -9999, np.nan],
    "tp": [25.5, -9999, np.nan],
    "wvdir": [381, -9999, np.nan],
    "wvspread": [381, -9999, np.nan]
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)


# SANTOS
santos = dict(
range_limits = {
    "swvht": [0.1, 19.9],
    "mxwvht": [0.1, 19.9],
    "tp": [1.7, 30],
    "wvdir": [0, 360],
    "wspd1": [0.1, 59],
    "wdir1": [0, 360],
    "gust1": [0.1, 59],
    "wspd2": [0.1, 59],
    "wdir2": [0, 360],
    "gust2": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "rh": [25, 102],
    "cspd1": [-4990, 4990],
    "cdir1": [0, 360],
    "cspd2": [-4990, 4990],
    "cdir2": [0, 360],
    "cspd3": [-4990, 4990],
    "cdir3": [0, 360],
    "tp": [1.7, 30],
    }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd1": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht": [20.47, -9999, np.nan],
    "mxwvht": [20.47, -9999, np.nan],
    "tp": [25.5, -9999, np.nan],
    "wvdir": [381, -9999, np.nan],
    "wvspread": [381, -9999, np.nan]
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)


# BMO SANTOS
bmo_santos = dict(
range_limits = {
    "swvht1": [0.1, 19.9],
    "mxwvht1": [0.1, 19.9],
    "tp1": [1.7, 30],
    "wvdir1": [0, 360],
    "swvht2": [0.1, 19.9],
    "tp2": [1.7, 30],
    "wvdir2": [0, 360],
    "wspd1": [0.1, 59],
    "wdir1": [0, 360],
    "gust1": [0.1, 59],
    "wspd2": [0.1, 59],
    "wdir2": [0, 360],
    "gust2": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "rh": [25, 102],
    "cspd1": [-4990, 4990],
    "cdir1": [0, 360],
    "cspd2": [-4990, 4990],
    "cdir2": [0, 360],
    "cspd3": [-4990, 4990],
    "cdir3": [0, 360],
    "tp": [1.7, 30],
    }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht1": [20.47, -9999, np.nan],
    "mxwvht1": [20.47, -9999, np.nan],
    "tp1": [25.5, -9999, np.nan],
    "wvdir1": [381, -9999, np.nan],
    "wvspread1": [381, -9999, np.nan],
    "swvht2": [20.47, -9999, np.nan],
    "tp2": [25.5, -9999, np.nan],
    "wvdir2": [381, -9999, np.nan],
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)



# VITÓRIA
vitoria = dict(
range_limits = {
    "swvht": [0.1, 19.9],
    "mxwvht": [0.1, 19.9],
    "tp": [1.7, 30],
    "wvdir": [0, 360],
    "wspd1": [0.1, 59],
    "wdir1": [0, 360],
    "gust1": [0.1, 59],
    "wspd2": [0.1, 59],
    "wdir2": [0, 360],
    "gust2": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "rh": [25, 102],
    "cspd1": [-4990, 4990],
    "cdir1": [0, 360],
    "cspd2": [-4990, 4990],
    "cdir2": [0, 360],
    "cspd3": [-4990, 4990],
    "cdir3": [0, 360],
    "tp": [1.7, 30],
    }
,
sigma_limits = {
    "swvht": 6,
    "rh": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "sst": 8.6,
    }
,
mis_value_limits = {
    "rh": [11, -9999, np.nan],
    "wspd1": [-9999, np.nan],
    "cspd1": [409.5, -9999, np.nan],
    "cdir1": [511, -9999, np.nan],
    "cspd2": [409.5, -9999, np.nan],
    "cdir2": [511, -9999, np.nan],
    "cspd3": [409.5, -9999, np.nan],
    "cdir3": [511, -9999, np.nan],
    "dewpt": [-10, -9999, np.nan],
    "atmp": [-10, -9999, np.nan],
    "sst": [40.955, -9999, np.nan],
    "swvht": [20.47, -9999, np.nan],
    "mxwvht": [20.47, -9999, np.nan],
    "tp": [25.5, -9999, np.nan],
    "wvdir": [381, -9999, np.nan],
    "wvspread": [381, -9999, np.nan]
    }
,
outlier_limits = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "tp": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
std_mean_values = {
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewpt": [-29, 39],
    "sst": [-3, 39],
    "apd": [1.7, 20],
    "cspd1": [-2500, 2500],
    "cspd2": [-2500, 2500],
    "cspd3": [-2500, 2500],
    }
,
height = {
    'wspd1': 4.4,
    'wspd2': 3.7
}
,
stuck_limits = 7
,
continuity_limits = 3
)
