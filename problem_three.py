import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from math import exp

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def line_plot(x, y, title, filename):
    plt.plot(x, y);
    plt.xlabel('X - Hours');
    plt.ylabel('Y');
    plt.title(title);
    plt.savefig(filename);
    plt.close();

linearTheta0 = .0411;
linearTheta1 = 0.172;
logisticTheta0 = -2.703;#1.4906701387463288;
logisticTheta1 =  1.046;#6554905329910404;


xValues = [];
step = .5
for i in frange(0.0, 6.0 + step, step):
    xValues.append(i);

#print(xValues);
linearRegressionYValues = [];
logisticRegressionYValues = [];

for x in xValues:

    linearRegressionYValues.append(linearTheta0 + .176 * x);
    logisticRegressionYValues.append( 1.0 / ( 1 + exp( -1 * (  logisticTheta0  +  logisticTheta1 * x ) ) ));
    
#print(linearRegressionYValues);
#print(logisticRegressionYValues);


line_plot(xValues, linearRegressionYValues, 'Linear', 'linearRegression.svg');
line_plot(xValues, logisticRegressionYValues, 'Logistic', 'logisticRegression.svg');