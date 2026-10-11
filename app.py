import streamlit as st
from chain import optimize

st.set_page_config(page_title="AI Prompt Optimizer", page_icon="✨")

st.title("✨ AI Prompt Optimizer")
st.caption("حوّل أي برومبت بسيط لبرومبت احترافي")

user_prompt = st.text_area("اكتب البرومبت البسيط:", placeholder="Write an advertisement.")

col1, col2 = st.columns(2)
with col1:
    domain = st.selectbox("المجال", ["General", "Marketing", "Coding", "Education", "Cybersecurity"])
with col2:
    language = st.selectbox("لغة المخرجات", ["English", "Arabic"])

if st.button("حسّن البرومبت 🚀"):
    if not user_prompt.strip():
        st.warning("اكتب برومبت الأول.")
    else:
        with st.spinner("جاري التحسين..."):
            try:
                result = optimize(user_prompt, domain, language)
            except Exception as e:
                st.error(f"حصل خطأ: {e}")
            else:
                st.subheader("✅ Improved Prompt")
                st.code(result.improved_prompt, language="markdown")

                st.subheader("🎭 Role")
                st.write(result.role)


                st.subheader("📚 Context")
                st.write(result.context)

                st.subheader("⛔ Constraints")
                for c in result.constraints:
                    st.markdown(f"- {c}")

                st.subheader("📦 Expected Output")
                st.write(result.expected_output)