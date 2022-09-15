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
    'sst': [13.7, 35.5],
    'swvht': [0.0, 6.1],
    'tp': [0.4, 18.8],
    'mean_tp': [0.0, 14.2],
    'wspd': [0.0, 16.5]
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
    "rh": [8, 48],
    "srad": [15, 48],
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
    'wspd1': [0.0, 15.2],
    'gust1': [0.0, 20.2],
    'atmp': [0.0, 62.4],
    'rh': [57.1, 126.3],
    'dewpt': [0.0, 41.3],
    'pres': [998.5, 1032.4],
    'sst': [11.1, 31.8],
    'swvht': [0.0, 4.9],
    'mxwvht': [0.0, 12.4],
    'tp': [0.0, 31.1]
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
    'wspd1': [0.0, 22.7],
    'gust1': [0.0, 25.1],
    'wspd2': [0.0, 21.4],
    'gust2': [0.0, 23.1],
    'atmp': [10.8, 32.7],
    'rh': [30.1, 121.8],
    'dewpt': [1.2, 32.9],
    'pres': [986.0, 1044.6],
    'sst': [14.1, 32.6],
    'srad': [0.0, 1271.2],
    'cspd1': [0.0, 1340.7],
    'cspd2': [0.0, 1332.5],
    'cspd3': [0.0, 1005.0],
    'swvht': [0.0, 7.4],
    'mxwvht': [0.0, 13.7],
    'tp': [0.3, 20.3]
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
    'wspd1': [0.0, 29.6],
    'gust1': [0.0, 28.9],
    'wspd2': [0.0, 24.3],
    'gust2': [0.0, 27.8],
    'atmp': [11.9, 33.4],
    'rh': [57.9, 134.4],
    'dewpt': [9.2, 34.9],
    'pres': [965.7, 1061.5],
    'sst': [12.4, 33.2],
    'srad': [0.0, 1674.5],
    'cspd1': [0.0, 1980.2],
    'cspd2': [0.0, 2217.1],
    'cspd3': [0.0, 2158.6],
    'swvht': [0.0, 8.7],
    'mxwvht': [0.0, 10.8],
    'tp': [0.0, 23.0]
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
    "rh": [8, 48],
    "srad": [15, 48],
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
outlier_limits = { # NOT VALID
    "swvht": [0, 15],
    "mxwvht": [0, 19],
    "tp": [1.7, 20],
    "wspd1": [0, 59],
    "gust1": [0, 59],
    "wspd2": [0, 59],
    "gust2": [0, 59],
    "atmp": [-8, 42],
    "rh": [8, 48],
    "srad": [15, 48],
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
    'wspd1': [0.0, 15.2],
    'gust1': [0.0, 28.5],
    'wspd2': [0.0, 14.7],
    'gust2': [0.0, 18.4],
    'atmp': [9.0, 38.5],
    'rh': [33.8, 126.7],
    'dewpt': [5.0, 35.2],
    'pres': [992.7, 1038.2],
    'sst': [14.4, 32.9],
    'srad': [0.0, 1132.6],
    # 'cspd1': [nan, nan],
    # 'cspd2': [nan, nan],
    # 'cspd3': [nan, nan],
    'swvht': [0.0, 2.3],
    'mxwvht': [0.0, 3.4],
    'tp': [0.0, 32.1]
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
    'wspd1': [0.0, 20.2],
    'gust1': [0.0, 21.6],
    'wspd2': [0.0, 24.6],
    'gust2': [0.0, 25.7],
    'atmp': [11.3, 38.0],
    'rh': [9.6, 109.9],
    'dewpt': [11.3, 32.4],
    'pres': [997.7, 1033.7],
    'sst': [20.9, 33.5],
    'srad': [0.0, 1298.5],
    'cspd1': [0.0, 1818.2],
    'cspd2': [0.0, 1813.3],
    'cspd3': [0.0, 1812.5],
    'swvht': [0.0, 5.7],
    'mxwvht': [0.0, 7.4],
    'tp': [0.0, 16.5]
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
    'wspd1': [0.0, 16.1],
    'gust1': [0.0, 20.3],
    'wspd2': [0.0, 17.2],
    'gust2': [0.0, 22.1],
    'atmp': [18.3, 34.7],
    'rh': [47.0, 106.1],
    'dewpt': [12.5, 31.7],
    'pres': [992.1, 1033.2],
    'sst': [20.4, 34.9],
    'srad': [0.0, 1212.3],
    'cspd1': [0.0, 1092.3],
    'cspd2': [0.0, 1244.0],
    'cspd3': [0.0, 1362.9],
    'swvht': [0.0, 5.6],
    'mxwvht': [0.0, 8.3],
    'tp': [0.0, 19.7]
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
    'wspd1': [0.0, 25.9],
    'gust1': [0.0, 31.2],
    'wspd2': [0.0, 25.1],
    'gust2': [0.0, 30.0],
    'atmp': [0.0, 39.9],
    'rh': [37.2, 115.9],
    'dewpt': [2.0, 31.3],
    'pres': [980.9, 1048.3],
    'sst': [13.6, 31.1],
    'srad': [0.0, 1167.1],
    'cspd1': [0.0, 1394.7],
    'cspd2': [0.0, 1399.4],
    'cspd3': [0.0, 1506.0],
    'swvht': [0.0, 10.9],
    'mxwvht': [0.0, 16.8],
    'tp': [0.0, 20.7]
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
    'wspd1': [0.0, 15.8],
    'gust1': [0.0, 24.8],
    'wspd2': [0.0, 19.5],
    'gust2': [0.0, 23.4],
    'atmp': [10.0, 36.1],
    'rh': [37.0, 118.3],
    'dewpt': [1.5, 36.4],
    'pres': [995.4, 1035.1],
    'sst': [16.3, 31.5],
    'srad': [0.0, 1204.2],
    'cspd1': [0.0, 1184.1],
    'cspd2': [0.0, 1159.1],
    'cspd3': [0.0, 1154.2],
    'swvht': [0.0, 7.9],
    'mxwvht': [0.0, 12.8],
    'tp': [0.0, 21.5]
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
    'wspd': [0.0, 19.5],
    'gust': [0.0, 23.4],
    'atmp': [10.0, 36.1],
    'dewpt': [5.1, 32.7],
    'rh': [1.5, 36.4],
    'pres': [995.4, 1035.1],
    'srad': [0.0, 1204.2],
    'sst': [16.3, 31.5],
    'cspd1': [0.0, 1184.1],
    'cspd2': [0.0, 1159.1],
    'cspd3': [0.0, 1154.2],
    'swvht1': [0.0, 7.9],
    'tp1': [0.0, 21.5],
    'mxwvht1': [0.0, 12.8],
    'swvht2': [0.0, 7.9],
    'tp2': [0.0, 21.5]
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
    'wspd1': [0.0, 19.7],
    'gust1': [0.0, 26.4],
    'wspd2': [0.0, 19.2],
    'gust2': [0.0, 25.6],
    'atmp': [16.1, 34.2],
    'rh': [45.5, 114.0],
    'dewpt': [10.1, 32.7],
    'pres': [995.6, 1036.0],
    'sst': [20.7, 32.1],
    'srad': [0.0, 1430.7],
    'cspd1': [0.0, 806.8],
    'cspd2': [0.0, 1044.0],
    'cspd3': [0.0, 1113.8],
    'swvht': [0.0, 5.2],
    'mxwvht': [0.0, 8.5],
    'tp': [0.0, 23.0]
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
