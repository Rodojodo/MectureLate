# Lecture 4: More Asymptotics - $O, \Omega$, and $\Theta$

## 1. Introduction and Function Hierarchy
Asymptotic notation is used to place the growth rates of runtime functions (like $T(n)$) on an absolute scale to compare algorithms regardless of implementation details.

### The Hierarchy of "Simple" Functions
In order of increasing growth rate:
1. **$1$**: Constant
2. **$\lg n$**: Logarithmic
3. **$\sqrt{n}$**: Square root
4. **$n$**: Linear
5. **$n \lg n$**: Log-linear
6. **$n^2$**: Quadratic
7. **$n^3$**: Cubic
8. **$2^n$**: Exponential
9. **$2^{2^n}$**: Double Exponential

**Rule of Thumb:** In this list, if $f$ appears before $g$, then $f \in o(g)$ (i.e., $f$ grows strictly slower than $g$).

---

## 2. Big $O$ Notation (Asymptotic Upper Bound)
**Spirit:** We only care about behavior "in the limit" (large $n$). Constant scaling factors are ignored.

### Formal Definition
$f$ is $O(g)$ if $f$ is eventually bounded above by some multiple of $g$:
$$\exists C > 0, \exists N, \forall n \ge N : f(n) \le C \cdot g(n)$$

### Properties and Proofs
*   **Dominant Terms:** In a polynomial, the term with the highest power is the "dominant" term; others are "small change."
    *   *Example:* $f(n) = 3n + \sqrt{n}$. To prove $f(n) = O(n)$, take $C=4, N=1$. Since $\sqrt{n} \le n$ for $n \ge 1$, then $3n + \sqrt{n} \le 4n$.
*   **Freedom of Choice:** There is no single "correct" $C$ or $N$. If you pick a larger $C$, you can often use a smaller $N$.
*   **Tightness:** $O$ provides an upper bound, but it doesn't have to be tight.
    *   *Example:* $n^2$ is $O(n^2)$ (tight), but $n^2$ is also $O(n^3)$ (not tight).
*   **The Exponent Trap:** Constant factors in exponents **do matter**.
    *   *Example:* $2^{2n}$ is **NOT** $O(2^n)$.
    *   *Reason:* The ratio $\frac{2^{2n}}{2^n} = 2^n$, which tends to $\infty$ as $n \to \infty$. It will eventually exceed any constant $C$.
*   **Logarithm Power Rule:** $\lg(n^k) = O(\lg n)$ because $\lg(n^k) = k \lg n$, which is just a constant multiple.

---

## 3. Big $\Omega$ Notation (Asymptotic Lower Bound)
**Spirit:** Dual to Big $O$. It represents the "best case" or the minimum growth rate.

### Formal Definition
$f$ is $\Omega(g)$ if $f$ is eventually bounded below by some multiple of $g$:
$$\exists c > 0, \exists N, \forall n \ge N : c \cdot g(n) \le f(n)$$

### Key Relation
$$f = \Omega(g) \iff g = O(f)$$

*   **Example Proof:** Show $n - \sqrt{n}$ is $\Omega(n)$.
    *   Take $c = 1/2, N = 4$.
    *   For $n \ge 4$, $\sqrt{n} \le n/2$.
    *   Therefore, $n - \sqrt{n} \ge n - n/2 = n/2 = cn$.

---

## 4. Big $\Theta$ Notation (Asymptotically Tight Bound)
**Spirit:** Captures the idea that $f$ and $g$ have the "same essential growth rate."

### Formal Definition
$f$ is $\Theta(g)$ if $f$ is both $O(g)$ and $\Omega(g)$.
Equivalently:
$$\exists c_1, c_2 > 0, \exists N, \forall n \ge N : c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n)$$

### Essential Properties
*   **Symmetry:** $f = \Theta(g) \iff g = \Theta(f)$.
*   **Simplification:** To find a "simple" $g$ for $f = \Theta(g)$, identify the dominant term and drop the coefficients.
    *   *Example:* $f(n) = 3n^2 - 2n + 19 \implies f(n) = \Theta(n^2)$.
    *   *Example:* $f(n) = 5 - 4/n \implies f(n) = \Theta(1)$ (The $4/n$ term vanishes as $n$ grows).

### The Harmonic Series (Harder Example)
The function $f(n) = \sum_{i=1}^{n} \frac{1}{i}$ is $\Theta(\ln n)$.
*   This is useful because the sum is hard to compute exactly, but its growth rate is easily estimated using the integral $\int_{1}^{n} \frac{1}{x} dx$.
*   **Note:** $\Theta(\ln n)$ is the same as $\Theta(\lg n)$ because they differ only by a constant factor ($\ln n = \frac{\lg n}{\lg e}$).

---

## 5. Summary Table: The "Gang of Five" Relations
Thinking of growth rates like numbers, we can use these loose analogies:

| Notation | Analogy | Meaning |
| :--- | :--- | :--- |
| $f = o(g)$ | $f < g$ | $f$ grows strictly slower than $g$ |
| $f = O(g)$ | $f \le g$ | $f$ grows no faster than $g$ (Upper bound) |
| $f = \Omega(g)$ | $f \ge g$ | $f$ grows no slower than $g$ (Lower bound) |
| $f = \Theta(g)$ | $f = g$ | $f$ has the same growth rate (Tight bound) |
| $f = \omega(g)$ | $f > g$ | $f$ grows strictly faster than $g$ |

---

## 6. Significance for Algorithms
Asymptotic notation allows us to abstract away from implementation detail (hardware, compiler, language).
*   All reasonable implementations of **MergeSort** will have a runtime $T(n) = \Theta(n \lg n)$.
*   All reasonable implementations of **InsertionSort** (worst case) will have a runtime $T(n) = \Theta(n^2)$.

### Common Growth Rate Names
*   $\Theta(1)$: Constant time
*   $\Theta(\lg n)$: Logarithmic time
*   $\Theta(n)$: Linear time
*   $\Theta(n \lg n)$: Log-linear time
*   $\Theta(n^2)$: Quadratic time
*   $\Theta(n^k)$: Polynomial time
*   $\Theta(b^n)$: Exponential time