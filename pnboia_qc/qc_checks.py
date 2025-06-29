"""
Python Version tested: Python 3 or greater

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
import plotly.express as px
import plotly.graph_objects as go

class QCChecks():
    """
    Class that contains all the quality control process.

    Variables:
    data:pd.DataFrame -> dataframe that has an index as datetime and variables in each column,
    variables:list -> list of variables that represents the data that will be QC. Ex.: ['wspd', 'tp']
    mis_values:dict=None -> dictionary for missing values for each variable. Ex: {'wspd': [-9999, np.nan], 'tp': [-9999]}
    limits:dict=None -> dictionary for sensors limits. If the sst sensor collect data between 0-40°C, the limits will {'sst': [0, 39]}
    fine_limits:dict=None -> dictionary for outlier limit.
    stuck_limit:int=None -> number of allowed repititive values
    sigma_values:dict=None -> dictionary of sigma values for each continuity limit
    continuity_limit:int=None -> number in hours that will be compared for time continuity value
    height:dict=None -> height of the anemometer below the see surface
    qc_config:dict=None -> configuration parameter that sumarizes all the quality control process
    """

    def __init__(self,
        data:pd.DataFrame,
        variables:list,
        mis_values:dict=None,
        limits:dict=None,
        fine_limits:dict=None,
        stuck_limit:int=None,
        sigma_values:dict=None,
        continuity_limit:int=None,
        height:dict=None,
        qc_config:dict=None
        ):

        self.id_flag = {

        }

        self.tests = list(filter(lambda a: a[0] != '_', dir(self)))

        self.mis_values = mis_values
        self.limits = limits
        self.fine_limits = fine_limits
        self.stuck_limit = stuck_limit
        self.sigma_values = sigma_values
        self.height = height
        self.continuity_limit = continuity_limit

        self.qc_config = qc_config

        self.data = data

        self.flag = (self.data[variables] * 0).replace(np.nan, 0).astype(int)


    def plot_comparison(self,
                        parameter:str,
                        ylim:list,
                        flag:str='all',
                        plot_type='matplotlib',
                        start_date=None,
                        end_date=None):


        """
        Class that contains all the quality control process.

        Variables:
        data:pd.DataFrame -> dataframe that has an index as datetime and variables in each column,
        variables:list -> list of variables that represents the data that will be QC. Ex.: ['wspd', 'tp']
        mis_values:dict=None -> dictionary for missing values for each variable. Ex: {'wspd': [-9999, np.nan], 'tp': [-9999]}
        limits:dict=None -> dictionary for sensors limits. If the sst sensor collect data between 0-40°C, the limits will {'sst': [0, 39]}
        fine_limits:dict=None -> dictionary for outlier limit.
        stuck_limit:int=None -> number of allowed repititive values
        sigma_values:dict=None -> dictionary of sigma values for each continuity limit
        continuity_limit:int=None -> number in hours that will be compared for time continuity value
        height:dict=None -> height of the anemometer below the see surface
        qc_config:dict=None -> configuration parameter that sumarizes all the quality control process
        """


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

        self.data_selected = self.data[parameter]
        if start_date != None:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            self.data_selected = self.data_selected.loc[self.data_selected.index>start_date]
            self.filtered_data = self.filtered_data.loc[self.filtered_data.index>start_date]
            self.filtered_bad_data = self.filtered_bad_data.loc[self.filtered_bad_data.index>start_date]
        if end_date != None:
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            self.data_selected = self.data_selected.loc[self.data_selected.index<end_date]
            self.filtered_data = self.filtered_data.loc[self.filtered_data.index<end_date]
            self.filtered_bad_data = self.filtered_bad_data.loc[self.filtered_bad_data.index<end_date]

        if plot_type == 'matplotlib':
            plt.plot(self.data_selected.index, self.data_selected, label = f"raw_{parameter}")
            plt.plot(self.filtered_data.index, self.filtered_data, label = "qc_{parameter}")
            plt.plot(self.filtered_bad_data.index, self.filtered_bad_data,marker='o', label = "bad_qc_{parameter}")
            plt.ylim(ylim[0], ylim[1])
            plt.show()
        elif plot_type == 'plotly':
            fig = go.Figure(layout_yaxis_range=[ylim[0],ylim[1]])
            fig.add_trace(go.Scatter(x=self.data_selected.index, y=self.data_selected,
                                mode='lines',
                                name='all data'))
            fig.add_trace(go.Scatter(x=self.filtered_data.index, y=self.filtered_data,
                                mode='lines',
                                name='good_data'))
            fig.add_trace(go.Scatter(x=self.filtered_bad_data.index, y=self.filtered_bad_data,
                                mode='markers',
                                name='bad_data'))
            fig.show()




    def mis_value(self,
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
                    (self.data[parameter] == float(mis_value)) &
                    (self.flag[parameter] == 0), parameter] = 1
        except:
            print("No mis_value_limit for " + parameter)

        self.flag.loc[(self.data[parameter] == np.nan) & (self.flag[parameter] == 0), parameter] = 1
        print(f'{parameter}: {self.flag.loc[self.flag[parameter] == 1, parameter].count()} flagged data')

    def range(self,
                    parameter:str,
                    limits:list= None,
                    test:str='gross'):

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
        try:
            if test == 'gross':
                flag_id = 2
                if limits == None:
                    limits = self.limits[parameter]
            if test == 'fine':
                flag_id = 9
                if limits == None:
                    limits = self.fine_limits[parameter]
            self.flag.loc[(self.data[parameter] < limits[0]) & (self.flag[parameter] == 0), parameter] = flag_id
            self.flag.loc[(self.data[parameter] > limits[1]) & (self.flag[parameter] == 0), parameter] = flag_id
            print(f'{parameter}: {self.flag.loc[self.flag[parameter] == flag_id, parameter].count()} flagged data')
        except:
            print("No range_limit for " + parameter)


    def swvht_mxwvht(self,
                           swvht_name:str = 'swvht',
                           mxwvht_name:str = 'mxwvht'):

        """
        Wave Significant Height x Wave Max Height
        Compares if the values of wind speed is higher than Gust.

        Required input:
        - swvht_name: name used in the dataframe for Wave Significance Height
        - mxwvht_name: name used in the dataframe for Maximun Wave Height

        Required checks: Missing value check, range check, range check fine

        Represented by number "4" -> HARD FLAG
        """

        self.flag.loc[(self.data[swvht_name] > self.data[mxwvht_name]) & (self.flag[swvht_name] == 0), swvht_name] = 4
        self.flag.loc[(self.data[swvht_name] > self.data[mxwvht_name]) & (self.flag[mxwvht_name] == 0), mxwvht_name] = 4
        print(f'{swvht_name}: {self.flag.loc[self.flag[swvht_name] == 4, swvht_name].count()} flagged data')
        print(f'{mxwvht_name}: {self.flag.loc[self.flag[mxwvht_name] == 4, mxwvht_name].count()} flagged data')

    def wind_speed_gust(self,
                              wspd_name:str = 'wspd',
                              gust_name:str = 'gust'):

        """
        Wind speed x Gust Check
        Compares if the values of wind speed is higher than Gust. Also verify if
        Gust is less of 0.5

        Required input:
        - wspd_name: name used in the dataframe for wind speed
        - gust_name: name used in the dataframe for gust speed

        Required checks: Missing value check, range check, range check fine

        Represented by number "3" -> HARD FLAG
        """

        self.flag.loc[(self.data[wspd_name] > self.data[gust_name]) & (self.flag[wspd_name] == 0), wspd_name] = 3
        self.flag.loc[(self.data[wspd_name] > self.data[gust_name]) & (self.flag[gust_name] == 0), gust_name] = 3
        self.flag.loc[(self.data[gust_name] < 0.5) & (self.flag[gust_name] == 0), gust_name] = 3
        print(f'{wspd_name}: {self.flag.loc[self.flag[wspd_name] == 3, wspd_name].count()} flagged data')
        print(f'{gust_name}: {self.flag.loc[self.flag[gust_name] == 3, gust_name].count()} flagged data')

    def dewpt_atmp(self,
                         dewpt_name:str = 'dewpt',
                         atmp_name:str = 'atmp'):

        """
        Dew point x Air temperature Check
        Compares if the dewptoint values is higher than Air temperature values.
        If so, dewpt value will be changed to atmp value and data will be soft flagged

        Required input:
        - dewpt_name: name used in the dataframe for dew point
        - atmp_name: name used in the dataframe for air temperature

        Required checks: Missing value check, range check, range check fine

        Represented by number "51" -> SOFT FLAG
        """

        self.flag.loc[(self.data[dewpt_name] > self.data[atmp_name]) & (self.flag[dewpt_name] == 0)  & (self.flag[atmp_name] == 0), dewpt_name] = 51
        self.data.loc[(self.flag[dewpt_name] == 51), dewpt_name] = self.data[atmp_name]
        print(f'{dewpt_name}: {self.flag.loc[self.flag[dewpt_name] == 51, dewpt_name].count()} flagged data')

    def battery(self,
                         battery_name:str='battery',
                         pres_name:str='pres'):

        """
        Battery x Air Pressure Check
        Pressure will be flagged if batterty is below of 10.5 V.

        Required input:
        - pres_name: name used in the dataframe for pressure
        - battery_name: name used in the dataframe for battery

        Required checks: Missing value check, range check, range check fine

        Represented by number "5" -> HARD FLAG
        """

        self.flag.loc[(self.data[battery_name] <= 10.5) & (self.flag[pres_name] == 0), pres_name] = 5
        print(f'{pres_name}: {self.flag.loc[self.flag[pres_name] == 5, pres_name].count()} flagged data')


    def stuck_sensor(self,
                            parameter:str,
                            stuck_limit:int = None):

        """
        Stuck Sensor Check
        Verify if the value of a parameter repeats until limits times

        Required input:
        - parameter: name of variable that will be checked
        - limits: number of repetition used in the test

        Required checks: Missing value check, range check, range check fine

        Represented by number "6" -> HARD FLAG
        """

        if stuck_limit == None:
            stuck_limit = self.stuck_limit

        value = self.data.loc[(self.flag[parameter] == 0), parameter].diff().abs()
        value = value.rolling(f'{stuck_limit}H').sum()
        index = value[value == 0].index
        self.flag.loc[(index), parameter] = 6
        print(f'{parameter}: {self.flag.loc[self.flag[parameter] == 6, parameter].count()} flagged data')

    def convert_wind(self,
                    wspd_name:str='wspd',
                    gust_name:str='gust',
                    height:float=10):
        """
        Convert wind to 10 meters
        Using Liu equation to convert wind data to 10 meters

        Required input:
        - wspd_name: name used in the dataframe for wind speed
        - gust_name: name used in the dataframe for gust speed
        - height: height of anemometer sensor in the buoy

        Required checks: Missing value check, range check, range check fine,
        stuck sensor, windspeedgust check

        Return: var
        """
        if height is None and hasattr(self, 'height') and wspd_name in self.height:
            height = self.height[wspd_name]

        # Only process rows where flag is 0 (good data)
        mask = (self.flag[wspd_name] == 0)
        self.data.loc[mask, wspd_name] = (self.data.loc[mask, wspd_name] * (10 / height) ** 0.11).round(2)

        if gust_name and gust_name in self.data.columns:
            mask = (self.flag[gust_name] == 0)
            self.data.loc[mask, gust_name] = (self.data.loc[mask, gust_name] * (10 / height) ** 0.11).round(2)

    def true_north(self,
                  parameter:str,
                  annual_variation:float,
                  year_reference:int,
                  mag_deg:float,
                  convert_to_int=True):
        # print(f"\n[DEBUG] Starting true_north for parameter: {parameter}")
        # print(f"[DEBUG] Input parameters - annual_variation: {annual_variation}, year_reference: {year_reference}, mag_deg: {mag_deg}, convert_to_int: {convert_to_int}")
        
        # Store original values for comparison
        original = self.data[parameter].copy()
        data_flags = self.data.copy()
        
        # Print sample of original data
        # print(f"[DEBUG] Sample original data (first 5 rows) for {parameter}:")
        # print(original.head())
        
        # Calculate year difference for annual variation
        data_flags['year'] = data_flags.index.year
        year_diff = data_flags['year'] - year_reference
        
        # Calculate magnetic declination for each timestamp
        data_flags['mag_decl'] = mag_deg + (year_diff * annual_variation)
        
        # Print sample of calculated magnetic declination
        # print("\n[DEBUG] Sample magnetic declination values (first 5 rows):")
        # print(data_flags[['year', 'mag_decl']].head())
        
        # Only apply correction to non-NaN values with flag 0
        filter_condition = (self.flag[parameter] == 0) & (data_flags[parameter].notna())
        # print(f"\n[DEBUG] Filter condition matched {filter_condition.sum()} rows for correction")
        
        # Get the magnetic declination for conversion
        tmp_mag = data_flags.loc[filter_condition, 'mag_decl']
        # print(f"[DEBUG] Applying correction to {len(tmp_mag)} rows")
        
        if len(tmp_mag) > 0:
            # Print sample of values before correction
            # print("\n[DEBUG] Sample values BEFORE correction:")
            # sample_before = data_flags.loc[filter_condition, parameter].head(5)
            # print(sample_before)
            
            # Apply correction only to non-NaN values with flag 0
            data_flags.loc[filter_condition, parameter] += tmp_mag
            
            # Print sample of values after correction (before wrap-around)
            # print("\n[DEBUG] Sample values AFTER correction (before wrap-around):")
            # print(data_flags.loc[filter_condition, parameter].head(5))
            
            # Handle wrap-around for degrees
            condition1 = (data_flags[parameter] < 0)
            condition2 = (data_flags[parameter] > 360)
            
            # print(f"[DEBUG] Rows with values < 0: {condition1.sum()}")
            # print(f"[DEBUG] Rows with values > 360: {condition2.sum()}")
            
            # if condition1.any():
            #     print("\n[DEBUG] Sample values < 0 before wrap-around:")
            #     print(data_flags.loc[condition1, parameter].head())
                
            # if condition2.any():
            #     print("\n[DEBUG] Sample values > 360 before wrap-around:")
            #     print(data_flags.loc[condition2, parameter].head())
            
            data_flags.loc[condition1, parameter] = data_flags.loc[condition1, parameter] + 360
            data_flags.loc[condition2, parameter] = data_flags.loc[condition2, parameter] - 360
            
            # # Print sample of values after wrap-around
            # if condition1.any() or condition2.any():
            #     print("\n[DEBUG] Sample values AFTER wrap-around:")
            #     sample_after = data_flags.loc[filter_condition, parameter].head(5)
            #     print(sample_after)
        
        # if convert_to_int:
        #     print("\n[DEBUG] Converting values to integers")
        #     non_na_count = data_flags[parameter].notna().sum()
        #     print(f"[DEBUG] Converting {non_na_count} non-NA values to integers")
        #     data_flags.loc[data_flags[parameter].notna(), parameter] = data_flags.loc[data_flags[parameter].notna(), parameter].astype(int)
        
        # # Show before/after for a few samples
        # sample_size = min(5, len(original[filter_condition]))
        # if sample_size > 0:
        #     print(f"\n[DEBUG] Sample of {sample_size} corrections for {parameter}:")
        #     sample_idx = original[filter_condition].index[:sample_size]
        #     for idx in sample_idx:
        #         print(f"  Row {idx}: {original[idx]} -> {data_flags.loc[idx, parameter]}")
        
        # Store the result back to self.data
        self.data = data_flags.drop(columns=['mag_decl', 'year'], errors='ignore').copy()
        
        # Print final sample of data
        # print(f"\n[DEBUG] Final sample of {parameter} after true_north correction (first 5 rows):")
        # print(self.data[parameter].head())
        
        print(f"[DEBUG] true_north completed for {parameter}")


    def best_sensor(self,
                            parameters1:list=["wspd1", "wdir1", "gust1"],
                            parameters2:list=["wspd2", "wdir2", "gust2"]):

        """
        Related Measurement Check
        Compares the values of the two anemometers to find the best one.

        Required input:
        - parameters: array of parameters names of wind data
        Example - ['wspd1', 'wspd2', 'wdir1', 'wdir2', 'gust1', 'gust2']

        Required checks: Missing value check, range check, range check fine,
        stuck sensor, windspeedgust check, convert_10_meters

        """

        self.data["wspd"] = self.data[parameters1[0]]
        self.data["wdir"] = self.data[parameters1[1]]
        self.data["gust"] = self.data[parameters1[2]]

        self.flag["wspd"] = self.flag[parameters1[0]]
        self.flag["wdir"] = self.flag[parameters1[1]]
        self.flag["gust"] = self.flag[parameters1[2]]

        self.data.loc[(self.flag[parameters1[0]] != 0) & (self.flag[parameters2[0]] == 0), "wspd"] = self.data[parameters2[0]]
        self.flag.loc[(self.flag[parameters1[0]] != 0) & (self.flag[parameters2[0]] == 0), "wspd"] = self.flag[parameters2[0]]

        self.data.loc[(self.flag[parameters1[1]] != 0) & (self.flag[parameters2[1]] == 0), "wdir"] = self.data[parameters2[1]]
        self.flag.loc[(self.flag[parameters1[1]] != 0) & (self.flag[parameters2[1]] == 0), "wdir"] = self.flag[parameters2[1]]

        self.data.loc[(self.flag[parameters1[2]] != 0) & (self.flag[parameters2[2]] == 0), "gust"] = self.data[parameters2[2]]
        self.flag.loc[(self.flag[parameters1[2]] != 0) & (self.flag[parameters2[2]] == 0), "gust"] = self.flag[parameters2[2]]

    def t_continuity(self,
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

        Required checks: Missing value check, range check, range check fine,
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
                delta_times_forward =  np.array((value.index - value.index[0]).total_seconds())/3600
                delta_times_backward = np.array((value.index - value.index[-1]).total_seconds())/3600
                times = np.array(value.index)
                for i in range(len(delta_times_forward) - 1):
                    if (0.58 * sigma * (np.sqrt(delta_times_forward[i + 1]))) < forward_values[i + 1]:
                        self.flag.loc[(times[i]), "tmp_forward"] = 1
                    if (0.58 * sigma * (np.sqrt(-delta_times_backward[i]))) < backward_values[i]:
                        self.flag.loc[(times[i]), "tmp_backward"] = 1

        self.flag.loc[(self.flag["tmp_backward"] == 1) | (self.flag["tmp_forward"] == 1), parameter] = 8

        self.flag.drop(columns=['tmp_forward','tmp_backward'], inplace=True)
        print(f'{parameter}: {self.flag.loc[self.flag[parameter] == 8, parameter].count()} flagged data')

    def front_except1(self,
                            wdir_name:str='wdir',
                            atmp_name:str='atmp'):

        """
        Frontal exception for time continuity checks
        Exception for the time continuity during frontal passages

        Required checks: Missing value check, range check, range check fine,
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
        print(f'{atmp_name}: {self.flag.loc[self.flag[atmp_name] == 53, atmp_name].count()} flagged data')

    def front_except3(self,
                            wspd_name:str='wspd',
                            atmp_name:str='atmp'):

        """
        Frontal exception for time continuity checks
        Exception for the time continuity during frontal passages

        Required checks: Missing value check, range check, range check fine,
        stuck sensor, time continuity

        Frontal exception 3
        Relation between wind speed and air temperature 2

        Required input:
        - wspd_name: name used in the dataframe for wind speed
        - atmp_name: name used in the dataframe for air temperature

        Represented by number "55" -> SOFT FLAG
        """

        self.flag.loc[((self.flag[atmp_name] == 8) & (self.flag[wspd_name] == 0) & (self.data[wspd_name] > 7)), atmp_name ] = 55
        print(f'{atmp_name}: {self.flag.loc[self.flag[atmp_name] == 55, atmp_name].count()} flagged data')


    def front_except4(self,
                            pres_name='pres',
                            wspd_name='wspd'):

        """
        Frontal exception for time continuity checks
        Exception for the time continuity during frontal passages

        Required checks: Missing value check, range check, range check fine,
        stuck sensor, time continuity

        Frontal exception 4
        Relation between low pressure and wind speed

        Required input:
        - wspd_name: name used in the dataframe for wind speed
        - pres_name: name used in the dataframe for pressure

        Return: flag
        Represented by number "56" -> SOFT FLAG
        """

        if 'date_time' not in self.data.columns and isinstance(self.data.index, pd.DatetimeIndex):
            self.data['date_time'] = self.data.index

        select_value = self.data.loc[(self.flag[wspd_name] == 8) & (self.data["date_time"] < 3700)]

        select_value_2 = self.data.loc[self.data.index.isin(select_value.index + np.timedelta64(-1, "h"))]

        select_value["pres_new"] = select_value_2["pres"]

        select_value = select_value.loc[(select_value["pres_new"] <= 995)]

        self.flag.loc[(self.flag.index.isin(select_value.index)), wspd_name] = 56

        print(f'{wspd_name}: {self.flag.loc[self.flag[wspd_name] == 56, wspd_name].count()} flagged data')
        # Do not delete date_time column to preserve it for other QC checks
        # del self.data['date_time']

    def front_except5(self,
                            pres_name:str='pres'):

        """
        Frontal exception for time continuity checks
        Exception for the time continuity during frontal passages

        Required checks: Missing value check, range check, range check fine,
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

        if 'date_time' not in self.data.columns and isinstance(self.data.index, pd.DatetimeIndex):
            self.data['date_time'] = self.data.index

        select_value = self.data.loc[(self.flag[pres_name] == 8) & (self.data["date_time"] < 3700)]

        select_value_2 = self.data.loc[self.data.index.isin(select_value.index + np.timedelta64(-1, "h"))]

        select_value["pres_new"] = select_value_2["pres"]

        select_value = select_value.loc[(select_value["pres_new"] < 1000)]

        self.flag.loc[(self.flag.index.isin(select_value.index)), pres_name] = 57

        # Do not drop date_time column to preserve it for other QC checks
        # self.data.drop(columns=['date_time'], inplace=True)
        print(f'{pres_name}: {self.flag.loc[self.flag[pres_name] == 57, pres_name].count()} flagged data')

    def front_except6(self,
                         wspd_name:str = 'wspd',
                         swvht_name:str = 'swvht'):

        """
        Frontal exception for time continuity checks
        Exception for the time continuity during frontal passages

        Required checks: Missing value check, range check, range check fine,
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
        print(f'{swvht_name}: {self.flag.loc[self.flag[swvht_name] == 58, swvht_name].count()} flagged data')

    def comparison_related(self,
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

    def hsts(self,
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

    def ascat_anemometer(self,
                                limits:dict,
                                parameters1:list=["wspd1", "wdir1", "gust1"],
                                parameters2:list=["wspd2", "wdir2", "gust2"]):

        """
        Comparison of Measurement Check
        Relation between related measurement (wind speed, gust, etc)

        Required input:
        - parameters: list of parameters names to be related

        Return: flag
        Represented by number "60" -> SOFT FLAG
        """

        for limit in limits:
            if limit["choice"] == 0:
                self.flag.loc[(self.flag.index >= limit["start_date"]) & (self.flag.index < limit["end_date"]), parameters1] = 11
                self.flag.loc[(self.flag.index >= limit["start_date"]) & (self.flag.index < limit["end_date"]), parameters2] = 11
            elif limit["choice"] == 1:
                self.flag.loc[(self.flag.index >= limit["start_date"]) & (self.flag.index < limit["end_date"]), parameters2] = 11
            elif limit["choice"] == 2:
                self.flag.loc[(self.flag.index >= limit["start_date"]) & (self.flag.index < limit["end_date"]), parameters1] = 11


    def run(self):
        if self.qc_config:
            for func_value in self.qc_config.keys():
                if func_value == 'miss_value':
                    print('-------------')
                    print(f'Check {func_value}')
                    for idx, parameter in enumerate(self.qc_config[func_value]['parameters']):
                        print(f'parameter: {parameter}')
                        self.mis_value(parameter=parameter, mis_values=self.qc_config[func_value]['limits'][idx])
                elif func_value == 'gross_range':
                    print('-------------')
                    print(f'Check {func_value}')
                    for idx, parameter in enumerate(self.qc_config[func_value]['parameters']):
                        print(f'parameter: {parameter}')
                        self.range(parameter=parameter, limits=self.qc_config[func_value]['limits'][idx], test='gross')
                elif func_value == 'fine_range':
                    print('-------------')
                    print(f'Check {func_value}')
                    for idx, parameter in enumerate(self.qc_config[func_value]['parameters']):
                        print(f'parameter: {parameter}')
                        self.range(parameter=parameter, limits=self.qc_config[func_value]['limits'][idx], test='fine')
                elif func_value == 'fine_range':
                    print('-------------')
                    print(f'Check {func_value}')
                    for idx, parameter in enumerate(self.qc_config[func_value]['parameters']):
                        print(f'parameter: {parameter}')
                        self.range(parameter=parameter, limits=self.qc_config[func_value]['limits'][idx], test='fine')
                elif func_value == 'ascat_anemometer':
                    print('-------------')
                    print(f'Check {func_value}')
                    self.ascat_anemometer(limits=self.qc_config[func_value]['limits'],
                                            parameters1=self.qc_config[func_value]['parameters'][0],
                                            parameters2=self.qc_config[func_value]['parameters'][1])
                elif func_value == 'swvht_mxwvht':
                    print('-------------')
                    print(f'Check {func_value}')
                    for idx, parameter in enumerate(self.qc_config[func_value]['parameters']):
                        self.swvht_mxwvht(swvht_name = parameter[0], mxwvht_name = parameter[1])
                elif func_value == 'wind_speed_gust':
                    print('-------------')
                    print(f'Check {func_value}')
                    for idx, parameter in enumerate(self.qc_config[func_value]['parameters']):
                        self.wind_speed_gust(wspd_name=parameter[0], gust_name=parameter[1])
                elif func_value == 'dewpt_atmp':
                    print('-------------')
                    print(f'Check {func_value}')
                    for idx, parameter in enumerate(self.qc_config[func_value]['parameters']):
                        self.dewpt_atmp(dewpt_name=parameter[0], atmp_name=parameter[1])
                elif func_value == 'battery':
                    print('-------------')
                    print(f'Check {func_value}')
                    for idx, parameter in enumerate(self.qc_config[func_value]['parameters']):
                        self.battery(battery_name=parameter[0], pres_name=parameter[1])
                elif func_value == 'stuck_sensor':
                    print('-------------')
                    print(f'Check {func_value}')
                    for idx, parameter in enumerate(self.qc_config[func_value]['parameters']):
                        print(f'parameter: {parameter}')
                        self.stuck_sensor(parameter=parameter, stuck_limit=self.qc_config[func_value]['limits'])
                elif func_value == 'convert_wind':
                    print('-------------')
                    print(f'[DEBUG] Starting {func_value} check')
                    print(f'[DEBUG] Parameters from config: {self.qc_config[func_value]}')
                    
                    # Check if parameters is a list of lists (old format) or a list of parameter sets
                    if (isinstance(self.qc_config[func_value]['parameters'], list) and 
                        len(self.qc_config[func_value]['parameters']) > 0 and 
                        isinstance(self.qc_config[func_value]['parameters'][0], list)):
                        # Old format: parameters is a list of [wspd_name, gust_name] lists
                        parameter_sets = self.qc_config[func_value]['parameters']
                    else:
                        # New format: parameters is a list of parameter sets
                        parameter_sets = self.qc_config[func_value]['parameters']
                    
                    for idx, parameter_set in enumerate(parameter_sets):
                        if not isinstance(parameter_set, (list, tuple)) or len(parameter_set) < 2:
                            print(f'[WARNING] Invalid parameter set at index {idx}: {parameter_set}. Skipping.')
                            continue
                            
                        wspd_name = parameter_set[0]
                        gust_name = parameter_set[1] if len(parameter_set) > 1 else None
                        
                        # Get the height, default to 10 if not specified
                        height_idx = min(idx, len(self.qc_config[func_value]['height']) - 1) if 'height' in self.qc_config[func_value] else 0
                        height = float(self.qc_config[func_value]['height'][height_idx]) if 'height' in self.qc_config[func_value] else 10.0
                        
                        print(f'[DEBUG] Processing parameter set {idx+1}: wspd_name={wspd_name}, gust_name={gust_name}, height={height}')
                        
                        try:
                            self.convert_wind(
                                wspd_name=wspd_name,
                                gust_name=gust_name,
                                height=height
                            )
                            print(f'[DEBUG] Successfully processed {wspd_name} and {gust_name}')
                        except Exception as e:
                            print(f'[ERROR] Error in convert_wind: {str(e)}')
                            import traceback
                            traceback.print_exc()
                    print(f'[DEBUG] Completed {func_value} check')
                elif func_value == 'best_sensor':
                    print('-------------')
                    print(f'Check {func_value}')
                    self.best_sensor(parameters1=self.qc_config[func_value]['parameters'][0],
                                    parameters2=self.qc_config[func_value]['parameters'][1])
                elif func_value == 't_continuity':
                    print('-------------')
                    print(f'Check {func_value}')
                    for idx, parameter in enumerate(self.qc_config[func_value]['parameters']):
                        print(f'parameter: {parameter}')
                        self.t_continuity(parameter=parameter,
                                        sigma=self.qc_config[func_value]['sigma'][idx],
                                        continuity_limit=self.qc_config[func_value]['limits'])
                    try:
                        front_excepts = self.qc_config[func_value]['exceptions']
                        if front_excepts:
                            print('-------------')
                            for front_except in front_excepts:
                                if front_except['test'] == 1:
                                    print(f'Check {func_value}: exception 1')
                                    self.front_except1(wdir_name=front_except['parameters'][0], atmp_name=front_except['parameters'][0])
                                elif front_except['test'] == 3:
                                    print(f'Check {func_value}: exception 3')
                                    self.front_except3(wspd_name=front_except['parameters'][0], atmp_name=front_except['parameters'][0])
                                elif front_except['test'] == 4:
                                    print(f'Check {func_value}: exception 4')
                                    self.front_except4(pres_name=front_except['parameters'][0], wspd_name=front_except['parameters'][0])
                                elif front_except['test'] == 5:
                                    print(f'Check {func_value}: exception 5')
                                    self.front_except5(pres_name=front_except['parameters'])
                                elif front_except['test'] == 6:
                                    print(f'Check {func_value}: exception 6')
                                    self.front_except6(wspd_name=front_except['parameters'][0], swvht_name=front_except['parameters'][0])
                    except:
                        continue
                elif func_value == 'true_north':
                    print('-------------')
                    print(f'Check {func_value}')
                    for idx, parameter in enumerate(self.qc_config[func_value]['parameters']):
                        print(f'parameter: {parameter}')
                        self.true_north(parameter=parameter,
                                        annual_variation=self.qc_config[func_value]['annual_variation'],
                                        year_reference=self.qc_config[func_value]['year_reference'],
                                        mag_deg=self.qc_config[func_value]['mag_deg'])
