from collections import defaultdict
from typing import Any, List, Dict

# Define the mapper function
def mapper(item: Any) -> List[tuple]:
    # Sample mapper function: Word count
    words = item.split()
    return [(word, 1) for word in words]

# Define the reducer function
def reducer(key: Any, values: List[Any]) -> Any:
    # Sample reducer function: Summing up values
    return sum(values)

# MapReduce function
def map_reduce(data: List[Any], mapper: callable, reducer: callable) -> Dict[Any, Any]:
    # Map phase
    print("Map Phase:")
    intermediate_results = defaultdict(list)
    for item in data:
        mapped_items = mapper(item)
        print(f"Mapper Output: {mapped_items}")
        for key, value in mapped_items:
            intermediate_results[key].append(value)
    
    # Reduce phase
    print("\nReduce Phase:")
    final_result = {}
    for key, values in intermediate_results.items():
        reduced_value = reducer(key, values)
        print(f"Reducer Input: ({key}, {values})")
        print(f"Reducer Output: ({key}, {reduced_value})")
        final_result[key] = reduced_value
    
    return final_result

# Sample data
data = [
    "neave is king",
    "neave paul",
    "paul is father"
]

# Perform MapReduce
result = map_reduce(data, mapper, reducer)
print("\nFinal Result:")
print(result)
