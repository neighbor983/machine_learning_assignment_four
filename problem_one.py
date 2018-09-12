data = [
    { 'x': 0.5,  'y': 0 },
    { 'x': 0.75, 'y': 0 },
    { 'x': 1.00, 'y': 0 },
    { 'x': 1.25, 'y': 0 },
    { 'x': 1.50, 'y': 0 },
    { 'x': 1.75, 'y': 0 },
    { 'x': 1.75, 'y': 1 },
    { 'x': 2.00, 'y': 0 },      
    { 'x': 2.25, 'y': 1 },
    { 'x': 2.50, 'y': 0 },
    { 'x': 2.75, 'y': 1 },
    { 'x': 3.00, 'y': 0 },
    { 'x': 3.25, 'y': 1 },
    { 'x': 3.50, 'y': 0 },
    { 'x': 4.00, 'y': 1 },
    { 'x': 4.25, 'y': 1 },
    { 'x': 4.50, 'y': 1 },
    { 'x': 4.75, 'y': 1 },
    { 'x': 5.00, 'y': 1 },
    { 'x': 5.50, 'y': 1 }
];

#Initial variables
theta0 = 0.0;
theta1 = 0.0;
alpha = .1;
m = len(data);

def simple_linear(theta0, theta1, x):
    '''
    description:
        takes in the thetas and the x_i and returns the predicted y for a simple linear regression
    params:
        theta0 = number
        theta1 = number    
        x = number
    output:
        number
    '''
    return theta0 + theta1 * x;

def cost_function(theta0, theta1, alpha, m, dataList):
    '''
    description:
        get the cost for a given model and thetas
    params:
        theta0 = number
        theta1 = number
        alpha = number
        m = number
        dataList = list of objects with 'x' and 'y'
    output:
        number
    '''
    summation = 0.0;
    for row in dataList: 
        x = row['x'];
        y = row['y'];
        summation += (simple_linear(theta0, theta1,x) - y)**2;
    cost = ( .5 * m ) * summation;
    return cost;
    
def theta0_gradient(theta0, theta1, alpha, m, dataList) : 
    '''
    description:
        Use gradient descent to generate the new theta0
    params:
        theta0 = number
        theta1 = number
        alpha = number
        dataList = list of objects with 'x' and 'y'
    output:
        number
    '''
    summation = 0.0;
    for row in dataList:  
        x = row['x'];
        y = row['y'];
        summation += (simple_linear(theta0, theta1, x) - y);
    theta0 = theta0 - ( alpha / m) * summation;
    return theta0
    
def theta1_gradient(theta0, theta1, alpha, m, dataList) : 
    '''
    description:
        Use gradient descent to generate the new theta1
    params:
        theta0 = number
        theta1 = number
        alpha = number
        dataList = list of objects with 'x' and 'y'
    output:
        number
    '''
    summation = 0.0
    for row in dataList: 
        x = row['x'];
        y = row['y'];
        summation += ((simple_linear(theta0, theta1, x) - y) * x)
    theta1 = theta1 - ( alpha / m ) * summation
    return theta1
    
j_theta = cost_function(theta0, theta1, alpha, m, data);    

theta0_new = theta0_gradient(theta0, theta1, alpha, m, data);
theta1_new = theta1_gradient(theta0, theta1, alpha, m, data);
theta0 = theta0_new;
theta_one = theta1;
j_theta_new = cost_function(theta0_new, theta1_new, alpha, m, data);

while( j_theta > ( j_theta_new * 1.001 ) ):
    theta0_new = theta0_gradient(theta0, theta1, alpha, m, data);
    theta1_new = theta1_gradient(theta0, theta1, alpha, m, data);
    theta0 = theta0_new;
    theta1 = theta1_new;
    j_theta = j_theta_new;
    j_theta_new = cost_function(theta0_new, theta1_new, alpha, m, data);

print(theta0);
print(theta1);
