#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article batch written 2026-09-03.

Topic choice is evidence-led, from 88 days of Search Console data:

  * Joint pain / arthritis - the site ranks for knee and back pain already but
    has no page for arthritis itself, the broadest term of the group.
  * Gout / high uric acid - extremely common in Pakistan and completely absent
    from the site.
  * Menstrual cramps - the clinic already ranks 6.7 for "hijama center near me
    for ladies", so women's-health intent is proven; there is no cramps page.
  * First-time guide - top-of-funnel. "hijama clinic near me" sits at 8.5 and
    those searchers are almost all first-timers with unanswered worries.

DELIBERATELY NOT WRITTEN: anything targeting "hijama in islam", "cupping in
islam", "hijama sunnah". blog/hijama-in-islam.html already exists, is 4,545
words, bilingual, and pulls 291 impressions at position 62.9 - the second
highest impression count on the site. Another page on that cluster would
cannibalise it, not help it. That cluster is also global informational intent:
someone in Indonesia searching "benefits of cupping in islam" will never book
in Karachi.
"""
import datetime
import sys

sys.path.insert(0, __import__("os").path.dirname(__file__))
from gen_article import build, write_queue_entry  # noqa: E402

DATE = "2026-09-03"
DATE_EN = "3 September 2026"
DATE_UR = "3 ستمبر 2026"

REL_JOINT = [
    dict(href="hijama-for-knee-joint-pain.html",
         t_en="Hijama for Knee & Joint Pain", t_ur="گھٹنے اور جوڑوں کے درد کے لیے حجامہ",
         d_en="Cupping as complementary support for stiff, aching knees.",
         d_ur="اکڑے اور دکھتے گھٹنوں کے لیے کپنگ ایک معاون طریقہ۔"),
    dict(href="hijama-for-back-pain-sciatica.html",
         t_en="Hijama for Back Pain & Sciatica", t_ur="کمر درد اور عرق النسا کے لیے حجامہ",
         d_en="What cupping can and cannot do for a painful lower back.",
         d_ur="کمر کے درد میں کپنگ کیا کر سکتی ہے اور کیا نہیں۔"),
    dict(href="hijama-side-effects-and-who-should-avoid.html",
         t_en="Side Effects & Who Should Avoid Hijama", t_ur="مضر اثرات اور کن کو حجامہ سے گریز کرنا چاہیے",
         d_en="An honest list of risks and the people we turn away.",
         d_ur="خطرات کی دیانتدار فہرست اور وہ لوگ جنہیں ہم منع کرتے ہیں۔"),
]

REL_WOMEN = [
    dict(href="hijama-for-pcos-womens-cycle-health.html",
         t_en="Hijama for PCOS & Cycle Health", t_ur="پی سی او ایس اور ماہواری کی صحت کے لیے حجامہ",
         d_en="Complementary support for PCOS, explained honestly.",
         d_ur="پی سی او ایس کے لیے معاون مدد، دیانتداری سے بیان کی گئی۔"),
    dict(href="hijama-for-fertility-and-womens-health.html",
         t_en="Hijama for Fertility & Women's Health", t_ur="زرخیزی اور خواتین کی صحت کے لیے حجامہ",
         d_en="What we do and do not claim about fertility.",
         d_ur="زرخیزی کے بارے میں ہم کیا کہتے ہیں اور کیا نہیں۔"),
    dict(href="../hijama-for-ladies-karachi.html",
         t_en="Hijama for Ladies in Karachi", t_ur="کراچی میں خواتین کے لیے حجامہ",
         d_en="Female practitioner, private room, home service.",
         d_ur="خاتون معالج، پرائیویٹ کمرہ، گھر پر سروس۔"),
]

REL_FIRST = [
    dict(href="what-is-hijama.html",
         t_en="What Is Hijama?", t_ur="حجامہ کیا ہے؟",
         d_en="The plain-language explanation, start here.",
         d_ur="سادہ زبان میں وضاحت، یہیں سے شروع کریں۔"),
    dict(href="how-to-prepare-for-hijama-session.html",
         t_en="How to Prepare for a Session", t_ur="سیشن کی تیاری کیسے کریں",
         d_en="Eating, fasting, clothing and timing before you come.",
         d_ur="آنے سے پہلے کھانا، روزہ، لباس اور وقت۔"),
    dict(href="hijama-price-in-karachi.html",
         t_en="Hijama Price in Karachi", t_ur="کراچی میں حجامہ کی قیمت",
         d_en="What a session costs and what is included.",
         d_ur="ایک سیشن کی قیمت اور اس میں کیا شامل ہے۔"),
]


TOPICS = [

# ---------------------------------------------------------------- 1. arthritis
dict(
  slug="hijama-for-joint-pain-arthritis", target="blog/hijama-for-joint-pain-arthritis.html",
  date=DATE, date_en=DATE_EN, date_ur=DATE_UR,
  eyebrow_en="Complementary Care", eyebrow_ur="معاون علاج",
  title_en="Hijama for Joint Pain & Arthritis — An Honest Guide",
  title_ur="جوڑوں کے درد اور گٹھیا کے لیے حجامہ — ایک دیانتدار رہنما",
  seo_title="Hijama for Joint Pain & Arthritis — An Honest Guide",
  seo_desc="Stiff, aching joints? An honest guide to Hijama (cupping) for arthritis and joint pain in Karachi — complementary support alongside your doctor, never a cure. جوڑوں کے درد اور گٹھیا کے لیے حجامہ، کراچی۔",
  og_desc="An honest guide to Hijama for arthritis and joint pain — complementary support alongside your doctor, never a replacement. Karachi clinic.",
  keywords="hijama for arthritis, cupping for joint pain, hijama for gathiya, arthritis treatment karachi, joint pain cupping, حجامہ گٹھیا, جوڑوں کا درد حجامہ, گٹھیا کا علاج کراچی",
  tag_en="Complementary Care", tag_ur="معاون علاج",
  blurb_en="Stiff knees, aching fingers, a back that protests every morning. What cupping may ease, what it cannot fix, and when to see a doctor first.",
  blurb_ur="اکڑے گھٹنے، دکھتی انگلیاں، ہر صبح شکایت کرتی کمر۔ کپنگ کس میں آرام دے سکتی ہے، کیا ٹھیک نہیں کر سکتی، اور پہلے ڈاکٹر کے پاس کب جانا چاہیے۔",
  lede_en="Joint pain wears people down quietly. It is not usually the sharp emergency that sends you to a hospital — it is the stiffness on waking, the knee that complains on the stairs, the fingers that will not close properly in winter. Patients often ask us whether Hijama can help. Our answer is careful: Hijama is a <strong>complementary traditional practice</strong>. It does not cure arthritis, it does not repair a damaged joint, and it does not replace the treatment your doctor has prescribed. What many patients do report is a period of easier movement and less muscular tightness around the painful joint. That is worth something — but it is worth being honest about its limits.",
  lede_ur="جوڑوں کا درد لوگوں کو خاموشی سے تھکا دیتا ہے۔ یہ عام طور پر وہ شدید ہنگامی حالت نہیں ہوتی جو آپ کو اسپتال لے جائے — یہ صبح اٹھتے وقت کی اکڑاہٹ ہے، سیڑھیوں پر شکایت کرتا گھٹنا، سردیوں میں وہ انگلیاں جو ٹھیک سے بند نہیں ہوتیں۔ مریض اکثر ہم سے پوچھتے ہیں کہ کیا حجامہ مدد دے سکتا ہے۔ ہمارا جواب محتاط ہے: حجامہ ایک <strong>معاون روایتی طریقہ</strong> ہے۔ یہ گٹھیا کا علاج نہیں کرتا، خراب جوڑ کی مرمت نہیں کرتا، اور آپ کے ڈاکٹر کے تجویز کردہ علاج کی جگہ نہیں لیتا۔ البتہ بہت سے مریض بتاتے ہیں کہ کچھ عرصے کے لیے حرکت آسان ہو جاتی ہے اور دکھتے جوڑ کے گرد پٹھوں کا کھنچاؤ کم ہوتا ہے۔ یہ بھی ایک قدر رکھتا ہے — لیکن اس کی حدود کے بارے میں دیانتدار رہنا ضروری ہے۔",
  sections=[
    dict(h2_en="Arthritis is not one condition", h2_ur="گٹھیا ایک بیماری نہیں ہے",
      paras=[
        ("The word covers very different problems. <strong>Osteoarthritis</strong> is wear in the joint surface, most often knees and hips, and it builds slowly with age and weight. <strong>Rheumatoid arthritis</strong> is an autoimmune disease in which the body attacks its own joints — it is inflammatory, it can move quickly, and it needs proper medical treatment without delay. <strong>Gout</strong> is a crystal problem driven by uric acid. They feel similar to the person suffering them, but they are not the same illness and they do not need the same care.",
         "یہ لفظ بہت مختلف مسائل کا احاطہ کرتا ہے۔ <strong>اوسٹیوآرتھرائٹس</strong> جوڑ کی سطح کا گھِس جانا ہے، عام طور پر گھٹنے اور کولہے، اور یہ عمر اور وزن کے ساتھ آہستہ بڑھتا ہے۔ <strong>ریمیٹائیڈ آرتھرائٹس</strong> ایک خود کار مدافعتی بیماری ہے جس میں جسم اپنے ہی جوڑوں پر حملہ کرتا ہے — یہ سوزشی ہے، تیزی سے بڑھ سکتی ہے، اور بغیر تاخیر مناسب طبی علاج چاہتی ہے۔ <strong>گاؤٹ</strong> یورک ایسڈ سے پیدا ہونے والا کرسٹل کا مسئلہ ہے۔ مریض کو یہ ایک جیسے محسوس ہوتے ہیں، مگر یہ ایک بیماری نہیں اور ان کا علاج بھی ایک نہیں۔"),
        ("This matters for Hijama. If you have rheumatoid arthritis, cupping is not a substitute for the medication that protects your joints from permanent damage — delaying that treatment can cost you function you will never get back. We will say so plainly rather than take your booking.",
         "یہ بات حجامہ کے لیے اہم ہے۔ اگر آپ کو ریمیٹائیڈ آرتھرائٹس ہے تو کپنگ اس دوا کا متبادل نہیں جو آپ کے جوڑوں کو مستقل نقصان سے بچاتی ہے — اس علاج میں تاخیر آپ کی وہ صلاحیت چھین سکتی ہے جو کبھی واپس نہیں آتی۔ ہم بکنگ لینے کے بجائے یہ بات صاف کہہ دیں گے۔"),
      ]),
    dict(h2_en="What Hijama may help with", h2_ur="حجامہ کس چیز میں مدد دے سکتا ہے",
      paras=[
        ("Around a painful joint, the muscles rarely stay relaxed. They tighten to protect it, and that guarding becomes its own source of ache — a stiff, heavy, restricted feeling that is separate from the joint damage underneath. This is the layer where patients most often notice a difference after cupping: the surrounding tissue softens, movement feels less braced, and sleep is sometimes easier for a few nights.",
         "دکھتے جوڑ کے گرد پٹھے شاذ و نادر ہی ڈھیلے رہتے ہیں۔ وہ اس کی حفاظت کے لیے سخت ہو جاتے ہیں، اور یہ حفاظتی کھنچاؤ خود ایک تکلیف بن جاتا ہے — ایک اکڑا، بھاری، محدود احساس جو نیچے موجود جوڑ کے نقصان سے الگ ہے۔ یہی وہ سطح ہے جہاں مریض کپنگ کے بعد اکثر فرق محسوس کرتے ہیں: ارد گرد کے ٹشو نرم پڑتے ہیں، حرکت میں جکڑن کم لگتی ہے، اور کبھی کبھی چند راتیں نیند بہتر آتی ہے۔"),
      ],
      bullets=[
        ("Muscular tightness and guarding around the joint", "جوڑ کے گرد پٹھوں کا کھنچاؤ اور جکڑن"),
        ("General stiffness on waking, for a period after the session", "صبح اٹھنے کی اکڑاہٹ، سیشن کے بعد کچھ عرصے کے لیے"),
        ("A sense of relaxation that helps with sleep and stress", "سکون کا احساس جو نیند اور ذہنی دباؤ میں مدد دیتا ہے"),
        ("Comfort as part of an overall routine — alongside movement, weight and diet", "مجموعی معمول کے حصے کے طور پر آرام — حرکت، وزن اور خوراک کے ساتھ"),
      ]),
    dict(h2_en="What Hijama cannot do", h2_ur="حجامہ کیا نہیں کر سکتا",
      caution=("Hijama does not regrow cartilage, reverse joint damage, cure rheumatoid arthritis, or remove the need for the medicines your doctor has prescribed. Anyone who tells you otherwise is selling you something. If a practitioner promises to cure your arthritis, walk away.",
               "حجامہ کارٹلیج دوبارہ نہیں اگاتا، جوڑ کے نقصان کو واپس نہیں پلٹتا، ریمیٹائیڈ آرتھرائٹس کا علاج نہیں کرتا، اور آپ کے ڈاکٹر کی تجویز کردہ دواؤں کی ضرورت ختم نہیں کرتا۔ جو کوئی آپ سے اس کے برعکس کہے وہ آپ کو کچھ بیچ رہا ہے۔ اگر کوئی معالج آپ کی گٹھیا کے علاج کا وعدہ کرے تو وہاں سے چلے جائیں۔"),
      paras=[
        ("We also want to be clear about how the benefit tends to behave. For most joint-pain patients, relief after a session is real but temporary — often days to a few weeks. It is best understood as periodic comfort within a longer plan, not a one-off fix. Patients who keep moving, manage their weight and take their prescribed treatment do better than those who rely on cupping alone. That is not a sales pitch; it is simply what we see.",
         "ہم یہ بھی واضح کرنا چاہتے ہیں کہ فائدہ عام طور پر کیسا ہوتا ہے۔ جوڑوں کے درد کے زیادہ تر مریضوں میں سیشن کے بعد آرام حقیقی مگر عارضی ہوتا ہے — اکثر چند دن سے چند ہفتے۔ اسے ایک طویل منصوبے کے اندر وقتاً فوقتاً ملنے والا آرام سمجھنا بہتر ہے، نہ کہ ایک بار کا حل۔ جو مریض حرکت جاری رکھتے ہیں، وزن کنٹرول کرتے ہیں اور اپنا تجویز کردہ علاج لیتے ہیں وہ صرف کپنگ پر انحصار کرنے والوں سے بہتر رہتے ہیں۔ یہ فروخت کی بات نہیں؛ یہ صرف وہ ہے جو ہم دیکھتے ہیں۔"),
      ]),
    dict(h2_en="Safety, and who we turn away", h2_ur="حفاظت، اور ہم کن کو منع کرتے ہیں",
      paras=[
        ("We do not cup directly over a hot, red, visibly swollen joint in an active inflammatory flare — that needs medical assessment, not suction. We take extra care with patients on blood thinners, with bleeding disorders, with poorly controlled diabetes, or with fragile skin. Anyone with a joint that is suddenly hot, severely swollen or accompanied by fever should see a doctor the same day: that can be infection or an acute gout attack, and both are urgent.",
         "ہم فعال سوزش کے دوران گرم، سرخ، واضح طور پر سوجے ہوئے جوڑ پر براہِ راست کپنگ نہیں کرتے — اس کے لیے طبی معائنہ چاہیے، سکشن نہیں۔ ہم خون پتلا کرنے والی دوا لینے والوں، خون بہنے کے امراض، بے قابو ذیابیطس، یا نازک جلد والے مریضوں میں خاص احتیاط کرتے ہیں۔ جس کا جوڑ اچانک گرم ہو، شدید سوجا ہو یا بخار کے ساتھ ہو، اسے اُسی دن ڈاکٹر کو دکھانا چاہیے: یہ انفیکشن یا گاؤٹ کا شدید حملہ ہو سکتا ہے، اور دونوں ہنگامی ہیں۔"),
      ]),
  ],
  faq=[
    dict(q_en="Can Hijama cure my arthritis?", q_ur="کیا حجامہ میری گٹھیا ٹھیک کر سکتا ہے؟",
         a_en="No. Hijama is complementary support that some patients find eases stiffness and muscular tightness for a period. It does not cure arthritis or repair a damaged joint, and it is not a reason to stop the treatment your doctor has prescribed.",
         a_ur="نہیں۔ حجامہ ایک معاون طریقہ ہے جسے کچھ مریض اکڑاہٹ اور پٹھوں کے کھنچاؤ میں کچھ عرصے کے لیے مفید پاتے ہیں۔ یہ گٹھیا کا علاج نہیں کرتا نہ خراب جوڑ کی مرمت کرتا ہے، اور یہ آپ کے ڈاکٹر کا تجویز کردہ علاج چھوڑنے کی وجہ نہیں۔"),
    dict(q_en="Where are the cups placed for knee pain?", q_ur="گھٹنے کے درد کے لیے کپ کہاں لگائے جاتے ہیں؟",
         a_en="Usually around the joint rather than on the kneecap itself — the thigh and calf muscles that support and move the knee, plus the lower back where much leg pain is referred from. The exact points depend on your examination, not a fixed chart.",
         a_ur="عام طور پر جوڑ کے گرد، نہ کہ خود گھٹنے کی ہڈی پر — ران اور پنڈلی کے وہ پٹھے جو گھٹنے کو سہارا دیتے اور حرکت دیتے ہیں، اور کمر کا نچلا حصہ جہاں سے ٹانگ کا بہت سا درد منتقل ہوتا ہے۔ اصل مقامات آپ کے معائنے پر منحصر ہیں، کسی مقررہ چارٹ پر نہیں۔"),
    dict(q_en="How soon would I feel a difference?", q_ur="مجھے کتنی جلدی فرق محسوس ہوگا؟",
         a_en="Some people feel lighter the same evening; others notice it over the following two or three days. If you feel nothing at all after two properly spaced sessions, we will tell you honestly that it may not be the right approach for you.",
         a_ur="کچھ لوگ اُسی شام ہلکا پن محسوس کرتے ہیں؛ کچھ کو اگلے دو تین دن میں اندازہ ہوتا ہے۔ اگر مناسب وقفے سے دو سیشن کے بعد بھی آپ کو کچھ محسوس نہ ہو تو ہم دیانتداری سے بتا دیں گے کہ شاید یہ آپ کے لیے مناسب طریقہ نہیں۔"),
    dict(q_en="Is it safe if I take blood thinners?", q_ur="اگر میں خون پتلا کرنے والی دوا لیتا ہوں تو کیا یہ محفوظ ہے؟",
         a_en="Wet cupping involves small skin incisions, so blood thinners need real caution. Tell us exactly what you take and bring your prescription. In many cases we will recommend dry cupping instead, or decline until your doctor has advised.",
         a_ur="گیلی حجامہ میں جلد پر باریک شگاف لگتے ہیں، اس لیے خون پتلا کرنے والی دوا میں حقیقی احتیاط چاہیے۔ ہمیں بالکل بتائیں کہ آپ کیا لیتے ہیں اور نسخہ ساتھ لائیں۔ اکثر صورتوں میں ہم اس کے بجائے خشک کپنگ تجویز کریں گے، یا آپ کے ڈاکٹر کی رائے تک انکار کریں گے۔"),
    dict(q_en="Do you offer home service for elderly patients?", q_ur="کیا آپ بزرگ مریضوں کے لیے گھر پر سروس دیتے ہیں؟",
         a_en="Yes. For patients who find travel painful, home service across Karachi is often the sensible choice, and it lets us see how you actually move at home. Message us on WhatsApp with your area and we will confirm availability.",
         a_ur="جی ہاں۔ جن مریضوں کے لیے سفر تکلیف دہ ہے، ان کے لیے کراچی بھر میں گھر پر سروس اکثر بہتر انتخاب ہے، اور اس سے ہمیں یہ بھی نظر آتا ہے کہ آپ گھر میں کیسے حرکت کرتے ہیں۔ اپنے علاقے کے ساتھ واٹس ایپ پر پیغام بھیجیں، ہم دستیابی کی تصدیق کر دیں گے۔"),
  ],
  cta_en="Living with stiff, painful joints?",
  cta_ur="اکڑے، دکھتے جوڑوں کے ساتھ زندگی گزار رہے ہیں؟",
  cta_body_en="Calm, careful, hygienic Hijama sessions at Shaheen Shafi Unani Clinic &amp; Hijama Center, Model Colony, Karachi — clinic or home visit. Tell us which joints trouble you and what your doctor has said, and we will give you an honest answer about whether this is worth your time.",
  cta_body_ur="شاہین شافی یونانی کلینک و حجامہ سینٹر، ماڈل کالونی، کراچی میں پُرسکون، محتاط، صاف ستھرے حجامہ سیشن — کلینک یا گھر پر۔ ہمیں بتائیں کون سے جوڑ تکلیف دیتے ہیں اور آپ کے ڈاکٹر نے کیا کہا ہے، ہم دیانتداری سے بتائیں گے کہ آیا یہ آپ کے وقت کے قابل ہے۔",
  related=REL_JOINT,
),

# ---------------------------------------------------------------- 2. gout
dict(
  slug="hijama-for-gout-uric-acid", target="blog/hijama-for-gout-uric-acid.html",
  date=DATE, date_en=DATE_EN, date_ur=DATE_UR,
  eyebrow_en="Complementary Care", eyebrow_ur="معاون علاج",
  title_en="Hijama for Gout & High Uric Acid — What Is Honest to Say",
  title_ur="گاؤٹ اور بلند یورک ایسڈ کے لیے حجامہ — دیانتداری سے کیا کہا جا سکتا ہے",
  seo_title="Hijama for Gout & High Uric Acid — What Is Honest to Say",
  seo_desc="High uric acid or gout attacks in the big toe? An honest guide to Hijama and gout in Karachi — why we never cup an active flare, and what actually lowers uric acid. گاؤٹ اور یورک ایسڈ کے لیے حجامہ، کراچی۔",
  og_desc="An honest guide to Hijama and gout — why we never cup an active attack, and what actually lowers uric acid. Karachi clinic.",
  keywords="hijama for gout, cupping for uric acid, high uric acid treatment karachi, gout karachi, hijama uric acid, حجامہ گاؤٹ, یورک ایسڈ کا علاج, یورک ایسڈ حجامہ",
  tag_en="Complementary Care", tag_ur="معاون علاج",
  blurb_en="A swollen, burning big toe at 3am is not a cupping problem. Where Hijama may sit in a gout plan, and the two things that actually move uric acid.",
  blurb_ur="رات تین بجے سوجا، جلتا انگوٹھا کپنگ کا مسئلہ نہیں۔ گاؤٹ کے منصوبے میں حجامہ کہاں آ سکتا ہے، اور وہ دو چیزیں جو واقعی یورک ایسڈ کم کرتی ہیں۔",
  lede_en="Gout announces itself brutally — often in the big toe, often in the middle of the night, hot and swollen and so tender that a bedsheet is unbearable. High uric acid is very common in Pakistan, and patients regularly ask whether Hijama can bring it down. We will be straightforward: <strong>Hijama is not a treatment for gout</strong>, and during an active attack it is the wrong thing entirely. There is a sensible place for cupping in the quiet periods between flares, as general comfort — but the things that genuinely change uric acid are medication and diet, and we would rather tell you that than take your money.",
  lede_ur="گاؤٹ اپنا اعلان بڑی سختی سے کرتا ہے — اکثر پاؤں کے انگوٹھے میں، اکثر آدھی رات کو، گرم اور سوجا ہوا اور اتنا حساس کہ چادر بھی برداشت نہیں ہوتی۔ پاکستان میں بلند یورک ایسڈ بہت عام ہے، اور مریض اکثر پوچھتے ہیں کہ کیا حجامہ اسے کم کر سکتا ہے۔ ہم صاف بات کریں گے: <strong>حجامہ گاؤٹ کا علاج نہیں</strong>، اور شدید حملے کے دوران تو یہ بالکل غلط چیز ہے۔ حملوں کے درمیان پُرسکون وقفوں میں عمومی آرام کے طور پر کپنگ کی ایک معقول جگہ ہے — لیکن جو چیزیں واقعی یورک ایسڈ بدلتی ہیں وہ دوا اور خوراک ہیں، اور ہم آپ سے پیسے لینے کے بجائے یہ بتانا پسند کریں گے۔",
  sections=[
    dict(h2_en="Never during an attack", h2_ur="حملے کے دوران ہرگز نہیں",
      caution=("If your joint is hot, red, badly swollen and exquisitely painful right now, do not book a cupping session — see a doctor. An acute gout flare needs anti-inflammatory treatment, and the same picture can also be a joint infection, which is a medical emergency. Suction and incisions over an actively inflamed joint can only make things worse.",
               "اگر آپ کا جوڑ ابھی گرم، سرخ، بری طرح سوجا اور شدید تکلیف دہ ہے تو کپنگ سیشن بک نہ کریں — ڈاکٹر کو دکھائیں۔ گاؤٹ کے شدید حملے کو سوزش کم کرنے والا علاج چاہیے، اور یہی صورت جوڑ کے انفیکشن کی بھی ہو سکتی ہے، جو ایک طبی ہنگامی حالت ہے۔ فعال طور پر سوجے جوڑ پر سکشن اور شگاف صرف حالت خراب کریں گے۔"),
      paras=[
        ("We turn patients away for this reason more often than for almost anything else, and we would rather lose the booking than harm a foot. Come back when the flare has settled and we can talk sensibly.",
         "ہم اسی وجہ سے مریضوں کو کسی بھی اور وجہ سے زیادہ منع کرتے ہیں، اور ہم پاؤں کو نقصان پہنچانے کے بجائے بکنگ کھونا بہتر سمجھتے ہیں۔ جب حملہ ٹھنڈا ہو جائے تو واپس آئیں، پھر ہم سمجھداری سے بات کر سکتے ہیں۔"),
      ]),
    dict(h2_en="What actually lowers uric acid", h2_ur="یورک ایسڈ اصل میں کیا کم کرتا ہے",
      paras=[
        ("Two things, mainly. The first is the medication your doctor prescribes to reduce uric acid production or help the kidneys clear it — taken consistently, not only when a toe hurts. The second is what you eat and drink. Neither is glamorous and neither is what people want to hear, but they are what works.",
         "بنیادی طور پر دو چیزیں۔ پہلی وہ دوا جو آپ کا ڈاکٹر یورک ایسڈ کی پیداوار کم کرنے یا گردوں کی مدد کے لیے دیتا ہے — مسلسل لی جائے، صرف اُس وقت نہیں جب انگوٹھا دکھے۔ دوسری یہ کہ آپ کیا کھاتے پیتے ہیں۔ ان میں سے کوئی دلکش نہیں اور نہ ہی وہ ہے جو لوگ سننا چاہتے ہیں، مگر یہی کام کرتی ہیں۔"),
      ],
      bullets=[
        ("Water, properly — dehydration concentrates uric acid, and Karachi's heat makes this worse", "پانی، صحیح مقدار میں — پانی کی کمی یورک ایسڈ کو گاڑھا کرتی ہے، اور کراچی کی گرمی اسے بڑھاتی ہے"),
        ("Less organ meat, red meat and shellfish — the classic high-purine group", "کم کلیجی، سرخ گوشت اور جھینگا — روایتی زیادہ پیورین والا گروہ"),
        ("Cut sugary drinks and anything with high-fructose syrup", "میٹھے مشروبات اور ہائی فرکٹوز والی اشیاء بند کریں"),
        ("Alcohol, especially beer, raises uric acid sharply", "شراب، خاص طور پر بیئر، یورک ایسڈ تیزی سے بڑھاتی ہے"),
        ("Gradual weight loss helps; crash dieting can trigger a flare", "بتدریج وزن کم کرنا مدد دیتا ہے؛ اچانک سخت ڈائٹنگ حملہ کر سکتی ہے"),
      ]),
    dict(h2_en="So where does Hijama fit?", h2_ur="تو حجامہ کہاں فٹ ہوتا ہے؟",
      paras=[
        ("Between flares, when nothing is inflamed, some patients come for cupping as part of a general wellbeing routine — the same reason others come for back or shoulder tension. Gout is exhausting and it disturbs sleep, and a calm session can be a genuine comfort. We will work away from the affected joint, not on it.",
         "حملوں کے درمیان، جب کوئی سوزش نہ ہو، کچھ مریض عمومی صحت کے معمول کے حصے کے طور پر کپنگ کے لیے آتے ہیں — اُسی وجہ سے جس وجہ سے دوسرے کمر یا کندھے کے کھنچاؤ کے لیے آتے ہیں۔ گاؤٹ تھکا دینے والا ہے اور نیند خراب کرتا ہے، اور ایک پُرسکون سیشن حقیقی سکون دے سکتا ہے۔ ہم متاثرہ جوڑ سے ہٹ کر کام کریں گے، اُس پر نہیں۔"),
        ("What we will not do is tell you that cupping is lowering your uric acid number. We have no honest basis for that claim. If your reading comes down, it will be because of your treatment and your diet — and that is a better result anyway, because it is one you can maintain.",
         "جو ہم نہیں کریں گے وہ یہ کہ آپ کو بتائیں کہ کپنگ آپ کا یورک ایسڈ کم کر رہی ہے۔ اس دعوے کی ہمارے پاس کوئی دیانتدار بنیاد نہیں۔ اگر آپ کی رپورٹ بہتر ہوتی ہے تو وہ آپ کے علاج اور خوراک کی وجہ سے ہوگی — اور یہ ویسے بھی بہتر نتیجہ ہے، کیونکہ اسے آپ برقرار رکھ سکتے ہیں۔"),
      ]),
  ],
  faq=[
    dict(q_en="Does Hijama reduce uric acid levels?", q_ur="کیا حجامہ یورک ایسڈ کی سطح کم کرتا ہے؟",
         a_en="We do not claim that. There is no reliable basis for saying cupping lowers uric acid. Medication prescribed by your doctor and changes to diet and hydration are what move that number.",
         a_ur="ہم یہ دعویٰ نہیں کرتے۔ یہ کہنے کی کوئی قابلِ اعتماد بنیاد نہیں کہ کپنگ یورک ایسڈ کم کرتی ہے۔ آپ کے ڈاکٹر کی تجویز کردہ دوا اور خوراک و پانی میں تبدیلی ہی وہ چیزیں ہیں جو یہ عدد بدلتی ہیں۔"),
    dict(q_en="My toe is swollen right now — can I come today?", q_ur="میرا انگوٹھا ابھی سوجا ہوا ہے — کیا میں آج آ سکتا ہوں؟",
         a_en="Please see a doctor instead. An active flare needs anti-inflammatory treatment, and a hot swollen joint can also be an infection, which is urgent. We would decline the session anyway.",
         a_ur="براہِ کرم اس کے بجائے ڈاکٹر کو دکھائیں۔ شدید حملے کو سوزش کم کرنے والا علاج چاہیے، اور گرم سوجا جوڑ انفیکشن بھی ہو سکتا ہے، جو ہنگامی ہے۔ ہم بہرحال سیشن سے انکار کر دیں گے۔"),
    dict(q_en="Can I have Hijama while taking gout medication?", q_ur="کیا میں گاؤٹ کی دوا کے دوران حجامہ کروا سکتا ہوں؟",
         a_en="Usually yes, between flares, provided you are not on blood thinners and your doctor has no objection. Bring your prescription so we can see exactly what you take.",
         a_ur="عام طور پر جی ہاں، حملوں کے درمیان، بشرطیکہ آپ خون پتلا کرنے والی دوا نہ لے رہے ہوں اور آپ کے ڈاکٹر کو اعتراض نہ ہو۔ اپنا نسخہ ساتھ لائیں تاکہ ہم دیکھ سکیں کہ آپ کیا لیتے ہیں۔"),
    dict(q_en="Is high uric acid the same as gout?", q_ur="کیا بلند یورک ایسڈ اور گاؤٹ ایک ہی چیز ہے؟",
         a_en="No. Many people have a raised reading and never get an attack. Gout is what happens when crystals form in a joint and cause inflammation. A high number alone is a risk factor, not a diagnosis.",
         a_ur="نہیں۔ بہت سے لوگوں کی رپورٹ بلند ہوتی ہے اور انہیں کبھی حملہ نہیں ہوتا۔ گاؤٹ وہ ہے جب جوڑ میں کرسٹل بنتے ہیں اور سوزش پیدا کرتے ہیں۔ صرف بلند عدد ایک خطرے کا عنصر ہے، تشخیص نہیں۔"),
    dict(q_en="What should I avoid eating in Karachi's summer?", q_ur="کراچی کی گرمی میں مجھے کیا کھانے سے بچنا چاہیے؟",
         a_en="Keep water up first — dehydration is the biggest local trigger. Then reduce organ meats, heavy red meat, shellfish and sugary drinks. Nihari and paye are much-loved but they are high-purine; occasional is different from regular.",
         a_ur="سب سے پہلے پانی کا خیال رکھیں — پانی کی کمی یہاں سب سے بڑا محرک ہے۔ پھر کلیجی، بھاری سرخ گوشت، جھینگا اور میٹھے مشروبات کم کریں۔ نہاری اور پائے بہت پسندیدہ ہیں مگر ان میں پیورین زیادہ ہے؛ کبھی کبھار اور باقاعدگی میں فرق ہے۔"),
  ],
  cta_en="Managing gout, and want an honest opinion?",
  cta_ur="گاؤٹ کے ساتھ گزارہ کر رہے ہیں اور دیانتدار رائے چاہتے ہیں؟",
  cta_body_en="Shaheen Shafi Unani Clinic &amp; Hijama Center, Model Colony, Karachi. Tell us where you are in the cycle — mid-attack or settled — and what your doctor has prescribed. If cupping is not the right thing for you right now, we will say so.",
  cta_body_ur="شاہین شافی یونانی کلینک و حجامہ سینٹر، ماڈل کالونی، کراچی۔ ہمیں بتائیں آپ کس مرحلے میں ہیں — حملے کے دوران یا ٹھہراؤ میں — اور آپ کے ڈاکٹر نے کیا تجویز کیا ہے۔ اگر ابھی کپنگ آپ کے لیے مناسب نہیں تو ہم کہہ دیں گے۔",
  related=REL_JOINT,
),

# ---------------------------------------------------------------- 3. cramps
dict(
  slug="hijama-for-menstrual-cramps", target="blog/hijama-for-menstrual-cramps.html",
  date=DATE, date_en=DATE_EN, date_ur=DATE_UR,
  eyebrow_en="Women's Wellbeing", eyebrow_ur="خواتین کی صحت",
  title_en="Hijama for Menstrual Cramps & Period Pain",
  title_ur="ماہواری کے درد اور مروڑ کے لیے حجامہ",
  seo_title="Hijama for Menstrual Cramps & Period Pain — A Careful Guide",
  seo_desc="Painful periods? A careful, private guide to Hijama for menstrual cramps in Karachi — female practitioner, home service, and an honest account of what cupping can and cannot ease. ماہواری کے درد کے لیے حجامہ، کراچی۔",
  og_desc="A careful, private guide to Hijama for menstrual cramps — female practitioner and home service in Karachi. Honest about what it can and cannot ease.",
  keywords="hijama for period pain, cupping for menstrual cramps, hijama for ladies karachi, period pain treatment karachi, female hijama practitioner, ماہواری درد حجامہ, خواتین حجامہ کراچی, پیریڈ درد کا علاج",
  tag_en="Women's Wellbeing", tag_ur="خواتین کی صحت",
  blurb_en="Cramps that stop you working or studying are not something to just endure quietly. What cupping may ease, in a private room with a female practitioner.",
  blurb_ur="وہ مروڑ جو آپ کا کام یا پڑھائی روک دیں، انہیں خاموشی سے برداشت کرنے کی چیز نہیں۔ کپنگ کس میں آرام دے سکتی ہے، خاتون معالج کے ساتھ پرائیویٹ کمرے میں۔",
  lede_en="Many women in Karachi treat period pain as something to be quietly absorbed — a day lost each month, a class missed, work done through gritted teeth. It does not have to be borne in silence. Patients ask us about Hijama for cramps regularly, and our answer is measured: cupping is a <strong>complementary comfort measure</strong>. It will not correct an underlying gynaecological condition, and pain severe enough to stop your life each month deserves a proper diagnosis first. Within those limits, some women find a session in the days before their period genuinely eases the heaviness and lower-back ache.",
  lede_ur="کراچی کی بہت سی خواتین ماہواری کے درد کو خاموشی سے برداشت کرنے کی چیز سمجھتی ہیں — ہر مہینے ایک دن ضائع، ایک کلاس چھوٹی، دانت بھینچ کر کیا گیا کام۔ اسے خاموشی سے سہنا ضروری نہیں۔ مریض اکثر ہم سے مروڑ کے لیے حجامہ کے بارے میں پوچھتی ہیں، اور ہمارا جواب متوازن ہے: کپنگ ایک <strong>معاون آرام دہ طریقہ</strong> ہے۔ یہ کسی بنیادی امراضِ نسواں کی اصلاح نہیں کرے گی، اور جو درد ہر مہینے آپ کی زندگی روک دے اسے پہلے مناسب تشخیص چاہیے۔ ان حدود کے اندر، کچھ خواتین ماہواری سے پہلے کے دنوں میں سیشن سے بھاری پن اور کمر کے نچلے درد میں حقیقی آرام پاتی ہیں۔",
  sections=[
    dict(h2_en="Privacy comes first", h2_ur="پہلے پردہ",
      paras=[
        ("We know this is the reason many women never ask. Sessions for female patients are with a <strong>female practitioner</strong>, in a private room, with the door closed and no one else present. Home service across Karachi is available if you would rather not come to a clinic at all, and a family member is welcome to stay with you throughout. Nothing is discussed outside the room.",
         "ہم جانتے ہیں کہ یہی وجہ ہے کہ بہت سی خواتین کبھی پوچھتی ہی نہیں۔ خواتین مریضوں کے سیشن <strong>خاتون معالج</strong> کے ساتھ، پرائیویٹ کمرے میں، بند دروازے کے پیچھے اور کسی اور کی موجودگی کے بغیر ہوتے ہیں۔ اگر آپ کلینک آنا ہی نہ چاہیں تو کراچی بھر میں گھر پر سروس دستیاب ہے، اور کوئی گھر کا فرد پورے وقت آپ کے ساتھ رہ سکتا ہے۔ کمرے سے باہر کوئی بات نہیں کی جاتی۔"),
      ]),
    dict(h2_en="What a session may ease", h2_ur="سیشن کس چیز میں آرام دے سکتا ہے",
      paras=[
        ("Period pain is not only in the abdomen. A great deal of it is felt in the lower back and hips, and the muscles there tighten in response, which adds a second layer of ache on top of the first. That muscular layer is where cupping is most plausible — the tissue relaxes, the back feels less gripped, and some women report better sleep in the days around their period.",
         "ماہواری کا درد صرف پیٹ میں نہیں ہوتا۔ اس کا بڑا حصہ کمر کے نچلے حصے اور کولہوں میں محسوس ہوتا ہے، اور وہاں کے پٹھے جواب میں سخت ہو جاتے ہیں، جو پہلے درد کے اوپر ایک دوسری تہہ بڑھا دیتا ہے۔ پٹھوں کی یہی تہہ وہ جگہ ہے جہاں کپنگ سب سے زیادہ قرینِ قیاس ہے — ٹشو ڈھیلے پڑتے ہیں، کمر کی جکڑن کم لگتی ہے، اور کچھ خواتین ماہواری کے دنوں میں بہتر نیند بتاتی ہیں۔"),
      ],
      bullets=[
        ("Lower-back and hip tightness around your period", "ماہواری کے دوران کمر اور کولہوں کی جکڑن"),
        ("A general feeling of heaviness and fatigue", "بھاری پن اور تھکن کا عمومی احساس"),
        ("Stress and poor sleep in the days beforehand", "ماہواری سے پہلے کے دنوں میں ذہنی دباؤ اور خراب نیند"),
      ]),
    dict(h2_en="When to see a doctor instead", h2_ur="کب اس کے بجائے ڈاکٹر کو دکھائیں",
      caution=("Pain that stops you functioning every month, bleeding that soaks through protection hourly, pain during intimacy, bleeding between periods, or periods that have suddenly changed character — these need a gynaecologist, not a cupping session. Conditions like endometriosis, fibroids and PCOS are treatable, and they are commonly missed because women are told period pain is normal. It is not normal to lose a day a month.",
               "وہ درد جو ہر مہینے آپ کو کام سے روک دے، ایسا خون بہنا جو ہر گھنٹے حفاظتی سامان بھگو دے، ازدواجی تعلق کے دوران درد، ماہواری کے درمیان خون آنا، یا ماہواری کا اچانک بدل جانا — ان کے لیے ماہرِ امراضِ نسواں چاہیے، کپنگ سیشن نہیں۔ اینڈومیٹریوسس، رسولی اور پی سی او ایس جیسی حالتیں قابلِ علاج ہیں، اور یہ اکثر نظرانداز ہوتی ہیں کیونکہ خواتین کو بتایا جاتا ہے کہ ماہواری کا درد نارمل ہے۔ مہینے میں ایک دن کھو دینا نارمل نہیں۔"),
      paras=[
        ("We would far rather send you for a scan and be wrong than let a treatable condition go unexamined for another year.",
         "ہم آپ کو اسکین کے لیے بھیج کر غلط ثابت ہونا کہیں بہتر سمجھتے ہیں، بجائے اس کے کہ ایک قابلِ علاج حالت مزید ایک سال بغیر معائنے کے رہ جائے۔"),
      ]),
    dict(h2_en="Timing within your cycle", h2_ur="آپ کے دورانیے میں وقت کا انتخاب",
      paras=[
        ("We generally suggest a session in the week <em>before</em> your period rather than during heavy bleeding. Wet cupping during a heavy flow is not sensible, and most women simply feel more comfortable beforehand. If your cycle is irregular, message us and we will work around it rather than hold you to a fixed date.",
         "ہم عام طور پر ماہواری سے <em>پہلے</em> والے ہفتے میں سیشن تجویز کرتے ہیں، نہ کہ زیادہ خون بہنے کے دوران۔ زیادہ بہاؤ کے دوران گیلی حجامہ مناسب نہیں، اور بیشتر خواتین پہلے زیادہ آرام دہ محسوس کرتی ہیں۔ اگر آپ کا دورانیہ بے قاعدہ ہے تو ہمیں پیغام بھیجیں، ہم کسی مقررہ تاریخ پر اصرار کے بجائے آپ کے مطابق وقت طے کریں گے۔"),
      ]),
  ],
  faq=[
    dict(q_en="Will a female practitioner do the session?", q_ur="کیا سیشن خاتون معالج کرے گی؟",
         a_en="Yes. Female patients are seen by a female practitioner, in a private room, and you may bring a family member. Home service is available across Karachi if you prefer.",
         a_ur="جی ہاں۔ خواتین مریضوں کو خاتون معالج دیکھتی ہیں، پرائیویٹ کمرے میں، اور آپ گھر کا کوئی فرد ساتھ لا سکتی ہیں۔ اگر آپ چاہیں تو کراچی بھر میں گھر پر سروس دستیاب ہے۔"),
    dict(q_en="Can I have Hijama during my period?", q_ur="کیا میں ماہواری کے دوران حجامہ کروا سکتی ہوں؟",
         a_en="We usually advise the week before instead. Wet cupping during heavy bleeding is not sensible, and most women find they are more comfortable beforehand.",
         a_ur="ہم عام طور پر اس کے بجائے پہلے والے ہفتے کا مشورہ دیتے ہیں۔ زیادہ خون بہنے کے دوران گیلی حجامہ مناسب نہیں، اور بیشتر خواتین پہلے زیادہ آرام دہ محسوس کرتی ہیں۔"),
    dict(q_en="Will it fix my irregular periods?", q_ur="کیا یہ میری بے قاعدہ ماہواری ٹھیک کر دے گا؟",
         a_en="No, and anyone promising that is overreaching. Irregular cycles have causes — thyroid, PCOS, weight, stress — that need proper assessment. Cupping may ease discomfort; it does not regulate a cycle.",
         a_ur="نہیں، اور جو کوئی اس کا وعدہ کرے وہ حد سے بڑھ رہا ہے۔ بے قاعدہ دورانیے کی وجوہات ہوتی ہیں — تھائیرائیڈ، پی سی او ایس، وزن، ذہنی دباؤ — جن کے لیے مناسب معائنہ چاہیے۔ کپنگ تکلیف کم کر سکتی ہے؛ دورانیے کو باقاعدہ نہیں کرتی۔"),
    dict(q_en="Is it safe if I am trying to conceive?", q_ur="اگر میں حمل کی کوشش کر رہی ہوں تو کیا یہ محفوظ ہے؟",
         a_en="Tell us, and tell us if there is any chance you are already pregnant. We do not perform wet cupping in pregnancy. If you are under fertility treatment, please check with your specialist first.",
         a_ur="ہمیں بتائیں، اور یہ بھی بتائیں کہ کیا آپ کے حاملہ ہونے کا کوئی امکان ہے۔ ہم حمل کے دوران گیلی حجامہ نہیں کرتے۔ اگر آپ زرخیزی کا علاج کروا رہی ہیں تو پہلے اپنے ماہر سے پوچھ لیں۔"),
    dict(q_en="How many sessions would I need?", q_ur="مجھے کتنے سیشن درکار ہوں گے؟",
         a_en="Try one and judge honestly. If it helped, some women repeat it once a cycle for a few months. If it did nothing, we will tell you not to keep paying for it.",
         a_ur="ایک آزمائیں اور دیانتداری سے فیصلہ کریں۔ اگر فائدہ ہوا تو کچھ خواتین چند مہینے تک ہر دورانیے میں ایک بار دہراتی ہیں۔ اگر کوئی فرق نہ پڑا تو ہم آپ کو مزید پیسے خرچ کرنے سے منع کر دیں گے۔"),
  ],
  cta_en="Painful periods, and want to talk privately?",
  cta_ur="ماہواری کا درد، اور نجی طور پر بات کرنا چاہتی ہیں؟",
  cta_body_en="Female practitioner, private room, and home service across Karachi. Message us on WhatsApp — you can ask anything you would rather not say on a phone call, and we will tell you honestly whether this is likely to help or whether you should see a gynaecologist first.",
  cta_body_ur="خاتون معالج، پرائیویٹ کمرہ، اور کراچی بھر میں گھر پر سروس۔ واٹس ایپ پر پیغام بھیجیں — آپ وہ سب پوچھ سکتی ہیں جو فون کال پر کہنا مشکل ہو، اور ہم دیانتداری سے بتائیں گے کہ اس سے فائدہ متوقع ہے یا آپ کو پہلے ماہرِ امراضِ نسواں سے رجوع کرنا چاہیے۔",
  related=REL_WOMEN,
),

# ---------------------------------------------------------------- 4. first time
dict(
  slug="first-time-hijama-guide-for-beginners", target="blog/first-time-hijama-guide-for-beginners.html",
  date=DATE, date_en=DATE_EN, date_ur=DATE_UR,
  eyebrow_en="Getting Started", eyebrow_ur="آغاز",
  title_en="Your First Hijama Session — A Guide for Beginners",
  title_ur="آپ کا پہلا حجامہ سیشن — نئے آنے والوں کے لیے رہنما",
  seo_title="Your First Hijama Session — A Complete Beginner's Guide",
  seo_desc="Booking Hijama for the first time in Karachi? Exactly what happens, whether it hurts, what to eat before, how long the marks last, and what it costs. پہلی بار حجامہ — مکمل رہنمائی، کراچی۔",
  og_desc="Booking Hijama for the first time? Exactly what happens, whether it hurts, what to eat before, and how long the marks last. Karachi clinic.",
  keywords="first time hijama, hijama for beginners, what happens in hijama, does hijama hurt, hijama clinic near me karachi, پہلی بار حجامہ, حجامہ کیسے ہوتا ہے, کیا حجامہ میں درد ہوتا ہے",
  tag_en="Getting Started", tag_ur="آغاز",
  blurb_en="Does it hurt? Should I eat first? How long do the marks stay? Everything a first-timer actually worries about, answered plainly.",
  blurb_ur="کیا درد ہوتا ہے؟ پہلے کھانا چاہیے؟ نشان کتنے دن رہتے ہیں؟ وہ سب کچھ جس کی پہلی بار آنے والے کو فکر ہوتی ہے، سادہ الفاظ میں۔",
  lede_en="Most people booking their first Hijama session have the same three worries, and are slightly embarrassed to ask any of them: will it hurt, will it leave marks people can see, and is it actually clean. They are good questions and they deserve straight answers. Here is exactly what happens from the moment you arrive to the day the marks fade — no mystique, no promises, just what to expect.",
  lede_ur="پہلا حجامہ سیشن بک کرنے والے بیشتر لوگوں کو تین ہی فکریں ہوتی ہیں، اور وہ ان میں سے کوئی پوچھتے ہوئے تھوڑا جھجکتے ہیں: کیا درد ہوگا، کیا ایسے نشان رہ جائیں گے جو لوگوں کو نظر آئیں، اور کیا واقعی صفائی ہوتی ہے۔ یہ اچھے سوال ہیں اور ان کے سیدھے جواب ملنے چاہئیں۔ یہاں بالکل وہ ہے جو آپ کے پہنچنے سے لے کر نشان مٹنے کے دن تک ہوتا ہے — کوئی اسرار نہیں، کوئی وعدے نہیں، صرف توقعات۔",
  sections=[
    dict(h2_en="Before you come", h2_ur="آنے سے پہلے",
      bullets=[
        ("Eat lightly two to three hours before — not a heavy meal, and not completely empty either", "دو تین گھنٹے پہلے ہلکا کھائیں — نہ بھاری کھانا، نہ بالکل خالی پیٹ"),
        ("Drink water through the day; being well hydrated genuinely makes the session easier", "دن بھر پانی پیئیں؛ جسم میں پانی کی مناسب مقدار سیشن کو واقعی آسان بناتی ہے"),
        ("Shower beforehand, and wear loose clothing that opens at the back", "پہلے نہا لیں، اور ڈھیلا لباس پہنیں جو پیچھے سے کھل جائے"),
        ("Bring your prescriptions — we need to know every medicine you take", "اپنے نسخے لائیں — ہمیں ہر وہ دوا جاننی ہے جو آپ لیتے ہیں"),
        ("Tell us if you are pregnant, diabetic, anaemic, or on blood thinners", "بتائیں اگر آپ حاملہ ہیں، ذیابیطس یا خون کی کمی ہے، یا خون پتلا کرنے والی دوا لیتے ہیں"),
      ],
      paras=[
        ("If you are fasting, tell us — the timing can usually be arranged around it, and many patients prefer a session after iftar.",
         "اگر آپ روزے سے ہیں تو بتائیں — وقت عام طور پر اس کے مطابق طے ہو سکتا ہے، اور بہت سے مریض افطار کے بعد کا سیشن پسند کرتے ہیں۔"),
      ]),
    dict(h2_en="What actually happens", h2_ur="اصل میں کیا ہوتا ہے",
      paras=[
        ("First we talk. We ask why you have come, what medicines you take, and what your doctor has said — this is not a formality, it decides whether we proceed at all. Then you lie down comfortably. The area is cleaned with antiseptic. Cups are placed and suction is applied for a few minutes, which draws the skin up; this feels like a firm pull, not a sharp pain. The cups come off, very small superficial incisions are made with a <strong>sterile, single-use blade</strong>, and the cups go back on briefly to draw a small amount of blood. The area is cleaned and dressed. Most sessions take thirty to forty-five minutes in total.",
         "پہلے ہم بات کرتے ہیں۔ ہم پوچھتے ہیں کہ آپ کیوں آئے ہیں، کون سی دوائیں لیتے ہیں، اور آپ کے ڈاکٹر نے کیا کہا — یہ رسمی کارروائی نہیں، اسی سے طے ہوتا ہے کہ ہم آگے بڑھیں یا نہیں۔ پھر آپ آرام سے لیٹتے ہیں۔ جگہ کو جراثیم کش سے صاف کیا جاتا ہے۔ کپ رکھے جاتے ہیں اور چند منٹ سکشن لگایا جاتا ہے، جس سے جلد اوپر کھنچتی ہے؛ یہ ایک مضبوط کھنچاؤ محسوس ہوتا ہے، تیز درد نہیں۔ کپ اتارے جاتے ہیں، <strong>جراثیم سے پاک، ایک بار استعمال ہونے والے بلیڈ</strong> سے بہت باریک سطحی شگاف لگائے جاتے ہیں، اور کپ تھوڑی دیر کے لیے دوبارہ رکھے جاتے ہیں تاکہ تھوڑا سا خون نکل آئے۔ پھر جگہ صاف کر کے پٹی کی جاتی ہے۔ زیادہ تر سیشن کل ملا کر تیس سے پینتالیس منٹ لیتے ہیں۔"),
      ]),
    dict(h2_en="Does it hurt?", h2_ur="کیا درد ہوتا ہے؟",
      paras=[
        ("Honestly: less than most people expect. The suction is a strong pulling sensation. The incisions are very shallow and most patients describe them as a scratch rather than a cut. The part people find surprising is how relaxed they feel afterwards. If at any point it is genuinely painful, say so — we adjust or stop. Nobody should be enduring a session in silence.",
         "دیانتداری سے: بیشتر لوگوں کی توقع سے کم۔ سکشن ایک مضبوط کھنچاؤ کا احساس ہے۔ شگاف بہت سطحی ہوتے ہیں اور اکثر مریض انہیں کٹ کے بجائے خراش بتاتے ہیں۔ لوگوں کو جو بات حیران کرتی ہے وہ یہ ہے کہ بعد میں وہ کتنا پُرسکون محسوس کرتے ہیں۔ اگر کسی بھی لمحے واقعی تکلیف ہو تو کہہ دیں — ہم کم کر دیں گے یا روک دیں گے۔ کسی کو خاموشی سے سیشن برداشت نہیں کرنا چاہیے۔"),
      ]),
    dict(h2_en="The marks, and how long they last", h2_ur="نشان، اور کتنے دن رہتے ہیں",
      paras=[
        ("You will have round marks. They are usually dusky red to purple at first and fade over roughly five to ten days, sometimes a little longer if you bruise easily. They are on the back in most cases, so ordinary clothing covers them. They are not burns and they are not scars. If you have a wedding or a beach trip in a few days, plan around it — plenty of patients do.",
         "آپ کے جسم پر گول نشان بنیں گے۔ یہ عام طور پر پہلے گہرے سرخ سے جامنی ہوتے ہیں اور تقریباً پانچ سے دس دن میں مٹ جاتے ہیں، اگر آپ کو آسانی سے نیل پڑتے ہوں تو کچھ زیادہ۔ بیشتر صورتوں میں یہ کمر پر ہوتے ہیں، اس لیے عام لباس انہیں ڈھانپ لیتا ہے۔ یہ جلنے کے نشان نہیں اور نہ ہی داغ۔ اگر چند دن میں شادی یا ساحل کا پروگرام ہے تو اسی حساب سے وقت رکھیں — بہت سے مریض ایسا کرتے ہیں۔"),
      ]),
    dict(h2_en="Afterwards", h2_ur="بعد میں",
      bullets=[
        ("Rest that evening; no gym, no heavy lifting for about 24 hours", "اُس شام آرام کریں؛ تقریباً 24 گھنٹے جم اور بھاری وزن نہیں"),
        ("Keep the area dry and covered for the rest of the day", "باقی دن جگہ کو خشک اور ڈھکا رکھیں"),
        ("Drink water and eat something nourishing", "پانی پیئیں اور کچھ غذائیت بخش کھائیں"),
        ("Avoid very hot showers, steam rooms and swimming for a day or two", "ایک دو دن بہت گرم شاور، بھاپ اور تیراکی سے بچیں"),
        ("Some tiredness the same evening is normal; feeling unwell for days is not — contact us", "اُسی شام کچھ تھکن معمول ہے؛ کئی دن طبیعت خراب رہنا نہیں — ہم سے رابطہ کریں"),
      ]),
    dict(h2_en="How to judge a clinic before you book", h2_ur="بکنگ سے پہلے کلینک کیسے پرکھیں",
      caution=("Ask one question before you book anywhere: are the blades single-use and opened in front of me? If the answer is anything other than a clear yes, do not book. Cups should be single-use or properly sterilised between patients, gloves should be worn and changed, and sharps should go into a proper container. This is not fussiness — reused blades transmit hepatitis and HIV.",
               "کہیں بھی بکنگ سے پہلے ایک سوال ضرور پوچھیں: کیا بلیڈ ایک بار استعمال کے ہیں اور میرے سامنے کھولے جائیں گے؟ اگر جواب واضح ہاں کے علاوہ کچھ ہو تو بکنگ نہ کریں۔ کپ ایک بار استعمال کے ہوں یا مریضوں کے درمیان ٹھیک سے جراثیم سے پاک کیے جائیں، دستانے پہنے اور بدلے جائیں، اور استعمال شدہ بلیڈ مناسب ڈبے میں جائیں۔ یہ نکتہ چینی نہیں — دوبارہ استعمال شدہ بلیڈ ہیپاٹائٹس اور ایچ آئی وی منتقل کرتے ہیں۔"),
      ),
  ],
  faq=[
    dict(q_en="Does Hijama hurt?", q_ur="کیا حجامہ میں درد ہوتا ہے؟",
         a_en="Less than most first-timers expect. The suction is a strong pulling feeling and the incisions are very shallow — most people describe a scratch rather than a cut. Tell us at any point if it is uncomfortable and we will adjust.",
         a_ur="بیشتر نئے آنے والوں کی توقع سے کم۔ سکشن ایک مضبوط کھنچاؤ ہے اور شگاف بہت سطحی — اکثر لوگ اسے کٹ کے بجائے خراش بتاتے ہیں۔ کسی بھی وقت تکلیف ہو تو بتائیں، ہم کم کر دیں گے۔"),
    dict(q_en="How long do the marks last?", q_ur="نشان کتنے دن رہتے ہیں؟",
         a_en="Usually five to ten days, fading from dark red to light brown. They are not scars and they are almost always in places ordinary clothes cover.",
         a_ur="عام طور پر پانچ سے دس دن، گہرے سرخ سے ہلکے بھورے ہوتے ہوئے۔ یہ داغ نہیں اور تقریباً ہمیشہ ایسی جگہوں پر ہوتے ہیں جنہیں عام لباس ڈھانپ لیتا ہے۔"),
    dict(q_en="Should I eat before my session?", q_ur="کیا سیشن سے پہلے کھانا چاہیے؟",
         a_en="Eat something light two to three hours before. Coming completely empty makes lightheadedness more likely; a heavy meal right before is also unhelpful.",
         a_ur="دو تین گھنٹے پہلے ہلکا کچھ کھائیں۔ بالکل خالی پیٹ آنے سے چکر آنے کا امکان بڑھتا ہے؛ عین پہلے بھاری کھانا بھی مناسب نہیں۔"),
    dict(q_en="How often should a beginner repeat it?", q_ur="نئے آنے والے کو کتنی بار دہرانا چاہیے؟",
         a_en="Have one, then wait and see how you feel over the following weeks. There is no need to commit to a package on day one, and we will not push you into one.",
         a_ur="ایک کروائیں، پھر آنے والے ہفتوں میں دیکھیں کہ آپ کیسا محسوس کرتے ہیں۔ پہلے ہی دن کسی پیکج کا وعدہ ضروری نہیں، اور ہم آپ پر زور نہیں دیں گے۔"),
    dict(q_en="Can you come to my home?", q_ur="کیا آپ میرے گھر آ سکتے ہیں؟",
         a_en="Yes, across most areas of Karachi. Home service suits first-timers who feel more relaxed in their own space, and elderly or less mobile patients. Message us with your area to confirm.",
         a_ur="جی ہاں، کراچی کے بیشتر علاقوں میں۔ گھر پر سروس ان نئے مریضوں کے لیے موزوں ہے جو اپنی جگہ میں زیادہ پُرسکون رہتے ہیں، اور بزرگ یا کم چلنے پھرنے والے مریضوں کے لیے۔ تصدیق کے لیے اپنے علاقے کے ساتھ پیغام بھیجیں۔"),
  ],
  cta_en="Thinking about your first session?",
  cta_ur="اپنے پہلے سیشن کے بارے میں سوچ رہے ہیں؟",
  cta_body_en="Ask us anything before you decide — including the awkward questions. Shaheen Shafi Unani Clinic &amp; Hijama Center, Model Colony, Karachi, with home service across the city. Sterile single-use blades, opened in front of you.",
  cta_body_ur="فیصلہ کرنے سے پہلے ہم سے کچھ بھی پوچھیں — بشمول وہ سوال جو پوچھتے ہوئے جھجک ہو۔ شاہین شافی یونانی کلینک و حجامہ سینٹر، ماڈل کالونی، کراچی، شہر بھر میں گھر پر سروس کے ساتھ۔ جراثیم سے پاک، ایک بار استعمال ہونے والے بلیڈ، آپ کے سامنے کھولے جاتے ہیں۔",
  related=REL_FIRST,
),
]


if __name__ == "__main__":
    print("Generating %d articles\n" % len(TOPICS))
    for t in TOPICS:
        build(t)
        write_queue_entry(t)
    print("\nQueued. publish-next.js will put them live one per run "
          "(cron: 05:00, 11:00, 16:00 UTC).")
