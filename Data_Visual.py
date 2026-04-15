# import os
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Load dataset
# df = pd.read_csv("Dataset/UNSW_NB15/Training and Testing Sets/UNSW_NB15_training-set.csv")
#
# # Create directory
# output_dir = "Image_Results/UNSWNB_15/"
# os.makedirs(output_dir, exist_ok=True)
#
# # Use multiple styles
# styles = ['ggplot', 'seaborn-v0_8', 'fivethirtyeight', 'bmh', 'dark_background']
#
# # -------------------------------
# # 1. Pie Chart (Attack Category)
# # -------------------------------
# plt.style.use(styles[0])
# plt.figure()
# df['attack_cat'].value_counts().head(6).plot(
#     kind='pie',
#     autopct='%1.1f%%',
#     colors=['red','blue','green','orange','purple','cyan']
# )
# plt.title("Attack Category")
# plt.ylabel("")
# plt.savefig(output_dir + "plot1_pie_attack.png")
# plt.close()
#
# # -------------------------------
# # 2. Horizontal Bar (Protocol)
# # -------------------------------
# plt.style.use(styles[1])
# plt.figure()
# df['proto'].value_counts().head(10).plot(
#     kind='barh',
#     color='teal'
# )
# plt.title("Top Protocols")
# plt.savefig(output_dir + "plot2_barh_proto.png")
# plt.close()
#
# # -------------------------------
# # 3. Histogram (Duration)
# # -------------------------------
# plt.style.use(styles[2])
# plt.figure()
# df['dur'].plot(
#     kind='hist',
#     bins=40,
#     color='gold',
#     edgecolor='black'
# )
# plt.title("Duration Distribution")
# plt.savefig(output_dir + "plot3_hist_dur.png")
# plt.close()
#
# # -------------------------------
# # 4. KDE Plot (Rate)
# # -------------------------------
# plt.style.use(styles[3])
# plt.figure()
# df['rate'].plot(
#     kind='kde',
#     color='magenta',
#     linewidth=2
# )
# plt.title("Rate Density Plot")
# plt.savefig(output_dir + "plot4_kde_rate.png")
# plt.close()
#
# # -------------------------------
# # 5. Scatter Plot (sbytes vs dbytes)
# # -------------------------------
# plt.style.use(styles[4])
# plt.figure()
# plt.scatter(
#     df['sbytes'],
#     df['dbytes'],
#     c=df['label'],
#     cmap='coolwarm',
#     alpha=0.6
# )
# plt.xlabel("Source Bytes")
# plt.ylabel("Destination Bytes")
# plt.title("sbytes vs dbytes")
# plt.colorbar()
# plt.savefig(output_dir + "plot5_scatter_bytes.png")
# plt.close()
#
# # -------------------------------
# # 6. Box Plot (Packet Features)
# # -------------------------------
# plt.style.use(styles[3])
# plt.figure()
# df[['spkts', 'dpkts']].plot(
#     kind='box',
#     patch_artist=True
# )
# plt.title("Packet Distribution")
# plt.savefig(output_dir + "plot6_box_packets.png")
# plt.close()
#
# # -------------------------------
# # 7. Area Plot (Top Services)
# # -------------------------------
# plt.style.use(styles[3])
# plt.figure()
# df['service'].value_counts().head(5).plot(
#     kind='area',
#     color=['skyblue','orange','green','red','purple'],
#     alpha=0.7
# )
# plt.title("Top Services Area Plot")
# plt.savefig(output_dir + "plot7_area_service.png")
# plt.close()
#
# # -------------------------------
# # 8. Line Plot (Mean values)
# # -------------------------------
# plt.style.use(styles[2])
# plt.figure()
# df[['smean', 'dmean']].head(100).plot(
#     kind='line',
#     color=['blue','red']
# )
# plt.title("Mean Values Trend")
# plt.savefig(output_dir + "plot8_line_mean.png")
# plt.close()
#
# # -------------------------------
# # 9. Hexbin Plot (dur vs rate)
# # -------------------------------
# plt.style.use(styles[3])
# plt.figure()
# plt.hexbin(
#     df['dur'],
#     df['rate'],
#     gridsize=25,
#     cmap='inferno'
# )
# plt.colorbar()
# plt.title("Duration vs Rate")
# plt.savefig(output_dir + "plot9_hexbin.png")
# plt.close()
#
# # -------------------------------
# # 10. Violin Plot (TTL values)
# # -------------------------------
# plt.style.use(styles[4])
# plt.figure()
# plt.violinplot([df['sttl'], df['dttl']])
# plt.xticks([1,2], ['sttl','dttl'])
# plt.title("TTL Distribution")
# plt.savefig(output_dir + "plot10_violin_ttl.png")
# plt.close()
#
# print("🔥 All stylish 10 plots saved in:", output_dir)


import os
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset/Bot_IoT/UNSW_2018_IoT_Botnet_Full5pc_2.csv")  # adjust if needed

# Create output folder
output_dir = "Image_Results/Bot_IoT/"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------
# 1. Attack Distribution
# -------------------------------
plt.figure()
df['attack'].value_counts().plot(kind='bar', color='blue')
plt.title("Attack Distribution")
plt.tight_layout()
plt.savefig(output_dir + "plot1_attack.png")
plt.close()

# -------------------------------
# 2. Category Distribution
# -------------------------------
plt.figure()
df['category'].value_counts().plot(kind='bar', color='green')
plt.title("Category Distribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_dir + "plot2_category.png")
plt.close()

# -------------------------------
# 3. Protocol Distribution
# -------------------------------
plt.figure()
df['proto'].value_counts().head(10).plot(kind='bar', color='orange')
plt.title("Top Protocols")
plt.xticks(rotation=45)
plt.savefig(output_dir + "plot3_proto.png")
plt.close()

# -------------------------------
# 4. State Distribution
# -------------------------------
plt.figure()
df['state'].value_counts().plot(kind='bar', color='purple')
plt.title("State Distribution")
plt.savefig(output_dir + "plot4_state.png")
plt.close()

# -------------------------------
# 5. Duration Histogram
# -------------------------------
plt.figure()
df['dur'].plot(kind='hist', bins=30, color='red')
plt.title("Duration Distribution")
plt.tight_layout()
plt.savefig(output_dir + "plot5_dur.png")
plt.close()

# -------------------------------
# 6. Packets Histogram
# -------------------------------
plt.figure()
df['pkts'].plot(kind='hist', bins=30, color='cyan')
plt.title("Packets Distribution")
plt.tight_layout()
plt.savefig(output_dir + "plot6_pkts.png")
plt.close()

# -------------------------------
# 7. Bytes Histogram
# -------------------------------
plt.figure()
df['bytes'].plot(kind='hist', bins=30, color='brown')
plt.title("Bytes Distribution")
plt.tight_layout()
plt.savefig(output_dir + "plot7_bytes.png")
plt.close()

# -------------------------------
# 8. sbytes vs dbytes Scatter
# -------------------------------
plt.figure()
plt.scatter(df['sbytes'], df['dbytes'], alpha=0.5)
plt.xlabel("sbytes")
plt.ylabel("dbytes")
plt.title("sbytes vs dbytes")
plt.tight_layout()
plt.savefig(output_dir + "plot8_scatter.png")
plt.close()

# -------------------------------
# 9. Rate Line Plot
# -------------------------------
plt.figure()
df['rate'].head(200).plot(kind='line', color='black')
plt.title("Rate Trend")
plt.tight_layout()
plt.savefig(output_dir + "plot9_rate.png")
plt.close()

# -------------------------------
# 10. Box Plot (pkts & bytes)
# -------------------------------
plt.figure()
df[['pkts', 'bytes']].plot(kind='box')
plt.title("Packets vs Bytes")
plt.tight_layout()
plt.savefig(output_dir + "plot10_box.png")
plt.close()

print("✅ 10 simple plots saved in:", output_dir)