from Yichuan.geneEncoding import geneEncoding
from Yichuan.decode import decodeChrom, printMax, decodeToValue
from Yichuan.select import select
from Yichuan.mutation import mutation
from Yichuan.crossover import crossover

if __name__ == '__main__':
    # fx表达式在funtion.py中进行修改
    # generation为要进化的代数
    # pop_size为每一代的个体数
    # select_size为每一代想要选择出的个体数
    # cross_size为每一代想要杂交出的个体数
    # new_size为每一代想要新产生的个体数（相当于外来物种了）
    # pm为突变概率
    generation = 10
    pop_size = 10
    select_size = 5
    cross_size = 5
    # new_size = 0
    max_value = 3  # 定义域上线
    min_value = -3  # 定义域下限
    chrom_length = 10  # 和精度有关，越大越精确
    pm = 0.1
    pop = geneEncoding(pop_size, chrom_length)

    for i in range(generation):
        fValue = decodeChrom(pop, chrom_length, max_value, min_value)
        value = decodeToValue(pop, chrom_length, max_value, min_value)
        maxvalue, maxX = printMax(fValue, value)
        print("第{}代，最大值为{},当x={}时取得".format(i + 1, maxvalue, maxX))
        selectPop = select(fValue, select_size, pop)
        crossPop = crossover(selectPop, cross_size)
        pop = selectPop + crossPop
        mutation(pop, pm)
        # newPop = geneEncoding(new_size, chrom_length)
        # pop += newPop
