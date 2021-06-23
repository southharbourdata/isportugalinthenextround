import streamlit as st 
import streamlit.components.v1 as stc 

import base64

from result_scrapper import get_live_score,arewewinning


SIII = "images/ronaldohattrickjpg.jpg"
NOOO = "images/sad-portuguese-soccer-fan-with-the-portuguese-CR8RCK.jpg"
MEH = "images/Ronaldo_fixe.jpg"


def main():
	st.title('Portugal está na próxima ronda?')
	st.subheader(' Não é preciso sacar da calculadora - vê aqui em tempo real')
	try: 
		df_test=get_live_score()
		df_test['home_score'] = df_test['home_score'].astype(int)
		df_test['away_score'] = df_test['away_score'].astype(int)
		passing=arewewinning(df_test)
		if passing:
			st.image(SIII,use_column_width = 'auto')
			st.success("'TAMOS LÁ - NUNCA DUVIDEI")
		else:
			st.image(NOOO,use_column_width = 'auto')
			st.error('EU JÁ SABIA - NUNCA ACREDITEI')
	except:
		st.image(MEH,use_column_width = 'auto')
		st.warning('AINDA NÃO COMEÇOU O JOGO... - MAS CONFIA PUTO')
	
##########
# Footer #                         #  https://discuss.streamlit.io/t/st-footer/6447
##########

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>with ❤ by <a style='display: block; text-align: center;' href="https://github.com/southharbourdata/isportugalinthenextround" target="_blank">South Harbour Data</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

#############
# Hide Menu #                         #  https://discuss.streamlit.io/t/how-do-i-hide-remove-the-menu-in-production/362/10
#############

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

if __name__ == '__main__':
	main()