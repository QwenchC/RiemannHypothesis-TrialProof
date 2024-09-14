[**中文简体**](./README.zh-CN.md)
# RiemannHypothesis-TrialProof

This repository contains code and explanations for verifying the non-trivial zeros of the Riemann Zeta Function using numerical methods. Specifically, we use tools like Python and high-precision libraries to explore the distribution of these zeros and provide numerical evidence supporting the Riemann Hypothesis.

## **Theoretical Background**

   The Riemann Zeta Function ζ(s) is defined for complex numbers s with real part greater than 1 as:
   <p align="center">
      $ζ(s) = Σ(1/n^s) for n=1 to infinity$
   </p>
   Through analytic continuation, this function is defined for all s in the complex plane, except for a simple pole at s = 1.

   **The Riemann Hypothesis**

   The Riemann Hypothesis conjectures that all non-trivial zeros of the zeta function lie on the "critical line" where the real part of s is 1/2.

   **Functional Equation**

   The Riemann Zeta Function satisfies the functional equation:
   <p align="center">
      $ζ(s) = 2^sπ^(s - 1)sin(πs / 2)Γ(1 - s)ζ(1 - s)$
   </p>
   where Γ(s) is the gamma function.
   
   **ξ Function and Symmetry**

   To simplify computations, the Riemann ξ function is often used. It is defined as:
   <p align="center">
      $ξ(s) = 1/2s(s - 1)π^(-s/2)Γ(s/2)ζ(s)$
   </p>
   This function has the important property of symmetry:
   <p align="center">
      $ξ(s) = ξ(1 - s)$
   </p>
   The symmetry implies that if ρ is a zero of ξ(s), then 1 - ρ is also a zero. This leads to the conjecture that all non-trivial zeros of ζ(s) lie on the critical line where the real part of s is 1/2.

## **Theoretical calculation**

### **The Riemann-Siegel Formula**
   
The Riemann-Siegel formula is an approximation used to efficiently compute the zeta function near the critical line for large imaginary parts. It is given by:
<p align="center">
   $Z(t) ≈ 2 Σ(cos(θ(t) - tln(n)) / sqrt(n)) for n=1 to N$
</p>
where t is the imaginary part of s, and $N = floor(sqrt(t / (2π)))$.

The Riemann-Siegel theta function θ(t) is defined as:
<p align="center">
   $θ(t) = Im(ln(Γ(1/4 + it/2))) - tln(π) / 2$
</p>
This formula allows for the efficient calculation of the Z function, an essential tool for finding the zeros of ζ(s) along the critical line.

### **Finding Zeros Numerically**

To find the zeros of the Riemann Zeta Function, we follow these steps:

**Choose the range**: Set the range of the imaginary part [T_min, T_max] to search for zeros.

**Evaluate Z(t)**: Compute Z(t) for each t value.

**Detect sign changes**: Identify intervals where Z(t) changes sign, which indicates a zero.

**Refine the zero location**: Use numerical root-finding methods (e.g., bisection, Newton-Raphson) to precisely locate the zeros within the detected intervals.

## **Using High-Precision Libraries**
Given the nature of the calculations (particularly for large t), high-precision floating-point arithmetic is required to avoid numerical instability. Libraries like mpmath in Python provide the necessary tools to perform these high-precision computations.

**Key Numerical Libraries**

**mpmath**: A Python library for high-precision arithmetic.

**SageMath**: A powerful open-source mathematics system that includes tools for high-precision computations.

**Mathematica**: A proprietary system capable of handling high-precision calculations and built-in support for the zeta function.

## **Existing Numerical Results**
Numerical verification of the Riemann Hypothesis has been performed up to very high values of t:

**Low-lying zeros**: The first few thousand zeros have been precisely computed and all lie on the critical line.

**High zeros**: Through the work of mathematicians like Andrew Odlyzko, non-trivial zeros up to the order of 10^13 have been numerically verified to lie on the critical line.

## **Example Workflow**
**Set up precision**: Configure the precision of the computations (e.g., using mpmath.mp.dps for decimal places).

**Calculate Z function**: Evaluate Z(t) across a chosen range of t values.

**Find zeros**: Detect sign changes in Z(t), then refine the location of the zeros using numerical methods.

**Analyze results**: Study the distribution and statistical properties of the zeros, comparing them with predictions from random matrix theory.

## **Challenges and Limitations**
**Computational resources**: Verifying high zeros requires significant computational power and storage.

**Numerical accuracy**: Careful attention must be paid to numerical errors, especially for high zeros.

**Limited verification**: While millions of zeros can be verified, the hypothesis remains unproven for all non-trivial zeros.

## **Further Reading and Resources**
**Andrew Odlyzko's research**: Odlyzko has performed extensive numerical calculations of the zeros of the Riemann zeta function. His results can be found on his website: http://www.dtc.umn.edu/~odlyzko/

**The Riemann Hypothesis**: Several books and papers provide an excellent introduction to the problem and its importance in number theory.

**Random Matrix Theory**: Study the connection between the statistical properties of zeta function zeros and random matrix theory.

#  Result Analysis
```
D:\...\RiemannHypothesis-TrialProof\python.exe E:\programs\RiemannHypothesis-TrialProof\main.py 
Found zero at t = 14.134725141734693790457251983562470270784257115699
Found zero at t = 21.022039638771554992628479593896902777334340524903
Found zero at t = 25.010857580145688763213790992562821818659549672558
Found zero at t = 30.424876125859513210311897530584091320181560023715
Found zero at t = 32.935061587739189690662368964074903488812715603517
Found zero at t = 37.586178158825671257217763480705332821405597350831
Found zero at t = 40.918719012147495187398126914633254395726165962777
Found zero at t = 43.327073280914999519496122165406805782645668371837
Found zero at t = 48.005150881167159727942472749427516041686844001144
Found zero at t = 49.773832477672302181916784678563724057723178299677

进程已结束，退出代码为 0
```
## What does that mean?
Our program successfully found the first ten **non-trivial zeros** of the Riemann zeta function on the **critical line** (Re(s)=1/2). These zeros are located at the imaginary part t values of the zeta function, where &ζ(1/2+it)=0&.
Each output zero represents the fact that the zeta function is zero at a specific imaginary part t value, i.e.:
1. **t = 14.134725...**

    This means $ζ(1/2+14.134725i)=0$
2. **t = 21.022039...**

    This means $ζ(1/2+21.022039i)=0$
3. **t = 25.010857...**

    This means $ζ(1/2+25.010857i)=0$

And so on, our program finds the non-trivial zero of the zeta function in the imaginary part interval [0,50].
