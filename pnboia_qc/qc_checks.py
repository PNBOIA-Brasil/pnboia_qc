"""
Python Version tested: Python 3 or greater

Required Dependencies: Numpy, time, math, pandas

Description: This module is designed to QC data colected by Fixed Station
(buoys, weather station). QC is based on "Manual de Controle de Qualidade de Dados
do PNBOIA". Each check generates a flag number. Depending the number of the flag,
the data is considered good, suspicious or bad

Flag Convention as follows:
 0 = good data or no QC performed
 1 - 50 = hard flag data. Bad data
 51 - 99 = soft flag data. Suspicious data

Author: Tobias Ferreira
Organization: Brazilian Navy, BR
Date: August 19th 2020
Version: 1.0

"""

import pandas as pd
import numpy as np
import time
import math
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

class QCChecks():

    def __init__(self,
        data:pd.DataFrame,
        variables:list,
        mis_values:dict=None,
        limits:dict=None,
        climate_limits:dict=None,
        stuck_limit:int=None,
        sigma_values:dict=None,
        continuity_limit:int=None,
        height:dict=None
        ):

        self.id_flag = {
            
        }

        self.mis_values = mis_values
        self.limits = limits       
        self.climate_limits = climate_limits
        self.stuck_limit = stuck_limit
        self.sigma_values = sigma_values
        self.height = height
        self.continuity_limit = continuity_limit
        
        self.data = data

        self.flag = (self.data[variables] * 0).replace(np.nan, 0).astype(int)

    def plot_comparison(self,
                        parameter:str,
                        ylim:list,
                        flag:str='all'):

        if flag == 'hard':
            bool_array = np.logical_or(self.flag[parameter]<1, self.flag[parameter]>50)
            bool_array_2 = np.logical_and(self.flag[parameter]>0, self.flag[parameter]<50)
        elif flag == 'soft':
            bool_array = np.logical_and(self.flag[parameter]<=50, self.flag[parameter] >= 0)
            bool_array_2 = np.logical_and(self.flag[parameter]>50, self.flag[parameter]<100)
        elif flag == 'all':
            bool_array = np.logical_and(self.flag[parameter]<1, self.flag[parameter]>=0)
            bool_array_2 = np.logical_and(self.flag[parameter]>0, self.flag[parameter]<100)


        self.filtered_data = self.data[parameter][bool_array]
        self.filtered_bad_data = self.data[parameter][bool_array_2]
        
        plt.plot(self.data.index, self.data[parameter], label = f"raw_{parameter}")
        plt.plot(self.filtered_data.index, self.filtered_data, label = "qc_{parameter}")
        plt.plot(self.filtered_bad_data.index, self.filtered_bad_data,marker='o', label = "bad_qc_{parameter}")
        plt.ylim(ylim[0], ylim[1])
        plt.show()


    def mis_value_check(self,
                        parameter:str,
                        mis_values:list = None):

        """
        Missing value check
        Flag the missing (MISVALUE) or None values

        Required input:
        - parameter: name of variable that will be checked
        - mis_values: list of values that represent that the data
        is incorrect or is missing

        Required checks: None

        Represented by number "1" -> HARD FLAG
        """

        if mis_values == None:
            mis_values = self.mis_values[parameter]
           
        try:
            for mis_value in mis_values:
                self.flag.loc[
                    (self.data[parameter] == mis_value) &
                    (self.flag[parameter] == 0), parameter] = 1
        except:
            print("No mis_value_limit for " + parameter)

        self.flag.loc[(self.data[parameter] == np.nan) & (self.flag[parameter] == 0), parameter] = 1


    def range_check(self,
                    parameter:str,
                    limits:list= None):

        """
        Range check
        Check to ensure values are within global and equipment ranges (LIMITS)

        Required input:
        - parameter: name of variable that will be checked
        - limits: limits for the equipment operation. It must be a tuple with
        the minimum and maximum value

        Required checks: Missing value check

        Represented by number "2" -> HARD FLAG
        """
        
        if limits == None:
            limits = self.limits[parameter]
            
        try:
            self.flag.loc[(self.data[parameter] < limits[0]) & (self.flag[parameter] == 0), parameter] = 2
            self.flag.loc[(self.data[parameter] > limits[1]) & (self.flag[parameter] == 0), parameter] = 2
        except:
            print("No range_limit for " + parameter)


    def range_check_climate(self,
                            parameter:str,
                            climate_limits:list = None):

        """
        Range check Climate
        Check to ensure values are within climatology ranges

        Required input:
        - parameter: name of variable that will be checked
        - limits: climatology limits. It must be a tuple with
        the minimum and maximum value
        
        Required checks: Missing value check, range check

        Represented by number "9" -> HARD FLAG
        """

        if climate_limits == None:
            climate_limits = self.climate_limits[parameter]

        try:
            self.flag.loc[(self.data[parameter] < climate_limits[0]) & (self.flag[parameter] == 0), parameter] = 9
            self.flag.loc[(self.data[parameter] > climate_limits[1]) & (self.flag[parameter] == 0), parameter] = 9
        except:
            print("No range_climate_limit for " + parameter)


    def swvht_mxwvht_check(self,
                           swvht_name:str = 'swvht',
                           mxwvht_name:str = 'mxwvht'):

        """
        Wave Significant Height x Wave Max Height
        Compares if the values of wind speed is higher than Gust.

        Required input:
        - swvht_name: name used in the dataframe for Wave Significance Height
        - mxwvht_name: name used in the dataframe for Maximun Wave Height

        Required checks: Missing value check, range check, range check climate

        Represented by number "4" -> HARD FLAG
        """

        self.flag.loc[(self.data[swvht_name] > self.data[mxwvht_name]) & (self.flag[swvht_name] == 0), swvht_name] = 4
        self.flag.loc[(self.data[swvht_name] > self.data[mxwvht_name]) & (self.flag[mxwvht_name] == 0), mxwvht_name] = 4

    def wind_speed_gust_check(self,
                              wspd_name:str = 'wspd',
                              gust_name:str = 'gust'):

        """
        Wind speed x Gust Check
        Compares if the values of wind speed is higher than Gust. Also verify if
        Gust is less of 0.5

        Required input:
        - wspd_name: name used in the dataframe for wind speed
        - gust_name: name used in the dataframe for gust speed

        Required checks: Missing value check, range check, range check climate

        Represented by number "3" -> HARD FLAG
        """

        self.flag.loc[(self.data[wspd_name] > self.data[gust_name]) & (self.flag[wspd_name] == 0), wspd_name] = 3
        self.flag.loc[(self.data[wspd_name] > self.data[gust_name]) & (self.flag[gust_name] == 0), gust_name] = 3
        self.flag.loc[(self.data[gust_name] < 0.5) & (self.flag[gust_name] == 0), gust_name] = 3


    def dewpt_atmp_check(self,
                         dewpt_name:str = 'dewpt',
                         atmp_name:str = 'atmp'):

        """
        Dew point x Air temperature Check
        Compares if the dewptoint values is higher than Air temperature values.
        If so, dewpt value will be changed to atmp value and data will be soft flagged

        Required input:
        - dewpt_name: name used in the dataframe for dew point
        - atmp_name: name used in the dataframe for air temperature

        Required checks: Missing value check, range check, range check climate

        Represented by number "51" -> SOFT FLAG
        """

        self.flag.loc[(self.data[dewpt_name] > self.data[atmp_name]) & (self.flag[dewpt_name] == 0)  & (self.flag[atmp_name] == 0), dewpt_name] = 51
        self.data.loc[(self.flag[dewpt_name] == 51), dewpt_name] = self.data[atmp_name]


    def bat_sensor_check(self,
                         battery_name:str='battery',
                         pres_name:str='pres'):

        """
        Battery x Air Pressure Check
        Pressure will be flagged if batterty is below of 10.5 V.

        Required input:
        - pres_name: name used in the dataframe for pressure
        - battery_name: name used in the dataframe for battery

        Required checks: Missing value check, range check, range check climate

        Represented by number "5" -> HARD FLAG
        """

        self.flag.loc[(self.data[battery_name] <= 10.5) & (self.flag[pres_name] == 0), pres_name] = 5


    def stuck_sensor_check (self,
                            parameter:str,
                            stuck_limit:int = None):

        """
        Stuck Sensor Check
        Verify if the value of a parameter repeats until limits times

        Required input:
        - parameter: name of variable that will be checked
        - limits: number of repetition used in the test

        Required checks: Missing value check, range check, range check climate

        Represented by number "6" -> HARD FLAG
        """
        
        if stuck_limit == None:
            stuck_limit = self.stuck_limit

        for counter in range(len(self.data)):
            value = self.data.loc[(self.data.index >= self.data.index[counter]) & (self.data.index <= self.data.index[counter] + pd.to_timedelta(stuck_limit, unit='h')) & (self.flag[parameter] == 0) & (self.flag[parameter] == 6), parameter]
            if value.size == 0:
                continue
            elif np.array(value == value[0]).all() and self.data.index[-1] - self.data.index[counter] >= pd.to_timedelta(limit, unit='h'):
                self.flag.loc[(index), parameter] = 6

    def convert_10_meters(self,
                          wspd_name:str='wspd',
                          gust_name:str='gust',
                          height:float=None):

        """
        Convert wind to 10 meters
        Using Liu equation to convert wind data to 10 meters

        Required input:
        - wspd_name: name used in the dataframe for wind speed
        - gust_name: name used in the dataframe for gust speed
        - height: height of anemometer sensor in the buoy

        Required checks: Missing value check, range check, range check climate,
        stuck sensor, windspeedgust check

        Return: var
        """
        if height == None:
            height = self.height[wspd_name]

        self.data.loc[(self.flag[wspd_name] == 0), wspd_name] = self.data[wspd_name] * (10 / height) ** 0.11

        self.data.loc[(self.flag[gust_name] == 0), gust_name] = self.data[gust_name] * (10 / height) ** 0.11


    def related_meas_check(self,
                           parameters:list):

        """
        Related Measurement Check
        Compares the values of the two anemometers to find the best one.

        Required input:
        - parameters: array of parameters names of wind data
        Example - ['wspd1', 'wspd2', 'wdir1', 'wdir2', 'gust1', 'gust2']

        Required checks: Missing value check, range check, range check climate,
        stuck sensor, windspeedgust check, convert_10_meters

        """

        self.data["wspd"] = self.data[parameters[0]]
        self.data["wdir"] = self.data[parameters[2]]
        self.data["gust"] = self.data[parameters[4]]

        self.flag["wspd"] = self.flag[parameters[0]]
        self.flag["wdir"] = self.flag[parameters[2]]
        self.flag["gust"] = self.flag[parameters[4]]

        self.data.loc[(self.flag[parameters[0]] != 0) & (self.flag[parameters[1]] == 0), "wspd"] = self.data[parameters[1]]
        self.flag.loc[(self.flag[parameters[0]] != 0) & (self.flag[parameters[1]] == 0), "wspd"] = self.flag[parameters[1]]

        self.data.loc[(self.flag[parameters[2]] != 0) & (self.flag[parameters[3]] == 0), "wdir"] = self.data[parameters[3]]
        self.flag.loc[(self.flag[parameters[2]] != 0) & (self.flag[parameters[3]] == 0), "wdir"] = self.flag[parameters[3]]

        self.data.loc[(self.flag[parameters[4]] != 0) & (self.flag[parameters[5]] == 0), "gust"] = self.data[parameters[5]]
        self.flag.loc[(self.flag[parameters[4]] != 0) & (self.flag[parameters[5]] == 0), "gust"] = self.flag[parameters[5]]

    def t_continuity_check(self,
                           parameter:str,
                           sigma:float = None,
                           continuity_limit:int = None):

        """
        Time continuity
        Check is to verify if the data has consistency in the time

        Required input:
        - sigma: value considered in the timecontinuity check variation in time
        - limit: number of hour considered in the time continuity test
        - parameter: name user in the dataframe to represent the parameter

        Required checks: Missing value check, range check, range check climate,
        stuck sensor

        Represented by number "8" -> HARD FLAG
        """

        if sigma == None:
            sigma = self.sigma_values[parameter]

        if continuity_limit == None:
            continuity_limit = self.continuity_limit


        self.flag['tmp_forward'] = 0
        self.flag['tmp_backward'] = 0

        for counter in range(len(self.data)):
            value = self.data.loc[(self.data.index >= self.data.index[counter]) & (self.data.index <= self.data.index[counter] + pd.to_timedelta(continuity_limit, unit='h')) & (self.flag[parameter] == 0), parameter]
            if value.size > 1:
                forward_values = np.array(value - value[0])
                backward_values = np.array(value - value[-1])
                delta_times_forward = np.array(value.index - value.index[0])/(10**9)/3600
                delta_times_backward = np.array(value.index - value.index[-1])/(10**9)/3600
                times = np.array(value.index)
                for i in range(len(delta_times_forward) - 1):
                    if (0.58 * sigma * (np.sqrt(int(delta_times_forward[i + 1])))) < forward_values[i + 1]:
                        self.flag.loc[(times[i]), "tmp_forward"] = 1
                    if (0.58 * sigma * (np.sqrt(int(-delta_times_backward[i])))) < backward_values[i]:
                        self.flag.loc[(times[i]), "tmp_backward"] = 1

        self.flag.loc[(self.flag["tmp_backward"] == 1) | (self.flag["tmp_forward"] == 1), parameter] = 8

        self.flag.drop(columns=['tmp_forward','tmp_backward'], inplace=True)

    def front_except_check1(self,
                            wdir_name:str='wdir',
                            atmp_name:str='atmp'):

        """
        Frontal exception for time continuity checks
        Exception for the time continuity during frontal passages

        Required checks: Missing value check, range check, range check climate,
        stuck sensor, time continuity
        
        Frontal exception 1
        Relation between wind direction and air temperature

        Required input:
        - wdir_name: name used in the dataframe for wind direction
        - atmp_name: name used in the dataframe for air temperature

        Represented by number "53" -> SOFT FLAG
        """

        self.data = self.data.sort_index(ascending=False)

        select_value = self.data.loc[((self.flag[atmp_name] == 8) | (self.flag[atmp_name] == 0)) & (self.flag[wdir_name] == 0)]

        self.flag.loc[(select_value.loc[(select_value[wdir_name].diff() > 40) &  (select_value[wdir_name].diff() < - 40) & (self.flag[atmp_name] == 8), atmp_name].index)] == 53

    def front_except_check3(self,
                            wspd_name:str='wspd',
                            atmp_name:str='atmp'):

        """
        Frontal exception for time continuity checks
        Exception for the time continuity during frontal passages

        Required checks: Missing value check, range check, range check climate,
        stuck sensor, time continuity
        
        Frontal exception 3
        Relation between wind speed and air temperature 2

        Required input:
        - wspd_name: name used in the dataframe for wind speed
        - atmp_name: name used in the dataframe for air temperature

        Represented by number "55" -> SOFT FLAG
        """

        self.flag.loc[((self.flag[atmp_name] == 8) & (self.flag[wspd_name] == 0) & (self.data[wspd_name] > 7)), atmp_name ] = 55


    def front_except_check4(self,
                            pres_name='pres',
                            wspd_name='wspd'):

        """
        Frontal exception for time continuity checks
        Exception for the time continuity during frontal passages

        Required checks: Missing value check, range check, range check climate,
        stuck sensor, time continuity
        
        Frontal exception 4
        Relation between low pressure and wind speed

        Required input:
        - wspd_name: name used in the dataframe for wind speed
        - pres_name: name used in the dataframe for pressure

        Return: flag
        Represented by number "56" -> SOFT FLAG
        """

        self.data = self.data.sort_index(ascending=True)

        self.data['date_time'] = self.data.index

        self.data['date_time'] = self.data.diff()["date_time"] / np.timedelta64(1, 's')

        select_value = self.data.loc[(self.flag[wspd_name] == 8) & (self.data["date_time"] < 3700)]

        select_value_2 = self.data.loc[self.data.index.isin(select_value.index + np.timedelta64(-1, "h"))]

        select_value["pres_new"] = select_value_2["pres"]

        select_value = select_value.loc[(select_value["pres_new"] <= 995)]

        self.flag.loc[(self.flag.index.isin(select_value.index)), wspd_name] = 56

        del self.data['date_time']

    def front_except_check5(self,
                            pres_name:str='pres'):

        """
        Frontal exception for time continuity checks
        Exception for the time continuity during frontal passages

        Required checks: Missing value check, range check, range check climate,
        stuck sensor, time continuity
        
        Frontal exception 5
        Relation between two pressures

        Required input:
        - pres_name: name used in the dataframe for pressure
        - var: dataframe for variables
        - flag: dataframe for flag

        Return: flag
        Represented by number "57" -> SOFT FLAG
        """

        self.data = self.data.sort_index(ascending=True)

        self.data['date_time'] = self.data.index

        self.data['date_time'] = self.data.diff()["date_time"] / np.timedelta64(1, 's')

        select_value = self.data.loc[(self.flag[pres_name] == 8) & (self.data["date_time"] < 3700)]

        select_value_2 = self.data.loc[self.data.index.isin(select_value.index + np.timedelta64(-1, "h"))]

        select_value["pres_new"] = select_value_2["pres"]

        select_value = select_value.loc[(select_value["pres_new"] < 1000)]

        self.flag.loc[(self.flag.index.isin(select_value.index)), pres_name] = 57

        self.data.drop(columns=['date_time'], inplace=True)

    def front_except_check6(self,
                         wspd_name:str = 'wspd',
                         swvht_name:str = 'swvht'):

        """
        Frontal exception for time continuity checks
        Exception for the time continuity during frontal passages

        Required checks: Missing value check, range check, range check climate,
        stuck sensor, time continuity
        
        Frontal exception 6
        Relation between significance wave height and wind speed

        Required input:
        - wspd_name: name used in the dataframe for wind speed
        - swvht_name: name used in the dataframe for significance wave height
        - var: dataframe for variables
        - flag: dataframe for flag

        Return: flag
        Represented by number "58" -> SOFT FLAG
        """

        self.flag.loc[((self.flag[swvht_name] == 8) & (self.data[wspd_name] >= 15)), swvht_name ] = 58

    def comparison_related_check(self,
                                 parameters:list):

        """
        Comparison of Measurement Check
        Relation between related measurement (wind speed, gust, etc)

        Required input:
        - parameters: list of parameters names to be related

        Return: flag
        Represented by number "60" -> SOFT FLAG
        """

        for i in len(parameters):
            params_test = parameters.remove(i)
            for param in params_test:
                self.flag.loc[((self.flag[param] < 51) & (self.flag[param] > 0) & (self.flag[parameters[i]] == 0)), parameters[i]] = 60

    def hsts_check(self,
                   swvht_name:str = 'swvht',
                   mean_tp_name:str='mean_tp'):

        """
        swvht x Average Period check
        Compare the wave significant height and Average period
        If the value do not change, it will be flagged

        Required input:
        - mean_tp_name: name used in the dataframe for mean period
        - swvht_name: name used in the dataframe for significance wave height

        Required checks: Range Check, Missing value check

        Represented by number "62" -> SOFT FLAG
        """

        self.data["hmax"] = 10000

        self.data.loc[(self.data[mean_tp_name] < 5), "hmax"] = 2.55 + (self.data[mean_tp_name] / 4)

        self.data.loc[(self.data[mean_tp_name] >= 5), "hmax"] = (1.16 * self.data[mean_tp_name]) - 2

        self.flag.loc[(self.data[swvht_name] <= self.data["hmax"]) & (self.data[swvht_name] == 0)] = 62

