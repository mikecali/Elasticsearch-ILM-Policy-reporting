# Description
This is a collection of a simple python code that can be use to create a simple summary of the ILM Policy and display it web using streamlit. This app process diagnostic data from Elasticsearch Cluster (ECE or ESS) and generate a report, ILM Policies, Number of Indices, Policy Details and Phases and Actions for each policy.

![Screenshot 2024-09-03 at 1 10 19 PM](https://github.com/user-attachments/assets/13d3f4c7-a37b-4916-a8d4-41822368b72a)
![Screenshot 2024-09-03 at 1 10 36 PM](https://github.com/user-attachments/assets/fdfd4cef-2656-438a-9664-450246ec3d98)
![Screenshot 2024-09-03 at 1 10 59 PM](https://github.com/user-attachments/assets/ec843dec-7b88-4313-935f-a6ff44baae0d)

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

4. Install the required Python libraries:

    ```pip install pandas json streamlit```

# Usage

Ensure you have Elasticsearch cluster diagnostic data in JSON format. 

The tool expects the following files:

ilm_policies.json
ilm_explain.json

There are two scripts in this repository, first we need to upload those 2 files above to flatten the json files.

1. Run the first application:

     ``` streamlit run ilm-combine-file.py ```

2. Upload the 2 files: ilm_policies.json and ilm_explain.json.

3. Donwload the flattend file.

4. Run the second application:
    
     ``` streamlit run ilm-report.py ```

4. Upload the donwloaded file: flattened_ilm_data-2.json

5. Review the report

# Contribution

Contributions to improve this tool are welcome. Please fork the repository and submit a pull request with your changes.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments

This tool uses D3.js for visualization
Inspired by the Elasticsearch community and the need for better cluster diagnostics visualization
Remember: Always use this tool responsibly and ensure you have proper authorization to access and visualize your Elasticsearch cluster data.
