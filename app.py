import streamlit as st

st.set_page_config(page_title="Пошук ІПН", layout="wide")

st.title("Співставлення ІПН та сум")

col1, col2, col3 = st.columns(3)

with col1:
    ipn_input = st.text_area("1. ІПН (з дужками)", height=300, placeholder="[5010031470]\n[7610052644]")

with col2:
    sum_input = st.text_area("2. Сума", height=300, placeholder="100.50\n200.00")

with col3:
    search_input = st.text_area("3. ІПН ПОШУКУ", height=300, placeholder="7610052644\n5010031470")

if st.button("Шукати", type="primary"):
    if ipn_input and sum_input and search_input:
        ipn_list = [line.strip() for line in ipn_input.split('\n') if line.strip()]
        sum_list = [line.strip() for line in sum_input.split('\n') if line.strip()]
        search_list = [line.strip() for line in search_input.split('\n') if line.strip()]
        
        # Видаляємо дужки
        cleaned_ipn_list = [ipn.replace('[', '').replace(']', '') for ipn in ipn_list]
        cleaned_search_list = [search.replace('[', '').replace(']', '') for search in search_list]
        
        # Створюємо словник для співставлення (ІПН -> Сума)
        min_len = min(len(cleaned_ipn_list), len(sum_list))
        data_dict = {cleaned_ipn_list[i]: sum_list[i] for i in range(min_len)}
        
        out_search = []
        out_ipn = []
        out_sum = []
        
        for search_val in cleaned_search_list:
            out_search.append(search_val)
            if search_val in data_dict:
                out_ipn.append(search_val)
                out_sum.append(data_dict[search_val])
            else:
                out_ipn.append("Не знайдено")
                out_sum.append("-")
                
        st.subheader("Результат")
        
        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.text_area("ІПН ПОШУКУ", value='\n'.join(out_search), height=300, key="res_search")
        with res_col2:
            st.text_area("Знайдений ІПН (з першої колонки)", value='\n'.join(out_ipn), height=300, key="res_ipn")
        with res_col3:
            st.text_area("Сума", value='\n'.join(out_sum), height=300, key="res_sum")
    else:
        st.warning("Будь ласка, заповніть всі три поля перед пошуком.")
