#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article batch 2, 2026-09-03.

Chosen for high commercial intent rather than informational volume, following
the same rule as batch 1: the site already ranks 8.5 for "hijama clinic near
me" and 6.7 for "hijama center near me for ladies", so the people arriving are
first-timers deciding whether to trust a practitioner. These four answer the
decisions they are actually making.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_article import build, write_queue_entry  # noqa: E402

DATE = "2026-09-03"
DATE_EN = "3 September 2026"
DATE_UR = "3 ستمبر 2026"

REL_GUIDE = [
    dict(href="what-is-hijama.html",
         t_en="What Is Hijama?", t_ur="حجامہ کیا ہے؟",
         d_en="The plain-language explanation, start here.",
         d_ur="سادہ زبان میں وضاحت، یہیں سے شروع کریں۔"),
    dict(href="hijama-side-effects-and-who-should-avoid.html",
         t_en="Side Effects & Who Should Avoid It", t_ur="مضر اثرات اور کن کو گریز کرنا چاہیے",
         d_en="An honest list of risks and the people we turn away.",
         d_ur="خطرات کی دیانتدار فہرست اور وہ لوگ جنہیں ہم منع کرتے ہیں۔"),
    dict(href="hijama-aftercare-safety.html",
         t_en="Aftercare & Safety", t_ur="بعد کی دیکھ بھال اور حفاظت",
         d_en="What to do in the 48 hours after a session.",
         d_ur="سیشن کے بعد 48 گھنٹوں میں کیا کرنا ہے۔"),
]

TOPICS = [

dict(
  slug="how-often-should-you-get-hijama", target="blog/how-often-should-you-get-hijama.html",
  date=DATE, date_en=DATE_EN, date_ur=DATE_UR,
  eyebrow_en="Practical Guidance", eyebrow_ur="عملی رہنمائی",
  title_en="How Often Should You Get Hijama? A Realistic Schedule",
  title_ur="حجامہ کتنی بار کروانا چاہیے؟ ایک حقیقت پسندانہ شیڈول",
  seo_title="How Often Should You Get Hijama? A Realistic Schedule",
  seo_desc="Every month? Twice a year? An honest answer on Hijama frequency in Karachi — why more is not better, and how to tell if it is working for you. حجامہ کتنی بار کروائیں، کراچی۔",
  og_desc="Every month? Twice a year? An honest answer on how often to have Hijama — and why more is not better.",
  keywords="how often hijama, hijama frequency, hijama every month, hijama schedule, hijama karachi, حجامہ کتنی بار, حجامہ کا وقفہ, حجامہ شیڈول",
  tag_en="Practical Guidance", tag_ur="عملی رہنمائی",
  blurb_en="Some people are told every month, some every week. Neither is a rule. How to pick a sensible interval — and how to tell when to stop.",
  blurb_ur="کچھ کو ہر مہینہ بتایا جاتا ہے، کچھ کو ہر ہفتہ۔ دونوں اصول نہیں۔ مناسب وقفہ کیسے چنیں — اور کب رکنا ہے۔",
  lede_en="This is the question we are asked most, and the one most often answered badly. You will hear every month, every forty days, twice a year, once a season — usually stated with great confidence and no reasoning. The honest answer is that <strong>frequency depends on why you are coming</strong>, and that more is not better. Cupping removes a small amount of blood each time; doing it too often is not a shortcut to feeling better, and for some people it is actively unwise.",
  lede_ur="یہ وہ سوال ہے جو ہم سے سب سے زیادہ پوچھا جاتا ہے، اور اکثر سب سے خراب جواب پاتا ہے۔ آپ سنیں گے ہر مہینہ، ہر چالیس دن، سال میں دو بار، ہر موسم میں ایک بار — عام طور پر بڑے اعتماد سے اور بغیر کسی دلیل کے۔ دیانتدار جواب یہ ہے کہ <strong>وقفہ اس پر منحصر ہے کہ آپ کیوں آ رہے ہیں</strong>، اور یہ کہ زیادہ کرنا بہتر نہیں۔ حجامہ ہر بار تھوڑا سا خون نکالتا ہے؛ اسے بہت زیادہ کرنا بہتر محسوس کرنے کا شارٹ کٹ نہیں، اور کچھ لوگوں کے لیے یہ واقعی غیر دانشمندانہ ہے۔",
  sections=[
    dict(h2_en="A sensible starting point", h2_ur="ایک معقول ابتدائی نقطہ",
      bullets=[
        ("General wellbeing, no specific complaint: two to four times a year is plenty", "عمومی صحت، کوئی خاص شکایت نہیں: سال میں دو سے چار بار کافی ہے"),
        ("A specific ache you are working on: an initial session, then reassess after three to four weeks", "کوئی مخصوص تکلیف: پہلا سیشن، پھر تین چار ہفتے بعد دوبارہ جائزہ"),
        ("Ongoing maintenance once something has improved: every eight to twelve weeks", "بہتری کے بعد برقرار رکھنے کے لیے: ہر آٹھ سے بارہ ہفتے"),
        ("Never twice within the same fortnight on the same area", "ایک ہی جگہ پر ایک پندرہ دن میں دو بار ہرگز نہیں"),
      ],
      paras=[
        ("If someone is proposing a weekly course of wet cupping for months on end, ask them why. There is rarely a good answer, and there is usually a package being sold.",
         "اگر کوئی مہینوں تک ہفتہ وار گیلی حجامہ کا کورس تجویز کر رہا ہے تو وجہ پوچھیں۔ اچھا جواب شاذ و نادر ہی ہوتا ہے، اور عام طور پر کوئی پیکج بیچا جا رہا ہوتا ہے۔"),
      ]),
    dict(h2_en="Why more is not better", h2_ur="زیادہ کیوں بہتر نہیں",
      caution=("Each wet cupping session removes a small quantity of blood. Repeated too frequently — particularly in people who are already anaemic, menstruating heavily, elderly, underweight or donating blood — this can leave you tired, lightheaded and iron-depleted. Anaemia is common in Pakistan and often undiagnosed. If you feel drained for days after a session, that is a signal to lengthen the interval, not to book another one.",
               "ہر گیلی حجامہ کے سیشن میں تھوڑی مقدار میں خون نکلتا ہے۔ بہت زیادہ بار دہرانے سے — خاص طور پر ان لوگوں میں جنہیں پہلے ہی خون کی کمی ہو، جن کی ماہواری میں زیادہ خون آتا ہو، بزرگ، کم وزن یا خون عطیہ کرنے والے — آپ تھکے، چکراتے اور فولاد کی کمی کا شکار ہو سکتے ہیں۔ پاکستان میں خون کی کمی عام ہے اور اکثر تشخیص نہیں ہوتی۔ اگر سیشن کے بعد آپ کئی دن نڈھال محسوس کریں تو یہ وقفہ بڑھانے کا اشارہ ہے، دوسرا سیشن بک کرانے کا نہیں۔"),
      ),
    dict(h2_en="How to tell if it is working", h2_ur="کیسے جانیں کہ فائدہ ہو رہا ہے",
      paras=[
        ("Decide before the session what you are hoping to change, and be specific — not &ldquo;feel better&rdquo; but &ldquo;climb the stairs without my knee aching&rdquo; or &ldquo;sleep through the night&rdquo;. Then judge honestly at three weeks. If two properly spaced sessions produce nothing you can name, cupping is probably not the right tool for your problem, and we would rather tell you that than keep taking your booking.",
         "سیشن سے پہلے طے کریں کہ آپ کیا بدلنا چاہتے ہیں، اور واضح رہیں — &rdquo;بہتر محسوس کرنا&ldquo; نہیں بلکہ &rdquo;گھٹنے کے درد کے بغیر سیڑھیاں چڑھنا&ldquo; یا &rdquo;رات بھر سونا&ldquo;۔ پھر تین ہفتے بعد دیانتداری سے فیصلہ کریں۔ اگر مناسب وقفے سے دو سیشن کے بعد بھی کوئی ایسی چیز نہ ہو جسے آپ بیان کر سکیں تو غالباً کپنگ آپ کے مسئلے کا صحیح حل نہیں، اور ہم آپ کی بکنگ لیتے رہنے کے بجائے یہ بتانا پسند کریں گے۔"),
      ]),
  ],
  faq=[
    dict(q_en="Is monthly Hijama safe?", q_ur="کیا ہر ماہ حجامہ محفوظ ہے؟",
         a_en="For a healthy adult with good iron levels, occasional monthly sessions are usually tolerated. As a permanent routine it is more than most people need, and it is not advisable if you are anaemic, elderly, underweight or menstruating heavily.",
         a_ur="اچھے فولاد کی سطح والے صحت مند بالغ کے لیے کبھی کبھار ماہانہ سیشن عام طور پر برداشت ہو جاتے ہیں۔ مستقل معمول کے طور پر یہ بیشتر لوگوں کی ضرورت سے زیادہ ہے، اور اگر آپ کو خون کی کمی ہو، آپ بزرگ، کم وزن ہوں یا ماہواری میں زیادہ خون آتا ہو تو یہ مناسب نہیں۔"),
    dict(q_en="Should I follow the Sunnah days every month?", q_ur="کیا مجھے ہر ماہ سنت کے دنوں پر عمل کرنا چاہیے؟",
         a_en="Many patients prefer to time a session on the 17th, 19th or 21st of the lunar month. That is a matter of personal practice and we are glad to schedule around it — but the medical spacing guidance above still applies.",
         a_ur="بہت سے مریض قمری مہینے کی 17، 19 یا 21 تاریخ کو سیشن رکھنا پسند کرتے ہیں۔ یہ ذاتی عمل کا معاملہ ہے اور ہم خوشی سے اس کے مطابق وقت رکھتے ہیں — لیکن اوپر دی گئی طبی وقفے کی رہنمائی پھر بھی لاگو رہتی ہے۔"),
    dict(q_en="Can I have Hijama and donate blood in the same month?", q_ur="کیا میں ایک ہی مہینے میں حجامہ اور خون کا عطیہ دونوں کر سکتا ہوں؟",
         a_en="We would not advise it. Space them well apart and prioritise the donation. Tell us if you donate regularly so we can plan a longer interval.",
         a_ur="ہم اس کا مشورہ نہیں دیں گے۔ ان کے درمیان اچھا وقفہ رکھیں اور عطیے کو ترجیح دیں۔ اگر آپ باقاعدگی سے عطیہ کرتے ہیں تو ہمیں بتائیں تاکہ ہم لمبا وقفہ رکھ سکیں۔"),
    dict(q_en="How long until I can judge the result?", q_ur="نتیجہ جانچنے میں کتنا وقت لگے گا؟",
         a_en="Give it three weeks and one repeat session. If you cannot name a specific change by then, it is reasonable to stop.",
         a_ur="تین ہفتے اور ایک دوبارہ سیشن دیں۔ اگر تب تک آپ کوئی مخصوص تبدیلی بیان نہ کر سکیں تو رک جانا معقول ہے۔"),
    dict(q_en="Do you sell session packages?", q_ur="کیا آپ سیشن کے پیکج بیچتے ہیں؟",
         a_en="We do not push them. A package bought before you know whether cupping helps you is a commitment made in the dark. Come once, judge, then decide.",
         a_ur="ہم ان پر زور نہیں دیتے۔ یہ جانے بغیر پیکج خریدنا کہ کپنگ آپ کو فائدہ دیتی ہے یا نہیں، اندھیرے میں کیا گیا وعدہ ہے۔ ایک بار آئیں، پرکھیں، پھر فیصلہ کریں۔"),
  ],
  cta_en="Not sure how often is right for you?",
  cta_ur="یقین نہیں کہ آپ کے لیے کتنا وقفہ درست ہے؟",
  cta_body_en="Tell us why you are considering Hijama and what you have tried already. Shaheen Shafi Unani Clinic &amp; Hijama Center, Model Colony, Karachi — clinic or home visit. If a longer gap or no session at all is the right advice, that is what you will get.",
  cta_body_ur="ہمیں بتائیں کہ آپ حجامہ کیوں سوچ رہے ہیں اور اب تک کیا آزما چکے ہیں۔ شاہین شافی یونانی کلینک و حجامہ سینٹر، ماڈل کالونی، کراچی — کلینک یا گھر پر۔ اگر لمبا وقفہ یا بالکل سیشن نہ کروانا درست مشورہ ہوا تو آپ کو وہی ملے گا۔",
  related=REL_GUIDE,
),

dict(
  slug="choosing-a-trustworthy-hijama-practitioner", target="blog/choosing-a-trustworthy-hijama-practitioner.html",
  date=DATE, date_en=DATE_EN, date_ur=DATE_UR,
  eyebrow_en="Safety First", eyebrow_ur="حفاظت اوّل",
  title_en="Choosing a Trustworthy Hijama Practitioner — A Checklist",
  title_ur="قابلِ اعتماد حجامہ معالج کا انتخاب — ایک چیک لسٹ",
  seo_title="Choosing a Trustworthy Hijama Practitioner — A Safety Checklist",
  seo_desc="Before you book Hijama anywhere in Karachi, check these seven things. Single-use blades, sharps disposal, and the questions a good practitioner will happily answer. محفوظ حجامہ سینٹر کیسے چنیں، کراچی۔",
  og_desc="Before you book Hijama anywhere, check these seven things — starting with single-use blades opened in front of you.",
  keywords="safe hijama karachi, hijama hygiene, single use blades hijama, best hijama center karachi, how to choose hijama practitioner, محفوظ حجامہ, حجامہ صفائی, بہترین حجامہ سینٹر کراچی",
  tag_en="Safety First", tag_ur="حفاظت اوّل",
  blurb_en="Reused blades transmit hepatitis. Seven checks to make before you let anyone cup you — and the answers you should expect.",
  blurb_ur="دوبارہ استعمال شدہ بلیڈ ہیپاٹائٹس منتقل کرتے ہیں۔ کسی کو حجامہ کرنے دینے سے پہلے سات جانچیں — اور متوقع جوابات۔",
  lede_en="Hijama involves breaking the skin. That single fact should govern how you choose where to have it done. Pakistan carries one of the world's heaviest hepatitis C burdens, and unsterile instruments are a documented route of transmission. A good practitioner will not be offended by any question on this page — they will be pleased you asked. Anyone who bristles, deflects or hurries you past it has told you what you needed to know.",
  lede_ur="حجامہ میں جلد کاٹی جاتی ہے۔ صرف یہی ایک بات طے کرنی چاہیے کہ آپ اسے کہاں کروائیں۔ پاکستان دنیا میں ہیپاٹائٹس سی کے سب سے زیادہ بوجھ والے ممالک میں سے ہے، اور غیر جراثیم سے پاک آلات اس کی منتقلی کا ثابت شدہ راستہ ہیں۔ ایک اچھا معالج اس صفحے کے کسی سوال پر ناراض نہیں ہوگا — بلکہ خوش ہوگا کہ آپ نے پوچھا۔ جو کوئی چڑ جائے، بات بدلے یا جلدی آگے بڑھ جائے، اُس نے آپ کو وہ بتا دیا جو جاننا ضروری تھا۔",
  sections=[
    dict(h2_en="The seven checks", h2_ur="سات جانچیں",
      bullets=[
        ("Blades are single-use and the packet is opened in front of you — this is non-negotiable", "بلیڈ ایک بار استعمال کے ہوں اور پیکٹ آپ کے سامنے کھولا جائے — اس پر کوئی سمجھوتہ نہیں"),
        ("Cups are single-use, or properly sterilised between patients — not merely rinsed", "کپ ایک بار استعمال کے ہوں، یا مریضوں کے درمیان ٹھیک سے جراثیم سے پاک کیے جائیں — صرف دھوئے نہیں"),
        ("Gloves are worn and changed between patients", "دستانے پہنے جائیں اور ہر مریض کے بعد بدلے جائیں"),
        ("Used blades go into a proper sharps container, not a bin", "استعمال شدہ بلیڈ مناسب شارپس ڈبے میں جائیں، عام کوڑے دان میں نہیں"),
        ("The practitioner asks about your medicines, conditions and pregnancy before starting", "معالج شروع کرنے سے پہلے آپ کی دوائیں، بیماریاں اور حمل کے بارے میں پوچھے"),
        ("They are willing to refuse you — a practitioner who never says no is not assessing anyone", "وہ آپ کو منع کرنے پر تیار ہوں — جو معالج کبھی انکار نہ کرے وہ کسی کا معائنہ نہیں کر رہا"),
        ("Women are seen by a female practitioner in a private room, if that matters to you", "اگر آپ کے لیے اہم ہے تو خواتین کو خاتون معالج پرائیویٹ کمرے میں دیکھے"),
      ]),
    dict(h2_en="Claims that should worry you", h2_ur="وہ دعوے جو تشویش کا باعث ہوں",
      caution=("Walk away from anyone who promises to cure cancer, diabetes, infertility or a chronic disease with cupping; who tells you to stop your prescribed medication; who offers a large discount for booking a long package today; or who cannot tell you what is in the room by way of sterilisation. These are not eccentricities. They are the warning signs that precede real harm.",
               "اُس شخص سے دور رہیں جو کپنگ سے کینسر، ذیابیطس، بانجھ پن یا کسی دائمی مرض کے علاج کا وعدہ کرے؛ جو آپ کو تجویز کردہ دوا بند کرنے کو کہے؛ جو آج لمبا پیکج بک کرانے پر بڑی رعایت پیش کرے؛ یا جو یہ نہ بتا سکے کہ کمرے میں جراثیم کشی کا کیا انتظام ہے۔ یہ محض عجیب باتیں نہیں۔ یہ وہ انتباہی علامات ہیں جو حقیقی نقصان سے پہلے آتی ہیں۔"),
      ),
    dict(h2_en="What we do, so you can compare", h2_ur="ہم کیا کرتے ہیں، تاکہ آپ موازنہ کر سکیں",
      paras=[
        ("Sterile single-use blades, opened in front of you. Gloves changed between patients. A sharps container in the room. A conversation about your medicines and history before anything begins — and a genuine willingness to send you to a doctor instead when that is the right answer. Female patients are seen by a female practitioner in a private room. You are welcome to ask to see any of it.",
         "جراثیم سے پاک، ایک بار استعمال ہونے والے بلیڈ، آپ کے سامنے کھولے جاتے ہیں۔ ہر مریض کے بعد دستانے بدلے جاتے ہیں۔ کمرے میں شارپس ڈبہ موجود ہے۔ کچھ شروع کرنے سے پہلے آپ کی دواؤں اور تاریخ کے بارے میں گفتگو — اور جہاں یہی درست جواب ہو، آپ کو ڈاکٹر کے پاس بھیجنے کی حقیقی آمادگی۔ خواتین مریضوں کو خاتون معالج پرائیویٹ کمرے میں دیکھتی ہیں۔ آپ ان میں سے کچھ بھی دیکھنے کی درخواست کر سکتے ہیں۔"),
      ]),
  ],
  faq=[
    dict(q_en="How do I know the blade is really new?", q_ur="مجھے کیسے پتا چلے کہ بلیڈ واقعی نیا ہے؟",
         a_en="Ask for the sealed packet to be opened in front of you. Any practitioner worth trusting will do this without hesitation, every time, for every patient.",
         a_ur="درخواست کریں کہ سربمہر پیکٹ آپ کے سامنے کھولا جائے۔ کوئی بھی قابلِ اعتماد معالج ہر بار، ہر مریض کے لیے، بلا جھجک ایسا کرے گا۔"),
    dict(q_en="Is hepatitis really a risk from cupping?", q_ur="کیا کپنگ سے واقعی ہیپاٹائٹس کا خطرہ ہے؟",
         a_en="From properly performed cupping with single-use blades, no. From reused or improperly sterilised instruments, yes — and Pakistan has a high background rate of hepatitis C, which makes the precaution more important here, not less.",
         a_ur="ایک بار استعمال ہونے والے بلیڈ کے ساتھ صحیح طریقے سے کی گئی کپنگ سے، نہیں۔ دوبارہ استعمال شدہ یا ناقص جراثیم کشی والے آلات سے، جی ہاں — اور پاکستان میں ہیپاٹائٹس سی کی شرح زیادہ ہے، جس سے یہاں یہ احتیاط زیادہ اہم ہو جاتی ہے، کم نہیں۔"),
    dict(q_en="Should a practitioner ever refuse to treat me?", q_ur="کیا کسی معالج کو مجھے علاج سے انکار کرنا چاہیے؟",
         a_en="Yes, and it is a good sign. Pregnancy, active infection, certain blood disorders, blood thinners and severe anaemia are all reasons to decline or refer. A practitioner who accepts everyone is not examining anyone.",
         a_ur="جی ہاں، اور یہ اچھی علامت ہے۔ حمل، فعال انفیکشن، خون کے بعض امراض، خون پتلا کرنے والی دوائیں اور شدید خون کی کمی — یہ سب انکار یا ریفر کرنے کی وجوہات ہیں۔ جو معالج سب کو قبول کر لے وہ کسی کا معائنہ نہیں کر رہا۔"),
    dict(q_en="Is a home visit less hygienic than a clinic?", q_ur="کیا گھر پر سروس کلینک سے کم صاف ہوتی ہے؟",
         a_en="It does not have to be. The same single-use blades, gloves and sharps container travel with the practitioner. Ask the same questions you would ask at a clinic.",
         a_ur="ضروری نہیں۔ وہی ایک بار استعمال ہونے والے بلیڈ، دستانے اور شارپس ڈبہ معالج کے ساتھ آتے ہیں۔ وہی سوال پوچھیں جو آپ کلینک میں پوچھتے۔"),
    dict(q_en="What if I have already had cupping somewhere unhygienic?", q_ur="اگر میں پہلے کسی غیر صاف جگہ کپنگ کروا چکا ہوں تو؟",
         a_en="Please get tested for hepatitis B and C. It is a simple blood test, widely available in Karachi, and both are treatable — far more so when found early.",
         a_ur="براہِ کرم ہیپاٹائٹس بی اور سی کا ٹیسٹ کروائیں۔ یہ ایک سادہ خون کا ٹیسٹ ہے، کراچی میں عام دستیاب ہے، اور دونوں قابلِ علاج ہیں — خاص طور پر جب جلد پتا چل جائے۔"),
  ],
  cta_en="Ask us the hard questions before you book",
  cta_ur="بکنگ سے پہلے ہم سے مشکل سوال پوچھیں",
  cta_body_en="We would rather answer ten questions than have you take a risk anywhere. Shaheen Shafi Unani Clinic &amp; Hijama Center, Model Colony, Karachi — sterile single-use blades opened in front of you, clinic or home visit across the city.",
  cta_body_ur="ہم چاہیں گے کہ آپ دس سوال پوچھیں بجائے اس کے کہ کہیں خطرہ مول لیں۔ شاہین شافی یونانی کلینک و حجامہ سینٹر، ماڈل کالونی، کراچی — جراثیم سے پاک، ایک بار استعمال ہونے والے بلیڈ آپ کے سامنے کھولے جاتے ہیں، شہر بھر میں کلینک یا گھر پر۔",
  related=REL_GUIDE,
),

dict(
  slug="ramadan-hijama-guidance-timing-fasting", target="blog/ramadan-hijama-guidance-timing-fasting.html",
  date=DATE, date_en=DATE_EN, date_ur=DATE_UR,
  eyebrow_en="Ramadan Guidance", eyebrow_ur="رمضان رہنمائی",
  title_en="Hijama in Ramadan — Timing, Fasting & Practical Advice",
  title_ur="رمضان میں حجامہ — وقت، روزہ اور عملی مشورے",
  seo_title="Hijama in Ramadan — Timing, Fasting & Practical Advice",
  seo_desc="Can you have Hijama while fasting? Practical guidance for Ramadan in Karachi — why we schedule after iftar, hydration, and who should wait until after Eid. رمضان میں حجامہ، کراچی۔",
  og_desc="Can you have Hijama while fasting? Practical Ramadan guidance — why we schedule after iftar, and who should wait.",
  keywords="hijama in ramadan, cupping while fasting, hijama after iftar, ramadan hijama karachi, does hijama break fast, رمضان حجامہ, روزے میں حجامہ, افطار کے بعد حجامہ",
  tag_en="Ramadan Guidance", tag_ur="رمضان رہنمائی",
  blurb_en="Why we book after iftar, how to hydrate through the day, and the people we ask to wait until after Eid.",
  blurb_ur="ہم افطار کے بعد کیوں بک کرتے ہیں، دن بھر پانی کیسے پورا کریں، اور وہ لوگ جنہیں ہم عید کے بعد تک انتظار کا کہتے ہیں۔",
  lede_en="Every Ramadan we are asked the same two questions: does Hijama break the fast, and is it safe to have it while fasting. The first is a matter of religious ruling and scholars have differed on it, which is why we do not issue rulings — ask someone qualified to give one. The second is a practical question and we can answer it clearly: <strong>having wet cupping late in a long fasting day, dehydrated and without food, is not a good idea</strong>. Almost everything below follows from that.",
  lede_ur="ہر رمضان ہم سے یہی دو سوال پوچھے جاتے ہیں: کیا حجامہ سے روزہ ٹوٹ جاتا ہے، اور کیا روزے کی حالت میں یہ محفوظ ہے۔ پہلا شرعی حکم کا معاملہ ہے اور علما کا اس میں اختلاف رہا ہے، اسی لیے ہم فتویٰ نہیں دیتے — کسی اہل شخص سے پوچھیں۔ دوسرا عملی سوال ہے اور اس کا جواب ہم واضح دے سکتے ہیں: <strong>لمبے روزے کے آخری حصے میں، پانی کی کمی اور بھوک کے ساتھ گیلی حجامہ کروانا اچھا خیال نہیں</strong>۔ نیچے کی تقریباً ہر بات اسی سے نکلتی ہے۔",
  sections=[
    dict(h2_en="Why we schedule after iftar", h2_ur="ہم افطار کے بعد کیوں وقت دیتے ہیں",
      paras=[
        ("A Karachi fasting day is long and hot, and by late afternoon most people are meaningfully dehydrated. Wet cupping on top of that makes lightheadedness, weakness and fainting far more likely. After iftar you have eaten, you have had water, and your body is in a much better state to handle a session comfortably. It is the same procedure — it simply goes better.",
         "کراچی میں روزے کا دن لمبا اور گرم ہوتا ہے، اور سہ پہر تک بیشتر لوگوں میں پانی کی نمایاں کمی ہو چکی ہوتی ہے۔ اس کے اوپر گیلی حجامہ چکر آنے، کمزوری اور بیہوشی کے امکانات کہیں بڑھا دیتی ہے۔ افطار کے بعد آپ نے کھا لیا ہوتا ہے، پانی پی لیا ہوتا ہے، اور آپ کا جسم سیشن کو آرام سے برداشت کرنے کی بہت بہتر حالت میں ہوتا ہے۔ عمل وہی ہے — بس بہتر گزرتا ہے۔"),
        ("Practically, we keep evening slots through Ramadan, and many families prefer a session after taraweeh. Home visits are popular in this month for exactly that reason.",
         "عملی طور پر ہم رمضان بھر شام کے اوقات رکھتے ہیں، اور بہت سے گھرانے تراویح کے بعد سیشن پسند کرتے ہیں۔ اسی وجہ سے اس مہینے گھر پر سروس زیادہ مقبول رہتی ہے۔"),
      ]),
    dict(h2_en="Hydration through the month", h2_ur="پورے مہینے پانی کا خیال",
      bullets=[
        ("Drink steadily between iftar and suhoor, not all at once at iftar", "افطار اور سحری کے درمیان مسلسل پانی پیئیں، افطار پر ایک ساتھ سب نہیں"),
        ("Go lighter on tea and coffee after iftar — both increase fluid loss", "افطار کے بعد چائے اور کافی کم کریں — دونوں پانی کا اخراج بڑھاتی ہیں"),
        ("Eat something with salt and fluid at suhoor, not just bread and tea", "سحری میں صرف روٹی اور چائے نہیں، نمک اور پانی والی کوئی چیز کھائیں"),
        ("Do not book a session on a day you have slept badly or skipped suhoor", "جس دن نیند خراب ہوئی ہو یا سحری چھوٹ گئی ہو، اُس دن سیشن بک نہ کریں"),
      ]),
    dict(h2_en="Who should wait until after Eid", h2_ur="کن کو عید کے بعد تک انتظار کرنا چاہیے",
      caution=("If you are anaemic, elderly, diabetic with unstable readings, pregnant, recovering from illness, or you already find fasting physically hard this year, wait. Ramadan is a demanding month on the body without adding blood loss to it. Nothing is gained by pushing through, and we will say so if you ask.",
               "اگر آپ کو خون کی کمی ہے، آپ بزرگ ہیں، ذیابیطس بے قابو ہے، آپ حاملہ ہیں، بیماری سے صحتیاب ہو رہے ہیں، یا اس سال روزہ رکھنا پہلے ہی جسمانی طور پر مشکل لگ رہا ہے — تو انتظار کریں۔ رمضان جسم پر ویسے ہی سخت مہینہ ہے، اس پر خون کا اخراج بڑھانے کی ضرورت نہیں۔ زبردستی کرنے سے کچھ حاصل نہیں ہوتا، اور اگر آپ پوچھیں گے تو ہم یہی کہیں گے۔"),
      ),
  ],
  faq=[
    dict(q_en="Does Hijama break the fast?", q_ur="کیا حجامہ سے روزہ ٹوٹ جاتا ہے؟",
         a_en="Scholars have differed, and we do not issue religious rulings. Ask a qualified scholar you trust. Practically, scheduling after iftar makes the question moot and is better for your body anyway.",
         a_ur="علما کا اختلاف رہا ہے، اور ہم شرعی فتویٰ نہیں دیتے۔ کسی قابلِ اعتماد اہل عالم سے پوچھیں۔ عملی طور پر، افطار کے بعد وقت رکھنے سے یہ سوال ختم ہو جاتا ہے اور یہ آپ کے جسم کے لیے بھی بہتر ہے۔"),
    dict(q_en="Can I have Hijama during the day while fasting?", q_ur="کیا میں روزے کی حالت میں دن کو حجامہ کروا سکتا ہوں؟",
         a_en="We advise against it in Karachi's climate. Dehydration plus blood loss is how people faint. We will offer you an evening slot instead.",
         a_ur="کراچی کے موسم میں ہم اس کے خلاف مشورہ دیتے ہیں۔ پانی کی کمی کے ساتھ خون کا اخراج ہی وہ چیز ہے جس سے لوگ بیہوش ہوتے ہیں۔ ہم آپ کو اس کے بجائے شام کا وقت دیں گے۔"),
    dict(q_en="Is Hijama recommended on particular days in Ramadan?", q_ur="کیا رمضان میں کسی خاص دن حجامہ کا مشورہ ہے؟",
         a_en="Many patients prefer the 17th, 19th or 21st of the lunar month as a general practice. That is personal observance; from a safety point of view the timing that matters is after iftar, not the date.",
         a_ur="بہت سے مریض عمومی طور پر قمری مہینے کی 17، 19 یا 21 تاریخ پسند کرتے ہیں۔ یہ ذاتی عمل ہے؛ حفاظت کے نقطۂ نظر سے اہم وقت افطار کے بعد ہونا ہے، تاریخ نہیں۔"),
    dict(q_en="Will I be too weak to fast the next day?", q_ur="کیا اگلے دن میں روزہ رکھنے کے لیے بہت کمزور ہوں گا؟",
         a_en="Most people are fine if they eat and drink properly after the session and at suhoor. If you felt drained after previous sessions, schedule for the last days of Ramadan or after Eid.",
         a_ur="بیشتر لوگ ٹھیک رہتے ہیں اگر سیشن کے بعد اور سحری میں ٹھیک سے کھا پی لیں۔ اگر پچھلے سیشنوں کے بعد آپ نڈھال محسوس کرتے رہے ہوں تو رمضان کے آخری دنوں یا عید کے بعد وقت رکھیں۔"),
    dict(q_en="Do you offer home visits during Ramadan?", q_ur="کیا آپ رمضان میں گھر پر سروس دیتے ہیں؟",
         a_en="Yes, and they are especially popular in this month — after iftar or after taraweeh, without anyone having to travel. Message us with your area.",
         a_ur="جی ہاں، اور اس مہینے یہ خاص طور پر مقبول ہیں — افطار کے بعد یا تراویح کے بعد، بغیر کسی کو سفر کیے۔ اپنے علاقے کے ساتھ ہمیں پیغام بھیجیں۔"),
  ],
  cta_en="Planning a session this Ramadan?",
  cta_ur="اس رمضان سیشن کا ارادہ ہے؟",
  cta_body_en="Evening slots after iftar and after taraweeh, at the clinic in Model Colony or at your home anywhere in Karachi. Tell us how your fasting is going this year and we will advise honestly on timing — including telling you to wait if that is the right answer.",
  cta_body_ur="افطار اور تراویح کے بعد شام کے اوقات، ماڈل کالونی کے کلینک میں یا کراچی میں کہیں بھی آپ کے گھر پر۔ ہمیں بتائیں کہ اس سال آپ کے روزے کیسے جا رہے ہیں، ہم وقت کے بارے میں دیانتدار مشورہ دیں گے — بشمول یہ کہ اگر انتظار کرنا درست ہو تو وہی کہیں گے۔",
  related=REL_GUIDE,
),

dict(
  slug="hijama-for-asthma-respiratory-wellness", target="blog/hijama-for-asthma-respiratory-wellness.html",
  date=DATE, date_en=DATE_EN, date_ur=DATE_UR,
  eyebrow_en="Complementary Care", eyebrow_ur="معاون علاج",
  title_en="Hijama for Asthma & Respiratory Wellness — Read This First",
  title_ur="دمہ اور تنفس کی صحت کے لیے حجامہ — پہلے یہ پڑھیں",
  seo_title="Hijama for Asthma & Respiratory Wellness — Read This First",
  seo_desc="Asthma in Karachi's air? An honest guide to Hijama and breathing — why your inhaler is not negotiable, and where cupping may sit alongside it. دمہ کے لیے حجامہ، کراچی۔",
  og_desc="An honest guide to Hijama and asthma — why your inhaler is not negotiable, and where cupping may sit alongside it.",
  keywords="hijama for asthma, cupping for breathing, asthma karachi treatment, hijama chest congestion, دمہ حجامہ, سانس کی تکلیف حجامہ, دمہ کا علاج کراچی",
  tag_en="Complementary Care", tag_ur="معاون علاج",
  blurb_en="Karachi's air is hard on the chest. What cupping may ease around the ribs and shoulders — and the one thing you must never stop.",
  blurb_ur="کراچی کی ہوا سینے پر بھاری ہے۔ کپنگ پسلیوں اور کندھوں کے گرد کیا آرام دے سکتی ہے — اور وہ ایک چیز جو کبھی نہ چھوڑیں۔",
  lede_en="Karachi's dust, traffic fumes and winter smog make breathing harder for a great many people, and asthma is common here. We are asked whether Hijama helps. The single most important sentence on this page is this: <strong>never reduce or stop your inhaler or prescribed asthma medication</strong> because of cupping or anything else you read online. Asthma kills people who stop their preventer. Within that absolute limit, some patients find cupping across the upper back eases the muscular tightness that comes with laboured breathing.",
  lede_ur="کراچی کی گرد، ٹریفک کا دھواں اور سردیوں کی اسموگ بہت سے لوگوں کے لیے سانس لینا مشکل بنا دیتی ہے، اور یہاں دمہ عام ہے۔ ہم سے پوچھا جاتا ہے کہ کیا حجامہ مدد دیتا ہے۔ اس صفحے کا سب سے اہم جملہ یہ ہے: <strong>کپنگ یا آن لائن پڑھی کسی بھی چیز کی وجہ سے اپنا انہیلر یا دمہ کی تجویز کردہ دوا ہرگز کم یا بند نہ کریں</strong>۔ دمہ اُن لوگوں کی جان لیتا ہے جو اپنی بچاؤ کی دوا چھوڑ دیتے ہیں۔ اس قطعی حد کے اندر، کچھ مریض محسوس کرتے ہیں کہ کمر کے اوپری حصے پر کپنگ سے وہ پٹھوں کا کھنچاؤ کم ہوتا ہے جو مشکل سانس کے ساتھ آتا ہے۔",
  sections=[
    dict(h2_en="The line we will not cross", h2_ur="وہ حد جو ہم عبور نہیں کریں گے",
      caution=("If you are having an asthma attack — struggling to speak in full sentences, using your reliever repeatedly, chest tight and worsening — go to a hospital. Do not come to us. And never let any practitioner, including us, imply that cupping can replace a preventer inhaler. It cannot, and people have died from that advice.",
               "اگر آپ کو دمے کا دورہ پڑ رہا ہے — پورے جملے بولنے میں دشواری، بار بار ریلیور کا استعمال، سینہ جکڑا اور بگڑتا ہوا — تو اسپتال جائیں۔ ہمارے پاس نہ آئیں۔ اور کسی معالج کو، بشمول ہمارے، یہ کہنے نہ دیں کہ کپنگ بچاؤ کے انہیلر کی جگہ لے سکتی ہے۔ نہیں لے سکتی، اور اس مشورے سے لوگ جان گنوا چکے ہیں۔"),
      ),
    dict(h2_en="What cupping may plausibly ease", h2_ur="کپنگ قرینِ قیاس طور پر کیا آرام دے سکتی ہے",
      paras=[
        ("Breathing badly is physically tiring. The muscles between the ribs, across the upper back and around the shoulders work harder and stay tight, and that tightness is uncomfortable in its own right. Cupping across the upper back is a plausible comfort for that muscular layer. It is not acting on your airways, and we will not pretend otherwise.",
         "خراب سانس لینا جسمانی طور پر تھکا دیتا ہے۔ پسلیوں کے درمیان، کمر کے اوپری حصے اور کندھوں کے گرد کے پٹھے زیادہ محنت کرتے اور سخت رہتے ہیں، اور یہ کھنچاؤ خود اپنی جگہ تکلیف دہ ہے۔ کمر کے اوپری حصے پر کپنگ اُس پٹھوں کی تہہ کے لیے ایک قرینِ قیاس آرام ہے۔ یہ آپ کی سانس کی نالیوں پر اثر نہیں کر رہی، اور ہم اس کا دعویٰ نہیں کریں گے۔"),
      ],
      bullets=[
        ("Tightness across the upper back and between the shoulder blades", "کمر کے اوپری حصے اور شانوں کے درمیان کھنچاؤ"),
        ("General relaxation, which helps sleep in a bad season", "عمومی سکون، جو خراب موسم میں نیند میں مدد دیتا ہے"),
        ("A sense of ease as part of a wider routine, alongside your medication", "اپنی دوا کے ساتھ، ایک وسیع معمول کے حصے کے طور پر آرام کا احساس"),
      ]),
    dict(h2_en="What actually helps breathing in Karachi", h2_ur="کراچی میں سانس کے لیے اصل میں کیا مدد دیتا ہے",
      bullets=[
        ("Take your preventer inhaler every day, including on good days — that is the whole point of it", "اپنا بچاؤ انہیلر روزانہ لیں، اچھے دنوں میں بھی — اسی کا تو مقصد ہے"),
        ("Learn your inhaler technique properly; a large share of people use it wrong and get a fraction of the dose", "انہیلر کی تکنیک ٹھیک سے سیکھیں؛ بہت سے لوگ غلط استعمال کرتے ہیں اور خوراک کا معمولی حصہ ہی پاتے ہیں"),
        ("Keep windows shut on high-dust days and during winter smog", "زیادہ گرد والے دنوں اور سردیوں کی اسموگ میں کھڑکیاں بند رکھیں"),
        ("Wash bedding hot and reduce soft furnishings if dust mites trigger you", "اگر گرد کے ذرات محرک ہوں تو بستر گرم پانی میں دھوئیں اور نرم سامان کم کریں"),
        ("No smoking in the home — including in another room", "گھر میں سگریٹ نہیں — دوسرے کمرے میں بھی نہیں"),
      ]),
  ],
  faq=[
    dict(q_en="Can Hijama cure asthma?", q_ur="کیا حجامہ دمہ ٹھیک کر سکتا ہے؟",
         a_en="No. Asthma is a long-term condition of the airways and cupping does not treat it. Anyone claiming otherwise is putting you at risk.",
         a_ur="نہیں۔ دمہ سانس کی نالیوں کی ایک طویل المدت حالت ہے اور کپنگ اس کا علاج نہیں کرتی۔ جو کوئی اس کے برعکس دعویٰ کرے وہ آپ کو خطرے میں ڈال رہا ہے۔"),
    dict(q_en="Can I reduce my inhaler if I feel better after a session?", q_ur="اگر سیشن کے بعد بہتر لگے تو کیا میں انہیلر کم کر سکتا ہوں؟",
         a_en="No. Only the doctor managing your asthma should ever change your medication, and feeling well is exactly what a working preventer is supposed to produce.",
         a_ur="نہیں۔ صرف وہ ڈاکٹر جو آپ کا دمہ دیکھ رہا ہے آپ کی دوا بدل سکتا ہے، اور بہتر محسوس ہونا ہی وہ نتیجہ ہے جو ایک کارگر بچاؤ دوا کو دینا چاہیے۔"),
    dict(q_en="Is cupping safe if I have asthma?", q_ur="اگر مجھے دمہ ہے تو کیا کپنگ محفوظ ہے؟",
         a_en="Generally yes when your asthma is stable and controlled. We would not proceed during a flare, a chest infection, or if you are wheezing on the day.",
         a_ur="عام طور پر جی ہاں، جب آپ کا دمہ مستحکم اور قابو میں ہو۔ ہم دورے، سینے کے انفیکشن، یا اُس دن سانس میں سیٹی کی صورت میں آگے نہیں بڑھیں گے۔"),
    dict(q_en="Where would the cups be placed?", q_ur="کپ کہاں لگائے جائیں گے؟",
         a_en="Across the upper back and between the shoulder blades — the muscles that work hard when breathing is laboured. Never on the throat or over the front of the chest.",
         a_ur="کمر کے اوپری حصے اور شانوں کے درمیان — وہ پٹھے جو مشکل سانس کے وقت زیادہ محنت کرتے ہیں۔ گلے پر یا سینے کے سامنے کبھی نہیں۔"),
    dict(q_en="My child has asthma — can they have Hijama?", q_ur="میرے بچے کو دمہ ہے — کیا اسے حجامہ کروا سکتے ہیں؟",
         a_en="We are cautious with children and would want their paediatrician's view first. For most children with asthma the answer is to get the inhaler routine right, not to add cupping.",
         a_ur="ہم بچوں کے معاملے میں محتاط ہیں اور پہلے ان کے ماہرِ اطفال کی رائے چاہیں گے۔ دمہ والے بیشتر بچوں کے لیے جواب یہ ہے کہ انہیلر کا معمول درست کیا جائے، کپنگ شامل نہ کی جائے۔"),
  ],
  cta_en="Breathing badly in Karachi's air?",
  cta_ur="کراچی کی ہوا میں سانس لینا مشکل ہے؟",
  cta_body_en="Keep taking your inhaler, and talk to us about comfort alongside it. Shaheen Shafi Unani Clinic &amp; Hijama Center, Model Colony, Karachi. If your asthma is not well controlled, the honest advice is a doctor first — and we will give you that advice.",
  cta_body_ur="اپنا انہیلر جاری رکھیں، اور اس کے ساتھ آرام کے بارے میں ہم سے بات کریں۔ شاہین شافی یونانی کلینک و حجامہ سینٹر، ماڈل کالونی، کراچی۔ اگر آپ کا دمہ اچھی طرح قابو میں نہیں تو دیانتدار مشورہ پہلے ڈاکٹر ہے — اور ہم آپ کو یہی مشورہ دیں گے۔",
  related=REL_GUIDE,
),
]


if __name__ == "__main__":
    print("Generating %d articles\n" % len(TOPICS))
    for t in TOPICS:
        build(t)
        write_queue_entry(t)
    print("\nQueued.")
