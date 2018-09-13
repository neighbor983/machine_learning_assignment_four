from math import exp, log

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
alpha = .5;
m = len(data);
count = 0;

def hypothese_function(theta0, theta1, x):
    a = exp( -1 * ( theta0 + theta1 * x ) );
    return 1.0 / ( 1.0 + a );

def cost_function(theta0, theta1, m, data):
    '''
    description:
        get the cost for a given model and thetas
    params:
        theta0 = number
        theta1 = number
        m = number
        data = list of objects with 'x' and 'y'
    output:
        number
    '''
    summation = 0.0;
    for item in data:
        x = item['x'];
        y = item['y'];
        summation += -y * log( hypothese_function( theta0, theta1, x ) ) - ( 1 - y ) * log( 1 -hypothese_function(theta0,theta1,x) )  ;
    return summation;

def theta0_update(theta0, theta1, alpha, m, data):
    '''
    description:
        get the updated theta0
    params:
        theta0 = number
        theta1 = number
        m = number
        data = list of objects with 'x' and 'y'
    output:
        number
    '''
    summation = 0.0
    for item in data:
        x = item['x'];
        y = item['y'];
        summation += ( hypothese_function( theta0, theta1, x ) - y );
    
    return theta0 - ( alpha / m ) * summation;

def theta1_update(theta0, theta1, alpha, m, data):
    '''
    description:
        get the updated theta1
    params:
        theta0 = number
        theta1 = number
        m = number
        data = list of objects with 'x' and 'y'
    output:
        number
    '''
    summation = 0.0
    for item in data:
        x = item['x'];
        y = item['y'];
        summation += ( ( hypothese_function( theta0, theta1, x ) - y ) * x );
    
    return theta1 - ( alpha / m ) * summation;

j_theta = cost_function(theta0, theta1, m, data);    

theta0_new = theta0_update(theta0, theta1, alpha, m, data);
theta1_new = theta1_update(theta0, theta1, alpha, m, data);
theta0 = theta0_new;
theta1 = theta1_new;
j_theta_new = cost_function(theta0_new, theta1_new, m, data);
count += 1;

while( j_theta > ( j_theta_new * 1.001 ) ):
    theta0_new = theta0_update(theta0, theta1, alpha, m, data);
    theta1_new = theta1_update(theta0, theta1, alpha, m, data);
    theta0 = theta0_new;
    theta1 = theta1_new;
    j_theta = j_theta_new;
    j_theta_new = cost_function(theta0_new, theta1_new, m, data);
    count += 1;

print(theta0);
print(theta1);
print(count);