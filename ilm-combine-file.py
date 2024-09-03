import streamlit as st
import json

st.title("Flatten ILM Policies and ILM Explain Data")

ilm_policies_file = st.file_uploader("Upload ILM Policies JSON", type="json")
ilm_explain_file = st.file_uploader("Upload ILM Explain JSON", type="json")

if ilm_policies_file and ilm_explain_file:
    ilm_policies = json.load(ilm_policies_file)
    ilm_explain = json.load(ilm_explain_file)

    flattened_data = []

    for policy_name, policy_details in ilm_policies.items():
        policy = {
            "policy_name": policy_name,
            "version": policy_details.get("version"),
            "modified_date": policy_details.get("modified_date"),
            "in_use_by": ", ".join(policy_details.get("in_use_by", {}).get("indices", [])),
            "phases": json.dumps(policy_details.get("policy", {}).get("phases", {})),
            "meta": json.dumps(policy_details.get("_meta", {})),
        }

        for index_name, index_details in ilm_explain.get("indices", {}).items():
            if index_details.get("policy") == policy_name:
                index_data = {
                    "index_name": index_name,
                    "index_creation_date": index_details.get("index_creation_date"),
                    "phase": index_details.get("phase"),
                    "action": index_details.get("action"),
                    "step": index_details.get("step"),
                    "snapshot_name": index_details.get("phase_execution", {}).get("snapshot_name"),
                }
                flattened_data.append({**policy, **index_data})

    if flattened_data:
        st.write("Flattened ILM Policies and ILM Explain Data:", flattened_data)
        st.download_button("Download Flattened Data as JSON", data=json.dumps(flattened_data, indent=4),
                           file_name="flattened_ilm_data.json", mime="application/json")
    else:
        st.write("No matching ILM policies and indices found.")
else:
    st.write("Please upload both ILM Policies and ILM Explain JSON files.")

