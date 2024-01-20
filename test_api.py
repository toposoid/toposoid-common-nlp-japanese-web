'''
  Copyright 2021 Linked Ideal LLC.[https://linked-ideal.com/]
 
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
 
      http://www.apache.org/licenses/LICENSE-2.0
 
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 '''
from fastapi.testclient import TestClient
from api import app
from model import NormalizedWord, SynonymList, FeatureVector
import pytest

#This is a unit test module
client = TestClient(app)
def test_EmptyWord():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": ""})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms == []

def test_SimpleVerb():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "論ずる"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    print(synonymList.synonyms.sort())
    assert synonymList.synonyms.sort() == ['論じる', '論述', '話し合う'].sort()

def test_SimpleNoun():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "映画"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms.sort() == ['フィルム'].sort()

def test_VocabularyNotFoundInWordNet():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "確約"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms.sort() == ['了承', '承諾', '約束'].sort()

def test_VocabularyNotFoundInWord2Vec():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "秀逸だ"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms == []

def test_ChiveModel():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "SEO"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms.sort() == ['セスアップ', 'リスティング', '検索エンジン'].sort()


def test_ChikkarSynonym():
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "ケータイ"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())    
    assert synonymList.synonyms.sort() == ['mobile', '携帯', '携帯電話', 'モバイル'].sort()
    
def test_getFeatureVector():
    import math
    response = client.post("/getFeatureVector",
                        headers={"Content-Type": "application/json"},
                        json={"sentence": "これはテストですよ。"})    
    assert response.status_code == 200
    featureVector = FeatureVector.parse_obj(response.json())
    correctVector = [0.11278565973043442, 0.41439199447631836, -0.3037640452384949, -0.054304543882608414, 0.06245023384690285, -0.11185586452484131, 0.5146267414093018, 0.0387960784137249, -0.11964543908834457, -0.09259825944900513, 0.15635785460472107, -0.6553782820701599, -0.004797791596502066, 0.1388808786869049, -0.346933513879776, -0.23154209554195404, 0.011978760361671448, -0.36967983841896057, 0.09088843315839767, 0.2552296221256256, 0.493522971868515, 0.008029891178011894, -0.07049628347158432, -0.012411599047482014, -0.15882478654384613, -0.07334205508232117, 0.28148961067199707, 0.0795278325676918, 0.18321578204631805, -0.2145964652299881, -0.192158505320549, -0.0838189423084259, -0.01605088822543621, -0.3024359941482544, 0.1674102544784546, -0.013714100234210491, -0.08433681726455688, -0.08877121657133102, 0.09049775451421738, -0.00046337037929333746, 0.0506000779569149, -0.4661227762699127, 0.07084602117538452, 0.34180447459220886, 0.2991635799407959, 0.39541754126548767, -0.031037762761116028, -0.0935303345322609, -0.03739825263619423, 0.04362259432673454, -0.12734028697013855, -0.3896472454071045, -0.2044910043478012, -0.39742472767829895, 0.16174861788749695, -0.1469392329454422, 0.14017076790332794, -0.004293935839086771, -0.24609576165676117, 0.1051730141043663, 0.13289673626422882, -0.16445156931877136, -0.2635742723941803, 0.29018735885620117, 0.10369053483009338, -0.25155964493751526, 0.08692675083875656, -0.15325626730918884, 0.04157624766230583, 0.3079780042171478, -0.4209780693054199, -0.020185723900794983, 0.021750157698988914, 0.0803896114230156, 0.026983147487044334, 0.45166292786598206, -0.11633634567260742, -0.11859321594238281, 0.1885170340538025, -0.05752743408083916, 0.1731032282114029, 0.03917103260755539, -0.027868198230862617, -0.03465576097369194, 0.3128320276737213, 0.2753579616546631, -0.13890822231769562, 0.3449161946773529, -0.11904887109994888, 0.027363846078515053, 0.2947850227355957, -0.11781866103410721, 0.15735690295696259, 0.1125907227396965, 0.353948712348938, 0.030711138620972633, 0.04498124495148659, -0.2143888920545578, 0.2651039659976959, 0.83623868227005, -0.10994943231344223, 0.026629379019141197, -0.34675607085227966, -0.0686158761382103, 0.00013715215027332306, 0.12435527890920639, -0.17572380602359772, -0.38156428933143616, 0.14881299436092377, -0.1538851261138916, -0.011795188300311565, -0.04023187234997749, 0.09135564416646957, 0.2919345498085022, 0.06315300613641739, -0.14979787170886993, 0.08858317136764526, 0.07892470061779022, -0.055082764476537704, 0.68656325340271, 0.21269077062606812, -0.4363057315349579, 0.19436593353748322, -0.2583276331424713, 0.5138310790061951, -0.6999726295471191, 0.06888336688280106, 0.14556114375591278, 0.09423019737005234, -0.21916885673999786, 0.4268066883087158, 0.20736320316791534, -0.3674708604812622, 0.2902625501155853, -0.2802681028842926, -0.017437374219298363, 0.18657910823822021, 0.3138512372970581, 0.18721903860569, 0.27654483914375305, -0.2980172634124756, 0.3152415454387665, 0.16767019033432007, 0.335844486951828, -0.2768055498600006, -0.06964529305696487, -0.5889192223548889, 0.13459978997707367, 0.17292962968349457, -0.2566312551498413, 0.346661239862442, -0.13390322029590607, 0.05371632054448128, 0.1368667483329773, -0.35472914576530457, -0.2806723415851593, 0.08074039965867996, 0.19906176626682281, 0.10966487973928452, -0.29626405239105225, -0.38493430614471436, 0.23703332245349884, -0.2435845583677292, 0.21386031806468964, 0.3649493157863617, -0.24451828002929688, -0.03945596143603325, -0.07298202067613602, -0.0729999914765358, 0.15274499356746674, 0.7061511874198914, -0.06810928881168365, -0.10050776600837708, -0.2878923714160919, -0.13487429916858673, 0.12582944333553314, -0.041417233645915985, 0.40706586837768555, -0.2695784270763397, 0.0804041177034378, 0.2214682251214981, -0.16176140308380127, -0.044823016971349716, -0.06749343872070312, -0.1350317746400833, 0.1284780502319336, -0.2976321578025818, -0.09528114646673203, 0.11841193586587906, 0.28807446360588074, -0.039475034922361374, -0.03895556181669235, -0.17381437122821808, 0.42097190022468567, -0.31263789534568787, -0.15649285912513733, 0.3540680408477783, -0.12985627353191376, -0.11849554628133774, -0.2642899751663208, -0.13150325417518616, -0.18474994599819183, 0.08638527244329453, -0.25631189346313477, 0.40141716599464417, 0.08849135786294937, 0.2473926544189453, -0.6509702205657959, 0.31066396832466125, 0.05104253068566322, -0.4556894302368164, -0.1519988477230072, -0.20185010135173798, -0.01897672936320305, 0.08236310631036758, -0.20054690539836884, -0.12233958393335342, -0.13411274552345276, -0.022364655509591103, 0.07158804684877396, -0.23592509329319, -0.31141841411590576, 0.20665937662124634, -0.620215892791748, -0.3500767648220062, -0.13181084394454956, -0.040625911206007004, 0.28839775919914246, 0.24937520921230316, -0.28372082114219666, 0.7051567435264587, 0.05615020915865898, 0.06173677742481232, 0.21720372140407562, 0.2037050724029541, -0.3387092053890228, -0.47984468936920166, 0.3562517464160919, -0.12952500581741333, -0.12634186446666718, -0.1791180521249771, -0.0937257707118988, 0.19539940357208252, -0.0422772653400898, -0.00701667508110404, 0.39389416575431824, 0.15408110618591309, 0.30928125977516174, -0.13130371272563934, 0.15693286061286926, -0.3148290812969208, -0.5973447561264038, 0.025083845481276512, 0.011120874434709549, -0.2213357537984848, -0.08941057324409485, 0.10881730169057846, 0.7285277843475342, 0.07962740212678909, -0.004177784081548452, 0.6003431081771851, -0.2342361956834793, -0.0014756893506273627, -0.08188766986131668, -0.014828766696155071, 0.08802015334367752, -0.040141236037015915, 0.1536916047334671, -0.0922597274184227, 0.23512166738510132, 0.10349816828966141, -0.11668816208839417, -0.07503877580165863, 0.18904507160186768, 0.08894229680299759, -0.1578015685081482, 0.028432318940758705, 0.10391929000616074, -0.05611351132392883, 0.05380607023835182, -0.16976559162139893, -0.37874993681907654, -0.04356588050723076, 0.07775814086198807, 0.28126856684684753, -0.20482508838176727, 0.21596203744411469, -0.10789752006530762, 0.0009096010471694171, 0.08970040082931519, -0.20217084884643555, 0.4396161139011383, 0.11080700159072876, 0.030551254749298096, -0.34465956687927246, 0.013970263302326202, 0.049880947917699814, -0.379999041557312, 0.12837333977222443, -0.02683260105550289, -0.29960259795188904, 0.2772023379802704, -0.44816648960113525, -0.04645182192325592, -0.010727599263191223, -0.09514069557189941, 0.14526720345020294, 0.3432563245296478, 0.23962421715259552, -0.05416618660092354, -0.044949278235435486, 0.07254564017057419, -0.053535524755716324, 0.33438706398010254, 0.19908513128757477, 0.0036502026487141848, -0.297419011592865, -0.14601677656173706, 0.1545119434595108, -0.37212851643562317, -0.09616126865148544, -0.15201909840106964, -0.29049867391586304, -0.025860905647277832, -0.025905989110469818, 0.251146137714386, -0.27911749482154846, -0.5049433708190918, -0.07062844187021255, -0.22494278848171234, -0.06990737468004227, 0.45163726806640625, -0.30654188990592957, -0.030230572447180748, -0.06615392118692398, 0.25338348746299744, -0.24649499356746674, 0.24580352008342743, -0.11402004957199097, -0.031281180679798126, 0.07329420745372772, -0.22316746413707733, -0.04488551989197731, -0.10518496483564377, -0.11443483084440231, 0.15220379829406738, -0.11687026172876358, -0.0652225986123085, -0.10624736547470093, -0.29237100481987, 0.07728082686662674, 0.280716210603714, -0.16781629621982574, -0.07840292900800705, 0.24126309156417847, 0.17070001363754272, -0.13392581045627594, 0.2686889171600342, 0.20155352354049683, 0.132932648062706, -0.18898867070674896, -0.26596546173095703, -0.08360010385513306, 0.2282651662826538, 0.17484928667545319, -0.045539721846580505, -0.43362030386924744, -0.17450682818889618, -0.1271907091140747, -0.09144792705774307, -0.1405448168516159, -0.03153778240084648, -0.09690139442682266, -0.16569817066192627, 0.2353072613477707, 0.1891816258430481, 0.17174874246120453, -0.12341713905334473, -0.3595544397830963, 0.25609102845191956, 0.30055350065231323, 0.3907020390033722, 0.27239248156547546, 0.11891061812639236]
    x = False in list(map(lambda x: math.isclose(x[0], x[1], abs_tol=0.00001), zip(featureVector.vector, correctVector)))
    assert not x
    

