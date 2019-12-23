from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [1.73486371e-04, 1.95329789e-04, 2.56553810e-04],
           [5.92213667e-04, 6.77498612e-04, 9.29838986e-04],
           [1.21203002e-03, 1.40234391e-03, 2.00730525e-03],
           [2.01643708e-03, 2.34817084e-03, 3.49881874e-03],
           [2.99956488e-03, 3.49901052e-03, 5.41963319e-03],
           [4.16254911e-03, 4.84105204e-03, 7.78709732e-03],
           [5.51226372e-03, 6.36120740e-03, 1.06189727e-02],
           [7.06076284e-03, 8.04639123e-03, 1.39324010e-02],
           [8.82503442e-03, 9.88326491e-03, 1.77414998e-02],
           [1.08264714e-02, 1.18580712e-02, 2.20574417e-02],
           [1.30903162e-02, 1.39568628e-02, 2.68859177e-02],
           [1.56446668e-02, 1.61657821e-02, 3.22265830e-02],
           [1.85192677e-02, 1.84714636e-02, 3.80726091e-02],
           [2.17441375e-02, 2.08614794e-02, 4.42384270e-02],
           [2.53482934e-02, 2.33246768e-02, 5.03177603e-02],
           [2.93588512e-02, 2.58513126e-02, 5.63003099e-02],
           [3.38005062e-02, 2.84330585e-02, 6.21791351e-02],
           [3.86953900e-02, 3.10628831e-02, 6.79494902e-02],
           [4.39143239e-02, 3.37347181e-02, 7.36090672e-02],
           [4.91960412e-02, 3.64432569e-02, 7.91575047e-02],
           [5.45402342e-02, 3.91837658e-02, 8.45959051e-02],
           [5.99402220e-02, 4.19109204e-02, 8.99264938e-02],
           [6.53904060e-02, 4.45472500e-02, 9.51523688e-02],
           [7.08857137e-02, 4.71065257e-02, 1.00276681e-01],
           [7.64222344e-02, 4.95920820e-02, 1.05302977e-01],
           [8.19963002e-02, 5.20070966e-02, 1.10234424e-01],
           [8.76054324e-02, 5.43539661e-02, 1.15074421e-01],
           [9.32473212e-02, 5.66349664e-02, 1.19825919e-01],
           [9.89201055e-02, 5.88520625e-02, 1.24491650e-01],
           [1.04622292e-01, 6.10069515e-02, 1.29074108e-01],
           [1.10352685e-01, 6.31011020e-02, 1.33575541e-01],
           [1.16110322e-01, 6.51357886e-02, 1.37997959e-01],
           [1.21894049e-01, 6.71123916e-02, 1.42343018e-01],
           [1.27703440e-01, 6.90317393e-02, 1.46612383e-01],
           [1.33537916e-01, 7.08947251e-02, 1.50807424e-01],
           [1.39396642e-01, 7.27023953e-02, 1.54929258e-01],
           [1.45279502e-01, 7.44552261e-02, 1.58979020e-01],
           [1.51185851e-01, 7.61540460e-02, 1.62957564e-01],
           [1.57115345e-01, 7.77994211e-02, 1.66865687e-01],
           [1.63067814e-01, 7.93917403e-02, 1.70704093e-01],
           [1.69042786e-01, 8.09315899e-02, 1.74473337e-01],
           [1.75039893e-01, 8.24194415e-02, 1.78173908e-01],
           [1.81059031e-01, 8.38555153e-02, 1.81806237e-01],
           [1.87099918e-01, 8.52401387e-02, 1.85370664e-01],
           [1.93162290e-01, 8.65735883e-02, 1.88867465e-01],
           [1.99245900e-01, 8.78560927e-02, 1.92296860e-01],
           [2.05350514e-01, 8.90878357e-02, 1.95659015e-01],
           [2.11475909e-01, 9.02689584e-02, 1.98954047e-01],
           [2.17621871e-01, 9.13995614e-02, 2.02182030e-01],
           [2.23788191e-01, 9.24797070e-02, 2.05342991e-01],
           [2.29974666e-01, 9.35094202e-02, 2.08436920e-01],
           [2.36181097e-01, 9.44886910e-02, 2.11463768e-01],
           [2.42407285e-01, 9.54174748e-02, 2.14423449e-01],
           [2.48653033e-01, 9.62956941e-02, 2.17315846e-01],
           [2.54918146e-01, 9.71232392e-02, 2.20140807e-01],
           [2.61202425e-01, 9.78999689e-02, 2.22898150e-01],
           [2.67505672e-01, 9.86257115e-02, 2.25587662e-01],
           [2.73827684e-01, 9.93002649e-02, 2.28209102e-01],
           [2.80168214e-01, 9.99234438e-02, 2.30762217e-01],
           [2.86527087e-01, 1.00494952e-01, 2.33246701e-01],
           [2.92904117e-01, 1.01014475e-01, 2.35662223e-01],
           [2.99299087e-01, 1.01481691e-01, 2.38008434e-01],
           [3.05711775e-01, 1.01896252e-01, 2.40284957e-01],
           [3.12141953e-01, 1.02257782e-01, 2.42491394e-01],
           [3.18589368e-01, 1.02565895e-01, 2.44627325e-01],
           [3.25053819e-01, 1.02820114e-01, 2.46692285e-01],
           [3.31535055e-01, 1.03019976e-01, 2.48685794e-01],
           [3.38032820e-01, 1.03164990e-01, 2.50607354e-01],
           [3.44546845e-01, 1.03254637e-01, 2.52456437e-01],
           [3.51076877e-01, 1.03288342e-01, 2.54232480e-01],
           [3.57622623e-01, 1.03265536e-01, 2.55934910e-01],
           [3.64183781e-01, 1.03185620e-01, 2.57563126e-01],
           [3.70760038e-01, 1.03047966e-01, 2.59116502e-01],
           [3.77351067e-01, 1.02851920e-01, 2.60594389e-01],
           [3.83956569e-01, 1.02596747e-01, 2.61996082e-01],
           [3.90576171e-01, 1.02281760e-01, 2.63320888e-01],
           [3.97209483e-01, 1.01906255e-01, 2.64568091e-01],
           [4.03856110e-01, 1.01469485e-01, 2.65736942e-01],
           [4.10515637e-01, 1.00970683e-01, 2.66826663e-01],
           [4.17187630e-01, 1.00409065e-01, 2.67836455e-01],
           [4.23871630e-01, 9.97838299e-02, 2.68765489e-01],
           [4.30567220e-01, 9.90940626e-02, 2.69612856e-01],
           [4.37273825e-01, 9.83390454e-02, 2.70377735e-01],
           [4.43990902e-01, 9.75179602e-02, 2.71059225e-01],
           [4.50717882e-01, 9.66299926e-02, 2.71656404e-01],
           [4.57454160e-01, 9.56743388e-02, 2.72168324e-01],
           [4.64199096e-01, 9.46502147e-02, 2.72594015e-01],
           [4.70952011e-01, 9.35568659e-02, 2.72932487e-01],
           [4.77712185e-01, 9.23935807e-02, 2.73182727e-01],
           [4.84478852e-01, 9.11597046e-02, 2.73343703e-01],
           [4.91251201e-01, 8.98546586e-02, 2.73414368e-01],
           [4.98028368e-01, 8.84779606e-02, 2.73393658e-01],
           [5.04809432e-01, 8.70292511e-02, 2.73280497e-01],
           [5.11593415e-01, 8.55083238e-02, 2.73073798e-01],
           [5.18379342e-01, 8.39150122e-02, 2.72772380e-01],
           [5.25166134e-01, 8.22494515e-02, 2.72375098e-01],
           [5.31952539e-01, 8.05122834e-02, 2.71880942e-01],
           [5.38737298e-01, 7.87043509e-02, 2.71288821e-01],
           [5.45519067e-01, 7.68269213e-02, 2.70597660e-01],
           [5.52296623e-01, 7.48812386e-02, 2.69806076e-01],
           [5.59068347e-01, 7.28699039e-02, 2.68913162e-01],
           [5.65832532e-01, 7.07962594e-02, 2.67918039e-01],
           [5.72587710e-01, 6.86635981e-02, 2.66819305e-01],
           [5.79331934e-01, 6.64772870e-02, 2.65616210e-01],
           [5.86063254e-01, 6.42436714e-02, 2.64307878e-01],
           [5.92779794e-01, 6.19700208e-02, 2.62893141e-01],
           [5.99479180e-01, 5.96665800e-02, 2.61371598e-01],
           [6.06159287e-01, 5.73445471e-02, 2.59742219e-01],
           [6.12817585e-01, 5.50185447e-02, 2.58004603e-01],
           [6.19451388e-01, 5.27062755e-02, 2.56158529e-01],
           [6.26058265e-01, 5.04274362e-02, 2.54203051e-01],
           [6.32635052e-01, 4.82078149e-02, 2.52138672e-01],
           [6.39178736e-01, 4.60765022e-02, 2.49965440e-01],
           [6.45686145e-01, 4.40673835e-02, 2.47683646e-01],
           [6.52154034e-01, 4.22189157e-02, 2.45293610e-01],
           [6.58578780e-01, 4.05753364e-02, 2.42796538e-01],
           [6.64956734e-01, 3.91749768e-02, 2.40193680e-01],
           [6.71284117e-01, 3.80988058e-02, 2.37486642e-01],
           [6.77557026e-01, 3.73849955e-02, 2.34677441e-01],
           [6.83771458e-01, 3.70710120e-02, 2.31768530e-01],
           [6.89923336e-01, 3.71957541e-02, 2.28762821e-01],
           [6.96008545e-01, 3.77993224e-02, 2.25663672e-01],
           [7.02022989e-01, 3.89227175e-02, 2.22474813e-01],
           [7.07962522e-01, 4.06051770e-02, 2.19200808e-01],
           [7.13823124e-01, 4.28152698e-02, 2.15846529e-01],
           [7.19600903e-01, 4.55509927e-02, 2.12417307e-01],
           [7.25292166e-01, 4.87906753e-02, 2.08918810e-01],
           [7.30893419e-01, 5.25043780e-02, 2.05357244e-01],
           [7.36401449e-01, 5.66564938e-02, 2.01739196e-01],
           [7.41813395e-01, 6.12082326e-02, 1.98071388e-01],
           [7.47126766e-01, 6.61198342e-02, 1.94360771e-01],
           [7.52339481e-01, 7.13521459e-02, 1.90614390e-01],
           [7.57449908e-01, 7.68677198e-02, 1.86839205e-01],
           [7.62456864e-01, 8.26314942e-02, 1.83042221e-01],
           [7.67359644e-01, 8.86111334e-02, 1.79230099e-01],
           [7.72158005e-01, 9.47771849e-02, 1.75409115e-01],
           [7.76852146e-01, 1.01103032e-01, 1.71585232e-01],
           [7.81442690e-01, 1.07564768e-01, 1.67763999e-01],
           [7.85930660e-01, 1.14140972e-01, 1.63950648e-01],
           [7.90317418e-01, 1.20812734e-01, 1.60149383e-01],
           [7.94604635e-01, 1.27563263e-01, 1.56364069e-01],
           [7.98794245e-01, 1.34377758e-01, 1.52597983e-01],
           [8.02888392e-01, 1.41243231e-01, 1.48853803e-01],
           [8.06889384e-01, 1.48148338e-01, 1.45133620e-01],
           [8.10799686e-01, 1.55083088e-01, 1.41439247e-01],
           [8.14621838e-01, 1.62038874e-01, 1.37771840e-01],
           [8.18358362e-01, 1.69008490e-01, 1.34131654e-01],
           [8.22011806e-01, 1.75985716e-01, 1.30518691e-01],
           [8.25584913e-01, 1.82964649e-01, 1.26933774e-01],
           [8.29080054e-01, 1.89941244e-01, 1.23375392e-01],
           [8.32499822e-01, 1.96911376e-01, 1.19843312e-01],
           [8.35846551e-01, 2.03872080e-01, 1.16336064e-01],
           [8.39122742e-01, 2.10820344e-01, 1.12853110e-01],
           [8.42330430e-01, 2.17754563e-01, 1.09392030e-01],
           [8.45471918e-01, 2.24672683e-01, 1.05951884e-01],
           [8.48549348e-01, 2.31573211e-01, 1.02531262e-01],
           [8.51564531e-01, 2.38455464e-01, 9.91277593e-02],
           [8.54519355e-01, 2.45318645e-01, 9.57396155e-02],
           [8.57415600e-01, 2.52162215e-01, 9.23649868e-02],
           [8.60254941e-01, 2.58985854e-01, 8.90019586e-02],
           [8.63038948e-01, 2.65789440e-01, 8.56485599e-02],
           [8.65769086e-01, 2.72573015e-01, 8.23027753e-02],
           [8.68446718e-01, 2.79336765e-01, 7.89625561e-02],
           [8.71073108e-01, 2.86080997e-01, 7.56258300e-02],
           [8.73649599e-01, 2.92805842e-01, 7.22910881e-02],
           [8.76177423e-01, 2.99511576e-01, 6.89567380e-02],
           [8.78657342e-01, 3.06199145e-01, 6.56199479e-02],
           [8.81090375e-01, 3.12869014e-01, 6.22790299e-02],
           [8.83477905e-01, 3.19521067e-01, 5.89337677e-02],
           [8.85820121e-01, 3.26156876e-01, 5.55803500e-02],
           [8.88118480e-01, 3.32776117e-01, 5.22194130e-02],
           [8.90373119e-01, 3.39380266e-01, 4.88475887e-02],
           [8.92585344e-01, 3.45969125e-01, 4.54657078e-02],
           [8.94755093e-01, 3.52544282e-01, 4.20704006e-02],
           [8.96883784e-01, 3.59105308e-01, 3.86569780e-02],
           [8.98971320e-01, 3.65653694e-01, 3.53548630e-02],
           [9.01018186e-01, 3.72190097e-01, 3.22108120e-02],
           [9.03025558e-01, 3.78714300e-01, 2.92268466e-02],
           [9.04993218e-01, 3.85227734e-01, 2.64009469e-02],
           [9.06921602e-01, 3.91730969e-01, 2.37336682e-02],
           [9.08811112e-01, 3.98224572e-01, 2.12258407e-02],
           [9.10662374e-01, 4.04708821e-01, 1.88792772e-02],
           [9.12475532e-01, 4.11184498e-01, 1.66947717e-02],
           [9.14250744e-01, 4.17652316e-01, 1.46735519e-02],
           [9.15988274e-01, 4.24112830e-01, 1.28174796e-02],
           [9.17688355e-01, 4.30566591e-01, 1.11286604e-02],
           [9.19351190e-01, 4.37014141e-01, 9.60943927e-03],
           [9.20976957e-01, 4.43456016e-01, 8.26239780e-03],
           [9.22565807e-01, 4.49892743e-01, 7.09035029e-03],
           [9.24117867e-01, 4.56324842e-01, 6.09634086e-03],
           [9.25633243e-01, 4.62752821e-01, 5.28364041e-03],
           [9.27112016e-01, 4.69177180e-01, 4.65574380e-03],
           [9.28554249e-01, 4.75598410e-01, 4.21636708e-03],
           [9.29959984e-01, 4.82016989e-01, 3.96944486e-03],
           [9.31329343e-01, 4.88433300e-01, 3.91930853e-03],
           [9.32662599e-01, 4.94847571e-01, 4.07078660e-03],
           [9.33959441e-01, 5.01260525e-01, 4.42786218e-03],
           [9.35219845e-01, 5.07672600e-01, 4.99530857e-03],
           [9.36443775e-01, 5.14084223e-01, 5.77810504e-03],
           [9.37631309e-01, 5.20495700e-01, 6.78164462e-03],
           [9.38782857e-01, 5.26907052e-01, 8.01202063e-03],
           [9.39897796e-01, 5.33319138e-01, 9.47389995e-03],
           [9.40976042e-01, 5.39732340e-01, 1.11730493e-02],
           [9.42018001e-01, 5.46146634e-01, 1.31161327e-02],
           [9.43023502e-01, 5.52562451e-01, 1.53091295e-02],
           [9.43992046e-01, 5.58980450e-01, 1.77578064e-02],
           [9.44924066e-01, 5.65400553e-01, 2.04693627e-02],
           [9.45819408e-01, 5.71823127e-01, 2.34503712e-02],
           [9.46677454e-01, 5.78248864e-01, 2.67070528e-02],
           [9.47499063e-01, 5.84677347e-01, 3.02475356e-02],
           [9.48283302e-01, 5.91109469e-01, 3.40780276e-02],
           [9.49030364e-01, 5.97545285e-01, 3.82061904e-02],
           [9.49740354e-01, 6.03984907e-01, 4.25698454e-02],
           [9.50412555e-01, 6.10429015e-01, 4.69558770e-02],
           [9.51047798e-01, 6.16877197e-01, 5.13641749e-02],
           [9.51644767e-01, 6.23330515e-01, 5.57924820e-02],
           [9.52204718e-01, 6.29788267e-01, 6.02407659e-02],
           [9.52726048e-01, 6.36251666e-01, 6.47073760e-02],
           [9.53210101e-01, 6.42719959e-01, 6.91926085e-02],
           [9.53655291e-01, 6.49194307e-01, 7.36953593e-02],
           [9.54062829e-01, 6.55674047e-01, 7.82159662e-02],
           [9.54431364e-01, 6.62160153e-01, 8.27537663e-02],
           [9.54761683e-01, 6.68652237e-01, 8.73089763e-02],
           [9.55052976e-01, 6.75150900e-01, 9.18813143e-02],
           [9.55305328e-01, 6.81656184e-01, 9.64708164e-02],
           [9.55518730e-01, 6.88168186e-01, 1.01077489e-01],
           [9.55692309e-01, 6.94687506e-01, 1.05701200e-01],
           [9.55827096e-01, 7.01213617e-01, 1.10342144e-01],
           [9.55921701e-01, 7.07747405e-01, 1.15000141e-01],
           [9.55976394e-01, 7.14288780e-01, 1.19675260e-01],
           [9.55991177e-01, 7.20837804e-01, 1.24367505e-01],
           [9.55965163e-01, 7.27395036e-01, 1.29076818e-01],
           [9.55898786e-01, 7.33960287e-01, 1.33803218e-01],
           [9.55791514e-01, 7.40533901e-01, 1.38546653e-01],
           [9.55642701e-01, 7.47116271e-01, 1.43307086e-01],
           [9.55452708e-01, 7.53707242e-01, 1.48084467e-01],
           [9.55220923e-01, 7.60307177e-01, 1.52878733e-01],
           [9.54946698e-01, 7.66916444e-01, 1.57689828e-01],
           [9.54630095e-01, 7.73535035e-01, 1.62517664e-01],
           [9.54270846e-01, 7.80163110e-01, 1.67362141e-01],
           [9.53868070e-01, 7.86801130e-01, 1.72223200e-01],
           [9.53421366e-01, 7.93449301e-01, 1.77100747e-01],
           [9.52931058e-01, 8.00107472e-01, 1.81994611e-01],
           [9.52395958e-01, 8.06776223e-01, 1.86904745e-01],
           [9.51815534e-01, 8.13455802e-01, 1.91831047e-01],
           [9.51189340e-01, 8.20146407e-01, 1.96773397e-01],
           [9.50517391e-01, 8.26848014e-01, 2.01731615e-01],
           [9.49798443e-01, 8.33561179e-01, 2.06705663e-01],
           [9.49031874e-01, 8.40286154e-01, 2.11695432e-01],
           [9.48217026e-01, 8.47023196e-01, 2.16700816e-01],
           [9.47353715e-01, 8.53772343e-01, 2.21721640e-01],
           [9.46440777e-01, 8.60534061e-01, 2.26757863e-01],
           [9.45477316e-01, 8.67308679e-01, 2.31809410e-01],
           [9.44462505e-01, 8.74096484e-01, 2.36876199e-01],
           [9.43395466e-01, 8.80897769e-01, 2.41958158e-01]]

test_cm = ListedColormap(cm_data, name="ember")