import streamlit as st 
import streamlit.components.v1 as stc 

import base64

from result_scrapper import get_live_score,arewewinning

# html_temp = """
# 		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
# 		<h1 style="color:white;text-align:center;">Early Stage DM Risk Data App </h1>
# 		<h4 style="color:white;text-align:center;">Diabetes </h4>
# 		</div>
# 		"""
SIII = "images/ronaldohattrickjpg.jpg"
NOOO = "images/sad-portuguese-soccer-fan-with-the-portuguese-CR8RCK.jpg"


def main():
	#st.beta_set_page_config(layout="wide")
	
	st.title('Portugal está na próxima ronda?')
	st.subheader(' Não é preciso sacar da calculadora')
	try: 
		df_test=get_live_score()
		df_test['home_score'] = df_test['home_score'].astype(int)
		df_test['away_score'] = df_test['away_score'].astype(int)
		passing=arewewinning(df_test)
		if passing:
			st.image(SIII,use_column_width = 'auto')
			st.success('TAMOS LÁ - NUNCA DUVIDEI')
		else:
			st.image(NOOO,use_column_width = 'auto')
			st.error('EU JÁ SABIA - NUNCA ACREDITEI')
	except:
		st.image(SIII,use_column_width = 'auto')
		st.success('TAMOS LÁ - NUNCA DUVIDEI')
	

if __name__ == '__main__':
	main()