1. **If you have trained five different models on the exact same training data, and they all achieve 95% precision, is there any chance that you can combine these models to get better results? If so, how? If not, why?**
بله این دقیقا همون تکنیکی هست که ما جای استفاده از چند مدل یکسان از چند مدل غیر یکسان استفاده میکنیم که خطا هاشون باهم فرق دارن و با ترکیب این خطا ها و با استفاده از توابع تجمیعی این خطا تا حدودی کم میشه و دقت مدل میره بالا تر.


2. **What is the difference between hard and soft voting classifiers?**
در روش soft voting مدل ensemble میاد و میزان احتمال های یک کلاس مثلا احتمال اونایی که گفتن کلاس 0 و اونایی که گفتن کلاس 1 رو جمع میکنه و میانگین میگیره که این سبب این میشه با توجه به میزان قطعیت مدل ها اون نمونه رو به کلاس اختصاص بدیم ولی در روش hard voting براساس اکثریت آرا هست یعنی یک مدل ممکنه با احتمال 100 درصد گفته باشه این 0 نیست ولی 2 مدل دیگه با احتمال 51 درصد گفته باشن این 1 هست و 1 انتخاب میشه بدون توجه به میزان عدم قطعیت مدل ها.
در soft voting مدل ها باید متد predict_proba رو داشته باشند، حتی میشه به مدل های بهتر وزن بیشتری بدیم


3. Is it possible to speed up training of a bagging ensemble by distributing it across multiple servers? What about pasting ensembles, boosting ensembles, random forests, or stacking ensembles?
بله به علت اینکه هر مدل در Bagging یا pasting از مدل های قبل خودش یا بعد خودش کاملا مستقل هست و میشود هر مدل رو روی یک سرور اجرا کرد که به صورت موازی train بشن.
در Random forest هم میشه چون یک تکنیک Bagging هست ولی بهینه شده برای Decision Tree.
در Boosting نمیشه چون مدل ها به صورت متوالی train میشن و هر مدل به خروجی مدل قبلیش نیاز داره.
در Stacking فقط بخش Base Learner ها میشه موازی سازی کرد و بخش Meta Learner نمیشه پس کاملا نمیشه موازی سازی کرد.

4. What is the benefit of out-of-bag evaluation?
در طول training در Bagging به علت اینکه bootstrap sampling داریم ممکنه یکسری داده ها هیچوقت انتخاب نشن برای train و حدود 63 درصد داده ها اگر تعداد مدل ها کافی باشه انتخاب میشن برای مرحله  train هر مدل پس میشه از اون 37 درصد استفاده کرد برای validation هر مدل مستقل به این validation میگن OOB Validation.
فایدش چیه؟ لازم نیست دوباره مجموعه train رو کوچیک کنیم برای validation و اینکه در همون حین training مدل ارزیابی هم میشه که از لحاظ زمانی یک سود هست.

برای هر نمونه، فقط مدل‌هایی که آن نمونه را در training خود ندیده‌اند (out-of-bag) در پیش‌بینی آن نمونه شرکت می‌کنند؛ سپس پیش‌بینی‌ها تجمیع می‌شوند (رأی/میانگین) و با برچسب واقعی مقایسه می‌شوند. این کار برای همه نمونه‌ها انجام می‌شود و یک **OOB score** کلی به دست می‌آید.


5. What makes extra-trees ensembles more random than regular random forests? How can this extra randomness help? Are extra-trees classifiers slower or faster than regular random forests?
دلیل اینکه چرا تصادفی تر میشه اینه که در Random Forest فقط یک زیر مجموعه از ویژگی ها انتخاب میشن برای رقابت بر سر اینکه ویژگی spliter باشن در Extra-Trees هم این قابلیت هست ولی یک مرحله تصادفی سازی بیشتری رو اضافه میکنه در Random Forest بهترین ویژگی و بهترین threshold را بر اساس معیار ناخالصی جستجو می‌کند ولی در extra-trees حتی این threshold رو هم به صورت تصادفی پیدا میکنه.
چرا این تصادفی سازی کمک میکنه؟ زمان کمتری صرف میشه چون پیدا کردن threshold عملیاتی زمانبر هست و اینکه پیدا کردن threshold برای داده های پرنویز موجب افزایش variance میشه که extra-trees موجب کاهش variance میشه چون یک تصادفی سازی زیادی اضافه میکنه در واقع تصادفی بودن تنوع درخت هارو افزایش میده و موجب میشه خطا هاشون غیر همبسته باشن و در این حالت variance کاهش پیدا میکنه

سرعتش بیشتره از random forest معمولی چون threshold رو تصادفی پیدا میکنه ولی ممکنه لزوما پیش بینی سریع تر نباشه.

6. If your AdaBoost ensemble underfits the training data, which hyperparameters should you tweak, and how?
میشه هایپر پارامتر n_estimator رو افزایش داد تا تعداد مدل ها بیشتر بشه و بتونن خطای هم دیگه رو حنثی کنن، یا حتی خوبه که base_estimator امون رو جوری انتخاب کنیم که پیچیده تر باشه، حتی میشه learning_rate رو افزایش داد که مدل زودتر یاد بگیرد، میشه خود hyperparameter های خود مدل رو هم تغییر داد مثلا در درخت تصمیم افزایش max_depth

7. If your gradient boosting ensemble overfits the training set, should you increase or decrease the learning rate?
کاهش میدیم، چون در gradient boosting هر learning rate که بهش میگیم Shrinkage تعیین میکنه هر درخت با چه نسبتی وارد ensemble بشه و با کاهش دادن learning rate میگیم که درخت ها کمتر در مدل نهایی تاثیر داشته باشن.

8. **Load the MNIST dataset (introduced in Chapter 3), and split it into a training set, a validation set, and a test set (e.g., use 50,000 instances for training, 10,000 for validation, and 10,000 for testing). Then train various classifiers, such as a random forest classifier, an extra-trees classifier, and an SVM classifier. Next, try to combine them into an ensemble that outperforms each individual classifier on the validation set, using soft or hard voting. Once you have found one, try it on the test set. How much better does it perform compared to the individual classifiers?**

9. **Run the individual classifiers from the previous exercise to make predictions on the validation set, and create a new training set with the resulting predictions: each training instance is a vector containing the set of predictions from all your classifiers for an image, and the target is the image’s class. Train a classifier on this new training set. Congratulations—you have just trained a blender, and together with the classifiers it forms a stacking ensemble! Now evaluate the ensemble on the test set. For each image in the test set, make predictions with all your classifiers, then feed the predictions to the blender to get the ensemble’s predictions. How does it compare to the voting classifier you trained earlier? Now try again using a StackingClassifier instead. Do you get better performance? If so, why?**
چون `StackingClassifier` میاد و مدل هارو به صورت k-fold آموزش میده و تمام مدل هارو روی یک مجموعه داده آموزش نمیده ، اموزش چندین مدل روی یک مجموعه داده میتونه نتیجه رو زیادی خوش بینانه بکنه.
و اینکه مدل Base نهایی روی کل training آموزش میبینه.
و اینکه out-of-fold prediction داره و مشکل نشست اطلاعات رو کم میکنه. 

پ.ن: یعنی با روش cross_val_pred پیش بینی ها انجام شده.


