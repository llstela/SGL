from .node_classification import HeteroNodeClassification
from .node_classification import NodeClassification
from .node_clustering import NodeClustering
from .node_clustering import NodeClusteringNAFS
from .link_prediction import LinkPredictionGAE
from .link_prediction import LinkPredictionNAFS

__all__ = [
    "NodeClassification",
    "HeteroNodeClassification",
    "NodeClustering",
    "NodeClusteringNAFS",
    "LinkPredictionGAE",
    "LinkPredictionNAFS"
]
