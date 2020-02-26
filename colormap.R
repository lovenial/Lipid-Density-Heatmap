install.packages("RColorBrewer", dependencies = TRUE)
library(RColorBrewer)

#import and adjustment of data matrix
data <- read.csv("yhist.csv")
rnames <- data[,1]
matrixdata <- data.matrix(data[,2:ncol(data)])
rownames(matrixdata) <- rnames

#adjustment of color palette
colorPalette <- colorRampPalette(c("black", "blue", "green", "red"))(n = 299)

#exports heatmap as png rather than opening it in xming (optional - commented out)
#png("heatmap(2/24).png",
#width = 5*300,
#height = 5*300,
#res = 300,
#pointsize = 8)

#sets color breaks (optional - commented out)
#col_breaks = c(seq(-1, 2,length = 100),seq(2.1, 4,length = 100),seq(4.1, 6,length = 100),seq(6.1, 50,length = 100))

#generates heatmap
heatmap(matrixdata, main = "Lipid Density Over Time - All Frames - Y Coords - POPE 8ILs",
col = colorPalette,
Colv = NA,
Rowv = NA,
xlab = "Time (picoseconds)",
ylab = "Spatial Bin",
labRow = FALSE,
labCol = FALSE,
scale = "column")
