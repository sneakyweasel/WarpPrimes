# Warp Primes by sneakyweasel

- Prime numbers whose reverse of the balanced ternary representation is also prime.
- Balanced ternary notation might allow insight into relations hidden by classical notation. [Balanced Ternary]( https://en.wikipedia.org/wiki/Balanced_ternary)

Python code used to generate Warp Primes:

- Warp Entry: [OEIS A323782](https://oeis.org/A323782)
- Warp Exit : [OEIS A323783](https://oeis.org/A323783)

## How-to

$ pip install sympy

$ py -3 warp.py

## Table

|index|prime|BT representation|reversed BT representation|warped prime|prime factors|
|---|---|---|---|---|
|1|2|+ -|- +|-2|-2|
|1|3|+ 0|0 +|1|[]|
|2|5|+ - -|- - +|-11|-11|
|3|7|+ - +|+ - +|7|7|
|4|11|+ + -|- + +|-5|-5|
|5|13|+ + +|+ + +|13|13|
|6|17|+ - 0 -|- 0 - +|-29|-29|
|6|19|+ - 0 +|+ 0 - +|25|[5]|
|6|23|+ 0 - -|- - 0 +|-35|[5, 7]|
|7|29|+ 0 + -|- + 0 +|-17|-17|
|8|31|+ 0 + +|+ + 0 +|37|37|
|9|37|+ + 0 +|+ 0 + +|31|31|
|9|41|+ - - - -|- - - - +|-119|[7, 17]|
|10|43|+ - - - +|+ - - - +|43|43|
|10|47|+ - - + -|- + - - +|-65|[5, 13]|
|11|53|+ - 0 0 -|- 0 0 - +|-83|-83|
|12|59|+ - + - -|- - + - +|-101|-101|
|13|61|+ - + - +|+ - + - +|61|61|
|13|67|+ - + + +|+ + + - +|115|[5, 23]|
|14|71|+ 0 - 0 -|- 0 - 0 +|-89|-89|
|15|73|+ 0 - 0 +|+ 0 - 0 +|73|73|
|15|79|+ 0 0 - +|+ - 0 0 +|55|[5, 11]|
|16|83|+ 0 0 + -|- + 0 0 +|-53|-53|
|17|89|+ 0 + 0 -|- 0 + 0 +|-71|-71|
|17|97|+ + - - +|+ - - + +|49|[7]|
|18|101|+ + - + -|- + - + +|-59|-59|
|19|103|+ + - + +|+ + - + +|103|103|
|19|107|+ + 0 0 -|- 0 0 + +|-77|[7, 11]|
|19|109|+ + 0 0 +|+ 0 0 + +|85|[5, 17]|
|19|113|+ + + - -|- - + + +|-95|[5, 19]|
|19|127|+ - - - 0 +|+ 0 - - - +|205|[5, 41]|
|19|131|+ - - 0 - -|- - 0 - - +|-335|[5, 67]|
|20|137|+ - - 0 + -|- + 0 - - +|-173|-173|
|21|139|+ - - 0 + +|+ + 0 - - +|313|313|
|22|149|+ - 0 - - -|- - - 0 - +|-353|-353|
|22|151|+ - 0 - - +|+ - - 0 - +|133|[7, 19]|
|22|157|+ - 0 - + +|+ + - 0 - +|295|[5, 59]|
|23|163|+ - 0 0 0 +|+ 0 0 0 - +|241|241|
|23|167|+ - 0 + - -|- - + 0 - +|-299|[13, 23]|
|24|173|+ - 0 + + -|- + + 0 - +|-137|-137|
|25|179|+ - + - 0 -|- 0 - + - +|-263|-263|
|26|181|+ - + - 0 +|+ 0 - + - +|223|223|
|26|191|+ - + 0 + -|- + 0 + - +|-155|[5, 31]|
|27|193|+ - + 0 + +|+ + 0 + - +|331|331|
|27|197|+ - + + 0 -|- 0 + + - +|-209|[11, 19]|
|28|199|+ - + + 0 +|+ 0 + + - +|277|277|
|28|211|+ 0 - - + +|+ + - - 0 +|289|[17]|
|29|223|+ 0 - + - +|+ - + - 0 +|181|181|
|29|227|+ 0 - + + -|- + + - 0 +|-143|[11, 13]|
|29|229|+ 0 - + + +|+ + + - 0 +|343|[7]|
|30|233|+ 0 0 - 0 -|- 0 - 0 0 +|-269|-269|
|30|239|+ 0 0 0 - -|- - 0 0 0 +|-323|[17, 19]|
|31|241|+ 0 0 0 - +|+ - 0 0 0 +|163|163|
|31|251|+ 0 0 + 0 -|- 0 + 0 0 +|-215|[5, 43]|
|31|257|+ 0 + - - -|- - - + 0 +|-341|[11, 31]|
|32|263|+ 0 + - + -|- + - + 0 +|-179|-179|
|33|269|+ 0 + 0 0 -|- 0 0 + 0 +|-233|-233|
|33|271|+ 0 + 0 0 +|+ 0 0 + 0 +|253|[11, 23]|
|34|277|+ 0 + + - +|+ - + + 0 +|199|199|
|34|281|+ 0 + + + -|- + + + 0 +|-125|[5]|
|34|283|+ 0 + + + +|+ + + + 0 +|361|[19]|
|34|293|+ + - 0 - -|- - 0 - + +|-329|[7, 47]|
|34|307|+ + - + 0 +|+ 0 + - + +|265|[5, 53]|
|35|311|+ + 0 - - -|- - - 0 + +|-347|-347|
|36|313|+ + 0 - - +|+ - - 0 + +|139|139|
|36|317|+ + 0 - + -|- + - 0 + +|-185|[5, 37]|
|37|331|+ + 0 + - +|+ - + 0 + +|193|193|
|37|337|+ + 0 + + +|+ + + 0 + +|355|[5, 71]|
|38|347|+ + + 0 - -|- - 0 + + +|-311|-311|
|38|349|+ + + 0 - +|+ - 0 + + +|175|[5, 7]|
|39|353|+ + + 0 + -|- + 0 + + +|-149|-149|
|39|359|+ + + + 0 -|- 0 + + + +|-203|[7, 29]|
|40|367|+ - - - - - +|+ - - - - - +|367|367|
|41|373|+ - - - - + +|+ + - - - - +|853|853|
|42|379|+ - - - 0 0 +|+ 0 0 - - - +|691|691|
|43|383|+ - - - + - -|- - + - - - +|-929|-929|
|44|389|+ - - - + + -|- + + - - - +|-443|-443|
|44|397|+ - - 0 - 0 +|+ 0 - 0 - - +|637|[7, 13]|
|45|401|+ - - 0 0 - -|- - 0 0 - - +|-983|-983|
|45|409|+ - - 0 0 + +|+ + 0 0 - - +|961|[31]|
|45|419|+ - - + - - -|- - - + - - +|-1037|[17, 61]|
|46|421|+ - - + - - +|+ - - + - - +|421|421|
|46|431|+ - - + 0 0 -|- 0 0 + - - +|-713|[23, 31]|
|46|433|+ - - + 0 0 +|+ 0 0 + - - +|745|[5, 149]|
|46|439|+ - - + + - +|+ - + + - - +|583|[11, 53]|
|47|443|+ - - + + + -|- + + + - - +|-389|-389|
|48|449|+ - 0 - - 0 -|- 0 - - 0 - +|-839|-839|
|49|457|+ - 0 - 0 - +|+ - 0 - 0 - +|457|457|
|49|461|+ - 0 - 0 + -|- + 0 - 0 - +|-515|[5, 103]|
|49|463|+ - 0 - 0 + +|+ + 0 - 0 - +|943|[23, 41]|
|50|467|+ - 0 - + 0 -|- 0 + - 0 - +|-677|-677|
|51|479|+ - 0 0 - + -|- + - 0 0 - +|-569|-569|
|52|487|+ - 0 0 0 0 +|+ 0 0 0 0 - +|727|727|
|52|491|+ - 0 0 + - -|- - + 0 0 - +|-893|[19, 47]|
|53|499|+ - 0 0 + + +|+ + + 0 0 - +|1051|1051|
|53|503|+ - 0 + - 0 -|- 0 - + 0 - +|-785|[5, 157]|
|54|509|+ - 0 + 0 - -|- - 0 + 0 - +|-947|-947|
|54|521|+ - 0 + + 0 -|- 0 + + 0 - +|-623|[7, 89]|
|54|523|+ - 0 + + 0 +|+ 0 + + 0 - +|835|[5, 167]|
|55|541|+ - + - 0 0 +|+ 0 0 - + - +|709|709|
|56|547|+ - + - + - +|+ - + - + - +|547|547|
|56|557|+ - + 0 - 0 -|- 0 - 0 + - +|-803|[11, 73]|
|56|563|+ - + 0 0 - -|- - 0 0 + - +|-965|[5, 193]|
|57|569|+ - + 0 0 + -|- + 0 0 + - +|-479|-479|
|57|571|+ - + 0 0 + +|+ + 0 0 + - +|979|[11, 89]|
|57|577|+ - + 0 + 0 +|+ 0 + 0 + - +|817|[19, 43]|
|57|587|+ - + + - + -|- + - + + - +|-533|[13, 41]|
|57|593|+ - + + 0 0 -|- 0 0 + + - +|-695|[5, 139]|
|58|599|+ - + + + - -|- - + + + - +|-857|-857|
|59|601|+ - + + + - +|+ - + + + - +|601|601|
|60|607|+ - + + + + +|+ + + + + - +|1087|1087|
|61|613|+ 0 - - - 0 +|+ 0 - - - 0 +|613|613|
|61|617|+ 0 - - 0 - -|- - 0 - - 0 +|-1007|[19, 53]|
|61|619|+ 0 - - 0 - +|+ - 0 - - 0 +|451|[11, 41]|
|61|631|+ 0 - - + 0 +|+ 0 + - - 0 +|775|[5, 31]|
|61|641|+ 0 - 0 - + -|- + - 0 - 0 +|-575|[5, 23]|
|62|643|+ 0 - 0 - + +|+ + - 0 - 0 +|883|883|
|62|647|+ 0 - 0 0 0 -|- 0 0 0 - 0 +|-737|[11, 67]|
|62|653|+ 0 - 0 + - -|- - + 0 - 0 +|-899|[29, 31]|
|62|659|+ 0 - 0 + + -|- + + 0 - 0 +|-413|[7, 59]|
|62|661|+ 0 - 0 + + +|+ + + 0 - 0 +|1045|[5, 11, 19]|
|62|673|+ 0 - + 0 - +|+ - 0 + - 0 +|505|[5, 101]|
|63|677|+ 0 - + 0 + -|- + 0 + - 0 +|-467|-467|
|63|683|+ 0 - + + 0 -|- 0 + + - 0 +|-629|[17, 37]|
|64|691|+ 0 0 - - - +|+ - - - 0 0 +|379|379|
|64|701|+ 0 0 - 0 0 -|- 0 0 - 0 0 +|-755|[5, 151]|
|65|709|+ 0 0 - + - +|+ - + - 0 0 +|541|541|
|66|719|+ 0 0 0 - 0 -|- 0 - 0 0 0 +|-809|-809|
|67|727|+ 0 0 0 0 - +|+ - 0 0 0 0 +|487|487|
|67|733|+ 0 0 0 0 + +|+ + 0 0 0 0 +|973|[7, 139]|
|68|739|+ 0 0 0 + 0 +|+ 0 + 0 0 0 +|811|811|
|68|743|+ 0 0 + - - -|- - - + 0 0 +|-1025|[5, 41]|
|69|751|+ 0 0 + - + +|+ + - + 0 0 +|919|919|
|70|757|+ 0 0 + 0 0 +|+ 0 0 + 0 0 +|757|757|
|71|761|+ 0 0 + + - -|- - + + 0 0 +|-863|-863|
|71|769|+ 0 0 + + + +|+ + + + 0 0 +|1081|[23, 47]|
|72|773|+ 0 + - - 0 -|- 0 - - + 0 +|-827|-827|
|72|787|+ 0 + - 0 + +|+ + 0 - + 0 +|955|[5, 191]|
|72|797|+ 0 + 0 - - -|- - - 0 + 0 +|-1043|[7, 149]|
|73|809|+ 0 + 0 0 0 -|- 0 0 0 + 0 +|-719|-719|
|74|811|+ 0 + 0 0 0 +|+ 0 0 0 + 0 +|739|739|
|74|821|+ 0 + 0 + + -|- + + 0 + 0 +|-395|[5, 79]|
|75|823|+ 0 + 0 + + +|+ + + 0 + 0 +|1063|1063|
|76|827|+ 0 + + - 0 -|- 0 - + + 0 +|-773|-773|
|76|829|+ 0 + + - 0 +|+ 0 - + + 0 +|685|[5, 137]|
|77|839|+ 0 + + 0 + -|- + 0 + + 0 +|-449|-449|
|78|853|+ + - - - - +|+ - - - - + +|373|373|
|79|857|+ + - - - + -|- + - - - + +|-599|-599|
|80|859|+ + - - - + +|+ + - - - + +|859|859|
|81|863|+ + - - 0 0 -|- 0 0 - - + +|-761|-761|
|82|877|+ + - - + + +|+ + + - - + +|1021|1021|
|82|881|+ + - 0 - 0 -|- 0 - 0 - + +|-815|[5, 163]|
|83|883|+ + - 0 - 0 +|+ 0 - 0 - + +|643|643|
|84|887|+ + - 0 0 - -|- - 0 0 - + +|-977|-977|
|84|907|+ + - + - - +|+ - - + - + +|427|[7, 61]|
|84|911|+ + - + - + -|- + - + - + +|-545|[5, 109]|
|85|919|+ + - + 0 0 +|+ 0 0 + - + +|751|751|
|86|929|+ + - + + + -|- + + + - + +|-383|-383|
|86|937|+ + 0 - - 0 +|+ 0 - - 0 + +|625|[5]|
|86|941|+ + 0 - 0 - -|- - 0 - 0 + +|-995|[5, 199]|
|87|947|+ + 0 - 0 + -|- + 0 - 0 + +|-509|-509|
|87|953|+ + 0 - + 0 -|- 0 + - 0 + +|-671|[11, 61]|
|87|967|+ + 0 0 - + +|+ + - 0 0 + +|895|[5, 179]|
|87|971|+ + 0 0 0 0 -|- 0 0 0 0 + +|-725|[5, 29]|
|88|977|+ + 0 0 + - -|- - + 0 0 + +|-887|-887|
|89|983|+ + 0 0 + + -|- + + 0 0 + +|-401|-401|
|89|991|+ + 0 + - 0 +|+ 0 - + 0 + +|679|[7, 97]|
|89|997|+ + 0 + 0 - +|+ - 0 + 0 + +|517|[11, 47]|