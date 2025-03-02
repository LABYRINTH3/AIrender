import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# 그래프 생성
G = nx.DiGraph()

# 입력 노드 개수
num_inputs = 10

# 입력 노드 추가 및 위치 지정 (x=0, y는 0~1 사이 균등 분포)
input_nodes = [f"I{i}" for i in range(num_inputs)]
y_positions = np.linspace(0, 1, num_inputs)
pos = {}
for node, y in zip(input_nodes, y_positions):
    G.add_node(node)
    pos[node] = (0, y)

# 중간 노드와 출력 노드 추가
G.add_node("Hidden")
G.add_node("Output")
pos["Hidden"] = (1, 0.5)
pos["Output"] = (2, 0.5)

# 입력 노드에서 중간 노드로 에지 추가
for node in input_nodes:
    G.add_edge(node, "Hidden")

# 중간 노드에서 출력 노드로 에지 추가
G.add_edge("Hidden", "Output")

# 그림 그리기
plt.figure(figsize=(10, 6))
# 모든 노드 그리기
nx.draw_networkx_nodes(G, pos, node_size=100, node_color='skyblue')
# 에지 그리기 (입력->중간, 중간->출력)
nx.draw_networkx_edges(G, pos, arrows=False, alpha=0.3)

# 중간 및 출력 노드만 노드 라벨 표시 (입력 노드는 너무 많으므로 생략)
labels = {"Hidden": "", "Output": ""}
nx.draw_networkx_labels(G, pos, labels, font_size=12)

plt.title("")
plt.axis('off')
plt.tight_layout()
plt.show()
