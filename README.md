# First Heading
For The data ingestion pipeline, I have created a plan for best retrieval afterwards. As these are programming docs and by default the writers have well divided them into files w.r.t the concepts these are discussing so its easy for us to chunk them and embed them and save them in Qdrant cloud instance. We will do the chunking like this:

Get all the files recursively from the directories
Get the text from the file
if the file's text is less than 10k characters, directly consider it as a chunk
if the file's text is greater than 10k characters, convert it into chunks by separating at heading for .md, .mdx, .ipynb and .rst as they have proper formatting in them with headings. For .txt files just divide at new paragraphs so that all the chunks should fall under 10000 characters. 
