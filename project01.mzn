int: adultn; %number of adults
int: dn; %number of diabetes patients, first dn adults in output from python script will be assigned as diabetes patients


int: aprotein; %protein reqirement for adult, per person
enum protein; %Food items in Protein Food Group

array [protein] of int: perpro; %protein value per unit of each food item
array [protein] of int: pronum; %number of units each protein food item
array [protein] of int: procost; %cost of protein per unit of each food

array[protein,1..adultn] of var int: ap; %amount of each protein food taken by each person
var int: apt; %total protein consumption
array[1..1] of var int: ap1; %total protein consumption in 1d array
int: pt=sum(i in protein)(perpro[i]*pronum[i]); %total protein value 
var int: aptr; %total remaining protein value

var int: aptc; %total cost of all protein items distributed
array[1..1] of var int: aptc1; %total protein cost in 1d array

constraint forall(i in protein)(
  sum(j in 1..adultn) (ap[i,j])<=pronum[i]
); %total number of protein each food item consumed by all adults won't exceed the number of that protein item

constraint forall(i in 1..adultn)(
  sum(j in protein) (ap[j,i]*perpro[j])>=aprotein
); %total protein consumed by each adult will be >= protein requirement for per adult

constraint forall(i in 1..adultn)(
  forall(j in protein) (ap[j,i]>=0)
); %amount of each protein food taken by each person is >=0

constraint ap1=[sum(i in 1..adultn)(
  sum(j in protein) (ap[j,i]*perpro[j])
)]; %adding sums of all adult's total protein consumption

constraint apt=sum(i in 1..1) (ap1[i]); %keeping total sum in an integer

constraint aptr=pt-apt;

constraint aptr>=0;

constraint aptc1=[sum(i in 1..adultn)(
  sum(j in protein) (ap[j,i]*procost[j])
)]; %adding sums of all adult's total protein cost

constraint aptc=sum(i in 1..1) (aptc1[i]); %keeping total sum in an integer



int: acarb; %carb reqirement for adult, per person, non-diabetes
int: dcarb; %carb reqirement for adult, per person, diabetes
enum carb; %Food items in Carb Food Group

array [carb] of int: percarb; %carb value per unit of each food item
array [carb] of int: carbnum; %number of units each carb food item
array [carb] of int: carbcost; %cost of carb per unit of each food

array[carb,1..adultn] of var int: ac; %amount of each carb food taken by each person
var int: act; %total carb consumption
array[1..1] of var int: ac1; %total carb consumption in 1d array
int: ct=sum(i in carb)(percarb[i]*carbnum[i]); %total carb value
var int: actr; %total remaining carb value

var int: actc; %total cost of all carb items distributed
array[1..1] of var int: actc1; %total carb cost in 1d array

constraint forall(i in carb)(
  sum(j in 1..adultn) (ac[i,j])<=carbnum[i]
); %total number of carb each food item consumed by all adults won't exceed the number of that carb item

constraint forall(i in 1..dn)(
  sum(j in carb) (ac[j,i]*percarb[j])>=dcarb
); %total carb consumed by each adult will be >= carb requirement for per adult (diabetes)

constraint forall(i in dn+1..adultn)(
  sum(j in carb) (ac[j,i]*percarb[j])>=acarb
); %total carb consumed by each adult will be >= carb requirement for per adult (non diabetes)

constraint forall(i in 1..adultn)(
  forall(j in carb) (ac[j,i]>=0)
); %amount of each carb food taken by each person is >=0

constraint forall(i in 1..dn)(
  forall(j in carb) (if j=6 then ac[j,i]=0 endif)
); %diabetes patients wont eat sweets

constraint ac1=[sum(i in 1..adultn)(
  sum(j in carb) (ac[j,i]*percarb[j])
)]; %adding sums of all adult's total carb consumption

constraint act=sum(i in 1..1) (ac1[i]); %keeping total sum in an integer

constraint actr=ct-act;

constraint actr>=0;

constraint actc1=[sum(i in 1..adultn)(
  sum(j in carb) (ac[j,i]*carbcost[j])
)]; %adding sums of all adult's total carb cost

constraint actc=sum(i in 1..1) (actc1[i]); %keeping total sum in an integer



int: afruit; %fruit reqirement for adult, per person, non-diabetes
int: dfruit; %fruit reqirement for adult, per person, diabetes
enum fruit; %Food items in fruit Food Group

array [fruit] of int: perf; %fruit value per unit of each food item
array [fruit] of int: fnum; %number of units each fruit food item
array [fruit] of int: fcost; %cost of fruit per unit of each food

array[fruit,1..adultn] of var int: af; %amount of each fruit food taken by each person
var int: aft; %total fruit consumption
array[1..1] of var int: af1; %total fruit consumption in 1d array
int: ft=sum(i in fruit)(perf[i]*fnum[i]); %total fruit value 
var int: aftr; %total remaining fruit value

var int: aftc; %total cost of all fruit items distributed
array[1..1] of var int: aftc1; %total fruit cost in 1d array

constraint forall(i in fruit)(
  sum(j in 1..adultn) (af[i,j])<=fnum[i]
); %total number of fruit each food item consumed by all adults won't exceed the number of that fruit item

constraint forall(i in 1..dn)(
  sum(j in fruit) (af[j,i]*perf[j])>=dfruit
); %total fruit consumed by each adult will be >= fruit requirement for per adult, diabetes

constraint forall(i in dn+1..adultn)(
  sum(j in fruit) (af[j,i]*perf[j])>=afruit
); %total fruit consumed by each adult will be >= fruit requirement for per adult, non-diabetes

constraint forall(i in 1..adultn)(
  forall(j in fruit) (af[j,i]>=0)
); %amount of each fruit food taken by each person is >=0

constraint af1=[sum(i in 1..adultn)(
  sum(j in fruit) (af[j,i]*perf[j])
)]; %adding sums of all adult's total fruit consumption

constraint aft=sum(i in 1..1) (af1[i]); %keeping total sum in an integer

constraint aftr=ft-aft;

constraint aftr>=0;

constraint aftc1=[sum(i in 1..adultn)(
  sum(j in fruit) (af[j,i]*fcost[j])
)]; %adding sums of all adult's total fruit cost

constraint aftc=sum(i in 1..1) (aftc1[i]); %keeping total sum in an integer



int: adairy; %dairy reqirement for adult, per person
enum dairy; %Food items in dairy Food Group

array [dairy] of int: perd; %dairy value per unit of each food item
array [dairy] of int: dnum; %number of units each dairy food item
array [dairy] of int: dcost; %cost of dairy per unit of each food

array[dairy,1..adultn] of var int: ad; %amount of each dairy food taken by each person
var int: adt; %total dairy consumption
array[1..1] of var int: ad1; %total dairy consumption in 1d array
int: dt=sum(i in dairy)(perd[i]*dnum[i]); %total dairy value 
var int: adtr; %total remaining dairy value

var int: adtc; %total cost of all dairy items distributed
array[1..1] of var int: adtc1; %total dairy cost in 1d array

constraint forall(i in dairy)(
  sum(j in 1..adultn) (ad[i,j])<=dnum[i]
); %total number of dairy each food item consumed by all adults won't exceed the number of that dairy item

constraint forall(i in 1..adultn)(
  sum(j in dairy) (ad[j,i]*perd[j])>=adairy
); %total dairy consumed by each adult will be >= dairy requirement for per adult

constraint forall(i in 1..adultn)(
  forall(j in dairy) (ad[j,i]>=0)
); %amount of each dairy food taken by each person is >=0

constraint ad1=[sum(i in 1..adultn)(
  sum(j in dairy) (ad[j,i]*perd[j])
)]; %adding sums of all adult's total dairy consumption

constraint adt=sum(i in 1..1) (ad1[i]); %keeping total sum in an integer

constraint adtr=dt-adt;

constraint adtr>=0;

constraint adtc1=[sum(i in 1..adultn)(
  sum(j in dairy) (ad[j,i]*dcost[j])
)]; %adding sums of all adult's total dairy cost

constraint adtc=sum(i in 1..1) (adtc1[i]); %keeping total sum in an integer




int: budget; %budget for total foods distributed

constraint aptc+actc+aftc+adtc<=budget; %total distributed food cost won't exceed the budget



solve maximize aptr+actr+aftr+adtr; %maximize the total remaining food value
