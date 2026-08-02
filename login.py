import streamlit as st

st.set_page_config(
    page_title="AI Auto Spare Parts PLM",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 AI Auto Spare Parts Lifecycle Management System")

st.markdown("### Login Portal")

# -------------------- USERS --------------------

users = {

    "admin": {
        "password": "admin123",
        "role": "System Administrator"
    },

    "praveen": {
        "password": "24ME0074",
        "role": "Project Admin"
    },

    "praveenraj": {
        "password": "24ME0073",
        "role": "Project Manager"
    },

    "manufacturing": {
        "password": "manufacturing123",
        "role": "Manufacturing Engineer"
    },

    "inventory": {
        "password": "inventory123",
        "role": "Inventory Manager"
    },

    "supplier": {
        "password": "supplier123",
        "role": "Supplier Manager"
    },

    "service": {
        "password": "service123",
        "role": "Service Engineer"
    },

    "analyst": {
        "password": "analyst123",
        "role": "AI Analyst"
    },

    "dr.suresh": {
        "password": "guide123",
        "role": "Project Guide"
    }

}

# -------------------- LOGIN --------------------

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if username in users:

        if password == users[username]["password"]:

            st.success("✅ Login Successful")

            st.balloons()

            st.write("## Welcome,", username)

            st.info("Role : " + users[username]["role"])

            st.markdown("---")

            st.subheader("Access Permission")

            role = users[username]["role"]

            if role == "System Administrator":

                st.success("✔ Full System Access")

            elif role == "Project Admin":

                st.success("✔ Full Project Access")

            elif role == "Project Manager":

                st.success("✔ Dashboard")
                st.success("✔ Reports")
                st.success("✔ Analytics")

            elif role == "Manufacturing Engineer":

                st.success("✔ Manufacturing")
                st.success("✔ Inventory")

            elif role == "Inventory Manager":

                st.success("✔ Spare Parts")
                st.success("✔ Inventory")

            elif role == "Supplier Manager":

                st.success("✔ Suppliers")

            elif role == "Service Engineer":

                st.success("✔ Service History")

            elif role == "AI Analyst":

                st.success("✔ AI Prediction")
                st.success("✔ Analytics")
                st.success("✔ Reports")

            elif role == "Project Guide":

                st.success("✔ View Dashboard")
                st.success("✔ View Spare Parts")
                st.success("✔ View Manufacturing")
                st.success("✔ View Inventory")
                st.success("✔ View Suppliers")
                st.success("✔ View Service History")
                st.success("✔ View AI Prediction")
                st.success("✔ View Analytics")
                st.success("✔ View Reports")

        else:

            st.error("❌ Incorrect Password")

    else:

        st.error("❌ Username Not Found")

st.markdown("---")

st.caption("AI Auto Spare Parts Lifecycle Management System")