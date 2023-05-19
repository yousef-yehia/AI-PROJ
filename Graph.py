import matplotlib.pyplot as plt

# Data for the table
algorithms = ['Minimax', 'Alpha-Beta', 'Minimax', 'Alpha-Beta', 'Minimax', 'Alpha-Beta']
difficulty_levels = ['Easy', 'Easy', 'Medium', 'Medium', 'Hard', 'Hard']
execution_times = [0.247, 0.108, 1.094, 0.546, 2.782, 1.387]

# Plotting the graph
plt.plot(range(len(execution_times)), execution_times, marker='o')

# Labeling the x-axis with algorithms and difficulty levels
labels = [f"{algo}\n({level})" for algo, level in zip(algorithms, difficulty_levels)]
plt.xticks(range(len(execution_times)), labels)

# Labeling the y-axis and giving a title to the graph
plt.ylabel('Execution Time (seconds)')
plt.title('Performance of Alpha-Beta vs. Minimax')

# Displaying the graph
plt.show()