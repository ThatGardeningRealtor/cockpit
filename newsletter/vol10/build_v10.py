import re
v9=open('../vol9/TGR-Garden-Edition-Vol9.html').read()
import re; _v9s=open('../vol9/build_v9.py').read(); R='https://raw.githubusercontent.com/ThatGardeningRealtor/cockpit/main/newsletter/'
head=v9[:v9.index('<!-- HERO IMAGE -->')]
tail=v9[v9.index('  <!-- SIGN OFF -->'):]
head=head.replace('Garden Edition Vol. 9','Garden Edition Vol. 10').replace('>Vol. 9<','>Vol. 10<')
head=re.sub(r'(<div style="display:none;[^>]*>)[^<]*(</div>)',r'\1Lawn lessons from Texas A&amp;M, how to plant a tree that lasts, free trees on November 14, and what a yard can tell you before you buy.\2',head,count=1)
# footer: drop livesimplyoutdoors link
tail=re.sub(r'\s*&nbsp;\s*<a href="https://www\.instagram\.com/livesimplyoutdoors/"[^>]*>[^<]*</a>','',tail)
exec(_v9s[_v9s.index("P='"):_v9s.index("hero=f'''")])
PH_N=[0]
IMGB='@@IMGB@@'
def img(f,alt,dw,dh,full=False):
    cls=' class="full-img"' if full else ''
    st=f'display:block;width:100%;max-width:{dw}px;height:auto;' if full else f'display:block;width:{dw}px;max-width:100%;height:auto;margin:0 auto 6px auto;border-radius:2px;'
    return f'<img{cls} src="{IMGB}{f}" width="{dw}" height="{dh}" alt="{alt}" style="{st}">'
def ph(desc,suggest,h=260,w=548):
    PH_N[0]+=1
    s=f'<br><span style="font-size:12px;color:#8a7a4a;">Suggested: {suggest}</span>' if suggest else ''
    return f'''<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="{w}" align="center" style="width:{w}px;max-width:100%;margin:0 auto 6px auto;">
        <tr><td align="center" valign="middle" height="{h}" bgcolor="#fbf6e3" style="height:{h}px;border:2px dashed #c9b26b;padding:16px;font-family:Arial,sans-serif;">
          <p style="font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:#8a6d1f;font-weight:700;margin:0 0 6px 0;">&#128248; Photo Placeholder {PH_N[0]}</p>
          <p style="font-size:14px;line-height:1.5;color:#5a4a1a;margin:0;">{desc}{s}</p>
        </td></tr></table>'''
NOTE=lambda t:f'<p style="font-family:Arial,sans-serif;font-size:13px;line-height:1.5;background:#fff3c4;color:#6b5300;padding:8px 12px;margin:0 0 14px 0;border-left:4px solid #e0b400;"><strong>CHRIS TO CONFIRM:</strong> {t}</p>'
SRC=lambda t:f'<p style="font-size:12px;line-height:1.6;color:#888888;margin:0 0 20px 0;">{t}</p>'
A=lambda href,t:f'<a href="{href}" target="_blank" rel="noopener" {LINK}>{t}</a>'

hero=f'''  <!-- HERO IMAGE -->
  <tr>
    <td style="padding:0;">
      {img("vol10-hero.jpg","A honeybee in flight over a yellow cosmos bloom, with another bee on the flower",620,426,True)}
    </td>
  </tr>
  <tr>
    <td bgcolor="#1a2e10" style="padding:8px 32px 0 32px;">
      <p style="font-size:12px;line-height:1.5;color:#8ab840;margin:0;font-style:italic;text-align:center;">Caught one mid flight. Fall cosmos are the busiest stop in the yard right now.</p>
    </td>
  </tr>

  <!-- HERO TEXT BANNER -->
  <tr>
    <td bgcolor="#1a2e10" class="mob-pad" style="padding:22px 32px;">
      <p style="font-family:Arial,sans-serif;font-size:10px;letter-spacing:3px;text-transform:uppercase;color:#a8d860;margin:0 0 8px 0;">October 2026</p>
      <p class="hero-title" style="font-family:Arial,sans-serif;font-size:40px;font-weight:900;color:#ffffff;line-height:1.1;text-transform:uppercase;margin:0;">FALL'S PLANTING SEASON.<br><span style="color:#a8d860;font-size:24px;">RIGHT PLANT, RIGHT PLACE.</span></p>
    </td>
  </tr>

  <!-- INTRO + HEADSHOT -->
  <tr>
    <td style="padding:28px 36px;">
      <table cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
          <td valign="top" width="96" class="intro-avatar" style="padding-right:20px;">
            <img src="{R}chris-headshot-garden.jpg" width="80" height="80" alt="Chris Drawdy That Gardening Realtor" style="display:block;width:80px;height:80px;border-radius:50%;border:3px solid #8ab840;margin:0 auto;">
          </td>
          <td valign="top" class="intro-text">
            <p style="font-family:Arial,sans-serif;font-size:10px;letter-spacing:3px;text-transform:uppercase;color:#8ab840;font-weight:700;margin:0 0 8px 0;">Hey neighbors</p>
            <p style="font-size:15px;line-height:1.75;color:#4a4a44;margin:0;">The heat finally broke, and that means one thing around here: it's planting season. I promised you lawns last week, so we're starting there. Then trees, because the City's urban forestry crew and this week's class gave me a whole notebook on them. And since a lot of you have been asking me about homes over the fence lately, there's a little more real estate in this one too. Don't worry, the plants are still the main event.</p>
          </td>
        </tr>
      </table>
    </td>
  </tr>

'''
turf=section('MASTER GARDENER INTERN','Master Gardener Intern','Your Lawn Runs on More Than Water',
 img("vol10-rain-gauge.jpg","A dry rain gauge standing in a bare garden bed",300,503)+
 CAP%"We need the rain, but water is only part of what feeds a lawn or garden."+
 P%"Dr. Emanuel Chavarria with Texas A&amp;M AgriLife taught our turfgrass class, and the line I keep repeating is this one: grass doesn't eat fertilizer. Its real food is sunlight. Fertilizer is more like vitamins. So the first question for any lawn is how much sun it actually gets."+
 card([("St. Augustine","Handles some shade better than Bermuda and roots deep. Watch out for cold snaps and chinch bugs. Fun fact: there's no St. Augustine seed for sale, so it always starts from sod or plugs."),
       ("Bermuda","Tough, fast, and handles heat, drought, and foot traffic. It wants more than 8 hours of sun, or it thins out and fades in the shade."),
       ("Zoysia","Handles shade, drought, and cold, and doesn't need much fertilizer. Its stiff blades dull a mower fast, so keep that blade sharp."),
       ("Buffalograss","A Texas native that needs about as little water and care as any lawn grass gets. It does better out west than in wetter East Texas.")])+
 P%"Mowing is where most of us get in trouble. Follow the one third rule: never cut off more than a third of the blade at once. Those blades are the solar panels, and scalping them leaves the grass with an empty kitchen."+
 callout("Try This Today",f"Do the catch can test. Set out a few empty tuna or cat food cans around the yard, run your sprinklers for 5 minutes, and measure the water in each one. Average them and multiply by 12 to see how many inches you put down in an hour. Then check {A('https://watermyyard.org','WaterMyYard.org')} for how much your lawn actually needs this week."))

trees=section('TREES','Planting Season','Plant a Tree That Outlives Your Mortgage',
 img("vol10-fig.jpg","A hand holding a fig branch with young green figs forming",548,253)+
 CAP%"Our young Celeste fig, already setting fruit. Fall is when trees put down roots."+
 P%"October through April is tree planting season here, and the City of San Antonio's urban forestry team walked us through how to do it right. Here's the short version:"+
 card([("Call 811 first","Before you dig, call 811 so the utility lines get marked. It's free."),
       ("Go wide, not deep","Dig the hole 2 to 3 times as wide as the root ball, but no deeper. Roots spread out sideways looking for water, way past the edge of the branches."),
       ("Water slow","A 5 gallon bucket with a small hole in the bottom lets water soak in slowly instead of running off."),
       ("Paint every oak cut","Oak wilt spreads by a little sap beetle drawn to fresh wounds. Paint any cut on an oak right away (cheap flat black spray paint works) and save big oak pruning for winter.")])+
 P%"What to plant? From this week's class: Lacey oak, Mexican white oak, Texas or Mexican redbud, and Barbados cherry if you want something compact the birds will love. The warning I wrote down twice: <strong><em>fast growing trees are often fast dying trees.</em></strong> Pick one that can actually reach maturity here."+
 P%"And that gray, fuzzy stuff hanging in your oaks? That's ball moss. It's not a parasite. It's a bromeliad, kin to pineapples, and it pulls everything it needs from the air. It will grow on a power line just as happily as a branch. If a tree is loaded with it, that's usually a sign of shady, dead, or stressed limbs, so focus on the tree's health and clear out the dead wood."+
 callout("Free Trees",f"Día del Árbol is <strong>Saturday, November 14, 10 AM to 1 PM at Mission Marquee Plaza</strong>, 3100 Roosevelt Ave. The City is giving away more than 1,000 free shade and ornamental trees, first come, first served. Details at {A('https://www.sa.gov/trees','sa.gov/trees')}."))

mid=f'''  <!-- MID CTA -->
  <tr>
    <td bgcolor="#f4f8ec" style="padding:28px 36px;text-align:center;border-top:4px solid #8ab840;border-bottom:4px solid #8ab840;">
      <p style="font-family:Arial,sans-serif;font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#6a8f2e;font-weight:700;margin:0 0 10px 0;">Thinking About a Move?</p>
      <p style="font-family:Arial,sans-serif;font-size:24px;font-weight:800;color:#1a2e10;margin:0 0 12px 0;line-height:1.2;">Let's Walk the Yard Together</p>
      <p style="font-size:15px;line-height:1.7;color:#4a4a44;margin:0 auto 18px auto;max-width:460px;">Whether you're getting ready to sell this spring or you've got your eye on a place with more room to grow, I'm happy to come by, walk the property with you, and talk through options. No pressure, just a neighbor who knows plants and houses. Reply to this email or call me at <a href="tel:2102142673" {LINK}>210 214 2673</a>.</p>
      <p style="font-family:Arial,sans-serif;font-size:13px;font-weight:700;color:#2c4a1e;margin:0 0 18px 0;">Chris Drawdy &nbsp;|&nbsp; eXp Realty</p>
      <table cellpadding="0" cellspacing="0" border="0" align="center" style="margin:0 auto;">
        <tr>
          {btn("Email Chris","mailto:chris@getrealtytx.com?subject=Let%27s%20walk%20the%20yard")}
          <td class="btn-spacer" width="16" style="font-size:0;line-height:0;">&nbsp;</td>
          {btn("Search Homes","https://christopherdrawdy.exprealty.com/",True)}
        </tr>
      </table>
    </td>
  </tr>

'''
re_=section('REAL ESTATE CORNER','Real Estate Corner','What a Yard Tells You Before You Buy',
 img("vol10-devine-yard.jpg","A tan country home behind a front yard full of white wildflowers under a blue sky",548,519)+
 CAP%"Wildflowers out front in Devine. The yard tells you a lot before you step inside."+
 P%"When I walk a property with someone, I look at the house, sure. But I'm also reading the yard, because the yard tells you what living there will actually be like. Here's what I check:"+
 card([("Where the sun goes","Full sun is 6 or more hours of direct light, part sun is 3 to 6, and deep shade is under 3. A backyard that's shady at 2 PM won't grow tomatoes or Bermuda. If you can, visit at different times of day."),
       ("Big trees","Shade trees take decades to grow, so look at them closely. Is the canopy full? Any dead limbs, or ball moss piling up on stressed wood? If there are oaks, ask whether oak wilt has been in the area."),
       ("The tree rules","San Antonio protects trees by trunk size: most are significant at 6 inches across and heritage at 24 inches, measured at chest height. If you're planning to build, add on, or clear, check the City's tree rules first."),
       ("The lawn and the water","What kind of grass is it, and is there a sprinkler system? A catch can test on a showing day tells you a lot.")])+
 P%"And for everyone who already owns a home here, property tax bills are landing in mailboxes now. In Bexar County, the last day to pay without penalty is normally January 31, and since that's a Sunday this time, it rolls to Monday, February 1, 2027. Bexar also offers payment plans, so check your options early."+
 P%f"While you've got the bill in hand, make sure your homestead exemption shows up on it. Texas school districts are required to give a $140,000 homestead exemption, and if you bought this year and haven't filed, you can generally still file late (up to two years after the deadline). {A('https://www.bcad.org','BCAD')} has the form and can confirm what you qualify for."+
 SRC("Sources: City of San Antonio Tree Preservation Ordinance and tree ordinance FAQ; Bexar County Tax Assessor Collector tax calendar; Bexar Appraisal District exemption overview and Form 50 114. This is general info, not tax advice.")+
 f'''<table cellpadding="0" cellspacing="0" border="0" align="center" style="margin:0 auto;">
        <tr>
          {btn("City Tree Rules","https://www.sa.gov/Directory/Departments/DSD/Constructing/Preservation-Conservation/Tree-Preservation")}
          <td class="btn-spacer" width="16" style="font-size:0;line-height:0;">&nbsp;</td>
          {btn("Search Homes","https://christopherdrawdy.exprealty.com/",True)}
        </tr>
      </table>''')

light=section('RIGHT PLANT RIGHT PLACE','Right Plant, Right Place','Do the Sun Walk This Weekend',
 img("vol10-bees-cosmos.jpg","A honeybee working an orange cosmos bloom in full sun",320,400)+
 CAP%"Cosmos love full sun, and so do the bees. Right plant, right place."+
 P%"Lynn Cox taught our perennials class, and her homework is something anyone can do. On a sunny day, check your yard every hour or so from 10 AM to 5 PM and jot down where the light lands. That's your real map for what to plant where. Do it again in spring, because the sun angle changes and leaves come and go."+
 P%"Turk's cap is a good example. In full sun it blooms like crazy but droops in the afternoon heat. In shade the leaves look great but the flowers slow down. Lynn's answer: morning sun, afternoon shade."+
 PL%"Two more tips from her: group plants that need the same water (that's called hydrozoning), and plan for the mature size. Plants crammed too close end up fighting each other and stay stunted.")

chk=section('LATE OCTOBER CHECKLIST','Late October Checklist','Before the First Cold Snap',
 card([("Overseed with the right rye","If you want winter green, use perennial ryegrass, not annual rye."),
       ("Find a spot for tender plants","Pick where your potted tropicals will go before the first freeze, not the night of."),
       ("Raise the mower","One third rule all the way into winter. Taller grass holds up better."),
       ("Get trees in the ground","The roots settle in all winter while the tops rest."),
       ("Check your lantana","Silvery, speckled leaves with dark spots underneath usually mean lace bugs.")],mb=12)+
 '<p style="font-size:12px;line-height:1.6;color:#888888;margin:0;">Sources: Bexar County Master Gardener classes with Texas A&amp;M AgriLife and the City of San Antonio.</p>')

stands=f'''  <!-- LRH STANDS -->
  <tr>
    <td bgcolor="#2c4a1e" style="padding:28px 36px;text-align:center;">
      <img src="{R}lrh-logo-sign.jpg" width="170" alt="The Little Red House of Seeds and Plants sign" style="display:block;width:170px;max-width:100%;margin:0 auto 24px auto;border-radius:2px;">
      <p style="font-family:Arial,sans-serif;font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#8ab840;font-weight:700;margin:0 0 10px 0;">Little Red House</p>
      <p style="font-family:Arial,sans-serif;font-size:32px;font-weight:800;color:#ffffff;margin:0 0 18px 0;line-height:1.15;">The Stands Are Winding Down</p>
      <p style="font-size:15px;line-height:1.6;color:#c8deb0;margin:0 auto 22px auto;max-width:440px;">All the Little Red House stands will be shutting down over the next few weeks for the season. There will still be some plants left for you to pick up, so swing by while they last. Whatever's left goes to the San Antonio Men's Garden Club, whose plant sales are open to everyone and raise money for the club. Thank you for every cutting you shared this year.</p>
      <table cellpadding="0" cellspacing="0" border="0" align="center" style="margin-top:4px;">
        <tr>
          <td bgcolor="#8ab840" style="padding:13px 28px;">
            <a href="https://getrealtytx.com/little-red-house/" target="_blank" rel="noopener" style="font-family:Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#ffffff;text-decoration:none;">Visit the Little Red House</a>
          </td>
        </tr>
      </table>
    </td>
  </tr>

'''
comm=section('COMMUNITY CORNER','Community Corner',"Thanks for Swapping, and the Pumpkins Are Out",
 P%"A big thank you to Ken Wolfgram for hosting our October 17 plant swap, and to everyone who showed up with cuttings, seedlings, and stories to trade. That's what this community is about: plants moving from one yard to the next, and neighbors meeting neighbors along the way. If you missed this one, there will be more, and I'll share the next date here first."+
 img("vol10-pumpkins.jpg","Painted jack o lantern pumpkins lined up on a wooden garden table at the San Antonio Botanical Garden",400,180)+
 CAP%"Painted by our Wednesday dementia friendly garden group at the Botanical Garden."+
 PL%f"Mark your calendar: besides Día del Árbol on November 14, the City is also giving away trees at the Farmers and Artisans Holiday Market on <strong>Saturday, November 21, 9 AM to 1 PM</strong>, also at Mission Marquee Plaza. Can't make either one? Send me a photo of what's growing in your yard. The good ones might land in a future issue.")

up=section('COMING UP NEXT WEEK','Coming Up','Copy What Already Works',
 PL%"Next week is Dr. Barron Rector's class on Texas landscapes, and his big idea stuck with me: rip off and duplicate what nature was already doing here. We'll talk about what this land looked like before the lawns, why change is normal, and how to borrow from the prairie in your own yard."+
 PL%"One last thing before next week: add <strong>christopher_drawdy@mail.expreach.com</strong> to your contacts. That's where the next issue is coming from, and I don't want it stuck in your spam folder.")

heads='''  <!-- HEADS UP: NEW SENDER -->
  <tr>
    <td bgcolor="#ffffff" style="padding:4px 36px 20px 36px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
        <td bgcolor="#f3f7ea" style="padding:16px 20px;border-left:4px solid #8ab840;font-family:Georgia,serif;">
          <p style="font-family:Arial,sans-serif;font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#4a7a1e;font-weight:700;margin:0 0 6px 0;">&#128680; Quick heads up</p>
          <p style="font-size:15px;line-height:1.6;color:#4a4a44;margin:0;">Starting next week, this newsletter will come from a new address: <strong>christopher_drawdy@mail.expreach.com</strong>. Add it to your contacts so the next issue doesn't land in spam.</p>
        </td>
      </tr></table>
    </td>
  </tr>
'''
body=hero+heads+DIV+turf+DIV+trees+DIV+mid+DIV+re_+DIV+light+DIV+chk+DIV+stands+DIV+comm+DIV+up+DIV
out=head+body+tail
import re as _re
out=_re.sub(r'<img src="[^"]*vol8/tgr-front-logo.png" width="340"', '<a href="https://thatgardeningrealtor.github.io/" target="_blank" rel="noopener" style="display:block;width:200px;margin:4px auto 14px auto;"><img src="@@IMGB@@tgr-letsgrow.png" width="200" height="200" alt="Lets Grow. Scan to follow @ThatGardeningRealtor" style="display:block;width:200px;height:200px;border:0;"></a><img src="@@IMGB@@tgr-strip.png" width="340"', out, count=1)
import os
if os.environ.get('LOGO_OPT')=='B':
    out=out.replace('RIGHT PLANT, RIGHT PLACE.</span></p>','RIGHT PLANT, RIGHT PLACE.</span></p><img src="@@IMGB@@tgr-strip.png" width="300" alt="Buy, Sell, Invest, Grow. #Community" style="display:block;width:300px;max-width:100%;height:auto;margin:16px 0 0 0;">',1)
out=out.replace('eXp Realty &nbsp;|&nbsp; Green Thumb Realty Co.<','eXp Realty &nbsp;|&nbsp; Green Thumb Realty Co. LLC<')
out=out.replace("Know a neighbor who'd love this? Forward it their way, or send them to <a ","Know a neighbor who'd love this? Forward it their way.<br><a ").replace('>past issues and sign up here</a>.</p>','>Read past issues and sign up here</a></p>')
out=out.replace('<p style="font-size:14px;line-height:1.7;color:#888888;margin:0 0 14px 0;font-style:italic;text-align:center;">','<p style="font-size:13px;line-height:1.6;color:#7a7a72;margin:4px auto 18px auto;max-width:520px;font-style:italic;text-align:center;">')
out=out.replace('>(210) 214-2673<','>(210) 214 2673<').replace(R+'chris-passafire-shirt.png','@@IMGB@@chris-signoff.png')
open('TGR-Garden-Edition-Vol10.html','w').write(out.replace('@@IMGB@@',R+'vol10/'))
open('preview-local.html','w').write(out.replace('@@IMGB@@','img/'))
print('placeholders',PH_N[0])
