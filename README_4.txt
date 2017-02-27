README

Program 1 does a montecarlo simulation of radioactive decay starting with Bismuth 213. It outputs a graph of amounts of Bi213, Ti209, Pb209, and Bi209 over time. 

Program 2 does a crappy job at monte carlo integrating a function with no analytic solution. oh well.

Solutions to 2:

we can see that p(x) =  sqrt(x)*(3./2) by using the formula given and w(x) = sqrt(x)
	p(x) = w(x)/integrate(w(x), 0, 1)
	p(x) = w(x)/(2/3)
	p(x) = w(x)*(3./2)
	p(x) = sqrt(x)*(3./2)

I don’t know how we got the p(x) given in the homework, that can’t be right if we’re using the formula 10.39 in the book and w(x) = sqrt(x) …

the transformation formula, therefore, is 
	u from (0,1)
	u = sqrt(x)*(3./2)
	(2u/3) = sqrt(x)
	(2u/3)**2 = x
but that gives us the wrong answer.