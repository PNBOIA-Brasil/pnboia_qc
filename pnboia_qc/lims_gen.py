import pandas as pd
import numpy as np
from pnboia_qc.qc_checks import QCChecks

import matplotlib.pyplot as plt
import plotly.graph_objs as go


def gen_outlier_lim(data,std_factor=3.):
    # drop unwanted parameters
    data = data.drop(columns='battery')
    # get buoys names
    buoys = data.index.levels[0]
    # generate global df
    lims = pd.DataFrame(columns=['buoy','param','mean','std','lower_lim','upper_lim'])

    # generate limits for each buoy and concatenate to the global dataframe
    for buoy in buoys:
        res = data.loc[buoy].dropna(how='all',axis=1).describe().loc[['mean','std']].T
        res.index.names = ['param']
        res.reset_index(inplace=True)
        res['lower_lim'] = res['mean'] - res['std']*std_factor
        res['upper_lim'] = res['mean'] + res['std']*std_factor
        res['buoy'] = buoy
        lims = pd.concat([lims,res])

    param_names = {'wspd':'wspd1','gust':'gust1'}
    lims['param'] = lims['param'].replace(param_names)
    lims.set_index(['buoy','param'],inplace=True)

    # replace negative lower_limits with 0.
    lims.loc[lims['lower_lim'] < 0,'lower_lim'] = 0.

    return lims


def gen_cont_lims(data,std_factor=3.):
    # drop unwanted parameters
    data = data.drop(columns='battery')
    # get buoys names
    buoys = data.index.levels[0]
    # generate global df
    lims = pd.DataFrame(columns=['buoy','param','mean','std','lim'])

    # generate limits for each buoy and concatenate to the global dataframe
    for buoy in buoys:
        res = data.loc[buoy].dropna(how='all',axis=1).diff().describe().loc[['mean','std']].T
        res.index.names = ['param']
        res.reset_index(inplace=True)
        res['lim'] = res['std']*std_factor
        res['buoy'] = buoy
        lims = pd.concat([lims,res])

    lims.set_index(['buoy','param'],inplace=True)

    return lims


def filter_data(data,
                buoy,
                limits,
                save_df=False,
                range_axys_limits=None,
                continuity_axys_limits=None):

    buoy_df = data.loc[buoy]
    variables = buoy_df.columns.to_list()


    if range_axys_limits:
        climate_limits = range_axys_limits
    else:
        climate_limits = limits['climate_axys_limits']

    if continuity_axys_limits:
        continuity_limit = continuity_axys_limits
    else:
        continuity_limit = limits['continuity_axys_limits']

    qc = QCChecks(data=buoy_df,
        variables=variables,
        mis_values=limits['mis_value_axys_limits'],
        limits=limits['range_axys_limits'],
        climate_limits=climate_limits,
        stuck_limit=limits['stuck_axys_limits'],
        sigma_values=limits['sigma_axys_limits'],
        continuity_limit=continuity_limit,
        height=limits['height']
        )

        # Missvalue test
    for parameter in limits['mis_value_axys_limits'].keys():
        qc.mis_value_check(parameter=parameter)
    print('mis_value_check done.')

    # Range test
    for parameter in limits['range_axys_limits'].keys():
        qc.range_check(parameter=parameter)
    print('range_check done.')

    # Climate range test
    for parameter in limits['climate_axys_limits'].keys():
        qc.range_check_climate(parameter=parameter)
    print('range_check_climate done.')

    # # Comparison between swvht and mxwvht
    # qc.swvht_mxwvht_check(swvht_name = 'swvht', mxwvht_name = 'mxwvht')

    # # Comparison of wind speed and gust
    # qc.wind_speed_gust_check(wspd_name='wspd1', gust_name='gust1')
    # qc.wind_speed_gust_check(wspd_name='wspd2', gust_name='gust2')

    # # Comparison of Dewpt and Atmp
    # qc.dewpt_atmp_check(dewpt_name='dewpt', atmp_name='atmp')

    # # Comparison of battery and pressure
    # qc.bat_sensor_check(battery_name='battery', pres_name='pres')

    # # Stuck sensor test
    # for parameter in variables:
    #     if parameter != 'battery':
    #         print(parameter)
    #         qc.stuck_sensor_check(parameter=parameter)

    # # Convert wind to 10 meters
    # qc.convert_10_meters(wspd_name='wspd1', gust_name='gust1')
    # qc.convert_10_meters(wspd_name='wspd2', gust_name='gust2')

    # # Select the best anemometer
    # qc.related_meas_check(parameters=['wspd1', 'wspd2', 'wdir1', 'wdir2', 'gust1', 'gust2'])

    # Time continuity test
    # for parameter in limits['sigma_axys_limits'].keys():
    #     print(parameter)
    #     qc.t_continuity_check(parameter=parameter)

    # # Front exception tests
    # qc.front_except_check1(wdir_name='wdir', atmp_name='atmp')
    # qc.front_except_check3(wspd_name='wspd', atmp_name='atmp')
    # qc.front_except_check4(pres_name='pres', wspd_name='wspd')
    # qc.front_except_check5(pres_name='pres')
    # qc.front_except_check6(wspd_name='wspd', swvht_name='swvht')

    def filter_data_dataframe(qc_object):
        filtered_bad_data = pd.DataFrame(index=qc_object.data.index,columns=qc_object.data.columns)
        bool_array_2 = np.logical_and(qc_object.flag>0, qc_object.flag<100)
        filtered_bad_data = qc_object.data[~bool_array_2]

        return filtered_bad_data

    filtered_data = filter_data_dataframe(qc)
    if save_df:
        filtered_data.to_csv(f'{buoy}_filtered.csv')

    return filtered_data


def manual_outlier_lims(buoy,limits_df):

    if isinstance(limits_df.index, pd.MultiIndex):
        lims_values = limits_df.loc[buoy,['lower_lim','upper_lim']].values.tolist()
        keys = limits_df.loc[buoy,['lower_lim','upper_lim']].index
    else:
        lims_values = limits_df.loc[:,['lower_lim','upper_lim']].values.tolist()
        keys = limits_df.loc[:,['lower_lim','upper_lim']].index

    outlier_lims_manual = dict()
    for key, value in zip(keys,lims_values):
        outlier_lims_manual[key] = value

    return outlier_lims_manual


def plot_interactive(data_raw,
         data_filt,
         parameter):

    layout = go.Layout(
            xaxis=dict(
                title='Datetime',
                titlefont=dict(color='black')
                    )
                        )

    trace1 = go.Scatter(
                    x = data_raw[parameter].index,
                    y = data_raw[parameter].values,
                    mode = 'markers',
                    line = dict(color='red',width=1)
                        )

    trace2 = go.Scatter(
                    x = data_filt[parameter].index,
                    y = data_filt[parameter].values,
                    mode = 'markers',
                    line = dict(color='red',width=1)
                        )

    fig = go.Figure(layout=layout)


    fig.add_trace(trace1)
    fig.add_trace(trace2)

    plot = fig.show()

    return plot


def plot_hist(data,
              parameter,
              color='lightcoral'):

    # stats calcs
    mean = data[parameter].mean()
    median = data[parameter].median()

    fig, ax = plt.subplots(1,2,sharey=True, figsize=(13,3.5),gridspec_kw={'width_ratios': [3, 0.4]})
    plt.subplots_adjust(wspace=0.03)

    data[parameter].plot(ls='None', marker='.', color=color, grid=False, ax=ax[0])
    ax[1].hist(data[parameter], color=color,bins=50, orientation='horizontal',alpha=0.8);

    ymin, ymax = ax[1].get_ylim()
    y_dash_line = ymin + (ymax-ymin)/2
    ax[0].axhline(y_dash_line, ls='--', lw=0.8, color='k')
    ax[1].axhline(y_dash_line, ls='--', lw=0.8, color='k')
    ax[1].axhline(mean, ls='--', lw=2, color='blue')
    ax[1].axhline(median, ls='--', lw=2, color='green')

    # norm_test = normaltest(data[parameter].values,nan_policy='omit')
    # norm_test_str = "p > 0.05" if norm_test[1] > 0.05 else "p < 0.05"
    # ax[1].annotate(norm_test_str,xy=(0.1,0.9),xycoords='axes fraction')

    ax[0].set_title(f"{parameter}", weight='bold',fontsize=16);

    plt.show()
