import numpy as np

def calculate(list):
    """output the mean, variance, standard deviation, max, min,
    and sum of the rows, columns, and elements in a 3 x 3 matrix."""
    
    if len(list)<9:
        raise ValueError("List must contain nine numbers.")
    
    list = np.array(list).reshape(3,3)
    
    calculations = {}
    
    for j in ["mean", "variance", "standard deviation", "max", "min","sum"]:
        results = [] 
        for i in ["axis1", "axis2",  "flattened"]:
            if j == "mean":
                if i == "axis1":
                    results.append(np.mean(list, axis =0).tolist())
                elif i == "axis2":
                    results.append(np.mean(list, axis =1).tolist())
                else:
                    results.append(np.mean(list).tolist())
            elif j == "variance":
                if i == "axis1":
                    results.append(np.var(list, axis =0).tolist())
                elif i == "axis2":
                    results.append(np.var(list, axis =1).tolist())
                else:
                    results.append(np.var(list).tolist())
            elif j == "standard deviation":
                if i == "axis1":
                    results.append(np.std(list, axis =0).tolist())
                elif i == "axis2":
                    results.append(np.std(list, axis =1).tolist())
                else:
                    results.append(np.std(list).tolist())
            elif j == "max":
                if i == "axis1":
                    results.append(np.max(list, axis =0).tolist())
                elif i == "axis2":
                    results.append(np.max(list, axis =1).tolist())
                else:
                    results.append(np.max(list).tolist())
            elif j == "min":
                if i == "axis1":
                    results.append(np.min(list, axis =0).tolist())
                elif i == "axis2":
                    results.append(np.min(list, axis =1).tolist())
                else:
                    results.append(np.min(list).tolist())
            elif j == "sum":
                if i == "axis1":
                    results.append(np.sum(list, axis =0).tolist())
                elif i == "axis2":
                    results.append(np.sum(list, axis =1).tolist())
                else:
                    results.append(np.sum(list).tolist())
            
            calculations[j] = results

    return calculations
