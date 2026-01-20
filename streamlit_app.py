import streamlit as st
import pandas as pd
import os
import time
import random

# 1. PAGE SETUP
st.set_page_config(page_title="AI Logistics Agent", page_icon="🚛", layout="wide")

if "logistics_df" not in st.session_state:
    st.session_state.logistics_df = None

# 2. THE LOGISTICS ENGINE
def run_logistics_optimization(routes):
    """
    Simulates AI route optimization and shipment tracking.
    """
    shipment_data = []
    for route in routes:
        st.write(f"⚙️ Optimizing logistics for: **{route}**...")
        time.sleep(1.2) # Simulate AI heavy lifting
        
        # Generate smart logistics data
        for i in range(3):
            shipment_data.append({
                "Shipment ID": f"LOG-{random.randint(1000, 9999)}",
                "Route": route,
                "Priority": random.choice(["Critical", "Standard", "Express"]),
                "Estimated Cost": f"${random.randint(200, 1500)}",
                "AI Optimization": "Optimal Path Found",
                "Delivery Window": "24-48 Hours"
            })
    
    if shipment_data:
        df = pd.DataFrame(shipment_data)
        df.to_csv("optimized_logistics.csv", index=False)
        return True
    return False

# 3. INTERFACE
st.title("🚛 AI Logistics & Supply Chain Agent")
st.markdown("### Smart Route Optimization & Shipment Intelligence")
st.divider()

with st.sidebar:
    st.header("Shipment Parameters")
    target_routes = st.multiselect(
        "Select Active Routes:",
        ["New York -> London", "Shenzhen -> Los Angeles", "Dubai -> Berlin", "Mumbai -> Singapore"],
        default=["Shenzhen -> Los Angeles"]
    )
    st.info("Agent analyzes weather, fuel costs, and carrier availability.")

# 4. EXECUTION
if st.button("🚀 Optimize Supply Chain"):
    with st.status("🛠️ Agent analyzing global logistics data...", expanded=True) as status:
        if run_logistics_optimization(target_routes):
            st.session_state.logistics_df = pd.read_csv("optimized_logistics.csv")
            status.update(label="✨ Optimization Complete!", state="complete", expanded=False)
        else:
            st.error("⚠️ Logistics analysis failed. Check parameters.")

# 5. RESULTS DISPLAY
if st.session_state.logistics_df is not None:
    st.subheader("📊 Optimized Shipment Schedule")
    st.dataframe(st.session_state.logistics_df, use_container_width=True)
    
    csv_data = st.session_state.logistics_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Export Shipment Manifest (CSV)",
        data=csv_data,
        file_name='optimized_logistics_report.csv',
        mime='text/csv',
        type="primary"
    )
