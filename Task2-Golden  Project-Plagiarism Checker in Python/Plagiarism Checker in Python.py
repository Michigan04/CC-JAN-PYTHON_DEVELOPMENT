import tkinter as tk
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def plagiarism_checker():
    t1 = text_entry1.get("1.0",'end-1c')
    t2 = text_entry2.get("1.0",'end-1c')
    vectorizer = CountVectorizer().fit_transform([t1, t2])
    vectors = vectorizer.toarray()
    similarity = cosine_similarity(vectors)
    similarity = round(similarity[0][1], 2)
    result.config(text = f'Similarity: {similarity}',font=20)

root = tk.Tk()
root.title("Plagiarism Detector")

text_entry1 = tk.Text(root, height = 10, width = 60)
text_entry1.pack()

text_entry2 = tk.Text(root, height = 10, width = 60)
text_entry2.pack()

check = tk.Button(root, text = "Calculate Plagiarism Ratio", command = plagiarism_checker,font=20)
check.pack()

result = tk.Label(root)
result.pack()

root.mainloop()
