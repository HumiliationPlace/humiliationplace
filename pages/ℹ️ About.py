import streamlit as st
import os

st.set_page_config(
    page_title="About",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("About")

st.write("**Version 0.0.1 ALPHA**")

try:
    if st.query_params["remove_post"] == "1":
        st.divider()

        file_path = f'content/posts/users/{st.query_params["access_token"]}/{st.query_params["post_id"]}'

        try:
            os.remove(file_path)
            print(f"{file_path} has been deleted.")

            st.success("Your post has been deleted. It may take a few minutes to reflect on the site.")
        except FileNotFoundError:
            print(f"{file_path} does not exist.")

        if os.path.exists(f'{file_path}.jpg'):
            os.rename(f'{file_path}.jpg', f'{file_path}_REMOVED.jpg')
            print(f'File renamed to {file_path}_REMOVED.jpg')
        else:
            print("File does not exist.")
except KeyError:
    pass
    
st.divider()

st.write("This website is operated by a single developer, and is in the early stages of development. Please be patient as I work to improve it.")

st.markdown("This website may require payment for those who choose to upload content to the site. All fees are non-refundable and paid by USDC via Coinbase. If you don't have a Coinbase wallet, [create one here](https://help.coinbase.com/en-gb/wallet/getting-started/create-a-coinbase-wallet).")

st.write("*Note that Humiliation Place does not regulate content as we are not required to by law. Thus, the site is not responsible and cannot be held responsible or liable for any illegal or unethical content uploaded to the service. However, we will make reasonable effort to remove any content that breaches our terms of service (see the Waiver).*")

st.write("**We hope you enjoy our product!!**")

st.divider()

st.markdown("If you would like to support the service's development, you can donate [here](https://commerce.coinbase.com/checkout/823f9f4c-6ec1-41c8-8b04-1df44aa21d9f) or to one of the crypto wallets below:")
st.code("BTC (Bitcoin): bc1qf9lej2jrpamx94fav0afqs3q8ledcxd498vl5z")
st.code("USDC (Ethereum): 0x9CC6ee2d10aE928b5e4c800124D2833e13E32BBd")
st.code("USDC (Polygon): 0x9CC6ee2d10aE928b5e4c800124D2833e13E32BBd")
st.code("ETH (Ethereum): 0x9CC6ee2d10aE928b5e4c800124D2833e13E32BBd")
