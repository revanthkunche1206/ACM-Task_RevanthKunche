![Screenshot 2024-09-28 215053](https://github.com/user-attachments/assets/d642c879-1375-4d87-aaec-3f39cc4409a8)

![Screenshot 2024-09-28 220533](https://github.com/user-attachments/assets/5ccbfa83-9321-4e5e-8c52-d2ae5cbbdc88)
# Approach
While adding binary numbers "0" and "0" gives **0**; "1" and "0" gives **1**; "1" and "1" gives **0** along with carry **1**.Now to add both numbers should be of same length for easier itrations.Now we will be starting from right to left and when the sum if greater than **2** i.e, if we take **1+1+1** give **3** now the **3%2** will be **1** this will be added to result and carry is set to **1** because first **1+1** is **10** and then again **10+1** is **11**. And in the other case if the sum is less than 2 i.e, if we take **1** and **0** gives **1** in this case no carry is needed and we can directly add this to result.Same in the case **0** and **0** gives **0**. And finally we will return the reversed string of result.
# Documentation
The above code is to find the sum of two binary numbers and return the resultant binary number as a string.

### Variables:
- result(string): The binary sum for two numbers is stored in this variable. And the result should be returned in the reverse order because the following **for loop** will start from last char of the given number to first.
- carry(int): The carry which will be occured in the binary addition will sored in this variable. It is first initialised to 0.
- max_len(int): The maximum length of the given two numbers will be stored in this variable.
  This will be used to make both **a** abd **b** of equal length.

### Process:
- Now this function first pads the binary strings **a** abd **b** to make them equal in length using **zfill()** method.Then, it iterates through the binary strings from right to left, adding the corresponding bits along with any carry from the previous addition.
- The loop iterates from the last character (least significant bit) to the first character (most significant bit).
- At each iteration, the sum of the corresponding bits from 'a', 'b', and the carry is calculated.
- If the sum is greater than or equal to 2, a carry is set to **1** for the next iteration, and the current sum's remainder with **mod 2** is added to the result.
- If the sum is less than 2, the carry is set to **0**, and the result is simply the current sum.
- After the all iterations if the carry is again **1** this will also added to the result.
- And finally the result is reversed by slicing and returned.
