# Flight Prices Data Analysis: Least Squares Fitting

This repository contains a simple analysis of one-way flight prices, retrieved from Expedia between 2022-04-16 and 2022-10-05. The dataset includes the following columns:

- **flightTimeInHours**: Flight duration in hours.
- **baseFare**: Base price of the flight (before taxes/fees).
- **totalFare**: Total price of the flight (including taxes/fees).

The sample used for this analysis was taken from the [original dataset](https://github.com/dilwong/FlightPrices).

## Objective

The analysis applies **least squares fitting** to explore the relationships between flight time and flight fare.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries: `pandas`, `numpy`, `matplotlib`

See requirements.txt for details.

Explore this project in Binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/skoudmani/flight-prices-least-squares.git/HEAD)
