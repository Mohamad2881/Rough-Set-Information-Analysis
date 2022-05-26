# Rough-Set-Information-Analysis

## Reduction of Condition Attributes Relative to Decision Attributes
- Attributes can be divided into condition attributes C and
decision attributes D. An attribute a ∈ C is called
superfluous with respect to D if μ(C,D) = μ(C-{a},D),
otherwise a is indispensable in C
- Eliminating a superfluous C-attribute will not decrease or
increase the degree of dependency. This means that this
attribute is not necessary for the decision.


## Prediction of Missing Values
We will introduce a method to predict the decision for missing values. This will be done by:
1) Converting qualitative information system into binary system.
2) Divide the binary system into complete decision table and incomplete decision table. 
3) Calculate the distance function between objects of complete decision table and incomplete decision table. 
4) The smallest distance means that the decision for missing value of the incomplete decision table equals the decision value of the complete decision table of complete object which makes that distance.
5) If the small distance is repeated with more than one object. then we use the method of most common values. where we select the decision which has the largest number of repeatation with the complete decision table. 

