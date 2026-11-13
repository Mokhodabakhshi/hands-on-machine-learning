1. **Which linear regression training algorithm can you use if you have a training set with millions of features?**

الگوریتم Stochastic Gradient Descent یا Mini-Batch Stochastic Gradient Descent.

2. **Suppose the features in your training set have very different scales. Which algorithms might suffer from this, and how? What can you do about it?**
الگوریتم GD و مشتقات چون تابعی که میخوان خطاش رو minimum کنن خیلی باز میشه یا به بیان دیگر بیضی هاش خیلی کشیده میشه و برای اینکه بهینه بشه خیلی نوسان میکنه.
راه حل: استفاده از scaler ها مثل Standard scaler یا MinMaxScaler

3. **Can gradient descent get stuck in a local minimum when training a logistic regression model?**
خیر چون تابع هزینه logistic regression یک تابع convex هست.

4. **Do all gradient descent algorithms lead to the same model, provided you let them run long enough?**
خیر این بستگی به چندین مورد دارد:
- مقدار learning rate
- مقیاس داده ها
اگر learning rate زیاد باشه با وجود epoch های زیاد ممکنه به نقطه بهینه نرسه و نوسان بکنه.
اگر تابع هزینه محدب باشد و الگوریتم‌ها با شرایط مناسب همگرا شوند، می‌توانند به یک مینیمم سراسری برسند.
اما لزوماً وزن‌های نهایی یکسان نیستند؛ مخصوصاً اگر چند جواب بهینه وجود داشته باشد.


5. **Suppose you use batch gradient descent and you plot the validation error at every epoch. If you notice that the validation error consistently goes up, what is likely going on? How can you fix this?**
مدل overfit شده و قابلیت تعمیم مقادیر رو به درستی نداره.
راه حل : استفاده از مدلی با پیچیدگی کمتر.


6. **Is it a good idea to stop mini-batch gradient descent immediately when the validation error goes up?**
در Mini-batch Gradient Descent به دلیل تصادفی بودن Batchها، ممکن است Validation Error در یک Epoch کمی افزایش پیدا کند و در Epoch بعدی دوباره کاهش یابد.

7. **Which gradient descent algorithm (among those we discussed) will reach the vicinity of the optimal solution the fastest? Which will actually converge? How can you make the others converge as well?**

fastest -> stochastic gradient descent
actually converge -> Batch Gradient Descent with suitable learning rate
How to make others converge -> Learning Rate Schedule

8. **Suppose you are using polynomial regression. You plot the learning curves and you notice that there is a large gap between the training error and the validation error. What is happening? What are three ways to solve this?**

overfitting

راه حل ها:
- استفاده از regularization
- افزایش نمونه ها 
- تکنیک data augmentation
- ساده تر کردن مدل

9. **Suppose you are using ridge regression and you notice that the training error and the validation error are almost equal and fairly high. Would you say that the model suffers from high bias or high variance? Should you increase the regularization hyperparameter α or reduce it?**

from high bias or high variance? -> high bias
چون مدل روی داده های آموزشی هم خوب عمل نمیکند.
باید مقدار alpha را کاهش دهیم تا مدل آزادی بیشتری برای یادگیری داشته باشد.


10. **Why would you want to use:** 
	 - **a. Ridge regression instead of plain linear regression (i.e., without any regularization)?** 
	 - **b. Lasso instead of ridge regression?** 
	 - **c. Elastic net instead of lasso regression?**

a:
چون Ridge با استفاده از L2 Regularization ضرایب را محدود می‌کند و به کاهش Overfitting کمک می‌کند.
همچنین در حضور Multicollinearity، تخمین ضرایب را پایدارتر می‌کند.
b:
چون Lasso از L1 Regularization استفاده می‌کند و می‌تواند بعضی ضرایب را دقیقاً صفر کند.
در نتیجه قابلیت Feature Selection دارد.
c:
چون Elastic Net ترکیبی از L1 و L2 است.
به‌خصوص زمانی مفید است که ویژگی‌های زیادی با یکدیگر همبستگی دارند. Lasso ممکن است به شکل ناپایداری فقط یکی از ویژگی‌های همبسته را انتخاب کند، درحالی‌که Elastic Net می‌تواند گروهی از آن‌ها را حفظ کند.

11. **Suppose you want to classify pictures as outdoor/indoor and daytime/nighttime. Should you implement two logistic regression classifiers or one softmax regression classifier?**
دوتا logistic regression چون softmax به صورت multiutput نیست بلکه multiclass هست فقط

12. Implement batch gradient descent with early stopping for softmax regression without using Scikit-Learn, only NumPy. Use it on a classification task such as the iris dataset.

