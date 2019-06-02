import matplotlib.pyplot as plt

whole_data_speed = [1,3038/2316,3038/1400,3038/1531]

one_eighth_speed = [1, 244/172, 244/147, 244/140]

one_fourth_speed = [1, 564/430, 564/376,564/299]

harf_data = [1,1601/1126,1601/628,1601/610]


nodes_number = [1,2,3,4]
plt.plot(nodes_number, one_eighth_speed)
plt.plot(nodes_number, one_fourth_speed)
plt.plot(nodes_number, harf_data)
plt.plot(nodes_number, whole_data_speed)

# plt.plot(year, pop_india, color='orange')

plt.legend(['1/8', '1/4', '1/3', 'whole data'], loc='upper right')
plt.xlabel('number of nodes')
plt.ylabel('speedup')
plt.title('Speedup')
plt.show()


# scaleup=[1,2316/3038 , 1455/3038 , 1325/3038 ]
# nodes_number = [1,2,3,4]
# plt.plot(nodes_number, scaleup)
# plt.xlabel('number of nodes')
# plt.ylabel('scaleup')
# plt.title('Scaleup')
# plt.show()
#
# one_node = [1,564/244, 1601/244,3038/244]
#
# two_nodes = [1,430/172, 1126/172,2316/172]
#
# three_nodes = [1, 376/117, 628/117,1325/117]
#
# four_nodes = [1,299/140,610/140,1400/140]
#
#
# size_of_dataset = [1/8,1/4,1/2,1]
# plt.plot(size_of_dataset, one_node)
# plt.plot(size_of_dataset, two_nodes)
# plt.plot(size_of_dataset, three_nodes)
# plt.plot(size_of_dataset, four_nodes)
#
# # plt.plot(year, pop_india, color='orange')
#
# plt.legend(['1 node', '2 nodes', '3 nodes', '4 nodes'], loc='upper right')
# plt.xlabel('size of dataset')
# plt.ylabel('sizeup')
# plt.title('Sizeup')
# plt.show()


