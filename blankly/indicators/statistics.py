"""
    Statistics functions
    Copyright (C) 2021 Brandon Fan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from typing import Any

import pandas as pd
import tulipy as ti
import btalib

from blankly.indicators.utils import check_series, convert_to_numpy


def stddev_period(data, period=14, use_series=False) -> Any:
    if check_series(data):
        use_series = True
    data = convert_to_numpy(data)
    stddev = ti.stddev(data, period)
    return pd.Series(stddev) if use_series else stddev


def var_period(data, period=14, use_series=False) -> Any:
    if check_series(data):
        use_series = True
    data = convert_to_numpy(data)
    var = ti.var(data, period)
    return pd.Series(var) if use_series else var


def stderr_period(data, period=14, use_series=False) -> Any:
    if check_series(data):
        use_series = True
    data = convert_to_numpy(data)
    stderr = ti.stderr(data, period)
    return pd.Series(stderr) if use_series else stderr


def min_period(data, period = 30, use_series=False) -> Any:
    if check_series(data):
        use_series = True
    data = convert_to_numpy(data)
    minimum = ti.min(data, period)
    return pd.Series(minimum) if use_series else minimum


def max_period(data, period, use_series=False) -> Any:
    if check_series(data):
        use_series = True
    data = convert_to_numpy(data)
    maximum = ti.max(data, period)
    return pd.Series(maximum) if use_series else maximum


def sum_period(data, period, use_series=False) -> Any:
    if check_series(data):
        use_series = True
    data = convert_to_numpy(data)
    maximum = ti.sum(data, period)
    return pd.Series(maximum) if use_series else maximum

def avg_price(open_data, high_data, low_data, close_data, use_series=False) -> Any:
    if check_series(open_data):
        use_series = True
    open_data = convert_to_numpy(open_data)
    high_data = convert_to_numpy(high_data)
    low_data = convert_to_numpy(low_data)
    close_data = convert_to_numpy(close_data)
    avg_price = ti.avgprice(open_data, high_data, low_data, close_data, period)
    return pd.Series(avg_price) if use_series else avg_price

def med_price(high_data, low_data):
    high_data = convert_to_numpy(high_data)
    low_data = convert_to_numpy(low_data)
    med_price = ti.medprice(high_data, low_data)
    return pd.Series(med_price)

def midpoint(close_data):
    midpoint = btalib.midpoint(close_data)
    midpoint_values = midpoint.df['midpoint'].values[-1]
    return midpoint_values

def midprice(high_data, low_data):
    midprice = btalib.midprice(high_data, low_data)
    midprice_values = midprice.df['midprice'].values[-1]
    return midprice_values

def typprice(high_data, low_data, close_data):
    typprice = btalib.typprice(high_data, low_data, close_data)
    typprice_values = typprice.df['tp'].values[-1]
    return typprice_values

def wclprice(high_data, low_data, close_data) -> Any:
    if check_series(high_data) or check_series(low_data) or check_series(close_data):
        use_series = True
    high_data = convert_to_numpy(high_data)
    low_data = convert_to_numpy(low_data)
    close_data = convert_to_numpy(close_data)
    wclprice = ti.wcprice(high_data, low_data, close_data)
    return pd.Series(wclprice) if use_series else wclprice

def beta(high_data, low_data, close_data, use_series=False) -> Any:
    if check_series(high_data) or check_series(low_data) or check_series(close_data):
        use_series = True
    beta = btalib.beta(close_data)
    beta_values = beta.df['beta'].values[-1]
    return beta_values

def correl(high_data, low_data) -> Any:
    correl = btalib.correl(high_data, low_data)
    correl_values = correl.df['correl'].values[-1]
    return correl_values

def tsf(close_data, period=14, use_series=False) -> Any:
    if check_series(close_data):
        use_series = True
    close_data = convert_to_numpy(close_data)
    tsf = ti.tsf(close_data, period)
    return pd.Series(tsf) if use_series else tsf
