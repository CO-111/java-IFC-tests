import os
import networkx as nx
import matplotlib.pyplot as plt

directory = '.'  # 当前目录，或者你想指定的路径

for filename in os.listdir(directory):
    # 只处理以 .graphml 结尾的文件，且文件名不以 .pdg 结尾
    if filename.endswith('.graphml') and not filename.endswith('.pdg'):
        # 但其实 .pdg 文件不会以 .graphml 结尾，所以可以简化判断为只过滤掉 .pdg 文件（不是graphml）
        if filename.endswith('.pdg'):
            # 直接跳过
            continue

        filepath = os.path.join(directory, filename)
        print(f'Processing {filepath}...')
        try:
            G = nx.read_graphml(filepath)
            plt.figure(figsize=(8, 6))
            nx.draw(G, with_labels=True, node_size=300, node_color='skyblue', font_size=8)
            png_filename = os.path.splitext(filename)[0] + '.png'
            plt.savefig(png_filename)
            plt.close()
            print(f'Saved {png_filename}')

            # 删除 graphml 文件
            os.remove(filepath)
            print(f'Removed {filepath}')
        except Exception as e:
            print(f'Failed to process {filename}: {e}')
