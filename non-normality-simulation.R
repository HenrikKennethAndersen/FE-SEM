# ======================================= # 
# FE-SEM Paper REVISION
# Simulation: Check normality assumptions
# Henrik Kenneth Andersen 
# 04.01.2021
# ======================================= # 

rm(list = ls())

library(lavaan)
library(ggplot2)

# Types of error distributions 
par(mfrow = c(2, 2))

hist(rnorm(n, 0, 1))
hist(runif(n, min(rnorm(n, 0, 1)), max(rnorm(n, 0, 1))))
hist(exp(rnorm(n, 0, 1)))

# Function to simulate data and estimate FE-SEM
sim_func <- function(dist, n) {
  
  # Generate the individual effects
  a <- rnorm(n, 0, 1)  
  
  x1 <- 0.5*a + rnorm(n, 0, 1)
  x2 <- 0.5*a + rnorm(n, 0, 1)
  x3 <- 0.5*a + rnorm(n, 0, 1)
  
  if(dist == "norm") {
    y1 <- -0.25*x1 + a + rnorm(n, 0, 1)
    y2 <- -0.25*x2 + a + rnorm(n, 0, 1)
    y3 <- -0.25*x3 + a + rnorm(n, 0, 1)
    } else if (dist == "unif") {
      y1 <- -0.25*x1 + a + runif(n, min(rnorm(n, 0, 1)), max(rnorm(n, 0, 1)))
      y2 <- -0.25*x2 + a + runif(n, min(rnorm(n, 0, 1)), max(rnorm(n, 0, 1)))
      y3 <- -0.25*x3 + a + runif(n, min(rnorm(n, 0, 1)), max(rnorm(n, 0, 1)))
    } else if (dist == "skew") {
      y1 <- -0.25*x1 + a + exp(rnorm(n, 0, 1))
      y2 <- -0.25*x2 + a + exp(rnorm(n, 0, 1))
      y3 <- -0.25*x3 + a + exp(rnorm(n, 0, 1))
    } else {
        stop("Choose from 'norm', 'unif' or 'skew' as a distribution for the errors.")
      }
  
  df <- data.frame(x1, x2, x3, y1, y2, y3)
  
  mx <- '
  alpha =~ 1*y1 + 1*y2 + 1*y3
  y1 ~ beta*x1
  y2 ~ beta*x2
  y3 ~ beta*x3
  alpha ~~ x1 + x2 + x3
  x1 ~~ x2 + x3
  x2 ~~ x3
  y1 ~~ u*y1
  y2 ~~ u*y2
  y3 ~~ u*y3
  '
  mx.fit <- sem(mx, df)
  
  beta <- lavInspect(mx.fit, what = "list")[4, 14]
  
  return(beta)
}

# Set the parameters for the simulation 
n = 1000
nreps = 500

# Repeat the simulation, save the estimated coefficients
sim_norm <- replicate(nreps, sim_func(dist = "norm", n = n))
sim_unif <- replicate(nreps, sim_func(dist = "unif", n = n))
sim_skew <- replicate(nreps, sim_func(dist = "skew", n = n))

# Check error message
# replicate(nreps, sim_func(dist = "blah", n = n))

sim_norm <- data.frame(rep = seq(1, nreps, 1), beta = sim_norm)
sim_unif <- data.frame(rep = seq(1, nreps, 1), beta = sim_unif)
sim_skew <- data.frame(rep = seq(1, nreps, 1), beta = sim_skew)


# Histograms 
sim_norm_hist <- ggplot(sim_norm, aes(beta)) + 
  geom_histogram(color = "black", fill = "grey", bins = 15)

sim_unif_hist <- ggplot(sim_unif, aes(beta)) + 
  geom_histogram(color = "black", fill = "grey", bins = 15)

sim_skew_hist <- ggplot(sim_skew, aes(beta)) + 
  geom_histogram(color = "black", fill = "grey", bins = 15)

sim_norm_hist
sim_unif_hist
sim_skew_hist

# Expected value
mean(sim_norm$beta)
mean(sim_unif$beta)
mean(sim_skew$beta)

# Standard deviation of sampling distribution 
sd(sim_norm$beta)
sd(sim_unif$beta)
sd(sim_skew$beta)


# Single models for standard errors
a <- rnorm(n, 0, 1)  

x1 <- 0.5*a + rnorm(n, 0, 1)
x2 <- 0.5*a + rnorm(n, 0, 1)
x3 <- 0.5*a + rnorm(n, 0, 1)

# Normally distributed errors 
y1 <- -0.25*x1 + a + rnorm(n, 0, 1)
y2 <- -0.25*x2 + a + rnorm(n, 0, 1)
y3 <- -0.25*x3 + a + rnorm(n, 0, 1)

df1 <- data.frame(x1, x2, x3, y1, y2, y3)

# Uniformly distributed errors 
y1 <- -0.25*x1 + a + runif(n, min(rnorm(n, 0, 1)), max(rnorm(n, 0, 1)))
y2 <- -0.25*x2 + a + runif(n, min(rnorm(n, 0, 1)), max(rnorm(n, 0, 1)))
y3 <- -0.25*x3 + a + runif(n, min(rnorm(n, 0, 1)), max(rnorm(n, 0, 1)))

df2 <- data.frame(x1, x2, x3, y1, y2, y3)

# Skewed errors 
y1 <- -0.25*x1 + a + exp(rnorm(n, 0, 1))
y2 <- -0.25*x2 + a + exp(rnorm(n, 0, 1))
y3 <- -0.25*x3 + a + exp(rnorm(n, 0, 1))

df3 <- data.frame(x1, x2, x3, y1, y2, y3)

# Specify FE-SEM 
mx <- '
  alpha =~ 1*y1 + 1*y2 + 1*y3
  y1 ~ beta*x1
  y2 ~ beta*x2
  y3 ~ beta*x3
  alpha ~~ x1 + x2 + x3
  x1 ~~ x2 + x3
  x2 ~~ x3
  y1 ~~ u*y1
  y2 ~~ u*y2
  y3 ~~ u*y3
  '
# Normally distributed errors
mx_norm.fit <- sem(mx, df1); summary(mx_norm.fit)

# Uniformly distributed errors 
mx_unif.fit <- sem(mx, df2); summary(mx_unif.fit)
mx_unif_rob.fit <- sem(mx, df2, estimator = "MLR"); summary(mx_unif_rob.fit)

# Skewed errors 
mx_skew.fit <- sem(mx, df3); summary(mx_skew.fit)
mx_skew_rob.fit <- sem(mx, df3, estimator = "MLR"); summary(mx_skew_rob.fit)
