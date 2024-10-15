import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from typing import Optional

def plot_flights_scatter_data(flights_df: pd.DataFrame, axis: Optional[plt.Axes] = None) -> plt.Axes:
    """
    Plot a scatter chart of flight duration versus price.

    Parameters:
    - flights_df: pd.DataFrame
        DataFrame containing flight data. Must have 'flightTimeInHours' and 'totalFare' columns.
    - axis: matplotlib.axes.Axes, optional
        An optional axis object to plot on. If None, a new figure and axis will be created.

    Returns:
    - axis: matplotlib.axes.Axes
        The axis with the scatter plot.
    """
    # Extract the relevant columns
    flight_duration = flights_df["flightTimeInHours"]
    flight_price = flights_df["totalFare"]

    # If no axis is provided, create a new figure and axis
    if axis is None:
        fig, axis = plt.subplots(figsize=(10, 6))

    # Create a scatter plot of the data
    scatter = axis.scatter(
        flight_duration, 
        flight_price, 
        color='royalblue', 
        s=100, 
        label="Flight data", 
        edgecolor='black'
    )

    # Customise the labels and title
    axis.set_xlabel("Flight Time [Hours]", fontsize=18)
    axis.set_ylabel("Flight Price [£]", fontsize=18)
    axis.tick_params(labelsize=16)

    # Customise the axis limits and layout
    axis.set_ylim(0, 365)
    axis.set_xlim(0, 12.5)

    # Optionally return the axis for further customisation
    return axis

def plot_best_fit_line(flights_df: pd.DataFrame, axis: plt.Axes, slope: float = 20, intercept: float = 50, 
                       error_check: bool = False, show_error_on_plot: bool = False) -> float:
    """
    Adds a best-fit line to the scatter plot and optionally computes the sum of squared vertical distances.

    Parameters:
    - flights_df: pd.DataFrame
        DataFrame containing flight data. Must have 'flightTimeInHours' and 'totalFare' columns.
    - axis: matplotlib.axes.Axes
        The axis object to plot on (must already contain the scatter plot).
    - slope: float, default=20
        The slope of the best-fit line.
    - intercept: float, default=50
        The intercept of the best-fit line.
    - error_check: bool, default=False
        Whether to calculate and plot the vertical offsets between points and the best-fit line.
    - show_error_on_plot: bool, default=False
        Whether to display the sum of squared errors on the plot itself.

    Returns:
    - total_squared_error: float
        The sum of squared vertical distances between the points and the best-fit line.
    """
    # Define the x-values for the best-fit line based on the axis limits
    x_values = np.array([0, 12.5])
    best_fit_line = slope * x_values + intercept

    # Plot the best-fit line on the given axis
    axis.plot(x_values, best_fit_line, color='coral', linewidth=3, label="Best fit line")

    # Initialise the sum of squared errors
    total_squared_error = 0

    if error_check:
        # Loop through each data point to calculate and plot vertical offsets
        for x, y in zip(flights_df["flightTimeInHours"], flights_df["totalFare"]):
            # Calculate the y-value of the best-fit line at the given x
            y_on_best_fit = slope * x + intercept
            total_squared_error += (y_on_best_fit - y) ** 2
            
            # Plot a grey dashed vertical line showing the offset
            axis.vlines(x, ymin=y, ymax=y_on_best_fit, colors='grey', linestyles='dashed', linewidth=1.5)

    # Optionally display the sum of squared errors on the plot
    if show_error_on_plot:
        axis.text(0.05, 0.95, f"Sum of squared errors: {total_squared_error:.2f}", 
                  transform=axis.transAxes, fontsize=14, verticalalignment='top', color='black')

    return total_squared_error

def plot_least_squares_fit(flights_df: pd.DataFrame, axis: plt.Axes, show_equation: bool = True) -> plt.Axes:
    """
    Calculates and plots the line of best fit using the least squares method, and prints the line equation on the plot.

    Parameters:
    - flights_df: pd.DataFrame
        DataFrame containing flight data. Must have 'flightTimeInHours' and 'totalFare' columns.
    - axis: matplotlib.axes.Axes
        The axis object to plot on (must already contain the scatter plot).
    - show_equation: bool, default=True
        Whether to display the line equation on the plot.

    Returns:
    - axis: matplotlib.axes.Axes
        The axis with the scatter plot and the best-fit line.
    """
    # Extract the relevant columns
    flight_duration = flights_df["flightTimeInHours"]
    flight_price = flights_df["totalFare"]

    # Perform the least squares fit (linear fit, degree 1 polynomial)
    slope, intercept = np.polyfit(flight_duration, flight_price, 1)

    # Define the x-values for plotting the best-fit line
    x_values = np.array([0, 12.5])
    best_fit_line = slope * x_values + intercept

    # Plot the best-fit line
    axis.plot(x_values, best_fit_line, color='coral', linewidth=3, label="Least Squares Fit")

    # Optionally display the equation of the line on the plot
    if show_equation:
        equation_text = f"y = {slope:.2f}x + {intercept:.2f}"
        axis.text(0.05, 0.9, equation_text, transform=axis.transAxes, fontsize=14, color='black')

    return axis