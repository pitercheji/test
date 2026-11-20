import numpy as np
import matplotlib.pyplot as plt
rng=np.random.default_rng(2024)
N=100,000

foundation=rng.triangular(5,8,15, N)
structure=rng.triangular(10,14,25,N)
finishing=rng.triangular(3,5,10,N)

total=foundation+structure+finishing
deadline=35
p_over=np.mean(total>deadline)

print(f"mean duration: {total.mean():.2f} days")
print(f"P90 duration: {np.percentile(total, 90):.2f} days")
print(f"P(project>{deadline} d) = {p_over:.4%}")

running=np.cumsum(total>deadline)/np.arrange(1, N+1)
idx=np.unique(np.logspace(1,np.log10(N),200).astype(int))-1

plt.semilogx(idx+1,running[idx])
plt.axhline(p_over,color='r',ls='--',label=f"final ={p_over:.3f}")
plt.xlabel("simulations")
plt.ylabel("estimated P(overrun)")
plt.title("monte carlo estimate of project overrun risk")
plt.legend()
plt.grid(True)
plt.show()