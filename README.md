# Hopfield Network

## データの記憶
$$
w_{ij} = \sum_{d\in D} x_i^d x_j^d
$$

## データの想起
$$
y_i = \sum_{j=1}^{N} w_{ij} x_j
$$

$$
x_i = \begin{cases}
    1  & y_i > 0 \\
    x_i & y_i = 0 \\
    -1 & y_i < 0
\end{cases}
$$