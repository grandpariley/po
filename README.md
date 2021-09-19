# Generic multi-objective optimization representation and example implementation for portfolio optimization

Written in Python 3.8

The purpose of this project is a clear, readable representation of multi-objective optimization problems for solving with Python.
Currently this is not available for use through `pip`, but that is a future state I would like to get to.
Included in this library is also an implementation for each of the following algorithms:
 
 - Branch and Bound
 - NSGA-2
 <!-- - Flower Pollination -->
 <!-- - Particle Swarm optimization -->
 <!-- - SPEA-II -->
 <!-- - MoBOA -->
 
More algorithm implementations forthcoming. 

In order to run this code, there are two environment variables that need to be set (I do it from a `.env` file in the root directory)
 - `LOG_LEVEL=debug | none`: this sets the granularity of the logging. Currently there is only `debug` and `none`, but more options can be added as the need arises.
 - `EXTERNAL_API=true | false`: this sets whether any client calls are made by the portfolio optimization implementation. 