import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from math import exp
import matplotlib.ticker as ticker

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
    plt.grid();
    axes = plt.gca();
    axes.set_xlim([ 0, 6]);
    axes.set_ylim([ 0, 1]);
    axes.yaxis.set_major_locator(ticker.MultipleLocator(.1));
    axes.xaxis.set_major_locator(ticker.MultipleLocator(.5));
    plt.savefig(filename);
    plt.close();
    
def two_line_plot(x1, y1, x2, y2, title, filename):
    plt.plot(x1, y1);
    plt.plot(x2, y2)
    plt.xlabel('X - Hours');
    plt.ylabel('Y');
    plt.title(title);
    plt.grid();
    axes = plt.gca();
    axes.set_xlim([ 0, 6]);
    axes.set_ylim([ 0, 1]);
    axes.yaxis.set_major_locator(ticker.MultipleLocator(.1));
    axes.xaxis.set_major_locator(ticker.MultipleLocator(.5));
    plt.savefig(filename);
    plt.close();    

linearTheta0 = 0.020966505425145464;
linearTheta1 = 0.18447316076872963;
logisticTheta0 = -2.091321055288621;
logisticTheta1 =  0.8471563086673924;


xValues = [];
step = .1
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
two_line_plot(xValues, linearRegressionYValues, xValues, logisticRegressionYValues, 'Combined', 'CombinedRegression.svg');