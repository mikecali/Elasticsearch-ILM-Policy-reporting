import streamlit as st
import pandas as pd
import json

st.title("ILM Policies and Phases Dashboard")

flattened_data_file = st.file_uploader("Upload Flattened ILM Data JSON", type="json")

if flattened_data_file:
    flattened_data = json.load(flattened_data_file)
    df = pd.DataFrame(flattened_data)

    df = df[~df['index_name'].str.startswith('.partial-')]

    include_partial = st.checkbox("Include 'partial*' in 'in_use_by'", value=False)

    def filter_in_use_by(in_use_by, include_partial):
        if isinstance(in_use_by, str):
            indices = in_use_by.split(', ')
            if not include_partial:
                indices = [idx for idx in indices if not idx.startswith('partial')]
            return ', '.join(indices)
        return in_use_by

    df['in_use_by'] = df['in_use_by'].apply(filter_in_use_by, include_partial=include_partial)

    st.write("Flattened ILM Data (Filtered):")
    st.dataframe(df)

    st.subheader("Summary Dashboard")
    
    phase_filter = st.multiselect("Filter by Phase", df['phase'].unique(), default=df['phase'].unique())
    action_filter = st.multiselect("Filter by Action", df['action'].unique(), default=df['action'].unique())
    
    filtered_df = df[df['phase'].isin(phase_filter) & df['action'].isin(action_filter)]
    
    st.metric(label="Total Number of Policies", value=filtered_df['policy_name'].nunique())
    st.metric(label="Total Number of Indices", value=filtered_df['index_name'].nunique())
    
    phase_summary = filtered_df.groupby("phase").size().reset_index(name='Count')
    st.bar_chart(phase_summary.set_index("phase"), use_container_width=True)
    
    st.metric(label="Most Common Action", value=filtered_df['action'].mode().iloc[0] if not filtered_df['action'].empty else "N/A")
    
    st.subheader("Policy Details")
    policy_name = st.selectbox("Select Policy Name", filtered_df["policy_name"].unique())
    policy_filtered_df = filtered_df[filtered_df["policy_name"] == policy_name]
    
    if not policy_filtered_df.empty:
        st.write(f"Details for Policy: **{policy_name}**")
        st.write(policy_filtered_df[["version", "modified_date", "in_use_by"]].drop_duplicates().reset_index(drop=True))
        
        st.subheader(f"Phases and Actions for Policy: {policy_name}")
        phase_data = policy_filtered_df[["index_name", "phase", "action", "step", "snapshot_name"]]
        
        cols = st.columns(len(phase_data['phase'].unique()))

        for i, phase in enumerate(phase_data['phase'].unique()):
            with cols[i]:
                st.subheader(f"{phase.capitalize()} Phase")
                phase_specific_data = phase_data[phase_data['phase'] == phase]
                st.write(phase_specific_data[["index_name", "action", "step", "snapshot_name"]])
                st.write(f"Total indices in {phase} phase: {len(phase_specific_data)}")

        phase_summary = phase_data.groupby("phase").size().reset_index(name='Count')
        st.bar_chart(phase_summary.set_index("phase"))
    else:
        st.write("No data available for the selected policy.")
else:
    st.write("Please upload the flattened ILM data JSON file.")

