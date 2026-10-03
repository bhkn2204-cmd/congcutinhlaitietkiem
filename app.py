import streamlit as st

# Cấu hình trang Streamlit
st.set_page_config(
    page_title="Công cụ Tính Lãi Tiết Kiệm",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Công cụ Tính Lãi Gửi Tiết Kiệm của Kiều Nhi")
st.write("Nhập thông tin khoản tiền gửi của bạn để tính toán tiền lãi chi tiết.")

st.divider()

# Tạo khung nhập liệu cho người dùng
col1, col2 = st.columns(2)

with col1:
    so_tien_gui = st.number_input(
        "Số tiền gửi (VNĐ):",
        min_value=1_000_000,
        value=100_000_000,
        step=5_000_000,
        format="%d"
    )

    ki_han_thang = st.number_input(
        "Kỳ hạn gửi (tháng):",
        min_value=1,
        max_value=60,
        value=12,
        step=1
    )

with col2:
    lai_suat_nam = st.number_input(
        "Lãi suất (%/năm):",
        min_value=0.1,
        max_value=20.0,
        value=6.0,
        step=0.1,
        format="%.1f"
    )

    hinh_thuc_nhan = st.selectbox(
        "Hình thức nhận lãi:",
        ["Cuối kỳ", "Hàng tháng", "Hàng quý"]
    )

# Tính toán các chỉ số
tong_tien_lai = so_tien_gui * (lai_suat_nam / 100) * (ki_han_thang / 12)
tong_goc_va_lai = so_tien_gui + tong_tien_lai

# Hiển thị kết quả
st.divider()
st.subheader("📊 Kết quả tính toán")

# Định dạng hiển thị số dư
c1, c2 = st.columns(2)
c1.metric("Tổng tiền gốc", f"{so_tien_gui:,.0f} VNĐ")
c2.metric("Tổng tiền lãi nhận được", f"{tong_tien_lai:,.0f} VNĐ")

st.metric("Tổng tiền gốc + lãi", f"{tong_goc_va_lai:,.0f} VNĐ")

st.divider()
st.subheader("🗓️ Chi tiết tiền lãi định kỳ")

if hinh_thuc_nhan == "Cuối kỳ":
    st.info(f"Bạn sẽ nhận **{tong_tien_lai:,.0f} VNĐ** tiền lãi vào cuối kỳ hạn ({ki_han_thang} tháng).")

elif hinh_thuc_nhan == "Hàng tháng":
    lai_hang_thang = tong_tien_lai / ki_han_thang
    st.success(f"Số tiền lãi nhận **mỗi tháng**: **{lai_hang_thang:,.0f} VNĐ** (trong {ki_han_thang} tháng).")

elif hinh_thuc_nhan == "Hàng quý":
    so_quy = ki_han_thang / 3
    if ki_han_thang < 3:
        st.warning("⚠️️ Kỳ hạn dưới 3 tháng không áp dụng hình thức nhận lãi theo quý.")
    else:
        lai_hang_quy = tong_tien_lai / so_quy
        st.success(f"Số tiền lãi nhận **mỗi quý (3 tháng)**: **{lai_hang_quy:,.0f} VNĐ** (tổng cộng {so_quy:.1f} quý).")
