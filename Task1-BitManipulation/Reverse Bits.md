![image](https://github.com/user-attachments/assets/058dc133-fc34-4a62-a38d-1334b0e11350)

![image](https://github.com/user-attachments/assets/c486782c-dc45-4ade-b111-274e940d530b)

# Approach:
- First we should have to iterte each bit of the number , since there will be 32bits this code we will be using loop
- Before adding the next bit, shift the result left by 1 to make space for the new bit. This prepares the result to store the reversed
  bit in the correct position.
- Use the bitwise AND operation (n & 1) to check if the last bit of n is 1 or 0.
- And now the n will be shifted to right so that the bit at the last position will changed to check for next iteration.

# Documentation:
=> The above code will reverses the bits of a given 32-bit unsigned integer.
### Process:
- Initialize the **result** to 0, which will store the reversed bits.
- Loop 32 times and, in each iteration:
  - Shift **result** to the left by 1 position to make space for the next bit.
  - Extract the last bit of **n** using **n & 1**
  - Add this bit to result.
  - Shift **n** to the right by 1 position to process the next bit.
- After all 32 bits are processed, return the result.

