# -*- coding:utf-8 -*-
from __future__ import print_function, division
import numpy as np
import random
import math


class sLDAModel(object):
    def __init__(self, K, beta, alpha, eta, sigma2, iter_times):
        #
        # 模型参数
        # 聚类个数K，迭代次数iter_times,每个类特征词个数top_words_num,超参数α（alpha） β(beta)
        # Y相关参数eta和sigma表示Y服从的高斯分布的参数
        #
        self.K = K
        self.beta = beta
        self.alpha = alpha
        self.iter_times = iter_times
        self.eta = eta
        self.sigma2 = sigma2

        # 文档数
        self.docs_count = 0  #TODO
        # 词汇数
        self.vocab_count = 0  #TODO
        # 文档
        self.docs = []  #TODO
        # Y值
        self.Y = []  #TODO

        # p,概率向量 double类型，存储采样的临时变量
        # nw,词word在主题topic上的分布
        # nwsum,每各topic的词的总数
        # nd,每个doc中各个topic的词的总数
        # ndsum,每各doc中词的总数
        self.p = np.zeros(self.K)
        # nw,词word在主题topic上的分布
        self.nw = np.zeros((self.vocab_count, self.K), dtype="int")
        # nwsum,每各topic的词的总数
        self.nwsum = np.zeros(self.K, dtype="int")
        # nd,每个doc中各个topic的词的总数
        self.nd = np.zeros((self.docs_count, self.K), dtype="int")
        # ndsum,每各doc中词的总数
        self.ndsum = np.zeros(self.docs_count, dtype="int")
        # Z M*doc.size()，文档中词的主题分布
        self.Z = np.array(
            [[0 for y in range(len(self.docs[x]))] for x in range(self.docs_count)])

        # 随机先分配类型，为每个文档中的各个单词分配主题
        for x in range(len(self.Z)):
            self.ndsum[x] = len(self.docs[x])
            for y in range(len(self.docs[x])):
                topic = random.randint(0, self.K - 1)  #TODO 随机取一个主题
                self.Z[x][y] = topic  # 文档中词的主题分布
                self.nw[self.docs[x][y]][topic] += 1
                self.nd[x][topic] += 1
                self.nwsum[topic] += 1

        self.theta = np.array([[0.0 for y in range(self.K)] for x in range(self.docs_count)])
        self.phi = np.array([[0.0 for y in range(self.vocab_count)] for x in range(self.K)])

    def sampling(self, i, j):
        # 换主题
        topic = self.Z[i][j]
        # 只是单词的编号，都是从0开始word就是等于j
        word = self.docs[i][j]
        # if word==j:
        #    print 'true'
        self.nw[word][topic] -= 1
        self.nd[i][topic] -= 1
        self.nwsum[topic] -= 1
        self.ndsum[i] -= 1

        Vbeta = self.vocab_count * self.beta
        Kalpha = self.K * self.alpha
        # TODO Z平均做归一化
        Zeta = np.matmul(np.array([self.nd[i]]), np.transpose(np.array([self.eta])))[0][0]
        Ysome = 1.0 / math.sqrt(2 * math.pi * self.sigma2) * math.exp(-((self.Y[i] - Zeta) ** 2) / (2 * self.sigma2))
        self.p = (self.nw[word] + self.beta) / (self.nwsum + Vbeta) * \
                 (self.nd[i] + self.alpha) / (self.ndsum[i] + Kalpha) * Ysome

        # 按这个更新主题更好理解，这个效果还不错
        p = np.squeeze(np.asarray(self.p / np.sum(self.p)))
        topic = np.argmax(np.random.multinomial(1, p))

        self.nw[word][topic] += 1
        self.nwsum[topic] += 1
        self.nd[i][topic] += 1
        self.ndsum[i] += 1
        return topic

    def est(self):
        # Consolelogger.info(u"迭代次数为%s 次" % self.iter_times)
        for x in range(self.iter_times):
            for i in range(self.docs_count):
                for j in range(len(self.docs[i])):
                    topic = self.sampling(i, j)
                    self.Z[i][j] = topic
            eta = np.linalg.solve()  #TODO
            sigma2 = 0  #TODO
