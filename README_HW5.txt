prob1
—————
the best fit values are [ 9.95049974  9.17189439  9.0432113 ] format=[a,b,c]
the mean temperature (after masking) is 8.93710711859 degrees celsius
the parameter b is just the time shift in the curve, basically when we start observing data relative to the seasons. 

prob2
—————
the best fit line values are
[-0.13980775  0.06148058] 
while the best fit quad values are
[-0.00723501 -0.14159439  0.06204996]

technically that’s a hard question to answer. Since the squared term in the quadratic plays such a little role, it contributes very weakly to predictive accuracy. That and the fact that the linear and constant variables are sufficiently close between the models implies that the linear function has a “better” fit, even though on some measures the quadratic might be better. In short, the extra parameter doesn’t give us enough new information to render the quadratic formula useful.

well, it depends on the outliers you choose. I tried a couple different ways and only one really worked. There was a small linear trend in some of the outliers in the upper region of the data set. The slope for this outlier group was positive rather than negative. Didn’t seem too significant though.