<!--
Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# DevLake Jupyter Playground

[DevLake](https://devlake.apache.org/) offers an abundance of data for exploration.
This playground contains a basic set-up to interact with the data using [Jupyter Notebooks](https://jupyter.org/) and [Pandas](https://pandas.pydata.org/).


# How to play

## Prerequisites
- [Python >= 3.12](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- Access to a DevLake database
- Optional: An IDE or plugin that supports running Jupyter Notebooks directly (e.g. [Visual Studio Code](https://code.visualstudio.com/))


## Usage
1. Have a local clone of this repository.
2. Run `poetry install` in the root directory.
3. Either:
    - navigate to the `notebooks` directory and run the jupyter server `poetry run jupyter notebook` 
    - navigate to one of the notebook files (`.ipynb`) in the `notebooks` directory from your IDE directly
4. Make sure the notebook uses the virtual environment created by poetry.
5. Configure your database URL in the notebook code.
6. Run the notebook.
7. Start exploring the data in your own notebooks!


## Create your own Jupyter Notebook

A good starting point for creating a new notebook is `template.ipynb`.
It contains the basic steps you need to go from query to output.

To define a query, use the [Domain Layer Schema](https://devlake.apache.org/docs/DataModels/DevLakeDomainLayerSchema#schema-diagram) to get an overview of the available tables and fields.

Use [Pandas](https://pandas.pydata.org/) api to organize, transform, and analyze the query results.


## Predefined notebooks and utilities

A notebook might offer a valuable perspective on the data not available within the capabilities of a Grafana dashboard.
In this case, it's worthwhile to contribute this notebook to the community as a predefined notebook, e.g., `process_analysis.ipynb` (it depends on [graphviz](https://graphviz.org/) for its visualization).

The same goes for utility methods with, for example, predefined Pandas data transformations offering an interesting view on the data.


## Contributing

Please check the [contributing guidelines](https://github.com/apache/incubator-devlake/blob/main/README.md#-how-to-contribute).
