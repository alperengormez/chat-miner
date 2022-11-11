from chatminer.chatparsers import WhatsAppParser
import chatminer.visualizations as vis
import glob
paths = glob.glob("./chats/WhatsApp Chat with *")

for FILEPATH in paths:
	parser = WhatsAppParser(FILEPATH)
	parser.parse_file_into_df()
	#print(parser.df.describe())
	
	vis.sunburst(parser.df, figuresavename=FILEPATH[27:-4])
	vis.wordcloud(parser.df, [], figuresavename=FILEPATH[27:-4])
	vis.weekday_plot(parser.df, figuresavename=FILEPATH[27:-4])
	vis.month_plot(parser.df, figuresavename=FILEPATH[27:-4])