1. **What are the main motivations for reducing a dataset’s dimensionality? What are the main drawbacks?**

Advantages:
- Mitigating the Curse of Dimensionality
- Reducing overfitting
- Reduce Computational Cost
- Enabling Data Visualization

Disadvantages:
- information lost.
- reduce Interpretability.
- Additional Computational Cost
- Potential Performance Degradation


2. **What is the curse of dimensionality?**
با افزایش تعداد ابعاد، حجم فضای ویژگی ها به سرعت افزایش می یابد، بنابراین برای پوشش مناسب این فضا با تراکم یا دقت مشخص به تعداد بسیار بیشتری نمونه لازم داریم ، این افزایش در حالت کلی نمایی است.

3. **Once a dataset’s dimensionality has been reduced, is it possible to reverse the operation? If so, how? If not, why?**
بله، در برخی روش‌های کاهش ابعاد می‌توان با استفاده از Inverse Transformation داده‌ها را به فضای اولیه بازسازی کرد؛ اما معمولاً بازسازی دقیق نیست، زیرا بخشی از اطلاعات در فرایند کاهش ابعاد از دست رفته است.


4. **Can PCA be used to reduce the dimensionality of a highly nonlinear dataset?**

برای مجموعه داده های بسیار غیر خطی مناسب نیست، زیرا پیش بینی های خطی را انجام می دهد و نمی تواند به طور موثر ساختارها و روابط غیر خطی پیچیده را در داده ها حفظ کند.

5. **Suppose you perform PCA on a 1,000-dimensional dataset, setting the explained variance ratio to 95%. How many dimensions will the resulting dataset have?**
این وابسته به دیتاست هست و واریانس داده ها.

6. **In what cases would you use regular PCA, incremental PCA, randomized PCA, or random projection?**

regular PCA :
دیتاست به اندازه کافی کوچک باشد که بتونیم داده های آموزشی رو در RAM قرار بدیم یا اینکه محدودیت خاصی از نظر حافظه نداشته باشیم.
incremental PCA :
دیتاست خیلی بزرگ باشه و نشه همش رو یکجا لود کرد توی RAM یا در فرایند Online Learning باشیم که داده ها به تردیجی وارد بشه و در اختیارمون قرار بگیره.

randomized PCA :
جاهایی که تعداد ویژگی بسیار زیاد باشه، بخوایم تعداد کمی از مولفه های اصلی رو استخراج کنیم و سرعت برامون اهمیت داشته باشه.

random projection : 
بخوایم ابعاد داده را با هزینه محاسباتی کم کاهش بدیم، حفظ تقریبی فاصله های بین نمونه ها برایمان مهم باشد، نیازی به پیدا کردن مولفه های اصلی یا بیشترینه کردن Explained Variance نداشته باشیم.


7. **How can you evaluate the performance of a dimensionality reduction algorithm on your dataset?**
بررسی خطای بازسازی یا سنجش عملکرد مدل با PCA و بدون PCA


8. **Does it make any sense to chain two different dimensionality reduction algorithms?**

بله و اتفاقا خیلی هم کاربردی هست مثلا با PCA بیایم و دیتاست رو ابعادش رو مثلا از 10.000 بیاریم روی 50 و بعد با t-SNE ابعادش رو بیاریم روی 2، البته که ممکنه اطلاعات از بین بره ولی همیشه هدف ما حفظ تمام اطلاعات نیست بلکه رسیدن به یک نمایش مناسب برای هدف مورد نظر است.

9. Load the MNIST dataset (introduced in Chapter 3) and split it into a training set and a test set (take the first 60,000 instances for training, and the remaining 10,000 for testing). Train a random forest classifier on the dataset and time how long it takes, then evaluate the resulting model on the test set. Next, use PCA to reduce the dataset’s dimensionality, with an explained variance ratio of 95%. Train a new random forest classifier on the reduced dataset and see how long it takes. Was training much faster? Next, evaluate the classifier on the test set. How does it compare to the previous classifier? Try again with an SGDClassifier. How much does PCA help now?


10. Use t-SNE to reduce the first 5,000 images of the MNIST dataset down to 2 dimensions and plot the result using Matplotlib. You can use a scatterplot using 10 different colors to represent each image’s target class. Alternatively, you can replace each dot in the scatterplot with the corresponding instance’s class (a digit from 0 to 9), or even plot scaled-down versions of the digit images themselves (if you plot all digits the visualization will be too cluttered, so you should either draw a random sample or plot an instance only if no other instance has already been plotted at a close distance). You should get a nice visualization with well-separated clusters of digits. Try using other dimensionality reduction algorithms, such as PCA, LLE, or MDS, and compare the resulting visualizations.