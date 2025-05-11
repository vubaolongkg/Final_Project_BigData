import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 Phân tích log NASA - Dashboard")

# --- Tải dữ liệu ---
@st.cache_data
def load_data(max_rows):
    df = pd.read_csv("output.csv")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    if max_rows > 0 and len(df) > max_rows:
        df = df.sample(max_rows, random_state=42)
    return df

with st.sidebar:
    st.header("⚙️ Tuỳ chọn lọc")
    max_rows = st.slider("🔢 Số dòng tối đa (0 = tất cả)", 0, 500_000, 100_000, step=10_000)

df = load_data(max_rows)

# --- Bộ lọc thời gian ---
start_date = st.date_input("Từ ngày", df['timestamp'].min().date())
end_date = st.date_input("Đến ngày", df['timestamp'].max().date())
filtered_df = df[(df['timestamp'].dt.date >= start_date) & (df['timestamp'].dt.date <= end_date)]

# --- Bảng hiển thị dữ liệu lọc được ---
st.subheader("📋 Dữ liệu sau khi lọc (hiển thị tối đa 1000 dòng)")
with st.expander("Xem bảng dữ liệu chi tiết", expanded=True):
    st.dataframe(
        filtered_df.head(1000), 
        use_container_width=True, 
        height=300
    )


st.markdown("---")

# --- Biểu đồ lượt truy cập theo giờ ---
st.subheader("1️⃣ Lượt truy cập theo giờ")
fig1, ax1 = plt.subplots()
sns.countplot(x=filtered_df['timestamp'].dt.hour, ax=ax1, palette='Blues')
ax1.set_xlabel("Giờ trong ngày")
ax1.set_ylabel("Số lượt truy cập")
st.pyplot(fig1)

# --- Biểu đồ top 10 host ---
st.subheader("2️⃣ Top 10 Host truy cập")
top_hosts = filtered_df['host'].value_counts().head(10)
top_hosts_df = pd.DataFrame({'Host': top_hosts.index, 'Lượt truy cập': top_hosts.values})
st.bar_chart(top_hosts_df.set_index('Host'))

# --- Biểu đồ tròn mã phản hồi HTTP ---
st.subheader("3️⃣ Tỷ lệ mã phản hồi HTTP")
response_counts = filtered_df['responsecode'].value_counts()
total = response_counts.sum()
threshold = 0.03
grouped = response_counts[response_counts / total >= threshold]
others = response_counts[response_counts / total < threshold].sum()
if others > 0:
    grouped['Khác'] = others
labels = grouped.index.astype(str)
sizes = grouped.values

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return f'{pct:.1f}%\n({val})'
    return my_autopct

fig2, ax2 = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax2.pie(
    sizes,
    labels=labels,
    autopct=make_autopct(sizes),
    startangle=140,
    colors=plt.cm.Pastel2.colors,
    labeldistance=1.1,
    pctdistance=0.75
)
for text in texts:
    text.set_size(10)
for autotext in autotexts:
    autotext.set_size(9)
ax2.axis('equal')
st.pyplot(fig2)

# --- Biểu đồ top 10 resource ---
st.subheader("4️⃣ Top 10 tài nguyên được truy cập nhiều nhất")
top_resources = filtered_df['resource'].value_counts().head(10)
fig3, ax3 = plt.subplots(figsize=(10, 6))
top_resources.plot(kind='barh', color='teal', ax=ax3)
ax3.set_title("Top 10 tài nguyên được truy cập nhiều nhất")
ax3.set_xlabel("Số lượt truy cập")
ax3.invert_yaxis()
st.pyplot(fig3)

# --- Biểu đồ tổng bytes truyền mỗi ngày ---
st.subheader("5️⃣ Tổng số bytes được truyền mỗi ngày")
bytes_per_day = filtered_df.groupby(filtered_df['timestamp'].dt.date)['bytes'].sum()
fig4, ax4 = plt.subplots(figsize=(12, 6))
bytes_per_day.plot(kind='line', color='green', ax=ax4)
ax4.set_title("Tổng số bytes truyền mỗi ngày")
ax4.set_xlabel("Ngày")
ax4.set_ylabel("Bytes")
ax4.grid(True)
st.pyplot(fig4)
