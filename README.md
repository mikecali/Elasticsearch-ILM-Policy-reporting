# Description
This is a collection of a simple python code that can be use to create a simple summary of the ILM Policy and display it web using streamlit. This app process diagnostic data from Elasticsearch Cluster (ECE or ESS) and generate a report, ILM Policies, Number of Indices, Policy Details and Phases and Actions for each policy.


# Disclaimer

IMPORTANT: This tool is provided as-is, without any warranties or guarantees. Neither the creator of this tool nor Elastic (the company behind Elasticsearch) can be held responsible for any issues, data loss, or damage that may occur from using this tool. Use it at your own risk and always ensure you have proper backups of your Elasticsearch data before running any diagnostic or visualization tools.

This tool is not officially supported by Elastic and is not a part of the official Elasticsearch product suite.

# Prerequisites

Python 3.7 or higher
Elasticsearch cluster diagnostic data (JSON format)
Required Python libraries: pandas, json, streamlit

# Installation

Clone this repository:

1. git clone https://github.com/mikecali/Elasticsearch-ILM-Policy-reporting.git

2. Navigate to the project directory:

3. cd Elasticsearch-ILM-Policy-reporting.git
Install the required Python libraries:

pip install pandas json streamlit

# Usage

Ensure you have Elasticsearch cluster diagnostic data in JSON format. The tool expects the following files:

nodes/nodes_stats.json
nodes/nodes_info.json
indices/indices_stats.json
Run the main script with the path to your diagnostics directory:

python main.py /path/to/your/diagnostics/directory
The script will generate an HTML file named elasticsearch_cluster_visualization.html in the same directory.

Open the generated HTML file in a web browser to view the interactive visualization.

# Features


# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments

This tool uses D3.js for visualization
Inspired by the Elasticsearch community and the need for better cluster diagnostics visualization
Remember: Always use this tool responsibly and ensure you have proper authorization to access and visualize your Elasticsearch cluster data.
