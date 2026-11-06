1. **How would you define machine learning?**  
نوشتن برنامه ای که خودش توانایی یادگیری را بر حسب ویژگی هایی که در دیتاستی که بهش میدیم رو داشته باشد.
2. **Can you name four types of applications where it shines?**  
تشخیص چهره
خوندن پلاک
فیلتر کردن ایمیل های اسپم
سیستم های توصیه گر
3. **What is a labeled training set?**  
یک مجموعه آموزشی که ماهیتش معلوم است چیه مثلا یک عکس داریم این label اش گربه هست. از این برچسب معلومه با چه نوع داده ای طرفیم.
4. **What are the two most common supervised tasks?**  
regression, classification
5. **Can you name four common unsupervised tasks?**  
clustering, Dimesional Reduction, Anomaly Detection , Feature Extraction
6. **What type of algorithm would you use to allow a robot to walk in various unknown terrains?**  
Reinforcement Learning
7. **What type of algorithm would you use to segment your customers into multiple groups?**  
Clustering
8. **Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem?**
Supervised

9. **What is an online learning system?**  
آموزش تدریجی مدل روی داده ها.
یعنی کم کم بهش پاس بدیم
مدلی که می‌تواند به صورت incremental از داده‌های جدید یاد بگیرد.
10. **What is out-of-core learning?**  
یعنی داده های آموزشی ما زیادن و ما توانایی وارد کردن کل دیتاست به فرایند یادگیری رو نداریم.
پس میایم به صورت دسته دسته وارد میکنیم.
11. **What type of algorithm relies on a similarity measure to make predictions?**  
Instance-based learning

12. **What is the difference between a model parameter and a model hyperparameter?**  

پارامتر های مدل میشه اونایی که مدل خودش در فرایند یادگیری یاد میگیره مثلا انتخاب بهترین و کارا ترین پارامتر،  هایپر پارامتر میشه اونایی که ما در فرایند یادگیری براش انتخاب میکنیم مثلا نرخ یادگیری در واقع این که خود مدل پارامتر هایی که پیدا میکنه بهینه هست یا نه خیلی بستگی به این هایپرپارامتر هایی که ما براش تنظیم میکنیم داره.

13. **What do model-based algorithms search for? What is the most common strategy they use to succeed? How do they make predictions?**  
الگوریتم های مبتنی بر مدل در واقع میان یک مدل تقریبی از داده ها ارائه میدن.
رایج ترین استراتژی که دارن اینه که یک تقریب نسبتا دقیقی داشته باشن و بتونن توزیع داده هارو خوب تقریب بزنن.
و از طریق همین تقریب پیش بینی میکنن یعنی مثلا یک سری پارامتر دارن ما کافی هست که داده ی تستمون رو وارد کنیم این با استفاده از پارامتر های بهینه که پیدا کرده سعی میکنه یک پیش بینی بکنه.

14. **Can you name four of the main challenges in machine learning?**  
تعداد داده های دیتاست کم باشه
بیش برازش بر روی داده ها
انتخاب ویژگی خوب برای مدل
تفاوت داده هایی که مدل باهاشون آموزش دیده و داده هایی که در production بهشون بر میخوره.

15. **If your model performs great on the training data but generalizes poorly to new instances, what is happening? Can you name three possible solutions?**  
بیش برازش اتفاق افتاده.
- پیش پردازش داده های آموزشی
- تعداد داده هارو بیشتر کنیم
- اگر شد از پیچیدگی مدل کم کنیم

16. **What is a test set, and why would you want to use it?**  
مجموعه ای هست برای ارزیابی مدل، که generalization error رو حساب بکنیم و ببینیم آیا مدل واقعا چیزی یاد گرفته یا فقط حفظ کرده.
17. **What is the purpose of a validation set?**  
اینکه مدل خودش رو با داده های تست تطبیق نده و تا مرحله تست نهایی اصلا داده های تست رو ندیده باشه
- انتخاب مدل
- تنظیم Hyperparameter
18. **What is the train-dev set, when do you need it, and how do you use it?**  
یک مجموعه ارزیابی هست برای اینکه ببینیم آیا مدل خوب عمل میکنیم.
چه زمانی استفاده میکنیم؟
ما معمولا داده هایی که در مرحله train داده میشه به مدلمون با اونایی که در production داده میشه یکی نیست.
و از طرفی هم اگر مجموعه validation ما از داده های production باشه اگر دقت پایین باشه ما نمیدونیم که ایا این خطا برای بیش برازش مدل هست یا data mismatch.
برای همین train-dev set و اندرو انگ معرفی کرد.
این مجموعه داده میاد و از همون داده های آموزشی پر میشه که ببینیم اگر اینجا خطا زیاد بود یعنی مدل overfit شده و اگر دقت خوب بود ولی validation error زیاد بود یعنی مشکل ما Data mismatch عه.
19. **What can go wrong if you tune hyperparameters using the test set?**  
ممکنه مدل خودش رو به صورت غیر مستقیم با داده های تست تطبیق بده. به این تطبیق میگن
**Data leakage**  

