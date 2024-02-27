import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA 
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.neighbors import KDTree
from sklearn.manifold import TSNE
import umap

class Alg():

    data_neighbors = None
    cluster = None
    C = 10

    def main_alg_v2(self):
        df = pd.read_csv('million_song_subset.csv',sep='###')
        data_scaled = pd.DataFrame(df,columns=['duration','year','energy','danceability', 'loudness', 'tempo', 'time_signature', 'segment_loudness_avg',
       'chroma1', 'chroma2', 'chroma3', 'chroma4', 'chroma5', 'chroma6',
       'chroma7', 'chroma8', 'chroma9', 'chroma10', 'chroma11', 'chroma12',
       'MFCC1', 'MFCC2', 'MFCC3', 'MFCC4', 'MFCC5', 'MFCC6', 'MFCC7', 'MFCC8',
       'MFCC9', 'MFCC10', 'MFCC11', 'MFCC12'])

        scaler = StandardScaler()

        res = pd.DataFrame(data = scaler.fit_transform(data_scaled),
        columns = data_scaled.columns)
        kmeans = KMeans(n_clusters = self.C)
        cluster = kmeans.fit_predict(res)
        self.cluster = cluster
        self.data_neighbors = res
        self.data_neighbors['clusters']= self.cluster

    def pca(self):
        pca = PCA(2) 
        pca_data = pd.DataFrame(pca.fit_transform(self.data_neighbors),columns=['PC1','PC2'])

        pca_data['clusters']= self.cluster


        plt.figure(figsize=(10,10))
        sns.scatterplot(data=pca_data,x='PC1',y='PC2',hue='clusters')
        plt.title('Music Recommendation after PCA')
        plt.show()

    def neighbor(self, idn):

        tree = KDTree(self.data_neighbors, leaf_size=2)              
        dist, ind = tree.query(self.data_neighbors[idn:idn+1], k=self.C)    

        self.data_neighbors['clusters'] = self.cluster
        cluster = self.data_neighbors['clusters'].loc[self.data_neighbors.index[idn]]

        result_song_id = []

        for elem in ind[0]:
            if (self.data_neighbors['clusters'].loc[self.data_neighbors.index[elem]] == cluster):
                result_song_id.append(elem)

        return result_song_id

    def dop_alg(self):
        tsne2D = TSNE(n_components=2)
        tsne_data2D = tsne2D.fit_transform(self.data_neighbors)
        tsne2D_df = pd.DataFrame(data =  tsne_data2D, columns = ['x', 'y'])

        tsne2D_df['cluster'] =  self.cluster

        sns.scatterplot(x='x', y='y', hue='cluster', data=tsne2D_df)
        plt.title("T-SNE")
        plt.show()

    def ump_alg(self):
        umap2D = umap.UMAP(n_components=2)
        umap_data2D = umap2D.fit_transform(self.data_neighbors)
        umap2D_df = pd.DataFrame(data =  umap_data2D,columns = ['x', 'y'])

        umap2D_df['cluster'] = self.cluster

        sns.scatterplot(x='x', y='y', hue='cluster', data=umap2D_df)
        plt.title("UMAP")
        plt.show()


alg = Alg()
alg.main_alg_v2()
alg.pca()
alg.dop_alg()
alg.ump_alg()

