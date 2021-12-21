import streamlit as st
import datetime

header = st.container()
caption = st.container()
coderd, kontonr1 = st.columns(2)
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, col8, col9 = st.columns(3)

generatedFile =st.container()


with header:
	st.title('MT940 Generator')


with caption:
    st.caption('by Fabio Fantoli')
    

with coderd:
    option =st.selectbox(
    'Einzahlung (C) oder Auszahlung (D)?',
    ('C','D'))
    

with kontonr1:
    konto1option =st.selectbox(
    'IBAN',
    ('DE35664900000022805304','DE95170550503162975459'))
    


with col1:
    today1 = datetime.date.today()
    VDatum=st.date_input('Datum Valuta', today1)
    yearVv = VDatum.strftime("%Y")
    yearV =yearVv[2:]
    monthV = VDatum.strftime("%m")
    dayV =VDatum.strftime("%d")


with col2:
    today = datetime.date.today()
    BDatum=st.date_input('Datum Buchung', today)
    yearBb = BDatum.strftime("%Y")
    yearB =yearBb[2:]
    monthB = BDatum.strftime("%m")
    dayB =BDatum.strftime("%d")
    
    
with col3:
    Betrag = st.text_input('Betrag in Euro','100,00')


with col4:
    referenz= st.text_input('Referenz (21)', ' ')
    
with col5:
    vwz1 = st.text_input('VWZ 1 (22) Mandatsref.', ' ')

with col6:
        vwz2 = st.text_input('VWZ 2 (23)', ' ')
    
with col7:
    kontoinhaber = st.text_input('Kontoinhaber', 'John J. Rambo')

with col8:
    bic = st.text_input('BIC','BELADEBE')

with col9:
    konto2option = st.text_input('IBAN','DE02100500000054540402')


with generatedFile:
    st.write(":20:DEUTDEMMXXX")
    st.write(":25:"+konto1option)
    st.write(":28C:00001/1")
    st.write(":60F:C190501EUR0,00")
    st.write(":61:"+yearV+monthV+dayV+monthB+dayB+option+Betrag+"N051NONREF//2108325339736237")
    st.write("86:166?GUTSCHRIFT?100004770?20"+kontoinhaber+'?21EREF+'+referenz+'?22SVWZ+'+vwz1+'?23'+vwz2+'?24?30'+bic+'?31'+konto2option+'?32'+kontoinhaber+'?35')
    st.write(':62F:C180716EUR0')



