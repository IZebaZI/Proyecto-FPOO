import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

valores = [5, 6, 1, 3, 8, 9, 3, 5]
nombres = ['Prod1', 'Prod2', 'Prod3', 'Prod4', 'Prod5', 'Prod6', 'Prod7', 'Prod8'] 

figure = plt.Figure(figsize=(5, 5), dpi=60)

graph = figure.add_subplot(111)

graph.bar(range(len(valores)), valores)

graph.set_xticks(range(len(valores)))  
graph.set_xticklabels(nombres)  

root = tk.Tk()
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.draw()

canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

tk.mainloop()
