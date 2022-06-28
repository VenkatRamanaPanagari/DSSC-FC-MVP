# candlestick ibm
st.subheader('IBM Stock:-')

candlestick = plt.figure(figsize = (15,7))

last20_ibm = data[:20]

up = last20_ibm[last20_ibm.Close >= last20_ibm.Open]
  
down = last20_ibm[last20_ibm.Close < last20_ibm.Open]
  
col1 = 'green'

col2 = 'red'
  
width = .3
width2 = .03
  
plt.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color=col1)
plt.bar(up.index, up.High-up.Close, width2, bottom=up.Close, color=col1)
plt.bar(up.index, up.Low-up.Open, width2, bottom=up.Open, color=col1)
  
plt.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color=col2)
plt.bar(down.index, down.High-down.Open, width2, bottom=down.Open, color=col2)
plt.bar(down.index, down.Low-down.Close, width2, bottom=down.Close, color=col2)

plt.xticks(rotation=30, ha='right')
plt.title('IBM Stock')  

st.pyplot(candlestick)

# MSFT Stock candlestick
st.subheader('MSFT Stock:-')
candlestick1 = plt.figure(figsize = (15,7))

last20_msft = data1[:20]

up = last20_msft[last20_msft.Close >= last20_msft.Open]
  
down = last20_msft[last20_msft.Close < last20_msft.Open]
plt.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color=col1)
plt.bar(up.index, up.High-up.Close, width2, bottom=up.Close, color=col1)
plt.bar(up.index, up.Low-up.Open, width2, bottom=up.Open, color=col1)
  
plt.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color=col2)
plt.bar(down.index, down.High-down.Open, width2, bottom=down.Open, color=col2)
plt.bar(down.index, down.Low-down.Close, width2, bottom=down.Close, color=col2)

plt.xticks(rotation=30, ha='right')
plt.title('MSFT Stock') 

st.pyplot(candlestick1)

st.subheader('IBM vs MSFT')
fig = plt.figure(figsize = (15,7))
plt.plot(data['Open'], label = 'ibm')
plt.plot(data1['Open'], label = 'msft')
plt.title('Stock Prices of IBM, MSFT')
plt.legend()
st.pyplot(fig)

# market cap
st.subheader('Marketcap IBM vs MSFT')
marketcap = plt.figure(figsize = (15,7))

data = vz.marketcap(data)
data1 = vz.marketcap(data1)
data['MarktCap'].plot(label = 'IBM', figsize = (15,7))
data1['MarktCap'].plot(label = 'MSFT')
plt.ylabel('Billions $')
plt.title('Market Cap')
plt.legend()

st.pyplot(marketcap)