
## 1.1. Random Access Machine (RAM)

: RAM is a part of every computer that usually stores temporary information (memory) from a running program.

: Suppose that the time of executing all basic memory operations is exactly `θ(1)` (e.g. getting a the index of any element regardless of the location in the RAM always takes `θ(1)`)

## 1.1.1. RAM Recall : As an Array of memory

: Consider RAM as a list of information, where every byte (8-bit string) of information has a specific address index, such that **contiguous** (adjacent/ neighboring) information has consecutive address.

>	e.g. suppose the character 'A' is in address 10000, given that another character 'B' is next to 'A', then its  address is 10001.


## 1.2. Dynamic Arrays

: Dynamic array is a list with a given current size, allocated size cap, and pointer