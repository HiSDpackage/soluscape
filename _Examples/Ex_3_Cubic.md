---
layout: single
permalink: /Examples/Ex_3_Cubic
title: "Example 3 : Cubic"
sidebar:
    nav: Examples
toc: true
toc_sticky: true
mathjax: true

---

```python
import sys
import os

# 将 code 文件夹添加到系统路径中
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'depart-code')))

```


```python
import Landscape
import numpy as np

# import packages needed
```

We can use the grad function that is either explicitly given by user or got by automatically derivating.

We test the example whose energy function is shown by 
\begin{aligned}
E(x)=\sum_{j=1}^{n}j(x_{j}^{2}-1)^{2}.
\end{aligned}

In particular,we take $n=3$.It is obvious that there are 27 saddle points 
$$
(a,b,c),a,b,c \in \{-1,0,1\}
$$
who happen to be the vertices, face centers, and body center of a cube.

```python
energyfunction=""
for i in range(3):
    energyfunction+=str(i+1)+"*(x"+str(i+1)+"**2-1)**2+"
energyfunction=energyfunction[:-1]
```


```python
print(energyfunction)
# given energy function
```

    1*(x1**2-1)**2+2*(x2**2-1)**2+3*(x3**2-1)**2
    


```python
# parameter initialization
x0 = np.array([0 for i in range(3)]) # initial point
dt = 1e-3 # time step
k = 3 # the index of expected saddle point
acceme = 'nesterov'
neschoice = 2
nesres = 100
mom = 0.8
maxiter = 1000 # max iter
```


```python
MyLandscape = Landscape.Landscape(MaxIndex=k, WhetherAutoGrad=True, EnergyFunction=energyfunction, InitialPoint=x0, TimeStep=dt, AccelerateMethod=acceme, CombinationOrder='all',
                    EigenMethod='euler',WhetherBBStep=False, NesterovChoice=neschoice, NesterovRestart=nesres, Momentum=mom, MaxIter=maxiter, WhetherReport=True, PrintStepInterval=100, MaxIterOfCalEigen=10, PerturbationLength=1e-2)
# Instantiation
MyLandscape.run()
# Calculate
```

    Parameters of HiSD solver:
    According to the dimension if the 'InitialPoint' parameter, the 'Dim'parameter was automatically set as 3.
    The 'InexactGrad' parameter was not passed in. Default value False was used.
    The 'DimerLength' parameter was not passed in. Default value 1e-05 was used.
    The 'Tolerance' parameter was not passed in. Default value 1e-06 was used.
    The 'SearchArea' parameter was not passed in. Default value 1000.0 was used.
    The 'LOfCalEigen' parameter was not passed in. Default value 1e-05 was used.
    The 'DSOfEuler' parameter was not passed in. Default value 1e-05 was used.
    The 'ExactHessian' parameter was not passed in. Default value False was used.
    The system is a gradient system, where HiOSD is used!
    Parameters of Landscape:
    The 'SameJudgementMethod' parameter was not passed in. Default value <function LandscapeCheckParam.<locals>.<lambda> at 0x000001A94C813380> was used
    The 'PerturbationMethod' parameter was not passed in. Default value uniform was used
    The 'InitialEigenVectors' parameter was not passed in. Default value None was used
    The 'PerturbationNumber' parameter was not passed in. Default value 2 was used
    The 'WhetherSaveDetail' parameter was not passed in. Default value True was used
    The 'MaxSearchGapOfIndex' parameter was not passed in. Default value 1 was used
    Iteration: 100|| Norm of gradient: 0.000395
    Iteration: 200|| Norm of gradient: 0.000011
    The index of the final saddle point is 3.
    Iteration: 100|| Norm of gradient: 0.701095
    Iteration: 200|| Norm of gradient: 0.120058
    Iteration: 300|| Norm of gradient: 0.002034
    Iteration: 400|| Norm of gradient: 0.000060
    The index of the final saddle point is 2.
    Iteration: 100|| Norm of gradient: 0.701121
    Iteration: 200|| Norm of gradient: 0.120000
    Iteration: 300|| Norm of gradient: 0.002032
    Iteration: 400|| Norm of gradient: 0.000059
    The index of the final saddle point is 2.
    Iteration: 100|| Norm of gradient: 0.877872
    Iteration: 200|| Norm of gradient: 0.157527
    Iteration: 300|| Norm of gradient: 0.006545
    Iteration: 400|| Norm of gradient: 0.000194
    The index of the final saddle point is 2.
    Iteration: 100|| Norm of gradient: 0.877896
    Iteration: 200|| Norm of gradient: 0.157552
    Iteration: 300|| Norm of gradient: 0.006546
    Iteration: 400|| Norm of gradient: 0.000194
    The index of the final saddle point is 2.
    Iteration: 100|| Norm of gradient: 3.268317
    Iteration: 200|| Norm of gradient: 0.001273
    Iteration: 300|| Norm of gradient: 0.000014
    The index of the final saddle point is 2.
    Iteration: 100|| Norm of gradient: 3.268640
    Iteration: 200|| Norm of gradient: 0.001272
    Iteration: 300|| Norm of gradient: 0.000014
    The index of the final saddle point is 2.
    Iteration: 100|| Norm of gradient: 2.725669
    Iteration: 200|| Norm of gradient: 0.289363
    Iteration: 300|| Norm of gradient: 0.000828
    The index of the final saddle point is 2.
    Iteration: 100|| Norm of gradient: 2.725944
    Iteration: 200|| Norm of gradient: 0.289275
    Iteration: 300|| Norm of gradient: 0.000828
    The index of the final saddle point is 2.
    Iteration: 100|| Norm of gradient: 2.721569
    Iteration: 200|| Norm of gradient: 0.019025
    Iteration: 300|| Norm of gradient: 0.000049
    The index of the final saddle point is 2.
    Iteration: 100|| Norm of gradient: 2.721581
    Iteration: 200|| Norm of gradient: 0.019025
    Iteration: 300|| Norm of gradient: 0.000049
    The index of the final saddle point is 2.
    Iteration: 100|| Norm of gradient: 2.739767
    Iteration: 200|| Norm of gradient: 0.018057
    Iteration: 300|| Norm of gradient: 0.000046
    The index of the final saddle point is 2.
    Iteration: 100|| Norm of gradient: 2.739761
    Iteration: 200|| Norm of gradient: 0.018057
    Iteration: 300|| Norm of gradient: 0.000046
    The index of the final saddle point is 2.
    Iteration: 100|| Norm of gradient: 0.002719
    Iteration: 200|| Norm of gradient: 0.002087
    Iteration: 300|| Norm of gradient: 0.000004
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.002773
    Iteration: 200|| Norm of gradient: 0.002087
    Iteration: 300|| Norm of gradient: 0.000004
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.295569
    Iteration: 200|| Norm of gradient: 0.000059
    Iteration: 300|| Norm of gradient: 0.000019
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.295569
    Iteration: 200|| Norm of gradient: 0.000059
    Iteration: 300|| Norm of gradient: 0.000019
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 2.780811
    Iteration: 200|| Norm of gradient: 0.019182
    Iteration: 300|| Norm of gradient: 0.000049
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 2.780811
    Iteration: 200|| Norm of gradient: 0.019182
    Iteration: 300|| Norm of gradient: 0.000049
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.179886
    Iteration: 200|| Norm of gradient: 0.005256
    Iteration: 300|| Norm of gradient: 0.000007
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.179885
    Iteration: 200|| Norm of gradient: 0.005256
    Iteration: 300|| Norm of gradient: 0.000007
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.904058
    Iteration: 200|| Norm of gradient: 0.001211
    Iteration: 300|| Norm of gradient: 0.000026
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.904058
    Iteration: 200|| Norm of gradient: 0.001211
    Iteration: 300|| Norm of gradient: 0.000026
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 3.280491
    Iteration: 200|| Norm of gradient: 0.001255
    Iteration: 300|| Norm of gradient: 0.000014
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 3.280491
    Iteration: 200|| Norm of gradient: 0.001255
    Iteration: 300|| Norm of gradient: 0.000014
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.589843
    Iteration: 200|| Norm of gradient: 0.081793
    Iteration: 300|| Norm of gradient: 0.000241
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.589844
    Iteration: 200|| Norm of gradient: 0.081793
    Iteration: 300|| Norm of gradient: 0.000241
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 2.688805
    Iteration: 200|| Norm of gradient: 0.018770
    Iteration: 300|| Norm of gradient: 0.000048
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 2.688805
    Iteration: 200|| Norm of gradient: 0.018770
    Iteration: 300|| Norm of gradient: 0.000048
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.868501
    Iteration: 200|| Norm of gradient: 0.147571
    Iteration: 300|| Norm of gradient: 0.006210
    Iteration: 400|| Norm of gradient: 0.000184
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.868492
    Iteration: 200|| Norm of gradient: 0.147562
    Iteration: 300|| Norm of gradient: 0.006210
    Iteration: 400|| Norm of gradient: 0.000184
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.684715
    Iteration: 200|| Norm of gradient: 0.157768
    Iteration: 300|| Norm of gradient: 0.003081
    Iteration: 400|| Norm of gradient: 0.000090
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.684724
    Iteration: 200|| Norm of gradient: 0.157745
    Iteration: 300|| Norm of gradient: 0.003080
    Iteration: 400|| Norm of gradient: 0.000090
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 2.197188
    Iteration: 200|| Norm of gradient: 0.003147
    Iteration: 300|| Norm of gradient: 0.000005
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 2.196980
    Iteration: 200|| Norm of gradient: 0.003147
    Iteration: 300|| Norm of gradient: 0.000005
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.315054
    Iteration: 200|| Norm of gradient: 0.001110
    Iteration: 300|| Norm of gradient: 0.000003
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.315184
    Iteration: 200|| Norm of gradient: 0.001109
    Iteration: 300|| Norm of gradient: 0.000003
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.440856
    Iteration: 200|| Norm of gradient: 1.095665
    Iteration: 300|| Norm of gradient: 0.022467
    Iteration: 400|| Norm of gradient: 0.000645
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.440866
    Iteration: 200|| Norm of gradient: 1.095609
    Iteration: 300|| Norm of gradient: 0.022466
    Iteration: 400|| Norm of gradient: 0.000645
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.023779
    Iteration: 200|| Norm of gradient: 0.861559
    Iteration: 300|| Norm of gradient: 0.139916
    Iteration: 400|| Norm of gradient: 0.005954
    Iteration: 500|| Norm of gradient: 0.000176
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.023768
    Iteration: 200|| Norm of gradient: 0.861217
    Iteration: 300|| Norm of gradient: 0.139532
    Iteration: 400|| Norm of gradient: 0.005941
    Iteration: 500|| Norm of gradient: 0.000176
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 1.380389
    Iteration: 200|| Norm of gradient: 0.008586
    Iteration: 300|| Norm of gradient: 0.000021
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 1.380449
    Iteration: 200|| Norm of gradient: 0.008586
    Iteration: 300|| Norm of gradient: 0.000021
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 2.730959
    Iteration: 200|| Norm of gradient: 0.017894
    Iteration: 300|| Norm of gradient: 0.000046
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 2.730956
    Iteration: 200|| Norm of gradient: 0.017894
    Iteration: 300|| Norm of gradient: 0.000046
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.916281
    Iteration: 200|| Norm of gradient: 0.194075
    Iteration: 300|| Norm of gradient: 0.007791
    Iteration: 400|| Norm of gradient: 0.000231
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.916277
    Iteration: 200|| Norm of gradient: 0.194072
    Iteration: 300|| Norm of gradient: 0.007791
    Iteration: 400|| Norm of gradient: 0.000231
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 1.048388
    Iteration: 200|| Norm of gradient: 0.276708
    Iteration: 300|| Norm of gradient: 0.010658
    Iteration: 400|| Norm of gradient: 0.000317
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 1.048392
    Iteration: 200|| Norm of gradient: 0.276710
    Iteration: 300|| Norm of gradient: 0.010658
    Iteration: 400|| Norm of gradient: 0.000317
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.623079
    Iteration: 200|| Norm of gradient: 0.002975
    Iteration: 300|| Norm of gradient: 0.000003
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 0.622542
    Iteration: 200|| Norm of gradient: 0.002974
    Iteration: 300|| Norm of gradient: 0.000003
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.501653
    Iteration: 200|| Norm of gradient: 0.000391
    Iteration: 300|| Norm of gradient: 0.000021
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.501557
    Iteration: 200|| Norm of gradient: 0.000391
    Iteration: 300|| Norm of gradient: 0.000021
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 1.165185
    Iteration: 200|| Norm of gradient: 0.308240
    Iteration: 300|| Norm of gradient: 0.011670
    Iteration: 400|| Norm of gradient: 0.000347
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 1.165188
    Iteration: 200|| Norm of gradient: 0.308240
    Iteration: 300|| Norm of gradient: 0.011670
    Iteration: 400|| Norm of gradient: 0.000347
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 1.159273
    Iteration: 200|| Norm of gradient: 0.307386
    Iteration: 300|| Norm of gradient: 0.011648
    Iteration: 400|| Norm of gradient: 0.000347
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 1.159269
    Iteration: 200|| Norm of gradient: 0.307386
    Iteration: 300|| Norm of gradient: 0.011648
    Iteration: 400|| Norm of gradient: 0.000347
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.807076
    Iteration: 200|| Norm of gradient: 0.001121
    Iteration: 300|| Norm of gradient: 0.000025
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.807006
    Iteration: 200|| Norm of gradient: 0.001121
    Iteration: 300|| Norm of gradient: 0.000025
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.065040
    Iteration: 200|| Norm of gradient: 0.000060
    Iteration: 300|| Norm of gradient: 0.000020
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 4.065279
    Iteration: 200|| Norm of gradient: 0.000059
    Iteration: 300|| Norm of gradient: 0.000020
    The index of the final saddle point is 1.
    Iteration: 100|| Norm of gradient: 2.766616
    Iteration: 200|| Norm of gradient: 0.019271
    Iteration: 300|| Norm of gradient: 0.000049
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 2.766614
    Iteration: 200|| Norm of gradient: 0.019271
    Iteration: 300|| Norm of gradient: 0.000049
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 1.024766
    Iteration: 200|| Norm of gradient: 0.000853
    Iteration: 300|| Norm of gradient: 0.000002
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 1.024867
    Iteration: 200|| Norm of gradient: 0.000853
    Iteration: 300|| Norm of gradient: 0.000002
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 6.566227
    Iteration: 200|| Norm of gradient: 0.006036
    Iteration: 300|| Norm of gradient: 0.000005
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 6.566048
    Iteration: 200|| Norm of gradient: 0.006036
    Iteration: 300|| Norm of gradient: 0.000005
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 2.636209
    Iteration: 200|| Norm of gradient: 0.018319
    Iteration: 300|| Norm of gradient: 0.000047
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 2.636203
    Iteration: 200|| Norm of gradient: 0.018319
    Iteration: 300|| Norm of gradient: 0.000047
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 4.829368
    Iteration: 200|| Norm of gradient: 0.001012
    Iteration: 300|| Norm of gradient: 0.000024
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 4.829331
    Iteration: 200|| Norm of gradient: 0.001012
    Iteration: 300|| Norm of gradient: 0.000024
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.477830
    Iteration: 200|| Norm of gradient: 0.000678
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.477426
    Iteration: 200|| Norm of gradient: 0.000679
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.805443
    Iteration: 200|| Norm of gradient: 0.000834
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.805840
    Iteration: 200|| Norm of gradient: 0.000836
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.782120
    Iteration: 200|| Norm of gradient: 0.003076
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.782517
    Iteration: 200|| Norm of gradient: 0.003076
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 1.907968
    Iteration: 200|| Norm of gradient: 0.012136
    Iteration: 300|| Norm of gradient: 0.000030
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 1.907948
    Iteration: 200|| Norm of gradient: 0.012136
    Iteration: 300|| Norm of gradient: 0.000030
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 2.778848
    Iteration: 200|| Norm of gradient: 0.019234
    Iteration: 300|| Norm of gradient: 0.000049
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 2.778848
    Iteration: 200|| Norm of gradient: 0.019234
    Iteration: 300|| Norm of gradient: 0.000049
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 2.587761
    Iteration: 200|| Norm of gradient: 0.015679
    Iteration: 300|| Norm of gradient: 0.000039
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 2.587758
    Iteration: 200|| Norm of gradient: 0.015679
    Iteration: 300|| Norm of gradient: 0.000039
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 2.169712
    Iteration: 200|| Norm of gradient: 0.014199
    Iteration: 300|| Norm of gradient: 0.000036
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 2.169727
    Iteration: 200|| Norm of gradient: 0.014199
    Iteration: 300|| Norm of gradient: 0.000036
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 1.962455
    Iteration: 200|| Norm of gradient: 0.002801
    Iteration: 300|| Norm of gradient: 0.000004
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 1.962431
    Iteration: 200|| Norm of gradient: 0.002801
    Iteration: 300|| Norm of gradient: 0.000004
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.300847
    Iteration: 200|| Norm of gradient: 0.001295
    Iteration: 300|| Norm of gradient: 0.000004
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.300875
    Iteration: 200|| Norm of gradient: 0.001295
    Iteration: 300|| Norm of gradient: 0.000004
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 4.706741
    Iteration: 200|| Norm of gradient: 0.000764
    Iteration: 300|| Norm of gradient: 0.000023
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 4.706737
    Iteration: 200|| Norm of gradient: 0.000764
    Iteration: 300|| Norm of gradient: 0.000023
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 1.828485
    Iteration: 200|| Norm of gradient: 0.010902
    Iteration: 300|| Norm of gradient: 0.000024
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 1.828462
    Iteration: 200|| Norm of gradient: 0.010902
    Iteration: 300|| Norm of gradient: 0.000024
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.291017
    Iteration: 200|| Norm of gradient: 1.803351
    Iteration: 300|| Norm of gradient: 0.032055
    Iteration: 400|| Norm of gradient: 0.000908
    Iteration: 500|| Norm of gradient: 0.000027
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.290963
    Iteration: 200|| Norm of gradient: 1.803435
    Iteration: 300|| Norm of gradient: 0.032057
    Iteration: 400|| Norm of gradient: 0.000908
    Iteration: 500|| Norm of gradient: 0.000027
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.746530
    Iteration: 200|| Norm of gradient: 0.027787
    Iteration: 300|| Norm of gradient: 0.000643
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.746578
    Iteration: 200|| Norm of gradient: 0.027698
    Iteration: 300|| Norm of gradient: 0.000645
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.852403
    Iteration: 200|| Norm of gradient: 0.129442
    Iteration: 300|| Norm of gradient: 0.005605
    Iteration: 400|| Norm of gradient: 0.000166
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.852358
    Iteration: 200|| Norm of gradient: 0.129388
    Iteration: 300|| Norm of gradient: 0.005603
    Iteration: 400|| Norm of gradient: 0.000166
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.954207
    Iteration: 200|| Norm of gradient: 0.224059
    Iteration: 300|| Norm of gradient: 0.008828
    Iteration: 400|| Norm of gradient: 0.000262
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.954250
    Iteration: 200|| Norm of gradient: 0.224089
    Iteration: 300|| Norm of gradient: 0.008829
    Iteration: 400|| Norm of gradient: 0.000262
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.551281
    Iteration: 200|| Norm of gradient: 0.574350
    Iteration: 300|| Norm of gradient: 0.013067
    Iteration: 400|| Norm of gradient: 0.000379
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.551300
    Iteration: 200|| Norm of gradient: 0.574275
    Iteration: 300|| Norm of gradient: 0.013066
    Iteration: 400|| Norm of gradient: 0.000379
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.709032
    Iteration: 200|| Norm of gradient: 0.102666
    Iteration: 300|| Norm of gradient: 0.001542
    Iteration: 400|| Norm of gradient: 0.000045
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.709014
    Iteration: 200|| Norm of gradient: 0.102704
    Iteration: 300|| Norm of gradient: 0.001543
    Iteration: 400|| Norm of gradient: 0.000045
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 1.053011
    Iteration: 200|| Norm of gradient: 0.278600
    Iteration: 300|| Norm of gradient: 0.010722
    Iteration: 400|| Norm of gradient: 0.000319
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 1.053026
    Iteration: 200|| Norm of gradient: 0.278606
    Iteration: 300|| Norm of gradient: 0.010723
    Iteration: 400|| Norm of gradient: 0.000319
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.048091
    Iteration: 200|| Norm of gradient: 1.430324
    Iteration: 300|| Norm of gradient: 0.279419
    Iteration: 400|| Norm of gradient: 0.010008
    Iteration: 500|| Norm of gradient: 0.000297
    The index of the final saddle point is 0.
    Iteration: 100|| Norm of gradient: 0.048110
    Iteration: 200|| Norm of gradient: 1.430601
    Iteration: 300|| Norm of gradient: 0.279316
    Iteration: 400|| Norm of gradient: 0.010003
    Iteration: 500|| Norm of gradient: 0.000297
    The index of the final saddle point is 0.
    


```python
MyLandscape.DrawHeatmap(ContourGridNum=100, ContourGridOut=25)
# Draw the search path. But because of the large dimension, we cannot draw the picture.
```

    Sorry! The dimension is larger than 2, where we cannot draw the search path. You can use the method 'DrawConnection' instead.
    


```python
MyLandscape.DrawConnection()
# Draw the decline curve of the norm of gradient vector
MyLandscape.Save('Ex_Cubic','mat')
# Save the output
```


    
![png](Ex_3_Cubic_files/Ex_3_Cubic_9_0.png)
    



```python
print(MyLandscape.SaddleList)
```

    [[0, array([[ 9.81789306e-08],
           [-9.27213960e-08],
           [-4.33256560e-08]]), 3, array([[0., 0., 1.],
           [0., 1., 0.],
           [1., 0., 0.]]), [-1]], [1, array([[-1.00000003e+00],
           [ 2.25233199e-11],
           [-9.56127846e-11]]), 2, array([[0., 0.],
           [0., 1.],
           [1., 0.]]), [0]], [2, array([[ 1.00000003e+00],
           [-2.25238389e-11],
           [ 9.56151990e-11]]), 2, array([[0., 0.],
           [0., 1.],
           [1., 0.]]), [0]], [3, array([[2.15484723e-08],
           [9.99999982e-01],
           [4.17281426e-09]]), 2, array([[0., 1.],
           [0., 0.],
           [1., 0.]]), [0]], [4, array([[-2.15477469e-08],
           [-9.99999982e-01],
           [-4.17276938e-09]]), 2, array([[0., 1.],
           [0., 0.],
           [1., 0.]]), [0]], [5, array([[ 8.96205925e-08],
           [-5.95856044e-08],
           [ 9.99999999e-01]]), 2, array([[0., 1.],
           [1., 0.],
           [0., 0.]]), [0]], [6, array([[-8.96250031e-08],
           [ 5.95833102e-08],
           [-9.99999999e-01]]), 2, array([[0., 1.],
           [1., 0.],
           [0., 0.]]), [0]], [7, array([[-9.99999923e-01],
           [-1.00000000e+00],
           [-5.62237496e-12]]), 1, array([[0.],
           [0.],
           [1.]]), [1, 4]], [8, array([[-1.00000004e+00],
           [ 1.00000000e+00],
           [-2.39884630e-10]]), 1, array([[0.],
           [0.],
           [1.]]), [1, 3]], [9, array([[-9.99999945e-01],
           [-6.11664592e-12],
           [ 1.00000000e+00]]), 1, array([[0.],
           [1.],
           [0.]]), [1, 5]], [10, array([[-9.99999940e-01],
           [ 4.57144146e-12],
           [-1.00000000e+00]]), 1, array([[0.],
           [1.],
           [0.]]), [1, 6]], [11, array([[ 9.99999923e-01],
           [-1.00000000e+00],
           [ 5.62240332e-12]]), 1, array([[0.],
           [0.],
           [1.]]), [2, 4]], [12, array([[1.00000004e+00],
           [1.00000000e+00],
           [2.39885856e-10]]), 1, array([[0.],
           [0.],
           [1.]]), [2, 3]], [13, array([[9.99999945e-01],
           [6.11686981e-12],
           [1.00000000e+00]]), 1, array([[0.],
           [1.],
           [0.]]), [2, 5]], [14, array([[ 9.99999940e-01],
           [-4.57166535e-12],
           [-1.00000000e+00]]), 1, array([[0.],
           [1.],
           [0.]]), [2, 6]], [15, array([[4.58516730e-08],
           [9.99999963e-01],
           [1.00000000e+00]]), 1, array([[1.],
           [0.],
           [0.]]), [3, 5]], [16, array([[ 1.28666065e-07],
           [ 9.99999957e-01],
           [-1.00000000e+00]]), 1, array([[1.],
           [0.],
           [0.]]), [3, 6]], [17, array([[ 1.32121070e-07],
           [-1.00000000e+00],
           [-9.99999999e-01]]), 1, array([[1.],
           [0.],
           [0.]]), [4, 6]], [18, array([[-1.32119466e-07],
           [-1.00000000e+00],
           [ 9.99999999e-01]]), 1, array([[1.],
           [0.],
           [0.]]), [4, 5]], [19, array([[-1.00000003],
           [-1.00000002],
           [ 1.        ]]), 0, array([], shape=(3, 0), dtype=float64), [7, 9, 18]], [20, array([[-0.99999999],
           [-1.00000001],
           [-1.        ]]), 0, array([], shape=(3, 0), dtype=float64), [7, 10, 17]], [21, array([[-0.99999997],
           [ 1.00000002],
           [ 1.        ]]), 0, array([], shape=(3, 0), dtype=float64), [8, 9, 15]], [22, array([[-1.00000001],
           [ 1.00000001],
           [-1.        ]]), 0, array([], shape=(3, 0), dtype=float64), [8, 10, 16]], [23, array([[ 0.99999995],
           [-1.        ],
           [ 1.        ]]), 0, array([], shape=(3, 0), dtype=float64), [11, 13, 18]], [24, array([[ 1.00000007],
           [-1.        ],
           [-1.        ]]), 0, array([], shape=(3, 0), dtype=float64), [11, 14, 17]], [25, array([[1.00000007],
           [1.        ],
           [1.        ]]), 0, array([], shape=(3, 0), dtype=float64), [12, 13, 15]], [26, array([[ 0.99999993],
           [ 1.        ],
           [-1.        ]]), 0, array([], shape=(3, 0), dtype=float64), [12, 14, 16]]]
    
