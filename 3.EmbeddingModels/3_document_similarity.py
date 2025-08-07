from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

# we are performing semantic search -- later we will use vector database for storing embeddings

documents=[
    "Virat Kohli is widely regarded as one of the best modern-day batsmen, with numerous records across all formats of international cricket.",
    "Sachin Tendulkar, known as the 'Little Master,' is often referred to as the greatest batsman of all time, having scored over 34,000 international runs.",
    "MS Dhoni is celebrated for his calm leadership and finishing abilities, leading India to win the 2007 ICC T20 World Cup, the 2011 ICC World Cup, and the 2013 ICC Champions Trophy.",
    "Rohit Sharma holds the record for the highest individual score in a One-Day International, with a stunning 264 runs against Sri Lanka in 2014.",
    "Jasprit Bumrah has emerged as one of the world’s leading fast bowlers, known for his deadly yorkers and exceptional death-over skills in limited-overs cricket."
]

query="tell me about dhoni"

doc_embeddings=embedding.embed_documents(documents)

query_embedding=embedding.embed_query(query)

scores=cosine_similarity([query_embedding],doc_embeddings)[0]

index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(documents[index])
print('Similarity score is: ',score)