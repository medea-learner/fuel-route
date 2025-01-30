import os
import pandas as pd


def load_fuel_prices():
    """
    Load fuel price data from a CSV file.

    :return: Pandas DataFrame containing fuel price data.
    """
    fuel_data = pd.read_csv('api/data/fuel-prices-for-be-assessment.csv')
    return fuel_data


def clean_fuel_data():
    """
    Clean and extract relevant columns from the fuel price dataset.

    :return: Pandas DataFrame with selected columns ('Truckstop Name', 'Address', 'City', 'State', 'Retail Price').
    """
    fuel_data = load_fuel_prices()
    cleaned_data = fuel_data[['Truckstop Name', 'Address', 'City', 'State', 'Retail Price']]
    cleaned_data.to_csv('api/data/cleaned_fuel_prices.csv', index=False)
    return cleaned_data


def load_cleaned_fuel_data():
    """
    Load the cleaned fuel price data from a CSV file. If the file does not exist, clean the raw data first.

    :return: Pandas DataFrame containing cleaned fuel price data.
    """
    # Check if the cleaned data file exists, if not, clean the data
    if not os.path.exists('api/data/cleaned_fuel_prices.csv'):
        cleaned_data = clean_fuel_data()
    else:
        cleaned_data = pd.read_csv('api/data/cleaned_fuel_prices.csv')
    return cleaned_data

def generate_cache_key(start, end):
    return f"directions_{start[0]}_{start[1]}_{end[0]}_{end[1]}"

directions_response1 = {
  "bbox": [
    -122.419446,
    34.052335,
    -118.227337,
    37.827531
  ],
  "routes": [
    {
      "summary": {
        "distance": 615306.6,
        "duration": 23349.5
      },
      "segments": [
        {
          "distance": 615306.6,
          "duration": 23349.5,
          "steps": [
            {
              "distance": 247.8,
              "duration": 33.1,
              "type": 11,
              "instruction": "Head northeast on Market Street",
              "name": "Market Street",
              "way_points": [
                0,
                5
              ]
            },
            {
              "distance": 191.5,
              "duration": 24.6,
              "type": 1,
              "instruction": "Turn right onto 10th Street",
              "name": "10th Street",
              "way_points": [
                5,
                8
              ]
            },
            {
              "distance": 1917.1,
              "duration": 193.4,
              "type": 0,
              "instruction": "Turn left onto Mission Street",
              "name": "Mission Street",
              "way_points": [
                8,
                36
              ]
            },
            {
              "distance": 125.2,
              "duration": 10,
              "type": 1,
              "instruction": "Turn right onto New Montgomery Street",
              "name": "New Montgomery Street",
              "way_points": [
                36,
                38
              ]
            },
            {
              "distance": 88.5,
              "duration": 21.3,
              "type": 0,
              "instruction": "Turn left onto Natoma Street",
              "name": "Natoma Street",
              "way_points": [
                38,
                39
              ]
            },
            {
              "distance": 261.5,
              "duration": 35,
              "type": 1,
              "instruction": "Turn right onto 2nd Street",
              "name": "2nd Street",
              "way_points": [
                39,
                46
              ]
            },
            {
              "distance": 117.9,
              "duration": 14.2,
              "type": 0,
              "instruction": "Turn left onto Folsom Street",
              "name": "Folsom Street",
              "way_points": [
                46,
                48
              ]
            },
            {
              "distance": 202.3,
              "duration": 16.2,
              "type": 13,
              "instruction": "Keep right onto Essex Street",
              "name": "Essex Street",
              "way_points": [
                48,
                54
              ]
            },
            {
              "distance": 9485.6,
              "duration": 602.9,
              "type": 6,
              "instruction": "Continue straight",
              "name": "-",
              "way_points": [
                54,
                106
              ]
            },
            {
              "distance": 74354.1,
              "duration": 2817.5,
              "type": 13,
              "instruction": "Keep right",
              "name": "-",
              "way_points": [
                106,
                696
              ]
            },
            {
              "distance": 388635.1,
              "duration": 13993.7,
              "type": 13,
              "instruction": "Keep right onto William Elton Brown Freeway, I 580",
              "name": "William Elton Brown Freeway, I 580",
              "way_points": [
                696,
                1379
              ]
            },
            {
              "distance": 35498.9,
              "duration": 1328.9,
              "type": 13,
              "instruction": "Keep right onto West Side Freeway, I 5 Truck",
              "name": "West Side Freeway, I 5 Truck",
              "way_points": [
                1379,
                1586
              ]
            },
            {
              "distance": 61716.4,
              "duration": 2338.7,
              "type": 6,
              "instruction": "Continue straight onto Golden State Freeway, I 5",
              "name": "Golden State Freeway, I 5",
              "way_points": [
                1586,
                2031
              ]
            },
            {
              "distance": 3318.9,
              "duration": 125.8,
              "type": 6,
              "instruction": "Continue straight onto Golden State Freeway, I 5",
              "name": "Golden State Freeway, I 5",
              "way_points": [
                2031,
                2050
              ]
            },
            {
              "distance": 8533.4,
              "duration": 322.2,
              "type": 13,
              "instruction": "Keep right onto I 5 Truck",
              "name": "I 5 Truck",
              "way_points": [
                2050,
                2122
              ]
            },
            {
              "distance": 24908.6,
              "duration": 943.9,
              "type": 13,
              "instruction": "Keep right onto Golden State Freeway, I 5",
              "name": "Golden State Freeway, I 5",
              "way_points": [
                2122,
                2352
              ]
            },
            {
              "distance": 211.3,
              "duration": 16.9,
              "type": 13,
              "instruction": "Keep right",
              "name": "-",
              "way_points": [
                2352,
                2354
              ]
            },
            {
              "distance": 3507.2,
              "duration": 285.7,
              "type": 13,
              "instruction": "Keep right",
              "name": "-",
              "way_points": [
                2354,
                2398
              ]
            },
            {
              "distance": 119.5,
              "duration": 14.3,
              "type": 13,
              "instruction": "Keep right",
              "name": "-",
              "way_points": [
                2398,
                2402
              ]
            },
            {
              "distance": 593.3,
              "duration": 50.6,
              "type": 12,
              "instruction": "Keep left",
              "name": "-",
              "way_points": [
                2402,
                2418
              ]
            },
            {
              "distance": 401.7,
              "duration": 43.3,
              "type": 12,
              "instruction": "Keep left",
              "name": "-",
              "way_points": [
                2418,
                2427
              ]
            },
            {
              "distance": 318.6,
              "duration": 49.1,
              "type": 13,
              "instruction": "Keep right",
              "name": "-",
              "way_points": [
                2427,
                2435
              ]
            },
            {
              "distance": 443.6,
              "duration": 47.8,
              "type": 1,
              "instruction": "Turn right onto North Spring Street",
              "name": "North Spring Street",
              "way_points": [
                2435,
                2441
              ]
            },
            {
              "distance": 108.6,
              "duration": 20.6,
              "type": 0,
              "instruction": "Turn left onto West 1st Street",
              "name": "West 1st Street",
              "way_points": [
                2441,
                2444
              ]
            },
            {
              "distance": 0,
              "duration": 0,
              "type": 10,
              "instruction": "Arrive at West 1st Street, on the right",
              "name": "-",
              "way_points": [
                2444,
                2444
              ]
            }
          ]
        }
      ],
      "bbox": [
        -122.419446,
        34.052335,
        -118.227337,
        37.827531
      ],
      "geometry": "k|peFp`ejVOU]c@{@kAOU_EsFtCwDJOrAiB_@g@_@i@y@gAcAuAg@q@w@eAsC}DwBuCOSwEsGaJ{LoBmCaCeDkBgC_@i@g@q@[c@oAgBiA}AoAeBOSGWuC{DoD{EUKaAsAu@eAwBwCtAeBjA_BqBkCnAcBHKXa@z@eAhA{AdA{ALQOOeCmDCO@IBGfDoEl@cA@c@FmB?mBIiAO}@I_@Uw@Wq@[q@{@uA_@i@{@_A{eCmoCKMaDkDqFaG_AeAiDuD}BaC{AgByAqBwAyBaAaB}@eBcSeb@k@qAw@oBiAqDs@uCk@{C[_C[{CqNsiBy@kM_@cIUcGAS]aLMyD[gG[}Dg@aFMaBo@uGi@oF_@sDm@uFoAoMyAkO[{EeAiSScCc@wDUuC]wCeAaK}@yHiBsNU{AY}A_@wAy@sC_@{AM}@IaAGaB?cAD_AHaAL_A\\{AlAmDTy@p@wCL_AH}@JaCAcAIgBIaBo@yFgAgKg@aEO{BE{BD}BRaCr@}Ep@qE\\{Bf@kDnA_JVaB`AgGt@eFT_B`B{KT}Ab@sCn@iEfAqHZiB\\kCrBmPT{ARmAVmAr@{CbAqDhAoDl@cB|A{DxAaDt@{Ar@uAr@mAfAiBjBmCvAiB`ByAfBqAz@e@z@a@vBu@nBe@hCa@jIaBjDq@f@MfAc@d@WhA{@d@e@\\a@v@wAx@wB\\iAViAlAwGrAmHdBgJt@gDpBsHrGgQvBqGv@qB|@wB`AsB`B_DvAuB|KaO`@m@x@{At@eBZy@p@{Bd@uB`@gCVuBhCaTrBcPPuAb@uCdB}K~A_K`DcSr@eD\\oA^mArGqQ`@iApAgD`AsBnAyBj@{@~AsBn@q@xNsMbAcAbAiAz@cAx@mAp@iAnByDrGmP^}@lC}Gn@mBnAmEt@}Cn@gDf@{Cj@_FTmCJaBDaALwDRqNTwT@kAHoDP_C^gCl@yBXy@x@iBhG}KbBgD|@oBxBiF|J_VxBmGbGwP^cAjCaHlHmQjAsCdCuEbBiCfB{Bv@{@pBoBlB}Ax@m@hBkAlDgBpM}Gz@g@pBwA~HeGvCmBzKmGpB{@dBm@dBa@fBSr@Cz@@pBNhB`@fBp@n@\\fBxA`A|@vFlGnAfAf@^vAt@bBf@pCd@`BHzCGtAWtAc@jE_B`SaItAu@j@_@n@g@j@i@pAuAd@o@pEcHp@_Ap@u@pAkAnHcFj@c@rAkAlAsAh@q@xEsGbAkAd@a@jA}@h@]n@]zAm@n@Q|AYpFw@hAOxCc@bEo@zGoAbCc@rBa@fASjB]vEk@bKy@nAQvBe@pAc@zBcAnAu@bFoD`EwCvBwA`DkBtC}AdBy@dEcBbN}EbBw@lCaB|AmA~A{An@s@tAgBlAkB`AgBz@mBr@iBhCaH~AoD`AaB~@uAvIuLrAsBbAuBnAoDtDqKbAkCrA}ClCsFvHsNfJ}PtAyBxAkBtAyA|@{@jJeItEaExBqBjAeAdSgQx@_Ax@eAr@iA`@w@t@cBf@wAj@sBZ}A\\}BNaBLaBDuB?qAEcBa@yHa@wHKeEAYQoHAyBGqc@CiM@aNIkXAuBG_HKeE[iG[cEe@aEi@}DuByLs@}DwD_Si@kD_@uDIcBG_BA{DFkDx@mODaC@yBGgDU_Ec@_Eq@{D_AsD}@oCeAiCaB{CcA}AaAoAqCaDoE_FsIqJoAcBeAgBqAiCy@sB_AwC{@mD[mB[}BO_BQoCIuC?gCFgDReDVeCT_BdBwJV}Ah@{EJyBFsC@gCEcCKaCQcCW}BYkBWyAm@iC{BiIg@yBi@}Cc@aEMcCIaCsBgmAAiEBiCJeEJcCd@cGd@cEj@_Ev@}Dz@wDdAwDtFqPn@sB|@wD`@{BZ}BRaC~@iP`@eG\\aEbAsKLkA|Dka@ZcEVcEPcEJeEFeGAgGGeEKcESeEWcESaC{BcUScDIeDAcDTyyABmNB_TEoEGeBKcB[}Dg@yDy@iFEk@uB_OaEcYaB{LsA{JUiBSyBWsGAm@EkDJc\\Ho@FcFFmWJyNB{c@@uBHc[CcLD}FBsFDsJ@wTC_W?eA?aKJcb@DgZ?qBTu_ABkLDwf@@}WRmaAXi~@CyNNgYF{j@@_]JmZ@mDA}H@wBD}DAyBFwCHeATyBdDwVTcCFiAHaCBeAAeCCkA[uIIyBcByb@Q}EYeF]eFa@eFQmBuBsU{Egh@YeEQyDMuDG}DA{A?aFPwOl@m`@j@}[DmJCwDIeDQwCUqCu@cGc@oCg@aC{@mDmQmj@iBkGq@qBiB{F_D{JkGgRmGaSiAoDk@qBmAuDaCmHiFqP_EuLcEiMcBgGeAkF_AuG_BqLi@gEaCuR{@qHmHen@eAgHsD_UW}BQeCG{B@}BHcC~@eQNaCXyB`@qBh@mBv@qB~@iBbCcEdAkBz@mBt@uBj@wBf@cC\\}BTgCJ{BDeCCqCMgCUcC]cCmBeK_EmToBwJsAyFeCaL{DkQoNsn@yJ_c@}CqIqEyFyIiGgD{CmCuD_BmCiCcGg@yAs@aCWeCa@sEyAyk@aBai@w@uKcBmMgBeKwGo^m@iEyAgMkGek@kDg\\QaByByUWgC[{De@mJeAoWDuCGmFEqBMgL?iCHmETkEpBsX`@iE\\cCd@_Cj@}Br@yBv@uB^w@`AmBfAgBjAaB|BwCbPoShEcFvjAgsApFoGvBoClBkCjBqCfBuCbBwC~BkEnZml@zAwCpf@o`ATe@nY}j@|@cB`JeQXm@|n@}mApe@}~@Vg@lYoj@no@aoA|Sqa@jBqDh@gAh[om@|Twc@~AuC`iAeyBlSo`@xh@cdAvCwF`^cr@nhA_xBbB}C~B_EpCqEbCqDhZsb@f@s@piAw_Bx@iAzt@ceAh@s@hT{Zx_@qi@r]yf@zyA{tB^k@npCs{DlG_Jd@o@nBiCv@iAbMkQjU{[lCqDlkBw~B\\c@|v@u`AtQoUnBqCtFkIpk@{{@`C}CbD{DvKaLj@i@phAeiAf@g@va@cb@pGoG~CiD~CqC~C{ClD{DxPyPfNmNv@k@fCyBjCsBrCqBrDyBpD{BjSoMbKgG|DeC|DoCxAgAvA{@`By@~QsLhL{I~^iVvH_F`GmDhJiEbP}GfKgDbKsEfMkFfGuBpOcGpBy@rHwCfAi@xc@kQ`HaDvGcDpJoFhg@e[`@WxVuOpLiHlAu@nQ{Krf@uZjJwFfB}@jCqAvD_BhGqBnImBn@O~h@wLl@M|cAoUf|@wR~@U`UsFvPiDtMuCvCy@dT_F|Cq@rOiDrOqDtZ}GbCk@zA_@vNaD`AU~NgDzUkFr@QrQaEdL}Bd^eGlYwEx@KxTsDlQyCp{AmVdAQtaAcPd]oFxFkAxb@eHt@K~J}An_@oGpOeChV}D\\GbTkDxAWd|Ceg@t@MzeBkY`FcAxF_BrFqBzFkCjGiD|d@{Wp@_@``Aoi@n@_@|KiGlF_DtNeIzReLpZyP~FmDdNyHpEoC~Ay@nsAiv@vC}Apm@o]v`@_UdAm@bH{DpAq@jMsH|LcHnBeArAs@dWaOvZ}PzA{@~GaElHsEjSiOr@m@vMyJx@o@xFmEhRyNrAcAfCoBta@g[rHcGlC{BdFuEbFyEz{@_z@v@s@jAgArBmBtIiId@g@lz@qx@dF_F~l@ok@lL}KbAy@d@_@lAuApUaUjc@_b@v@y@rq@yo@r_@__@j\\k[t@q@rPePvCyCrF_FbOuNfSmRzJsJ|HqHh@e@~\\_\\nEcEpLmLz[wZvOqMhGsFjTwQ`CgBvEuDdK_JvUuRbFsEpOoMvSuP~N_M~JuItVwSrBgB~D_EzEmFnKeNpx@meAz@gAbAuAnB_CtL}OxOoSfCkDtBkCpD_FvAcB~c@ol@lSqWnTiYx@sArRuVxGwIlAsAhJwKzCgDtEyErJaKjLiLfDqDzT_UhCsC`A}@xA_B`BsBtByBbDuDdOcQhAuA~@eAdAsAtFeGpDuD|CwChC}BtCaCpEqDvDeDdY{Ujf@ga@hLuJlI}Gl@i@jAaAxNwKfLsHpL}GVUnk@{]fMsHrYiQdSaMlWsOrRqL|IuF|JcGpFmDbGoDrb@sWzjGgwDtA{@|oCsbBn_@eUdMyHzlAct@h`GooDne@}Zdq@_f@r`@{Xj`@kXl[aUxQgMdNyJbJkG~@k@fByA`r@gf@f{@_m@fOuK|P{Lzm@yb@xAeAzw@sj@he@k\\nj@a`@fWsQ|HoGjGgGhFyGvJcNpPsVh_@ui@zZed@|Tk\\~E{GrFmIh_@si@p@_AlsAaoBfdAmzAbnBerCznAqhBb^ih@rBuCdLqPrGgJtEaHvJmNhm@c|@jJcLfKiKp[e\\zj@gk@fs@is@bAeAfFeFpCwCjEeE|l@eg@hYkU`NqLvIuHnBgB`BwAxJcKrVoUxIsInl@ej@`c@wa@pRmQnSaRhr@km@n[oXzXoVpFqEdj@ie@`j@qe@nAgApG{FjhAi`A~f@ac@pAgA~ZcXl\\aYfUeSn|@{u@bmA}dAhcA{{@pAkA|i@ge@rP{N|UkStr@em@lb@q]dh@ga@tr@wj@vTaSpV{SjWiUpIeHfBuA|DcCxK}FtNeIhaBe}@rKuF`_Bq{@b_@gS|KeGreAok@|o@_^dB{@fdCsrArxAqw@ztAau@xAw@jH{DhEwCxDqC|DkDpBgBzx@at@|BqB~|CsoCla@k^j{EshEvh@_e@bA_Ahe@{a@lEyD`e@ab@tEeFlBaC|AyBfBkC~AkClAwBvI}PrAaCtTec@zIyPbJ{Qf{@sbBlXmi@hJqQv^{s@fVgi@dYen@dWik@bKyTbHuOhFkKjEkI~IgPxC_FnEmIxIqO`GsK`DwF|E_Jdc@{v@dKaR`G{K`GaKlJ_QnAeC`EuG~CgEvAgBdIyIdGmG`F_FtIiJvSwSxIiJtFwFlD{Dzw@_y@fMsMzB_C`MkMlAoAh~Au`BhBkBrb@_d@~^k_@bZe[jRmRnc@od@zI{IhM{MbKeKp]o^ddAseAfNwNvc@id@hJ{JvVgWvFcGxPgQfGgGzTqUjVyVvEwEpNgNrLuKvd@wb@rO_OlK{JtJ}I~ZyY|VeU~ZsYro@wl@l]iXtS{OrLkJxL}Irg@}_@~gGwdEz|@im@lnC_jBp}AseAle@w[nc@{Y``Aso@thBsmAvaFehDxzG}qEnb@mY~J}G|e@u[pEeDpC}BdHqGvU_U`IyHz]s\\~bC_}BzQaRdS}Tf}@ocAjv@g{@xtA{{An[u^ll@wo@jh@kl@niA{oArDiEf[u]|LeN`G_I|GyJfk@e|@~pDatF|HeMjVu^b[}e@lk@}{@xzBeiD~`@sm@rpAgnBnMqRdDaFtBiDzj@e{@zp@cdAbVk_@fSuZxQiYjf@yv@rk@y}@|MmTrZue@brAitB~Zcf@tTy]Xc@`a@qn@zXed@d]ii@xWqa@dWw^|Yua@zPcVtCcErZma@xF}Gzg@oj@tuBm}B`c@ke@d`G_qG~cAahAne@_h@hM_Nxj@}m@tj@io@`|@ccAfCyCrF_GzwAkaBd^qa@ho@{t@r`DaqDn`AsgAfa@ud@pb@if@zf@uj@dY{ZhdAyhApe@uh@d^i`@h[o]~XwZpOmPhSyThBoBfAeAbNoO|UqW~GqGf_@_]z_@y\\~QwPbEaEdCmCbCuCxd@wl@xV}[lCsCnB_B`BoAbBiA|A}@nAo@vAg@rGkCpXmKnCiAzNuFlKcErLgEp@c@rfBw_@xTqE|JaCbYgGdn@{M`Ds@dQoDzSyEhy@kQlUcFjk@}LbTwE|Ck@nBYzC[j@E~@GlDEhD?vCJpIJ|AJjDBzCCt@Kx@SpAc@rAq@lFsD~Aw@dD_A~@QhBMpAAjAH|CFhAE~@Gl@KlBo@j@YlCkB`AoAfAaBvAyA|@q@fCoA|Ai@pBWlHe@xMCvAOrAYhA_@xB_AxDiBbBe@bCa@hBGxABrBXdFhAzBTrADfTm@tDa@rEy@hGaAfO_BpASlD_ApAi@nAm@hAo@dAs@hAy@hKsI`Ay@~BiCrN}QbAcB|@oBv@_Ch@cCXcBj@oERmA`@qBf@gBjO_`@nAsC|AmCdByBxBsBhAy@pBkAtLgFhAk@`BcArAcA|BuBfBuBz@mA|LsR`BcChB_CdBsBnByBnKkK~u@uv@zBwBzF}EtCuBtCoBvxBaxA|BsAjAc@vCs@hAQpAIpACjADjCXlCp@x@Zv@`@zBxAtBnBnExElP|Pl]x^hb@jc@`MpMj@l@tAvAjAfAvAdAvA~@|At@rAh@xAb@zA\\zAVv@H~DHrDMrAOxAYrA_@pAc@hAa@fAk@lAu@bAw@fA_AdAgAja@ag@fSwV|@oAx@qAr@sAn@{Ah@}AfAaEXcBVeBPkBx@qNnDwm@fAmQp@uJPmChCy_@`BsVxAoVLmBPeBVmBZcB^cBb@gBj@gBj@yAr@}At@wAv@uAnTe[hBqC~AkC`BwCr_AojBdBcDx@wAzC_FjDcFnDqEzAeBtDaEjAkAbBeBzAuAvD}C|DsCxE{ClBgAfB_AfTcKdBy@`Bs@|Am@jEmA|Bc@nAS|AO`CQfDKjYOfBC~RMxCDl@@xGVvFb@`gBrQbCRbCL~FNrF@dCE~~@}CrAKxAQrAUvA]dA[rE{AjPsF`Bk@rYuJjAc@xF}AnSwEjDgApp@}YrCuAdAq@hCoBpi@qd@`DcC~A{@bBu@dG{BfB_AbBeA|AmApAqAnAuAxAkBfAeB~@gB|@wBf@yAp@{B\\{Ax@kEhBqKb@qBl@yBd@yAb@iAfAcCp@kAjBiCbAkAtAyAxAqApBsA`K{Et@a@rB_AnAy@nByA|B{B`BmBpBaDzBcEtBuDtAyBvBmCtCiC`DwBzCwAlC{@nCk@pCY`EIfID`FE~BS`Ca@lCw@rq@aU|CiAbBw@lBkAvAkA`B_BtBeCpAkBv@uAz@iB`Qg`@p@qBb@{A\\cBdAmGPeBJeBLoBL{E?eFDyBN}DH{@V{Ab@eBvBiGfAcCtAsBjDeElBuB|DuDnEuDjAiArC_DhA}AzC{GhGaJdC{CpB_BdBqA~@o@`Ai@vNgHvJoEzKgFvQcIrCkA|Bm@hB_@nAOzAOxAGpWSzGMxCWxDi@nGsA`C]bCM~D?xAHjAJtOhBhDRjABjSi@~Mc@`CMxC]fB_@nCu@nCoAdBcA`BiAhC{B~BuCbGiJlJ_OlAcBjA{AtAuAbCqBtCyBrBgBfBqAnBeBhBsB|AcCxAeC~@wBp@iBl@iBzI{\\t@wBx@qB~@iB`BiCxAmBzAeBfBsAnAu@xCeBvAq@nKmEhBm@`EuBtAaA~A{AnAuAhB}B`G}JtCkEpPyWzCcEtM}Oz@iAx@qAv@qAt@wAfK{TxJkUdCuF|KuUnO}\\hAsBjAoBlAaBjAsArAqA|R_QxRcQtAiAbBgA~A}@`EwAzA]zAW~`@}EvBe@hBi@jBs@fB}@rCaB|iBwnApCcBxAq@zAm@vAc@tA[vAWtAQnESrDOnAKnAQtAWxA_@zAe@zAk@rAo@dAk@dAs@pM{IvAcAr@e@ds@}e@zEaD|A}@~Aw@`Bs@hBo@hBk@lBc@lB_@nBYnBQrBMrBEtB?vBDrBJrBRpt@`KlAJnAFnAB~CElAIlAOzCi@lA[xFeBhAYnAUlAQlAKlAGnAAjA@xCLxBVzN`BlAHnAF~C@nAE|CSlAOxCk@jA[jA_@vCkAxBkA|B{AhI_GlJwGlC{BbAgAbB_Cp@eAn@kAvA{CjMuZdOa^zAaDbBuCnBwC`AoArOsR|MqPtHmJxAeB\\a@vAqAvAiA~BwAzAs@nAi@jHyCvAm@~FgCpHaDxCoAzPmHhRcIpDwA|FkBhLaDtMkE~PaGxQ_G|QkG`DeA`Du@dLgBlPeCrAOfAQhPgC|J{AnCi@lCq@xGqBfCw@vKeDbNcElE_BdEqBdf@}W^StI}E|HgEnFuDvOaL`@W|A}@tBaArBs@lG{AvBg@|HcBzCu@nCgAhCsAjBqAhByAzCcDlT{VdBcCfAsBz@mBr@qBdC{InDmMbOsh@z@_CjAcCxAcCxAoB`BeBlC}B|ByBtBgCnAoBfAwBx@kBn@iBf@gBb@aBp@yDPoAXeDfAwOXqCPsATsAp@yC\\oA`@iApL}ZjByEZu@bAsB`EqHxBoDhA_BvD{EvAsAvAeAl@_@|Aq@`Bq@rE}AjOuFbFoB|Ay@|B_BvAsAtAyAdAuAlAgBtBmEhU}f@hAwB`CqDlDgEbBgBlBeBpB_BpEyCjD}BbEoCtOaKbIyFlVcUfCcCrHeH|@w@xEoEjGgGhB_BfVkVzEaDhGcGjA_Aj@_@|@c@dFwBbB}@dAq@z@o@xAwAz@eAhAaBr@oAjG{LtEkJp@eBnHwNdAaBj@w@bAoA~@cA`CsBxCmBlRoJ|AaAvAiAz@w@zBaCbCoC`AgAlFyFnFsF|AoAlA}@nAw@~@m@`F_DxB}Al@i@dAaAdEkEf@i@zFgG~BeC~AeB~@w@hBmAtEoCrAu@tGmDhAq@fB}@nAu@vAeAxAmAzDqDzRcTbAiA|EgFvJmKhOgP~@cAhI{IhGyGtOuPjAiA\\_@~HwI~@cAbTiUxA_BdFoFzGsH|GoHp@w@~BcCbBaC\\i@v@cBlA{D\\{AVuAhAyLt@gKRiCbDq_@P}AXeBXcBf@qBp@yBbCyG~EgMbCwGn@mBj@uBr@}DXqCH}A@eA?gB[eRE{BKyHKwIA_ABmAD}@NcBR}ARgAd@iBVw@^iAt@{AhAqBzFmHnCwDd@u@`@{@p@eBj@kBXqATqA\\_EFqAl@}ZPeFLgFLqBToBPeAl@eCZaAl@{At@wAh@}@~AoBtAmAbGaFb@]dByAdB_BfAoAhJmL\\k@jM{OtBgC|EoG|AeBh@i@lAsAnBkBhB_BjEwCvJ_G`EeCzLmHlOuIJG|ByAzB{BzAoBjImNnCuFxAoD`BoD|AuCbAkB|CaFnE{F~AwBdHoJnGqJ`DaFlCeEZi@hB{D|CcHvAwCn@iAdCsDf@k@fDuC`FcDvC}BpBqB`BoB|AwBv@wAxCkFfG}KxAwBf@k@VQd@c@\\WfCaBdBm@rA]fE{@bAS|Bc@rA_@hBu@v@e@rB{Ah@i@xAkBd@u@nFeInCkEpBuC~@uAhNcTjBwClAmBxAoB~C}CnBuApBkAhBcAlUcLrBoAxBaBpBqB~@eArA_Bj@}@vAgC~@oBn@}Ap@kB|@gDrBkIl@kBp@aBdAqBd@u@r@_AzA_BbA}@nBsArAo@~@]fBi@nCg@tDu@vJgBlHeAxJkAlCc@jA[nGkBbFsAlu@oNjH}Ab[aGfDu@bDeAfBq@zRkIbA_@bNaGfDwAfAi@nAy@bA{@`AeAz@iAlDmFdF}ItAgCnCyFfHsQnE{KhAiC^w@b@y@x@uA`BcC|CcFT]bAeBbJuMxA_BjAgAfCmBTWnI_Fj@c@hA{@`C{B`M}L|@{@hI{HtJcJjHmHjBsBrBkCfAcBnCyE|@{@|DyGxCaFxQkXx@gAz@}@b@[j@Y\\KzCg@RG`BaAzAq@l@QZE^?\\JTNrCbEpDvErDvExAnB~A|A~BzBl@r@t@t@hBjBzDxDr@j@dAr@nC|@vAl@rAh@zDvAnAj@|A|@pAdA`A`A`AvAt@zAnGdPdE`Kr@rB\\~AXdBr@tFJ~ALr@Pp@Rn@j@hAvChFb@f@RNVLl@Lp@FtAFp@Cn@Mj@[TQnCiCVOVU`@a@POb@e@f@o@b@{@t@cBd@w@|B_DX_AxAyBp@e@f@i@j@}@l@cAXi@\\q@`@w@dB_DXT`A|@vCjC|CvC`BzA`CxBp@gAPYx@sA",
      "way_points": [
        0,
        2444
      ]
    }
  ],
  "metadata": {
    "attribution": "openrouteservice.org | OpenStreetMap contributors",
    "service": "routing",
    "timestamp": 1738083197982,
    "query": {
      "coordinates": [
        [
          -122.4194,
          37.7749
        ],
        [
          -118.2437,
          34.0522
        ]
      ],
      "profile": "driving-car",
      "profileName": "driving-car",
      "format": "json"
    },
    "engine": {
      "version": "9.0.0",
      "build_date": "2024-12-02T11:09:21Z",
      "graph_date": "2025-01-21T09:49:30Z"
    }
  }
}

directions_response2 = {
  "bbox": [
    -122.332209,
    41.875632,
    -87.629742,
    47.714312
  ],
  "routes": [
    {
      "summary": {
        "distance": 3321152.8,
        "duration": 116145.8
      },
      "segments": [
        {
          "distance": 3321152.8,
          "duration": 116145.8,
          "steps": [
            {
              "distance": 133.7,
              "duration": 10.7,
              "type": 11,
              "instruction": "Head south on South Federal Street",
              "name": "South Federal Street",
              "way_points": [
                0,
                3
              ]
            },
            {
              "distance": 279.8,
              "duration": 25.7,
              "type": 1,
              "instruction": "Turn right onto West Van Buren Street",
              "name": "West Van Buren Street",
              "way_points": [
                3,
                10
              ]
            },
            {
              "distance": 132.5,
              "duration": 17.2,
              "type": 0,
              "instruction": "Turn left onto South Financial Place",
              "name": "South Financial Place",
              "way_points": [
                10,
                16
              ]
            },
            {
              "distance": 49.9,
              "duration": 9,
              "type": 1,
              "instruction": "Turn right onto West Ida B. Wells Drive",
              "name": "West Ida B. Wells Drive",
              "way_points": [
                16,
                17
              ]
            },
            {
              "distance": 735.8,
              "duration": 26.5,
              "type": 6,
              "instruction": "Continue straight onto Eisenhower Expressway, I 290, IL 110",
              "name": "Eisenhower Expressway, I 290, IL 110",
              "way_points": [
                17,
                28
              ]
            },
            {
              "distance": 7642.3,
              "duration": 661.9,
              "type": 13,
              "instruction": "Keep right",
              "name": "-",
              "way_points": [
                28,
                123
              ]
            },
            {
              "distance": 466.5,
              "duration": 30.5,
              "type": 12,
              "instruction": "Keep left",
              "name": "-",
              "way_points": [
                123,
                127
              ]
            },
            {
              "distance": 4289.8,
              "duration": 328.5,
              "type": 6,
              "instruction": "Continue straight onto Kennedy Express Reversable Lane, I 90, I 94",
              "name": "Kennedy Express Reversable Lane, I 90, I 94",
              "way_points": [
                127,
                170
              ]
            },
            {
              "distance": 896.9,
              "duration": 69.7,
              "type": 13,
              "instruction": "Keep right onto I 90",
              "name": "I 90",
              "way_points": [
                170,
                181
              ]
            },
            {
              "distance": 12254.8,
              "duration": 620.1,
              "type": 12,
              "instruction": "Keep left onto Kennedy Expressway, I 90",
              "name": "Kennedy Expressway, I 90",
              "way_points": [
                181,
                276
              ]
            },
            {
              "distance": 250499.4,
              "duration": 9026.2,
              "type": 6,
              "instruction": "Continue straight onto Jane Addams Memorial Tollway, I 90",
              "name": "Jane Addams Memorial Tollway, I 90",
              "way_points": [
                276,
                1198
              ]
            },
            {
              "distance": 101992.1,
              "duration": 3671.7,
              "type": 12,
              "instruction": "Keep left onto I 90, I 94",
              "name": "I 90, I 94",
              "way_points": [
                1198,
                1557
              ]
            },
            {
              "distance": 250884.4,
              "duration": 9047.3,
              "type": 13,
              "instruction": "Keep right onto I 94",
              "name": "I 94",
              "way_points": [
                1557,
                2600
              ]
            },
            {
              "distance": 473.9,
              "duration": 31,
              "type": 13,
              "instruction": "Keep right",
              "name": "-",
              "way_points": [
                2600,
                2604
              ]
            },
            {
              "distance": 19146.4,
              "duration": 825.2,
              "type": 13,
              "instruction": "Keep right",
              "name": "-",
              "way_points": [
                2604,
                2717
              ]
            },
            {
              "distance": 6013,
              "duration": 254.7,
              "type": 13,
              "instruction": "Keep right onto I 694",
              "name": "I 694",
              "way_points": [
                2717,
                2755
              ]
            },
            {
              "distance": 50913.8,
              "duration": 1987.6,
              "type": 12,
              "instruction": "Keep left",
              "name": "-",
              "way_points": [
                2755,
                3049
              ]
            },
            {
              "distance": 1667968.4,
              "duration": 56186,
              "type": 13,
              "instruction": "Keep right onto MnRoad Mainline, I 94",
              "name": "MnRoad Mainline, I 94",
              "way_points": [
                3049,
                9388
              ]
            },
            {
              "distance": 502286.7,
              "duration": 16867,
              "type": 12,
              "instruction": "Keep left onto I 90",
              "name": "I 90",
              "way_points": [
                9388,
                12922
              ]
            },
            {
              "distance": 91057.8,
              "duration": 3289,
              "type": 12,
              "instruction": "Keep left onto I 90, US 395",
              "name": "I 90, US 395",
              "way_points": [
                12922,
                13169
              ]
            },
            {
              "distance": 350788.8,
              "duration": 12953.2,
              "type": 12,
              "instruction": "Keep left onto I 90",
              "name": "I 90",
              "way_points": [
                13169,
                15083
              ]
            },
            {
              "distance": 1175.7,
              "duration": 74.4,
              "type": 13,
              "instruction": "Keep right",
              "name": "-",
              "way_points": [
                15083,
                15110
              ]
            },
            {
              "distance": 268,
              "duration": 32.2,
              "type": 12,
              "instruction": "Keep left",
              "name": "-",
              "way_points": [
                15110,
                15113
              ]
            },
            {
              "distance": 560.5,
              "duration": 60.2,
              "type": 13,
              "instruction": "Keep right",
              "name": "-",
              "way_points": [
                15113,
                15121
              ]
            },
            {
              "distance": 232.4,
              "duration": 33.4,
              "type": 0,
              "instruction": "Turn left onto Madison Street",
              "name": "Madison Street",
              "way_points": [
                15121,
                15128
              ]
            },
            {
              "distance": 9.4,
              "duration": 6.8,
              "type": 0,
              "instruction": "Turn left",
              "name": "-",
              "way_points": [
                15128,
                15129
              ]
            },
            {
              "distance": 0,
              "duration": 0,
              "type": 10,
              "instruction": "Arrive at your destination, on the right",
              "name": "-",
              "way_points": [
                15129,
                15129
              ]
            }
          ]
        }
      ],
      "bbox": [
        -122.332209,
        41.875632,
        -87.629742,
        47.714312
      ],
      "geometry": "cir~F`ezuOtBARAdBA@|@?j@?|A@lB@~A@~D?lAtAAP?B?x@An@AVA?vBEhG?zC?|@?p@@bD?^BlC@vF@`L@v@@vDMnFGlASjASl@_@l@c@f@s@`@[Js@Le@\\iBJi@@_DKoDCaGIeD?qHFiCBuC?iAD{@Js@LgARaBd@aBl@}Ar@iAp@eAp@EDeAv@s@n@gAfAeBxB_CtDeAhBoA`CkCdEsBxC}CvE}@zAgAdByDdHeBrCgBbCs@z@mAjAkAbAgBjA_CjA}LlE}Bx@gAZ_Cb@qCV_CBeCIaCQwBIgBH}@LqBd@gAd@sAx@y@l@wAzAaGzGwAtA}AfAw@f@cB|@mInEm@\\{M~GiBlAuBdBkAbAmApAoBfCaBbC}BhEqD|HgFrKoAlCmAfCgBxDaApBi@fA}KxUaBhDwNtZMXgA`CWh@wBrEgBrDWlAiEdKsEdK_@fAWh@wAtCgD|GeAtBYj@S`@cHpNwDpHaApBgDjHwFdMmAhCeBrDuE`Kw@lCUnAi@jDe@tCq@hEa@|Am@hBe@fAo@hAs@`A{@`A{@t@o@f@y@d@mPvHcBnAk@l@_AnA_@n@w@fBqBdGoA~CaPb]_ArBaGbMiBxDcChFaArBqD~Ho@~@mDhGkBzDs@p@uAzCcAxBWh@iDnHuAjC_BjCeCjDqChEaBjCo@nAi@rA_@fA_@pAc@hBkBbJ}@nDu@vBi@hAcAjBoCvE}AjCoBnD}A~CiNzYuChG}@xBY~@]jAm@~Bm@~C]`Co@vD[|A_AjDa@nAqAzCmFfLaT`d@a@|@cBpD}Tte@_AtB_@bAq@|B[xAUzAStBEz@ErBAfAHjg@BfI?lIFh`@Pv_A?bBGpDO`DKjAe@|D}B|Nc@`EO~Aq@zJyArTYpGQjGIpDG|H?~CBnIBdFz@bf@V`Ml@n]HzFA`FGfDM`EM|CSpCUjCYfC[zBi@|Cu@lDm@hC_CpJqCrIa@fA_IxQmQ~`@sAtCu@vAk@bAiAbBy@dAuFxFy@t@qCtCeCdCwB|BkBdC}@xA_AdBk@pAe@jAqJbXeB`Fs@pBa@~@s@lBu@vB}GnRqC|HsFnOmJxWaCnIy@fDy@dEmEfW}@dFyElXShAaFvYWrA_BhJ{@nF}ApISnAwAjIMz@aIjd@cArGmE`WQ~@g@dD}AfLk@xE{@|HkGhh@yFfd@y@lGe@dC}@hDa@nAeApC_AlBw@vAiBlCiNpSuApBuOlUuF~IiMvQ_EfGuHbLeBjCaCfEwEzIuBjEaDhHgH|QmE~M{@`CuXxu@y\\z_AaGlPoBrFuBhGq@jBsAtD_BrDmEhNqDlN{ArHsArHcBtL[hCkA~Ks@~Ia@bHQtDc@pHw@xK{AzUm@xJwLhnBeFbz@qCbd@}P~qC}Cfg@c@xNA`B?bkD?fID~fCAb^?h|CCrU?`IBbODtm@BdW@~B@~GGzr@Bbi@AjIAbaEA|D?|\\Jdy@E|]DrdACrEGrEWtHc@~FeArIUnBQtA{Dh\\iAjKs@tGeC~ReL~`AIx@qA|G_A`Ei@rBu@vCyClIqMn`@iGnQqDhKkIxW_Rpi@eKd[aVds@cj@faB}ArEuGbRcGxQ{EnNqEvQ}EfTu]j{AuDpOcFnOoGdPiUjm@IReBnEuEvL]lAcEnK}L~[uZbw@iKzXiBpFyAxFcB`IkUlxAgkA|qHa@|B}A|JaA~GyBhNmIpc@a^ngBaBvHuKpj@}Qp~@wDxR}Lpm@_Ix`@gClL}CvMeG~UmBbIwBjJaC|J{CvLaH|W}F|VuEtPiGnVmExQyDbOoApF}BtIkCpKiGnV}@rDaDnMwAhFsLxd@aT~{@cI~[c@fBsUr_A}_@z_BiCnKyAnF{S`~@_CrKmj@nrCgX~sAyLnn@kYhxAkNts@_DpN_ApDoBbH}o@xxBUv@eVxx@u@hDi@lCm@fE]fDWpDMvDKzODpa@Efo@Cp]Flq@TfqADp[@x@D`[Pbv@PzcARvvA`@b|BHha@?xLe@dLy@fLk@pEy@|EU~@}AvGqB|GyAtDeBbEiBrD_CdE{Xxe@cDlFyGxLiBzD_CzFuAhE_@nAeA~D}@`Ew@fEq@xE[xCe@|EQfCKxBM~DG`EA~FLh]DfKLte@HhMA~B@lEElCMlDSxBk@vDq@~C}@tCsAhDaB|C{BfDoBzBkB~AgCfByCzAuBr@uBj@{B\\uBP}BFmWBmk@H_[?}B?oGI}IFwZAkbAAcwAQy|@S}XIad@QgpBc@}y@Icp@QcMLoLp@sF^{NdC_N~DkC|@kYhJy\\tKeq@xTkM~DcIvC}u@b^i^nQ_H`D{EfBqBd@yDt@gCPuCB{AB{k@JgA@eZReGHiE?cEd@uDf@oZ|HoXlHcd@dLiCp@aIbBaFnAsHrBqIdCoG`BmIlB{BXq@HeG\\_n@BqzACsB?uo@D_OQiHWwHm@yNgCaVgFcGuA}H_B{D}@eDoAmCyAyB{AwAqAgAmA}m@qq@}@gA{GkHaBmBgDeDeA}@}D}CqDoBcBw@gBu@sBk@{A_@mAW{B_@eCWgBKwAC}BC_n@]{fA_@uHCsD@yS`@qb@QeJCgCFiEXuALuBZ}EdAwA^_Bh@ol@rTE@wAh@gIzCqD`AcATwCf@cBTuDXsDNalAt@{@@iRHgUPoyA`A}YPkIHa`@Zoc@\\iCD}`@^oRRex@\\mUL{nAbAqb@FyNN}C@O?{OA_IFc^L{J@}@?qVN{GHcAAwH@cA?g^Jmg@X{A?oRF{@?{r@N}QFqURqE\\cCZ_BZcCt@uC`AiBz@oDpBeE~CyBjBwAtAsA`BuBvCuA`Cq@bAqIhNoArB{ChFuFvI_GzIw@nAwCtE}@tAw@bAoAxAsCvCmGxFkDdC{@f@iGzCiCbAkA\\gBd@eBZeJhAqHR{UyAuPk@sg@I}_@AaAAwEAsnADeGG{REuWa@{RKeC@aAAwMEs@AkJMyRCaNO_H?yEh@uF|AmBt@mClAeDtBeCpBkCjCuCrDgKvO}HvLcAvAyLtRsLhQqCxCaEzCcDrBeE`BaFtA{a@vG{`@fIiKbCcIbBuKxCwg@`L_i@rLaLbD_GxB{FdCsE|B{HrEqAx@aDvBsFtE{JfJiWjZ}GnIwCjDuL|MyG~HsTnXmZz\\i[dYoPxN{KfJmL~Ja@\\gKxIsKhIgEpC}R|MoNhJuc@d[oEpCwBfAkBx@cDjAuDdA}Cn@wDp@oCZoDPqBDqGIab@YiGI}ACiGEoLM}C?oGRuFd@wC^}Ez@kBb@gF`BuEdByF`CkU|KkPnHwQdJaElByJtEsDzAuBt@yHhC}DhAoG|A{AXoAVmKjBiBTsEj@qPlAkCZkCf@gAZoA`@gBz@gBbAoBzAkAdAsAzAc@h@gR~WsAjBeFzGkcAxvAiAxA_bA`uAcDfFgCpEg@bAgA|BaDjIkC`JmAtE_@bB}@nEc@dC_CpPyL~|@yFpa@{BxPe@rESnCWbGGlEAfDFvEJnChA|ULzBhC~h@RbFDrCB~CA~CIdGMxDOnCa@dF]hDw@~F_@xBe@bCiB~HoOzn@aCpJeY~jAmDhPeOts@aApD}@lCiAzCqApCQXw@bBuHtOaAxB[p@oZdn@qE`JiHjO{BlE}B~DcBnCoCxDmHlJiC~CaAlAcLdOgBdCkDlFoFlJy[dk@iO|WyFbJkA`BcApAcBvA_BfAmBfAaFjB_ATmAPeAJ}BDaBEuDE}AEuHY{CQeBIwHM_BCyJJeEBgJSkWg@qDAmCB{DR}BVoC^gGhAaB^cpCtl@iCd@aCZmCN{BFaCAmDQqAKwAQwAYyEgA{GkBmI{B{D}@_FuA{A]aCo@_CWqDSm@CiD@uBHaD^_B\\uCh@oDtAgDjBiGvDmAt@gBz@c@RgE~AaEpAkQzEsTvF}DdAy@RyHpBkJ~BqAZeD|@cCn@wd@xLwDrAgEtBqMzHsBrAmVjNkCvA{RlLwSxLwCvAyDbBwDxAeErA{`@bMeHlCoDbBeAj@oGvD{RxLsKlGgh@f[sD|BqA`AwBnB_B`BqA~A}AxBmL|PcCjDsM|R}p@`bAaB`CiJjNoAjBu@hAwBvC_@b@sCpCgBbBeLlKcT|Reb@b`@wDhD_BrAyEdDkF~C_F~B}B|@gCz@{k@xQ{IrCgCz@gNfE}y@tWkXbIuH|CyL`G}K`G}DnBqIxDiCvAwe@nUuBx@kDpBoFxCgAr@oCtB{BnBwHbGkc@b`@y~@~w@_[fX{CxCaIrIylAvqA_^x_@}fCpoCkDpDcA~@mDvCsBzAaEhCkDfBaDvAkDnA_TdG_\\fJuBh@{FdBkOjEmr@|R_Ch@yEv@uBVaCRaGXyiCfDoBFeETyFf@mCZsGbAaCf@wFtAoEpAgCz@kCbAuD|AgD|AuDnBcK|FqBbAyAl@iBl@_Cl@{Cf@kBP}@DyBB{RK_@@su@YyA@u@?sELgCNkCV}Fv@sFdAkCr@yC|@cCz@{ClAeChAkCrA}FlDsCpB}BfBiHlGk@n@wDxCgCtB{GdFcH`FiG`EqIbF}IxEcFdCgZdOaEtBqK~FcEbCcHhEaGzDkFlD_IzFeL~Ic[xUgDbCoCbBoCpAgBr@qAd@eBf@gCh@gEj@}CP{AB{CAeDQmAM}B[amAcTmI_BwGeAcDk@wUiEcDe@mC]aEOmCEsB@aDLcFb@eDh@eCj@kDbAgItCmTpHsHdCmCfAwBlAwB`B}AvA}@bA}@jAeBhCwApC}@xBw@`C{FfRiDtKoUru@cAtCkAnCuAdCw@nA{AnBoBpB}BfBsG`EiEpCyA|@iWxOqIjFyAbAwBbByArAcCbC{BpCwB|CoBdDgBnD}ArDwA|DcAfDqAfF}@rEmk@`jDwGp`@}[xnBkUjwAyOpaAkUhwA_FxZc@hDk@xEg@fEy@`Jg@rHSzEI`B_Bt^}@jTWrFaAnVW`I[bOInHGtHEvn@GfKGpESdJc@~M_@bI[pFo@dJgAjMe@rEyA|LmBbNwp@flE}SpuAgXrgBy@nFk@rEq@tGe@nG]nGeG`uAg@dMoCrl@OdDyAp[a@hK]nHaBr_@YfFQjBi@lE[lB_AhEc@xAu@|BWx@_@z@k@pAq@vAoAxBm@|@w@fAwBdCoBfBw@n@mCdBmCnAy@ZgHvByDhAyKfDeA`@gBr@cAf@yBpAgDhCkFbF}AbBoKpKkAhAgBfBcAfA{CvCgBrAeCvAoAj@yBp@iAVkARqANiBJ}B@oBI{@KqAQkA[w@Ua^eKuj@qPqPyEyi@cPsEkAyA]{Ek@uAImFIgCFiDV}Cb@sAXoDbAw@Vy@VqDlAeJlDuy@|YqY`KoBj@yDx@sBXwD^gCLeDDwCAaFa@}AQcJk@oMgAyAI}IcAiBOoKm@_C@}@?kAJoDj@aATaDhA{@\\qBbAmBnAu@h@s@n@eB`B_BlByAtBsSv]eHjLqHzKib@dm@kShYoIpKsBdCoc@~h@}CzDwC`EuChEmCnEiCvEeCzEo^fu@os@vxAql@jmA_MbWmA|ByBzEqItPuLjUwKzS}`@pv@{A~C}BzEmdA|zB_d@~`Akh@~hAoYnn@cC|FyAvD{D`Ly@pC}CbLse@ltB}BpJsBbIq`@pyAoDdO{@vD}CdOcApFug@tpCcB|HkB|G_B`FqBlFkBjEq@tAkA|BaAbB_CvDkAdBgChDcEvEcB`BwB`B}AxAyQhPcSnQyAnA_TlRsFjFqL|LaA`AcOdPoDvDkhAzkAgCjCeC`CsBhBmCzBmCrBkFpD_sBjnAwBtA}DrCmFdEaDrCqDlDkdC~eCwC|CoBzB_CpCmCnD{B~C}A~B_EtGkBhDmChFeClFuh@dpAcBlEaNh\\gGtN{@|BwCnHk@lAsSjg@wJxU}@tBa@jAcD|HiAbDuAjEiBrGeAnE]hBo@~CuPv_Aol@rfDuBvMmp@hsEcAjG{@dEm@pCkCbK}C~IcAjCqEdKwOzX}ArCiFfKi@zAwDxKm@rB}CjLUdAoBjK{@~EwBjLwBfJeD~K{@~BuBrF_i@nlAaC`GsCxHoDbLkf@|dBeLv`@i@pB{GhUqExPcN`n@mQbcAmGr^eW`yA{Nfy@_CzLoExTcEhRu@hC[jAqLpe@_Szt@s~@tlD{DtNaDxKo@nBiWns@{E|LuFbOqAvDgBjGcGfXcTtaAuCjNmEbSsAjG}@fDaBtFkDtJoG`NwBbDq@hAiDhFkCjDcNjPw\\j`@kUfXuB|BwFzGsKvLuHxKq@fA_AdBiCrFyBrFyAzE}@fDgCnLgArFyArGw@lCoCzGsBvD_BzBsCvD_AbAqBlByB`BaAn@kBdAmCfAiEtAkAVwBVoCN_D@oBEeNk@}U{@kBAcBFsCTcEv@uL|CeE|@_NfBya@zEsAPaMzA_\\|FmCv@eAZ{YjHcEtAyRdFyKxCwBj@kz@zT_]xPuDfBwXjNwGxCqA\\sFhAiFh@{X\\}|@jBgy@hCcHFwPGoKWeAAQAy\\i@wI`@{DXqClA}DrBeGvE}KzMuMhOsLlN_QrQs@l@{E|DaGdE}AfAkShNmC`CcDlDyBrCcBjDmBlEeA|CsArF_AlEkBfMwDvUkBlHcGnRoCzEwGvKkE`H{MfRiCtE_BxCgCfG{DnL_Lj`@iCxJaJj\\aFhR_EvK{FfNyj@bjAuEzKcKvZ{O`g@cWzw@cJjYc@rAyLx_@}BdHyBzFoCjGmCfFgB~CqAtB}[xe@mIdMeDtFcDbGkEfJ}DpJwbBfoEeCdGwCrG{CbGeDzFoB`D}CtEkE~F{DvE{EdFmCjCw@p@sNdNwAxAuA`BsA`BwB|CqBbDgApBeAvBcCtF{@|BsA~DmAnEm@dCyDbRgHd]_C|LuNxq@eBvHkBjHu@hC_BhFyBnGwEnKmBrEmMtX_]zr@eUpd@sDxHuZpn@sGlNwGpQoHbVo\\neAu@|B}D~LqDbJ_AnB}D|GmFnHkKxJeOjL}^b[kUpY_Ur\\iFtGcNnRkA|AuSjYyEpGgB|BkBjCaBlCeBjDuAxC_AzB}@`Cw@bCs@`CiApE{@bEy@vE}@bHcB|NqBrPqBrNuLpu@WzAkAnH{@rEiB~I{ArGkCvJuLrb@s@dC}@nCg@rAk@zAaA~BeBrDkBhDkAlBoAjBgGjIkf@zr@iDbGiIzPqC`HuExMuc@xiA}GpOeFvMiF`MiDnKcE~Oc@nBeSjz@i_@|{AwEfQmDfJ}I~PeJ~RwH~OwOd[oDnHsHvMwLbQsQ~VaWh`@iSpY{EfGkFlIsCbFgCbG}DbKoCbIqG~OyAnDgG~OoA|CqHvRi@tAaBdEc@`A{ApC_BdCg@n@i@p@uAzA}AtA}AlAaBbAcBz@yPzGoAl@kHtFwE`F}ClEqElIyCrHcDfIgNv\\iJjVuOf_@iLjc@qCtJ}B`GwCbHqFfJySpYaDzDyTzXkTx\\iGpIoJtJwc@~Z{HpGyDhEoAlAoPzTqIjJsGrE_IjD}MhFuNfJsBhB{DvD{DzEgE`HkH`MiDhF[h@qDfEuFvFaGjFkLfIsAbAoAz@{J~GgEdCiBfAkGvBqGx@oL^aEn@kC`AoIbFyB|BoC|D{BtEgBtEiBtF_DbKcInViD~IcCjE{KxL{BpAoPlH{I`E{[lOoEvA}DbBeDlAaIfCsCbAgHjE{BjAaGbFwEdF}UlZ_EdEqCbCgDpAqCbAqDhA}F|A{GzCsEzCeJ|IoEdFgJtJiLnLaGrFoD~C}KbIiJbGmKlHue@f[s@d@wGnCeHrD}^tPqCvAcLnGqAhAiCxBeCnCiC|CuGfJoRnXyIvLyBfDmMvQ_MzPgG`JeDbFaF~IkD`H}CdHqSxi@mBpEiB`EgBjDcC`E}BhD{EbGcEpEkAhAqBdB{C`C}HnFid@lZo`@tW{@j@kAt@wA`AmUnOmPfLyCxBiD|CoGnHqMnQiEvDuDxBmDjBsEpCeHnG_GfHcEpGmFbKwBhGaJlXeHlQ{_@x}@{BzGcC|KgAlGoBbOmPbtAmBzJiDjNuEnNgy@f|BeDzGqFjJwGfIiGrE{BfBuKrFgAd@aTjJYJ{@\\_JbEoPhHwFxBmItD}CnAwCfAoi@nQaOdFeNpEqMxF}IvFil@fc@gAv@ao@te@uVxQsQdKiHvDmHnDqJxDmPbG}@\\{r@fWaTtHsJnEcCnA_GfDaHzEqCtBcCpBmG|FgJ`KaDfEgGtIi@|@cFrIoFbK}FlKw@hAaAtA{F~HkSrSieA|dAoNfNoInJcGxIuNrXcHhNip@dbAuA`CcDbGyBxFyAnEiA~Dg@rBuBnKy@nFm@lFiAhOQvDG~GD~GRrElCnf@TzDnC`h@l@vU@nRc@neAg@xbAMjMMf^EtFA~WHdM^|THxCpAnj@@dBC|DQ~F_@lF_@fDoIjn@[~BkDnW[rB_@lBgAxEuAlFqBxGo@dBeDlHqClHeC`Hi@hBcAzDiEhPk@tBqDvMiG`TaKj]GRu@bC}ExPqFhRgBpFmAxCQ^_A`ByAtB{AfBqC~BsFbD}BtAmf@fYeAp@_`B~_Awc@vWgAn@mLdHqHnFeH|Fak@~f@uJdIqCfCiCpC_DtDqFrIqA`CoAjCoAtC_AbCoE~Lk\\z~@yIpWgClIqDjM}B`JkD~NuEjTqD|SmAxHsAfJiBtNc\\jnC}@xGwAdJs@xDqCxMe@xBaNlm@a@lB{t@niDyDhN_DdKsEbMo|A|dEcMd]sAtDeBrESj@{Mh^}[v|@IVwG`QcMj]sGzPkBlFsAfD_EpO[pAq@pEa@|BgA`Kc@tGs@fQG~AkBxf@gFzxACd@i@zMUdI[jHsC|x@oDfaAKtGC|Xp@tlCDb[ZnrATnz@AfLQdHUdH[tG_B|Pu@dFwDrYoBfOk@fGc@xGWjFE|AErCApD@zJDbKBpIh@`b@l@xx@`AxkA@hDh@|p@?`FKjG?NGhBOfDa@`GkBnTWrDIlCG~B?~BD`CVhHHfB|@dUHzCBtBAtCEhCWpGg@bGw@lF}FzZc@zBsJbh@yBxKyGf_@q@xFcA`RU~Ls@fZEzBQhIc@xGQtBa@|Ci@hDq@lD_XdqAw@vEo@hEs@tGQbCe@rII`DEfCCfC?tDDlCJzEtAh]~Ax^dArTL`Cp@|QvAnZ^xQHrVi@tv@MjHk@fGu@xGqAdHg@`GWdDKrF?xCZdGpAdKhArFxApF~BpJfAdF^nCVzBRbCLbFBjDC~FO~v@GdCC~BMfC_A~JaMn}@_AzKKxB_@hJgB`f@MtCS~Gk@hO]fEYxBu@bEm@bCu@hCm`@`cAwE~LwBxGaBxFmBnJiBpNmAxOOzByBhZqEbp@_@`IQrJItWKts@?zA?jo@ChHCri@Bpj@Oze@C`c@Unr@_@zu@UhY@f\\A|AJ|u@EvM?tB@|NS|Gy@tQ{AvZ]~IMbN?bMd@`i@Jd[?`ME~DApAEhCg@n}@o@du@uA~tAQvHUlE{@xN_Cp[wCh[u@pL[zFKnI\\p]NvS?tCGdFOdFW~EeEji@_@lIIvCEdF@nHFxCPdFX`FjBrWd@fGfAhOPxCTjGBlBDfFCxEKjFSdF]~Ee@|ESlBs@zEcDdRcDxQk@pDMfAYrC]`FKvCGtD?`BDzEJtChBjb@VpHJdFF`F@~JA~EE|De@vPsJnvBm@lPIbLDbJ~@dg@fAjj@JrHEvK_@zKuEbr@kA|RSjKDvI^xN|Dtd@bBzSRrGD`FK~]c@hyB[b_A?fHKfCIjBUdDs@xHcA`GwBdIyZf}@c@pAkFvOiDzIwDfJmGdMw]vo@cArBkD~ImA|D}A~Gs@`ESpAo@bFe@hFOpCS`FQxLIrKIbPu@to@k@di@SdTK`ZFhQJjJBtA\\za@LzKEbHMhIwAjT_E|TsCzP}@zMOnIk@nqB?`BK~\\M~JWzF[|EcDx\\YbEQpEMdIErGR~q@LpHZpFjAtL|@hJXnDP~DB~A@bBEzn@@~n@?vD?z@AbF@f_@An`ABhHH`GBdFnAze@ZxPHfLLrQF~Gx@t`AJjOH`NBzN?fD?J?dCCfEAhBIfNAhF?bBHbHTzVThU?HHzIJ|JJrDVjFf@vF^~Ch@fDp@rDhApF~@|EdBvHdZ~vAvDrQBP~ErUtA`G`ExRfBnJ|@dFzArJf@`DTrAbAfJt@zF`AvJh@lHl@fJp@pJ^`JLlEL|CThNDvEBhEBpsAC~BCboA@he@Btj@Bhd@?lo@DvkA@zk@?nj@Bx^?hi@KxI[`TOxKD~S?|@x@lZNtKBbIIn_@C|MOtCIjFKpLC|JC`@ClDGrAK~@SlA[lAYv@u@zAcAzAcArAu@t@k@`@_Ab@s@T}ALyABkb@w@{MG{O?aFGqKA_DFyFVyEXwu@zDkDTsCPiHZki@xCoFL_E@uEMmBKmGu@kBWoB[oH_AcIiA{BYwG{@cCg@}B]_M_B{BUoCQ_DOyHI}FRqh@tCmf@rCcAFmZbB[@}BTeAPuAZoA`@mAd@mAl@yBrA}AnAo@l@wA|A]^gAzA}@vAeBlD}@~BeAdDo@jC_@jB[rBs@jGkAxZYdGk@zNM~Cs@`Rm@vMm@jKo@vIqAzN_Cba@k@pLsFnfAYrGUlHKpBK`N?bQBfCNp_@BtFA|NQx\\Qt[[z^CnFCxSSp^]n_@N`N`@xKd@dJFzFQvO@dCJ|CdAtTn@pPZrGpCtd@~A`TRvF?rBIvB_@dDk@xCeA|CcBrCk@x@aAbAiDnDuCdE{A~CgApDuA|Fs@jCqBdJc@`BmA`E}BhGiAdCyZbo@eBlDsElJcAjBcPlXwBhEqBvEgBbFo@tByApFi@`CeAtFwCpRyDdYiCnRM|@oIln@uJzt@y@lJaAzPYzDaAzGS|@g@|AsAjDoA|BiLfQaA~Au@|A}@vBe@tA]tAg@~Be@~C[fEK~BErDC|BcAv|@YjTCjI@lA@l@DbD?^dAz]VdKPtH\\jJXpEf@lFn@nFzB`PTrB^`E`@fGNzDHvDDdHJ`ZF~INx]CfIOxH_@`Ke@zHsJtvA_D`e@WxD]pFOpCS`F{@xXa@lMGfBQrFOrGEpDAxG?dC?|SCbFIhIYxMUpMm@xXCbCGtCShLGnESzME`DMvFi@`JIbCApCRpJPdFPvKHjHBtHEhCKhCUbFYnEi@vF[lCuAtI{DvSOt@qHt`@uFb[cClNe@fDSlBq@~IYlGMzEApCAxV?tF?vKKn`@U|f@c@jo@QhKOnDUjDoEfi@c@jGYxGe@v\\SfPEfDa@b]YhVSzHUjD]tDYbCg@dDc@~ByCrMS|@aF~ToIp_@Qt@oHr\\aAvEm@dDoArIyIfn@yB~NwB~P{@pJsCra@YdEy@xKwAlTm@pH[rCSrAYbBa@hBoBhHu@xByBnHa@hAw@nB]v@}AnCcGzIkKzMkEhFmU`ZqQpUsC~DyBvDsAzCsCvHaEtLk@tAcBnD}C`F_f@tt@q@dA_@j@aApA_BhBaAbAeA`AcAv@qBvAsCzAgOfH}RjJ}FjCuC`BiBhAwCvBuC~BiCvByRrOcOvLc\\tWg@^kC~AmCrAcE`Bc^|MqBbAcAl@mBrAiBzAmCnCiCdDgDhFaOvV{X~d@wCfFsIpNuYhf@m@|@qBzBkAbAeAt@{@f@{B~@mBf@}@NwBPuV^sBNiAPgBb@cA\\cBv@sBnAgA~@_B`BkFzGgh@rp@s`@lg@uJfMwBhDy@|A{@hB}@vB{@`CiLj^iF`PgZ`_A{CtIs@jBoArCuAvC{Upd@{AzCej@peAiBlDkB|DoErIeH~Mc@z@_Wjf@kI~O{A|C}AnDqAdDaAtCoAlE_AtDc@nB{@pEu@vEg@`E{U|tBkBzO}@`Gk@|Cy@vDk@|B}@|CsBpGw@|BeBdEmAlCuAlCkB~CoB~CaN|SmAdCeAnCo@`Cm@xCSnASrBU|CwBl`@OrBS`Co@zEo@nD_@nBm@xCqGf\\g@~Bw@vCy@tCye@vaBgEvN_AhDa@l@}ArEmDxJ{E|LqDvIgQl`@iQt`@uY~o@y@jBeBxDeCxFiC|FuA~CwUxh@sAxCcBxD}FvMmCpGuDzJaFlNwArDYfAaPr^mHhPoH~NcCnE{BvDcCnDgCdD_EvEmDnDcDbD{AjBs@fAg@~@g@`A{@zB[bAs@jCSbAa@rCMdAUvCCdAEhC?pCJpFFzBBhADhCEjDMnCSpCq@`Fs@pD_A|DgAzEsAvFqBlIqOxp@kClLg@xBm@lCo@hDy@hFi@dEkBnQ]hDsF~g@WhC{D|^k@~EcBpPo@hEiApFe@lBg@dBu@|B_@~@eB~DaB~CgBpCuRbWgAvAyEpGyU`[gAbBqAtBaCpEo@tAwOl_@eBdEcCpFcDzGsCfF_DjFac@fq@aAzA_RjY{AhCo@rAqA~Ci@`B_Wnx@kvAt_EuBxFqB~FkAtDi@nBkBdIg@lC]vB{@nGa]l~Cc@zDa@vCg@`Dm@bDo@vCi@zBsSdw@_BpGof@|xBcAjFu@fFSlB]lEUhG_Ch{@M~CIvAO~A[rCa@jCe@xBo@fCw@bCiz@xuB}ErLuClFuBtCs@z@oAxAac@`e@gBxB{@nAwBlDw@|AoBhEszBjfFkGxNcBlEqArD{A|EyAjFuDvNcEbP_XndAm@vBq@rBy@xB{B~EyBrDgBdCiNbQ}A~B}AlCq@pAm@tAkcA|gCeB|DsAjCeAjBuBfDaB|ByBpCmBrBo@p@uChCgDdCopBfnAkc@lXk|Ah`A{DlCyC|B_c@~]{VrSoCpCyC|DmB|CsAjCk@pAeAjC{@jCm@rBm@fCa@jBw@rEg@jEUdC[lFaLfxEMbHGdH?zG`B`wD\\ru@?f@D|H`@~}@BfJAtBO`HQnDUzDOnBa@bE[`CaApGoArG_@~AkAjEi@hBaBxEcBdEyBtEgCrE_AvAeA|A}q@f_AgYd`@uR|WqApByAdCaCpEeA`CsBdF{BjGi@zA{GbRwRti@uElMsBvEeArB}@~A{BhDs@`AgApAkClCoBdB}AlAoBzAsGlFym@lf@{IfHqEdE{AxAkFzFmEpFcq@||@eUlZ{ApBkThYce@fn@qKjNiAjAaAz@gBrAwBlAoBz@_Bd@_Cd@q@Jkm@fGoAPo@NkCx@_Bx@q@`@oC~BmAtAgAzAy@rAyAzCuG`O}FnN{CzHyAlDsAtC{ElIuZlf@sDpG{AzCsA|C{AxDqBxFgE`MuFdPcWhs@uQrg@w@`C[dAa@`BSjAe@xCOtAMxAIdBKtD@xDLzDxJl~A`@|IFtCHlFH`q@H`FPrETtEb@hFtDt^hM`oAzBdTrBjP^jER|DL`F@hEA`BEvBItB]dFg@~Ee@|CUtAiAfFeFbRkMth@wA|FiGdWuj@v}BqA`G}@bFc@~Cs@`GS|BSnCWfEsIfgCSxEe@lIc@jFcGzs@Y`D_AdHgAjGk@pCe_@n}AuHl[k@fCaCrLsAdHqA|H}@dGw@xFsNfjAy@|F_AbGomAf_HmBdKqAbGsAjFq|@dyC_Odg@w@~Cm@pCkAnGe@`DWxBq@jG{Ij|@oEtc@[rD_@rFKxBOfFuE~yF_AhjAObSCrBkEbrFMtGShF[lGo@bKaGzaAW|DQpBg@zEYpBg@pCc@lBa@fBoAfEgBzEaBhDmQ~]{BhFs@jB{eAv|Ci@~A_r@tpB}JhYe@pAa@nAqIpV}AtEeBpFsA~Eq@pCucBvoHa@dBqI|^iErRsDnPcO|o@cGpWoAhEu@xByAfDaApBw@vAoAnB}@rAqA~Asr@dv@oUzV{@|@uj@|m@sClDeBfCiB~Cs@vAeA|BkApC_BxEwQ`l@wxAbxEyCfJ_ClGmAzC}q@lcBaBrE{bAjuCk\\h`AqL|\\eB`EgBfDs@hAcAxAuAdBmCrCqfAnfAiBnB}AtByOfWalBf}CiFvIgBrDq@~AmAfDoAnEgA~Es@jEYvBYjC[~DSlFExCAhEv@v`AnExoFFxM@fuBY~|BSjdCo@t}BKzo@I`HUpH[~GSvCu@hI{KrgAUpCa@nGY`HMhFGvGm@b|BAtAEpS]toAIb_@CfCKxDQnDKxAa@`Es@`FkE|T]dBcJhd@oGlZyJbg@yQj~@uEzUqKfi@aXvsAy@tDcAzDkBbG}A~DiC~FoAbC{AjCcCpDcC`DcMrO{O~RuAjBiAdByAhC_B`DsA`Dq@hBo@jB{@pCo@dCo@rCs[|~AeI|a@aSfbAiB`HuD|KsRlg@uAxFi@dEk@dGWlH}@rWWjF}@nQ}Bph@e@tEu@lFiAtE{ApEkB~DwBnDaCtC_CzBmCbByGrCiQbHgTnJsDpBqCrB}B~BuEfGod@`{@qCpFgB|CgGvLcB~D{BlG}Tbu@uSbs@oClHsDjJmI|PwcAdkBgIfNqGzJij@fy@kFbHaC~E}ClHoVxy@wU`x@kBhGa@hAw@lBo@lAqBfDcBxBeBdB}ApAgZbTiA~@qBbBmDlDmBrBiB|BcBzB}BjDuBlD{BhEyBxEq@`By@vBmBvF}AlFm@|BuAbGam@`vCsAzFsAzEeBdFk@xAwAfDu@~A}w@f~AaAxBmAzCiApDcAzD}@nEWxAg@|Da@fEMlBUjFgAjvACdC[nKC|CK|CSpCm@bE_AjFsYjvAuGbZcBjEeCbFuCdE}E`FsGdGcJjJsAnAiKlJuIhIsB`C_BdCqBnDkB`FiCzImFbToDrO}ApKmCtVgStqBgAbKiDv]{AfNaA~HeAlF_FtQu`@lvAcL~^ej@|~AsQzi@_JfWiElMsJxXcK`[}C~HcArB{BzD{AtBmCxBeDvBmDfBew@r\\yPtHkYpLaKrEgJbGmDbDuEbGyE|Go}@pyAk~@pzAuJvNkCjCgEnCoEdBsBb@aCVwCToNHkPG{]TsDXyB`@{D|AcDjB_DnCuFbGuz@j}@yHzIgDxEoPjXcFxIaOzUgBzB{B`CyBfBkBjAcFvBgc@~N{LbEsErB{DdCyApA{BbCqGdK{CnGmBtG_Qpj@uLj_@mApCqCnF}BzDmBnCuD`E}IdHse@dWcWnO_F~DgM`MwErFwrBjhC}MhPmGvIcH~MmQta@gLbYmt@naB}H`RqEfJeEjFs@`AqsBnhC_V`\\wJpNcb@ng@kCrD{FdJyWnf@q_@zs@gSf_@{AbCaLfPgN~PcG|IyDxGaAbBmHbOqTpg@_Uxd@aAfBaCtEmGfJuFtF_F|D_BjA}W`Pgf@rXeTpMyDvBcDnAkAXeAPcCXoBH_F@_MPck@Csu@TcBAumBb@uCHmDXgCl@kA`@}CbB}AnA{CdDoC|D_FvKkFbMmArBoG~HcArAsLbOmJvMoBvCyAlCuCpHuQ|j@qAxCsAfCeB`CkEnEuFdE_SdNqC~BwEtEsFvG{F`Imu@niAiOtUcO~TwCpD}BfCoFbFci@~ZkAv@ms@vb@wCnB_J`HgCxBoJpJiIbJkArAez@p_AiN~MkFdEijAfy@yJ|GwFvEs]`\\sjC`eC}LtLyHvG}FlFuDbDyExDiIdG{PfLwk@r`@iChB_CrBsArAeAlAoBlCmB|C_DjG}EtM}KtY{W~r@cBlEs@fBw@dBaAfBm@~@}ApBm@r@qApA_BlA_BbAcCjAoCt@wA\\aBTiAHoABaZAaMDyv@Dga@Eil@PwDH{BPeD`@sEfAiAb@_Bb@sEbByC|AeDpB}ObK}h@r\\gNjJoG|DiG~D{KzGoCrBgaAxn@qQfLeDzBoXzP{g@j\\yErCyFrCkIlDiHnCs@Rsu@|YmG|CsEhCwKzGoYvQmThNuYxQuNfJaz@th@_UvNqD|B_DhBmK`HeQrK_RtLcKdGeOrKgDrCeCxByDtDqGhHoTbXwIxKeb@nh@qLdNqM`PmCzC}CfDkCdCoDzC{WpSam@rd@k}@xq@cFjGoExImCrJmD|U}PhjAkIlk@e@bD{@|Fq@xDkAdF_@tAgAfDiApCc@dAcBdDkB|C{BtCmjB`wBmEbGcyAdbCok@f_AcYze@yb@zs@ki@r|@cFpGkE`DcChAkEdA}D`@mTJeDC{ROaID_HM{CCwJEiJZuDz@aDhAaDlBaDvC}ClDuFbK}T|c@u`@px@cVxf@uh@xdA}Vbh@iIhNwG`J}v@jdAi`@fh@oJpMuSrXah@xq@gClDuHnJaR|VmElG{f@fp@aK|M}FvHi[jb@cL`OsFzHgBzD_BpEuAdFw@dEe@vD_@dEGhAcA|TgBh^cGrmAUhFYjIOfJ?nACvGBvi@GpcB?vXBviA@vPCdJ@dQA|u@AhVBja@?pWAvo@DtRD|j@?tFDbXHt]Txz@EfGAjDK~EObD[`GeAzQEl@_@hGuBr[[vFK`B_@vG]dIKbHBxEHhCHjC~@tRLjClAzV|A|W\\rGLvDFnFBvJBvIBr]Bzc@CjZEpV?|IGj\\CvCA|GAnC@tIO`d@?xCIpa@M|[?~H?jOE~IBhL?z]ClCBdv@\\~o@Vze@C|GKnDo@vImAdJo@|Cs@rCk@rB[dA_BfEqBrE}@jBmEjIwAzB{@zAs@dAaP~YwLlTGJ{HbNuDbHsH|MiWre@_DjEwE~FqCtCwFtEaE|CuErEuDlEuFfIuAhCcCnFoBdFiC`IgB`H_B`IoAlIy@hI]rDWdFUfK@xIAxH?pEB~_@@vp@@pCEbBGrCU`DWtCg@bD_@tDQhG?lEFnDLpEX`Ex@~HPdCR`GDfDDzh@@~J?`AJfz@D~M@|a@CtGf@|iEHf}@p@fsC?zD@p@Nzz@h@rxBD|yB?tAEz`ADx{AIbxA?toAA~YBnJFfE^tJTxDTzCVjCtAhKzBzMbAjH|@`Ij@vGPlCRtFH~EBdE@lQCpL?zLAzi@OnHGzBc@xHeGdt@u@zKShFGjKRpmBDr]Ex]Fr`Df@|vEFjmABvYCh[QbjASxaC?`~@F~uBLxoABdO?nj@CzWJjkECrjBAbx@Cj|BBho@Ad|@Mt~AGhdAM|uDMhaCErJGpDq@~Kq@nF}@jFw@hDwAzEaAvC}@xB_AnBgCrEcy@~sAcTb^uEvHk_@vn@yeBxuCyC~EqJhPg@|@uAtCq@bBmB`GmBpIw@~E[~BYfCU~COlCK|DAxCKrqA?rOF~dBB|IA|TDttBAhM@`E?d_@@ds@E|nA?bf@?rXCnD?|]Iz`C?xYCjd@?pcCD|oBCjSEf`A?lMCrI?`JW|uAInqAElb@GvQ]vcA@pIFzIZvSfBjy@T|LXjKVbEb@tD`@jC`ApEx@rD`AtDfAzE`@|BXfBT`BNbAp@fHXlILpF?fNC|B@zIAvPK||@BjDJpE`@lJTjDZjD~@tHRxA`E~Zn@jFpBvN~@dIbCpQfC~R~@vGl@xErBfP^hDn@lEPtAZlCNnB^fGNdG?`EC~BKpCMdDMpBQrBwBvO_@hCiB|MSrBSnDKvD?nDFjERfE^pFHjBFtE?dECtBGrBUfFCx@KdBa@nHKnAQlB{BbSSjCa@xG[rHEfW@h]Cz[BhSEbs@AbCH|RVjND~@VbH`@lH`@zFXvDh@xF|AnN~@xGzBbMjA`G~FrWjGpXzBfKbAtGnA`Lf@`HZdJDlC@jCA|i@QxkCIdb@M`bCAdB@xEAdxC@~FCpR@lAIvWFvb@CbkACh^BnC@bVEvY@bNArpAKp^KndAKfb@M`wBNzHV`Gh@jIXjCp@pFr@lEh@fClBvIlBvGjJ|YtKr\\dAjDxEtNvSdp@hCtHfEpNvBfJxAtIv@nF~@`NRpEP|EBhTGbCDlHJtcAHriD?rm@?v|AKbeACfREjYIpZEpaA@dZZlxF@fY?fB@jE@tRDjRNh|@ArLPrdA?nKLvw@DbrA@j_@AdVHfoA?zABnl@Cfg@@lM{@h{BCldAB`V?ldABnKCnLBhx@BthA?j}ADhGNdGJxBZvERvBTvBhFdb@b@zCjBrP\\hCHx@dD~YJt@`@~CrF`c@VzBpChXj@hEj@xDZvCd@nDn@xGnDtXrBfQl@bILbDBjB@bEGbEMzCSrBUhBm@xDiBvJqL`p@eHr`@gPd}@{AhJa@rCa@nEMvBGhCEdn@GpME|s@Ifc@IddAIhgCIp`AChl@@lLChV?jsC?dw@Dbp@DdcC@b{AAv[?rs@?`oAC|UOdt@@tIf@|YvB~cAl@xVjArn@f@dVj@fVRfN?`GC`CM~D_@jI{AlSi@`Ie@vHMpCUpGM~DGlDGjH@dFLrPDxf@D~Zn@piCBhPFdLBjR?|JLlJ@h[?fLHxRD`VJdV@~b@F`UDrWPnYBhC\\jL~@|U\\rHf@jN`AxTlBzh@PrDb@fHd@zE\\vCv@hFr@hEtBhKhEhUf@xCv@xFZfCh@zF`@bHH|BLzFBdIAfAMrGi@lOE|AyA~YgBp`@y@vRKhDMbHI~KAxERfa@ZbWXdd@V|UFzHHzQ\\tZPzUL~KBpINpPH|PVfVJjH\\pf@jAh{AdCfxCTrN\\jIHjBn@zKb@xG~H~y@lBtThH`t@nA`O|@rJdAbK`B`Q~@pKvB~T^~ELrBR|GHvG]dxAGty@Chn@?je@IbkBCtV@~TCvXCf}@I~j@?~j@AxIGnJ@xJA`NDbIJjKPpHj@pPlBlf@ZlJVlHr@`Uh@rLd@jNj@`Nz@fU`@xNXbIz@nRVbH`@rO~@nVFfB^`Mj@vKJtBJbDJtE\\zJLlCnBfh@VfIDzAn@vN^`NZzI^lID`CB`GEnFYrFW|CWtBu@bFaA|EmAvEcAdDaBdEmD|GaBdDoAnCsBfE{AhDaCpGm@hByAnFcAfEUzA{@tF_@jC_@bEa@~FY`KMfIE`Bs@t[QzKCzF?~IxBpyCRdTXna@tAvdBD|KBv~@D|SGdZMzIWfJUpEuA|V]jGOvGA~D?~BBbD`@dVlCftADpE@hFAbT]niB?dq@GtI_@hJSzCo@jHyBvSW|CE~@[dGKhEGxG@jENfJXnGJvA~@fKrHpq@b@lFJ`B^pIJzFEvaDCxM@|eAOrnCKxfAG`WIru@?`WFhw@@~}@Exn@Q`fA@`LEjW@bFFjENpETbF^rFd@tEfB|LxDfVvNd_ArDhUbBlLj@hFh@nGZrFLlDH~FB`HA|I@rCCbGEnEA`b@Cj`@ItTBbDM`yAB`ERbGb@bJV`Dp@`Hb@|CvLvw@bDzTnIzj@vChSrC`RTlBh@hFVjD\\pGJdDJfFCht@CdMExm@EnJBjLE|_AW|aAK~_A?puABb`AAlkB@`KAjzBBrTEp_AB|C?nn@DpxBCjYB|jAA~S?~jACpS@vREhx@@|e@Ehf@ElRD~ZGbt@?~k@EfS?|c@Ere@@df@Ery@Af{@DpHRhIt@bMx@~HrBjQPlAnB`PN`AtEv`@d@bDrBhQ~BjRxNnmAbCnRrA`Lr@hEv@zDr@jDpA~E~@zCvAbE~BxF~DzHfKtPdMjSrDfGxZdg@tD~FhA~AvKxQzAxCzCfHpAvD~AdFv@vC~@~D~@|Eb@xCx@xG^jDZ~D\\nGJpDF|CBxGMjc@A`BQrq@Yh`ACff@Bzx@BtLB~tAAlf@?paBCxx@CnlDEx_BClz@CfAGrd@I~d@GnbDm@rcPQ|eAO`x@Etf@CjxAC~mA@hL?~CC~TAfWJty@BhlAF|l@SpRKdF_@dKuAjXe@~KkArUO~DQ`JEjQ?jVMpu@@vUCrNS`SGzROjy@BdLEl^@nWTlI`@xG`@nEZ|CrAfJh@`Dh@dCbMfh@xEtRjCzKd@|BZvApAtHdArH|@rIb@dFd@xIL~CHzCH|ED~FC`|@Alp@?dF@`_@E|tAA~lAA|i@?lC?|VCdS?hC?|h@F|FPvFb@~E^~Cd@bDVxA~@nElBlI\\fBz@nDbA~EvCrMzAjHP|@pFrWr@dDtEjRnFfVpGvY~B|K`@rCf@nEHdCD|BC~CKvCOnCc@lDYlBiAdFiChKqMth@oAdFcB`FyBfG}AnDeCpF{ApCiB`DiAdB_DlEoChDuC|CeNnNeBtB{@pAmBrD{BtFg@dBm@~Bg@|BUpA_@dCIv@yAjOw@dH[~C_C`ViC~VcIhw@w@hGYpByBvMiLxo@qEvVa@xB}BlMy@dEgAlEkAlEgA`DoE|LwWhs@}Zlz@qIbUcGvP{GxQ_ArCw@dCg@pBsAvFcArF}@|Fs@dGa@pE]pEOhEOxH@dPL~YBhZXhu@Nxt@\\xoABtSFfSVf}@HdJj@feC@`ZCvFGfCkBfi@MtEaAjUcApXoApYgB`i@e@tLIhCGdDElD?vBN~Jx@~Up@tOpCdu@fGh}AZjKFdDHnUBts@JbwAHhKLtFTnHpA`WrB|d@\\|JNxGDxJ?jIFxWNxcAEzDOlGSpEY|De@rFy@fGk@vDcArF}BrKsCbNu@tEs@bFgAtMg@|JIrEBlJDtGJvDLpCl@fIhBzYrBrWp@hIr@pNVvJTdQNb\\b@ds@F|YR`ZH|XQlLMpG}@rTWxHiD|w@KxDA|E@~DHnCP|C~@pKn@bIdC|VvAtPVzD\\bILnE@~IBlXGpGLps@?~oAFvXDnlA@`CDbk@AfQNn{@EdWAvi@I|sAGvi@I~TCxl@Kbo@B`o@EvdA?z`AEj[At{EEfp@?|aBIlsABvg@EvX?`g@C~FAdfAD|eAEriBItlA?fYKr\\Ahd@Cbd@@|IDvETxSLhIL|FBfEE~FOdFiCpb@QxEKzECtCDjDL~E`@`Gf@~FzBjUp@xKNvEDjF@zIEpCK`De@`JqAlUuAfVg@dL_@jMOf]Ypi@IlUO|TKjYBjGr@jb@JvIC|ES`KmDhy@UbIMjKCjG@rIFtFJfGVvHn@dPzEpfARpGFvCNvLBzFKji@e@peBDxMZxQ`@fKt@vTHjHAnHStIOjDuDhh@aD|d@i@lIUpHKhID~IFrAVdIbBj^jAvWxAzZPzFP`JD~a@K~pAAja@?bB?`DAzs@?fJX~~ABrn@Lpo@Blo@MpzA?nSVbIN|Cr@fKfCvV`@rE\\~ERnDDbEAnJ[fHwMjdBWxBqAbKy@pE_Nzn@w@nFk@nFW`ES`FEbG?rG@lG?nIBxIAnXDbi@@rp@DxDRnE\\hF^nDd@nDnAhGhIn_@z@jFr@|FVnDXbFD|C@zOEp`@Er{@?nc@Cl[@zGE|JIvFuAzi@QhJEzG?hGD~\\CrMB|PAjTFxENxFVxF|@nMnD`f@^`GNnDHzE?dEGnEK|Do@tKmBhY}@tOIlFAbD@dCH|DtD~eALvEFdGGvEOvGSpFe@hH_Enc@]`FM`DKzDE`E?jL@dGAvTDh{@AtOJlLTfN`Bfc@HdERrM@jECbG@|ECdYH~UE`V?tOB~FErOC~}@B`GClGCjw@DbENvEf@lK\\bEh@tEv@|Fz@rEdAdF`D|NlAfFxFdWt@pCpAhFrCxKlC|JpE|OdApDr@tBpA~EzAjHp@xDjA|I^nDtBzX\\nFX|ClApOT~DNvDHfE?bHKnEWrGSjCg`@|iEg@rEiArIgAfHs@dEcBxIcAvE}UbbA{B~IaF|SmApFeBvIs@|D{@|FyArK_CjT{L`kAkAxKq@tF[`DsHdt@u@dGaBtPyDt^k@hFg@vDy@nI_E|_@O|AqA`MiBrQYhC[jD[`FOhDQvH?vL@bTAdTBvb@A~H@|s@Enp@Dfj@AbH@h^AzEDdXAvPBvDAhT@vBCt[D|g@@nQCfI@lD?dIB`GCbQ@rh@BlCAlCBbk@Dtr@DzFAhMFt_@d@vfFJdd@FzMHrWJfN@hRHjPFxCVvGVhEXfD^nDjBjNbQ|kAt@nH^|EPxCNlDL|EBrB@|CEtDc@fO_@`Gq@dGaCdQcA`Ik@vE]fCeEf[iCxQiBxNkCxRo@fEs@`FyInq@wBtOsCrT}BlP}@dHa@pDk@xF[hEO|CQbFInE?fFDjFJ`FR`E^rF^rEtDv^bEf_@p@jH\\hD~AlO|Exe@h@`HLtBL~CBtBDbHE|EG`CMfCs@xIk@rEw@fE_AvEqAhF{A|EkKdZgBnFcAnDg@nByAzGi@xCs@vEu@fH_@fEUrDQrDMnDGpF@da@EfQBrEC`LB|@Ip\\FbVG|K@`RArJBrLC~I?fQ@`IBhEH|CDlFBvGd@t_@H~L`BbzAp@th@PtUEjFGvCQ|Ce@xFuAfJSrAg@~BkAtEoBfF}DlJiDtIg@rAaMtZiApCyD|K{BpIc@jB_AjFmArHQhAe@~Eg@tGmSjlDSrEa@bPInGCtDEhb@?tBChe@Gv{A?hB?tFH|GHdC\\pHl@bIbAbI`@pC`@|BdIf`@b@|AvEnTh@dC`@nBh@vC`AzGRvBZvDP|Cb@~GJnDJpGBdECr^@te@C|`EC|lAClnAEpI?dm@I|k@@jN_@f_GDvV\\rPTzFd@dJj@zHvBrWPdCdFdo@HpBLhEP~GA`HCxA]hJOxC]vEw@zH{AhLyEt`@c@jFQ~BWdGMxFCfDCnl@FvnDAtGB~HA|[Bl[BzBEp^Fhl@G`QDzPA`PAfC?hICfBqAx_@E`CAvZFlUApTDnU?na@Ej_@Bzk@ChAAnY@zICbU@fHAvC@vf@ApF@zCKvJIxDEtAa@vHg@jFk@jFk@tDeEp\\cCrQkDpXaAnHcAhHaAfIaA`Hw@lGm@bHg@pHKvCErBGrMCl`@BfJAnD@~a@AhKAzEEpHQzFGvAYnEW`Dg@vE_@~DiAvKkA~Li@zIKbCKzGChEB~FNbIhB~g@rAha@j@lRLtJDrOBdhADvSFjjCLbP|Ch`B^pVH|LHbYBnI?zd@@~DAtFD|ILbIRhIN`Ex@~O~AzR`BjNdDfSjPxz@`B~IXhBr@tFlA`MXjFHlEJtK?fEDlHDlNR~GfAtNjCpUnA~LPvEK~KMjD[jDo@dEe@|Bo@jCkB|FiDpJmC~Ha@rAqAbF_@nB_A|Fo@tFEjH@bDDhCFfBxBb_@vDhl@PxDB|DMrFO`CYbCm@~Do@xCe@hBmA|DaB|Du@zAsBdDuCvC_Av@}BdB_FdDyCnBoD`DaCbCwArB{CbGmAxCcAtCq@hCk@`Ci@jCc@fCSbBi@jGSbDGjByBteAMhFShEUzC_@nDm@nEm@`DoA`F_A|CuAxDoNn^gBfFs@dCgAvDiApFoA`Hy@hFg@zE[`Dm@vKIhFIr^I~Ge@dKsB~Va@dGYpGw@z[MdCUbDg@jEi@tCe@rBsCnIoEdMwBnGoAdEyAvF_BrGwAbHu@vEu@jFc@zD]hCu@xHqBtQo@tGe@jE]vBs@pGq@fHaAzGiD|L_AvBiAlBwAhBuAvAaBhByGhIsC~CaD~EgBhDyBpE_BdEsAhEmAvEmHh[sAvHg@~D]~D_@hFiB~`@e@pHc@hFe@fEuDhX[pCW|DKnF?vBBjBLzCRrCr@tGvB~PxAhMl@rEp@rGpDnZjBlPT`CPtB^jGH~D@nFGjCOnE[zEm@jGy@bHkBxOW|BaBhN}ApNk@hG[xCSbCaBpLeC|M]|Ai@rBiAtDuFxOkLb]qInVmDrKqCrKkB~FmHbYeE~No@lC{U|{@gArDkApEiEnOgBhHo@`Dm@zD}@tI]~GGzD?vE@|ADxAdArSl@xJhCzf@FxDBbE?bCGzDm@jSWzEg@zGu@rM}@fPMlBq@bKk@xL[hKWjUYxQUvJi@nb@aA`l@[`Ve@`XOjM?tBQjDmAfRe@pD_DxYqCfTa@nEaB|NcFv_@k@`FSdDMfDCtEJpENpC`@fF`@hEp@`Fn@jEx@bFnBdJlAzEnAhEpBrGhMt_@zBhH|FjQ`AhDh@zBf@~Bb@dCr@bF\\jD^zFJ~HCvsB?pCGx\\@xWBtFLtE`@vHvSvmCTzBhCt^d@vIHxDBdFItImAx}@UjLc@t]e@pNYrD]lHyDlk@GvBS`HCrFBfEFlCJpD`@lJt@~Hn@nFnZzmBzBxNfEtWdBlKbBzKb@zC`CbPjB`LfB`LpBzM^|Cp@rGXzDNbCJfDDzBFtGGviB@rNCv_@J~Ij@pO|@`RTnJDvW@xtE?rUD`GN~HZlHrDdo@NrFF~EMp\\A|PSx`@@lCCrGAbP?vh@Qz{@CdESlFc@vIk@xHyAbLu@~Ds@zCsAfFyD|MaXnaAyBrMoAdL[lEYnF{@hXo@fXGlDA`CCvKD|TAhCMhHOxF_@dHm@fI_AlIsGxh@mB`McA~EsClKyC`ImAvCqb@h~@mClFwBvDwDnG_ClDeExFkElFeAjAkCrCeuBbvBeExEeArAaArA}BtDaCxEqArCwAfDaC~Go@|BcB~GaDhNgc@jnBoErRmBbJeD`SsBhOoCvWm@lFkDj[_AnJm@|Fg@tE{A`M_@~D_AxHcEr_@oApKaA|HgAnGwAbIuDpPkFnQkC~IaB`GgN`e@}AtFoAvFyApHiAlGiAnH{@zG_BlQa@dG[pFUrGUjLCtEDxFEbV@jhAMjbBBfTCfX?~i@GhKShIO`Ec@nHm@zGy@bIs@xF{AzIc@rBuAhGyB~HgArDgD`JoCxGgMpY}y@|mBes@x`BeFvLgEhKYx@kA`DcBtFwCdKoClLg@hCo@jCePru@aC~LwC~LgGxY_Ht[yKzh@oA`GeDrNg@|BuH~]sFbXgDfSqBvJmAnF}FnZqCbM{@nFqAxGgCtL}DdS{BzL}FhY}BxKsAfG{@dFg@`Cg@rBi@jCqAdIaBjIiI~`@qBrKaAjDoAzHeCpMqAhGgAhGcAzEaDlSyEl\\wAdJgBfM}DlXiAnGgC`S}A~IaBnMmBfMiA~FuFza@yH|h@oJdo@gEpV{AzGcAbEiDvLyAtEmD|J}Oba@{Lp[q@`B}Lj[k@zAeH|Q}CvH{A`Eqi@ruAmLl[gGzRgDfMeCpKyBlKYpAuQz~@kB|Js@pF]nDu@|IYxHOtFAhHP~K\\nH^|FzIty@dCzTzBlTlObvAf@jHJ~BBhD?jCGlDSrDW|BeAzH_ApDm@xBgA`DiAfCeApBmAjBs@bAqArAmXhWq@t@yBxBaBtB{B`Eo@~A}AvEaAfEa@fCWfCMxBc@xR]pQ]tIc@dE}@vF_@rBk@jCuAjFsA`EoBjEqBtDkWld@sBzD}B|FgApDmAdFo@hDi@pD[fC]rEe@nI[lHm@~H{Ij|@QdCM~FCdEBtBN`HdAzRPhFVdGn@pSXrJr@pOv@vW~@nXJ|Eb@~KfAxI\\fBz@pDf\\~pA|@xDDLbGxU`AbEnFrUjEpRhCpKt@lD\\nBx@`DzBhKpGzXx@fDtMtk@jCvL|@bD`@nAzAbEdAvBzCpEvB~BxD~CnKzG~HjFvGzE|VbPpEfC~FpCjEfBnJbDtE`B`Ab@nBp@f@PbGpBhHpClKvDhEzAlEjBvEdCbElCrM|IjR|Ln\\xTn@`@zaAto@|k@``@v]hUbTvNvMrIpXlQ|F`EfFjDdR|LtZfSpZvRvXhRrQfLbRjMtCfBjK~GrM|IrG~D`U|N|TdOxW`Qjd@zYtg@~\\hFhD~KxI`CrBjF|ExNrNnG~H`JtLrGzJ~GjL~C|FzCbGxDjIxFrMnDfJxHnUjLp^xSro@jItWdOxd@bCxHxKp]p@xBbLr]x_@blA|Lb`@xX|{@xLj_@fRzk@jo@dqBd@nAhBxFtCdJze@jzA|T|q@jS`o@nPxg@rAlEnIdX|Kx\\tA`EfOxe@pZ~~@bDbKrRxl@|Zn`AxTnq@fAvDhQri@rBxGfItV|EjPnFpSzE`PlEjNvI~WbMd_@xA`FrGlSrAvCpB`ElB|DpBtDlCvDzCtDrExE~F~E`A`AxCbC`PhNlLlKhNpLbC|BnNxL`L`KjTfR~C`DvGdFtGzEzQhM`L|HpBlBjDrCzEdIxB~DdDxIxC|LbNpu@t@fElJ~g@|SpkAtAjHfT~kAzDpTpDtSzE~TlBrGpNxb@bHlT|Mta@tL`^hI~V~W`{@tAhExDzMbCxKzB|Ox@pIp@vHr@tRrBf`DVvg@d@hOdAnMrAzI~A|IvA~FpSjt@tRlr@|GrUhOti@nGnS~DjL~}@~eCjEzLxSvk@xhBnaFzCjIbGlOvFtObKtXlFfOfFbNfM~]zFtO`BdE~AlDfCpEfC|DjFjHfA`BlFbHhGrHvGjIbHjJnNvQp@|@jD~DpAnAnExDzCtBnCzAtCtAvNzFnJfEzDvAtMhF|[fNbTnIlN|FzZ`MfJzD~FdDbBhAjCvBhDzC|DnEvY`b@zp@t`AdJvN~HnO\\l@zPr\\zBxE`DhGlBbDdCrDtCnDbFnFlEhDbC`B`CvA|DjBxMtFhCtAzAdApAjAzCdD`AvAjBhD|@nBdLbYpBzEt@xA|BxDjBtBjBhBn@f@lDbCdDpBdCxBv@z@zArBr@jAv@|Af@lAf@vAbBtFnClLrAnGlBrHxAtFrBdG|B~FdEbIfC|DnAbBhC|C~@bAlGvFfCjBdDpB`Bz@lCfAlFhBfLlDxCzAtBrApCvBrEbEz@bAbFjHrGfK`EdGlVn`@fBvC`A|ApAjBhBvBdDfDnBxAxGxD`FlCdKnFxGnEvAhAdEhDnE`ExEbF~A|ApNrOhFpFvAxAfEzEpe@`g@|GnHvz@x}@b@`@|FnGfJrJ`I`JnCnD|AbCxAtCtC|GrJpZdKt\\rOff@zAjFdAhCbB~ChDxDpAfA|B`BtHbEfQ~IrEvCtDbDhFxFnDrE|DxGpD|HxDrKjFrStGzWvDfT|@~Hf@lFThF`@hF`AvHtAnH`CdLvD|LxDvIvBfEzFpIlBtBfCfCtDhDtCzBjCbBvCbB~`@pQ~CpAlHnFhEzD`EjEvC`EpCrEtDbHnDhJbYtz@|Ntc@pFtOtD|KlGdQpa@rgAh@`BjC`HvAhDpBzDnEhIfBpClCrDvB~CvPtWhBdD~GjK`HhKfFfI|A|BdC~CbBhBzBjB`CdBxIdF`bBx_AxAhA~BtB|AzAdCdDlCfEnVn`@d{@luA|LrR|N`Vpg@vx@d^|k@nK~OhEnH|B|C|ElFlQ|K`L|HlMjIze@j[|H|ElCzAhWbQ~ErCfLzHdPjKrd@dZlLzH|LxHjEtCfCzA`DvBnGtEhGlFpErDnD~DzDdEjFhH`DtEfCxDtGzLlDjHlEnJ|FdQpB`HpHhUbEzLr@zB`HpT~G|Sr@vB~e@pzAzArEfUps@n@vBtRfm@~Pvh@zNjd@hrA~aEblBnmFtDtJvJvS|Yzj@pFrKzJpRrZ~k@vBhEdCrGpBdGdAhDtT~_Az@zD~BlJ`ClKfN|l@`Jp_@f^z|Av@bEx@|EvArLl@bKVpHBbBBzD?pCKjHq@pPUzDoFtkAs@lOQjFGfEAdNB~_A?~aBB`IE~HM|FYtFk@~HaEn_@_Fve@[pDc@zHOfEMbGDrJR`IPjD`@rFTbCt@jGjH|h@`BxKf@xChApFzAzFdBxF`ApC`B|DdA|BdB~CdAtB`Yvl@`CxE`u@l~AzUxf@~b@~}@dAzBdD|HhBdF`@zAjDdO`K|n@N`A~Jxn@n@fDdApEhEtOzAlGf@hCvFp^`AvILfBnAtUz@~IZnCjEhZxr@fyE`E|Xl@vErAbM^bEZ~Dt@lKb@fKPpHpAxk@D`F?lBArEW~IaAbN{AzLeNdbA_@|Ck@|G{@tO}Ah]eAtSm@rJo@`HeEta@k@hFmBhR[hEQpEG`FDzFPfFTfD`@~DZfCl@lDp@hDbBlH|AlG`@tBZpB^lCJjBBzECzBOzDc@tDeAdFkDdLuAjGYzAQtAQfBS~E@jCJnCf@tGZlD^jHJnCJbG@lJCpk@?pzAAr]?tiB@bBCjzCBjo@Cta@@|H@pwDFvPhAj_ABhDDjC^bYB~Br@nj@`Atu@BlM@`j@?~zBBjRBpCPxGLbDbAzRXtHNjFJtGH`L?bGOdL[vKwAlX_@xJOhHMnJCtDB`nDA~\\Bjv@Fl|BEtV_@hVo@dWi@rOKnGG`H@tFDnFt@|Wf@vHr@hTr@`QJdEAfDC`CMfEeBbc@oAdYCzCBzBH~CP~Cp@dFh@tCx@xC|@hC~@zB`BjCjEpF`DjEdDhEnIhK`EvFxAzB`ArBhAvCzAzEjAdGh@tD`@lFLrCLnHVrTJtFXnFf@tFp@tEn@jD~BjK|@nEx@lE~@bHb@|D\\fE`@xGpD`u@`AxPRxGDvD?dEE|DGlCMfDkDjv@_GdyAeAbV_Bv`@UxHIlGEvF@rGL|NVfJd@|Jp@dLjEpp@rBhX^xGhGp`ApCz_@tD|j@l@zI|@rN^fGD|ALhG@hFAvBWtNs@t`@o@l[IdJ@lTvBjhFGvMKbKk@xTcLleCm@tI{@xImAtI}CbQiL|m@sQl`Aw@lEcBfKw@rFaBvM_@fDaFfc@gA|JwCr[kNh}Aq@tI]nFYtFQpEMtEM~FIdI]j}CSj|@CfT[blDF~IRnKh@tNnLruCVrJLjJz@pnDd@v{B^tzAXzkA@jCJtZJ~j@L|I`JhvDT`JRpFHlFjAhg@jFxvBf@jTLdDRxC`@bDXtBZbBh@~Bl@vB`ApCv@nBpB~Dz@pAnChDhCpCjDdDlCxCxRrS`D`DhEnD`DrBvDpB`^fQxGjCnFdBtVjHxEhAlSbGlPtErEtAxIzChZhMnSpI~HzCjq@tSzFnBtFfCnLrHtf@h\\pWrP~DdDzA~AvZn^p_AliApFlGtZr_@hG`J|AhD`CfH`CbJbB|ItEnQ|@xF~AhGvCfNpAjKf@~IT|IS`KO|WDxKMpI@hEMvQAdTOrNSnI[xIi@tQMnH_Bvf@SlDIpEo@xVCpGPdJ`@`HrAxJvAdGvHv^`CjKrCtNfBhHjDzPrDvP~@lH`@pFL|EJdGCnGi@hL]hJe@lG{Av]iBb^WfDcArWsA|WU|FA~IPfJ~@~L|G`e@lB`MrD~PxF`ThSzt@vJr]jQ`o@z_@~tAtCdKfCtJxCbOl@hEh@|Ep@~HZdHRpZJhh@N|V?~HZ`Ox@vLxCn\\`AfMdCd[fDba@pCl[jErq@fCtp@|AjTvCxUhChO~Hr`@h@tCtFr_@PtAnD|WfBjLvBjKfEhQxMvd@tHpXzGzTxFhNvCvG~BnGrCjGvBxHbHhP`EnGrS`Vxi@|m@nErGpD`IrCdJrB|JhCxQdBfHjEzMfDtIdCbLhBjSvC`a@r@vElBxHdLbTnDhIlC|K|@nIpArV|Bxh@d@xFb@lEb@jC`ApFtAlFnAxDrAfDvDzHbBbC~ErHb]ji@fDzFtBhElC|GpBfGtDzMtEfMnDbI|BhEtXvd@pGfMnCxHrCjJjA|Ez@~E|Jhp@`ChPf@jGPtCxA|m@^fIbAtJbAtHtA|HlBzHlCtIpIrVpD`MxBhJvQr_ArDtRxBtL~E|V`@xB~AbI`EpTdBtIpJlh@fAvIf@`GZ`G`Atb@d@fRb@rHh@fHp@vEt@fEzB~IvBjGZdAdQld@bI~RvBdEbCzDdEvFjGvFxRvN~K`IdEhD|DvDdErFnCvEtAjCdCjG~B|HbBbItCnUfBra@bEjy@d@hGn@xF|BzM|AzGtA`F`BnEpCzGfDrH`@bArKvUhDdJzBzGrDrNpCvOb@dElAfKj@nITpHHvAPtD@nDFnEUh[RhJb@zGPdBlAhI|BzJjBtFfHjS|ApD`EfL~AtFpAdGbKxi@~@bE~I~YxBfJzAbJpArNh@tILzKBvADtTLhMXdOt@zLpAvLxBnLlBxH|BrHdK|[hQfj@nBlHlB`KhAdIl@zGNzBbCh`@F|A|GniArMvhBdBdP`DnSnAxG|B~JxBpIfD|LfAnDzE|PzCdKzWx~@xa@txAxFrRjZneA^pAvA`FpBrJtAlJ~@jIhH`jAHzA~F``AxDtl@bIxqA~Dtm@d@rFn@rFbAlGjAjGf@tBvBhIrC|It\\|gAzB~Hnh@xdBnRfo@dK|\\d@|AvKn^tGbT|T`u@~ArF`BlG`DnNhLpo@lWlyAxhAhnGPdA`Knk@fApFxAhGfBjGpBtFrBdF~Xrm@pZ~p@`GbPzCxJtCrKrBlJhBdJlIbi@zJxo@vAjHbBdHfCtHvMf]~DxKbBlE`DjIvHzRh@nAlK~WzCrIdCdGvPvc@|Ytu@rCfI|CfH|z@zyBbFjM`D~GlB|DxB`E~DtGpGtJtCtDvDnEf{Ar_BxUzVhAnAlN|NzU`W`F~FlC|DhAhBfAzBrGvLrf@d}@xPh[vLrTz@|AvDbHpB|DlCzFzBdFhB~ExTzh@hBtEvAhEnA`EjArE|C`O`A~DhAlFlAzEvf@~bB~GhUjB`HfAxFbAtFhAfIjJbn@bDpTXvB~@fFdApEtAdEdBxDtBpD~BtCjCfCdDxB|CrAbDlAd`Ah\\vDhAvDz@vAXpBX`Hd@fEDdH@bDJpDXpDf@rDt@lDbAtC`A`DxAlDjBpC`BjClBnCbC`C~B|BdCvBjCrBxClCjErBzDjBzD|AxDtDvKhAhEdA|E`A~En@bEj@jEf@tE\\fEZpFV~GJjFDhKDxb@BxcAFlkA@l[BhDJxDRjD^tDpAlGtBnI|E`RZ|A^dCRvCNzD@hDGzC}@nQOtDCpIFnBr@xF`AxEhApDn@~AXt@`CnGnoAxdDnMf]jAzCxQdf@rLxZr@fBtRlg@jM|XpgAltClXbs@t@lB`h@rsA|IfShHrOlAjCtk@d|AbDvI\\|@vGlQ|@tChA|EpIt]\\zAhJda@vMdj@bFlRl_AbjDz@rDp@xCn@nDrAbKtIju@r@nFX`BbF~Y\\tCLp@`A~FzAvI|DlU`AlGb@fEJ~BD|BGfCQpC[bCc@nBe@dBw@jCsFzP_E|KY`AWbAa@|AYvAe@~CQvAMnBMjCCrED|BFvAd@pEXrBrArGrFnVhBtIz@|DlBpJlXpfBT|Az}@~~Fr^t~BX~AhCxMdFbUlAdGjA`HrL~w@|@xGVxBF|@Jt@N`CJbDD`D?pDCzD?vCEnIDlCFfBPbDTzBXbCV~Ab@zBf@pBnDrMdEhNtDhMbCtIx@dDTjAtDvUxJxo@j@nEvFxf@P|A`DlYRrBlGrh@zNdqAvB|R|KflAl@lEn@zD~AdHbRbr@fBhH~A~HxJbh@^fBxi@`rCRbAlGl[~@lFv@rFj@|Fd@bGPxED`BlD``Aj@`Ij@jGt@tFt@zEjBjHvAlITnAf@rBb@bDVlCdCpb@RdEXdCPvCPtEt@hKh@~D|BxL~FrUjAzEr@fFj@dF`@pFN|ARbEB~BMpGE`KK|BeArKw]vuDeAhN_@dH[hI_G`rAsAf[a@~Fi@zEo@|EoH|d@i@tDgErX}@jDsAdEoAxCsAfCwA`CwFxG_D`EgBhCaBvCyAjDkB`FmMn_@oBrEmBbEwB`Ei\\nh@eCjDmC`DkYdZmC|CiCnDoClEwBtEiBdEmBrFqAjFgAzEuGtXa@vBsGlYq@fCo@fDaLzg@uA`FmAlFmWjkAqRn{@i@nBu@hCmApDeHxR{@zB}Ll]{Yly@eBnFiAfEmAhFo@nCu@zDw@zEy@`Gs@nGm@bH[|Fi@`PCnFA~ZMrESlFa@xFe@tEgB|Mk@pDk@~Da@|Da@~EUvEKhFGjEHxENvFrChs@BdFEpGOhGYlGaApOkEdt@o@`Ho@pFmAfG_BnGiBxFmBvEiBzD{BpDg]lg@qCpE_CtE}BnFmb@nhAuAvC{AxByB~BuCnB_ExBiG|CkVrM{VxMsDvBcEzCwClCyCdDiCtDkCrEcCjFmBpFw`@htAoGhT{@jDa@~Be@zDUlDIjD@~DHhCLjBB\\HnAtDra@f@~E|@dG`AxFxAlG|AbFlBvFpBbFfC`F|BdE|e@|p@tBtDrBfE~Nh]bB|DtNr\\fEtJjApCz@fDt@`FVtCJhDEjDMlCUtCkOxsAyCzWeMzhAw@tF_AhFkAbFcM`g@}AbFoB~EmE~IiCnEu{@tiAwCbEqCzEaCrEqBxE}AlEwD`NyAlHgB~Mi@fG]|FS|FQxLE|L@~ML~MVhMd@|Mb@pIb@~H|@lL`A|KvDv]pCrWRfBrCxWnAvLPjCXjFRbIBjGE~FO|F[bGc@|Fg@pEk@bEaBdJkApFUjAg\\p}AuAbHm@lEc@~EWfFEfCD~HNdEZ|Dh@nEr@bE^`B~@hDvGvRpAzDp@tBj@|Bd@rBbArFt@vFf@jF^hGNrF@vGQxI]xGU`CcSn~A{@rGiCxMkDjLgd@loAed@toAoChKgAfFaUdmAmGl\\a@xBiEbUcAjFi@~C}BbMeAjHy@rGk@hGc@nG]bGuHppCQ|Q?pHDtHPfJNrEXjI`JlqAj@nJ^bHTfIBxHKhGC~AQ~Ea@xFo@xG}@pGy@pEa@bBsAhGwAxEsB~FsB|EkCjFsBnDsBrC_LtOuMrQmSfYgIvKqJlL_OrOqPlOwYvVkJvHyW|TyJvIgR~OsAhAuL`KqCvBgExDsErDcKtJuCtDwHvK]j@yEdJ{EdLijAr~Cs@lB}Xxu@qP~b@cB`EaCjEuA|BcO~SwUt]el@h{@__@jj@sCbFaGzMgp@p_BaDdIiBxEqA`EcA`F}@zG[bEKrDCzAApBDbBFfCVrD~@fJl@jFpFfd@tKz~@dI`q@~@tMRtELvFz@dl@FjHjDtaCHdFJjJNlG\\hHPvBf@nFr@~FdAhGt@zD`CxJpBvFtg@x{Af|@niC|AxD`BxD|BrEpChF`Yth@zYni@jCxEhCbFzOrY`@v@r}@|lBvBzEvExKxX~p@hp@x~AhFxM`BhFtArFrA~GdA~Gts@frFNfAb`@~wCPrArS~}AbGh_@p`@t}BjN~w@pDbTfCtQR|AlDh\\^|CxCvXtAjLt@nEl@dD|@vDtBbHdApCx@rB|@jBpA~BnB|CfBfCpCbDnRtUfCnDx@tA~@dB~BpFnDbK|JnYtFfP|T|o@~AvDpBnDpB`ClAlAhA`AvBpAzAr@|Al@nCl@bBPvBFfDKjC[~CgAnCqAnHaF~BsAnCgAhBi@|A[jBQtAEzB?`CLlBXnBd@nCbAr@\\jVlMx@d@bAx@|@z@|AdBjA`BrAhCn@rAj@xAd@xAd@|A^bBZ`Bv@vGTrEBrFo@lZ}@l_@Ad@iCtfA}Bpp@y@dZMdDYpE]|Di@nEaAxFa\\x`BgKxh@kArH{@zFuBtQy@fKa@bG[fHY~Gk@vQErA_MjeEWlE]fEs@rFoBvIeAnDwKhZgBvEuArEwAdG{@dE}@hF}@nHO`B_@bFIzAQrCMxEGvEFrOxBv_DVvWJrERtEZrEd@lF^fDh@vDr@bEfAhFvAjFpLda@x@xCtQbn@lCdJzf@lcBzSxs@pWn|@lBxF|EfMdBzDzEzJ~CxFpCvEbD`FdCfD|CxDnh@tl@r@v@dfB|oBhY~[lD~EzZ~e@h[hg@~@lBx@hBbArCt@vCj@bC`@hC\\nCh@~HFzC@dM?`QDt`@Bp]A|A@bE@r]GzEWhGW~E}QroBw@xF}@bFaIb^{FfW[rAcGxWmRlz@{AjG{F`SeI~WiJvW_A`D}@`Eg@xCe@nEa@vHAjFVbHf@rFrBrO\\~ENxD?zEKbF]fGOvF@|El@hQApDQrDYrCe@tCeBlJe@`Dy@zGc@dF[fFE|@SlIKpLIpEIhDS`EOfCo@pH_DbUWvCQtDClDLtFn@fKJrHOlHWdI?`HFfDLlDh@pHVzBrCtP`@zC^fGHvB?hCAzBYzKa@hLi@rLwArTMzCC|BDpCJlCr@xFxCbMh@zCd@tDRpCLbDLfIF|BN|BRdCrAbMPdCJjCBfCC|BIzBq@tHs@fHUxCYxFEbBEbIF`DHrCVzDf@hFh@~Dh@|CpCfMp@jDf@fEb@pEnHpdAd@tFl@pGt@lFn@zDbExT^xB\\~CLpCBrCKxCWvC]hCa@jBkb@n|Aq@xBi@rBi@dCc@fC_@tCsAnPYzBc@lCqA`EgAxBeHhLaBrDwA~E[pB]fCWrDGxC@|BrAvw@Tjr@PnH\\jHZbE`@dEh@hEvAlI~@lEhAlEb@vAvApE~AbEpCjG|C`G`q@|_AlC~ElAjCvApD`Ypv@x@pCh@bCZvBNnBDbCS|FM|Aw@bHM~BClADrBNbBZlBb@`Br@lB`DpIrAfEp@pCb@vCP|BJrC?|DKbDQ`DwBfZIbBEvDBxBNzCR`CVnBd@bC`YprAxMjk@n@`DX~BLlBBpCEzBOxBQxAUxAe@pBmI|\\e@pBk@nCgDfRm@nCoAbE}@hBy@zAiEdGsAfCeAfCiA`EaElUuAxH_@rBk@hCi@tBm@jBw@lB{@~A}@zA_ApAaAfAoEbEcN~Lw@t@sLnKqHbH_H~GsCfDcAbBiAvBoAtCkBpH}@nGuOrgB_BrKeHdd@QjAed@~tCgCdNuAnEeA~BiAtBoAjBmAnA_BvAw@l@}C`BqBn@}Ch@aDTy@BmD\\eEZuCn@{BbAeBhAeWrToDlDmF|GsCjEkFtK{DxKm@vBgAzDoA~Fo@`D_DbSqA`IsD`UyArJiCjSiDvWcDvWo@vEg@lCo@jCkBvH}@hCqAhDeD`HaDxEgDzDgGjFaHzD}GxBwF|@qNp@iDd@cEz@sC~@wClAwFfDeEjD_ExE{CnE}BbEyErKkbAbaCe@fAc`@x~@uv@njBkG`P}FlRgw@p~CiGzV}EpRmKjb@gBdHuT`}@cOvl@_EhPeLld@oC|JeB`FmBpEoB`EmChEgEhFsFfFqBxAaE~ByHrCoCf@mSlCmEr@yDfAqDvAwF~CkFdEeGzG_EdG{BjEsFxMkrBl~Eui@hrAk@tAwg@|mAeA`CkBtEcHfPeRtb@kHxPi@hAoc@pcAa@`AoIrR]r@oc@jcAiArCs@tBaAvCk@rBgAlEaAhEgAtGiAxIa@vEaDnf@SrCqBvZUlDk@zIo@tIo@dHgAjHiAnFaCvIqBlF{BtEeB|CeBjC}D~E}MrMaDvDcDdFmC`FiCfGmB~Fu]xoA{c@naBoC|KiBvJcy@xtF}@jJa@lHOvEE~EIjb@C~CKhYQtGa@jGu@rHiAbHkBzH}AhF}BbGoCtFkLhQoDrHaChGuA~EgAvEcAdF_AfH{]duDUhCmDb_@UzBiBhRc@`H_@nH[jHUhHK`GArCChEI`XCtBKlFc@bJi@`HgAnLwBpNuElVkMvq@}@bEmAfEmAlD{BdFaAfBmB~CsBpC}CfDqAjA}PhM_ChBiK|HyDpDkFlGcFtIqBnEwA|DsAlEqAbF{AfIq@`Gg@`GSzEQ`FGvIb@`cDDv`ANdeAeEnnBkEnnBUfSHdPp@xU~Blm@LzHJtI?fHGvHgDt~CC|GB~FVnI`@|Gf@pFl@~E~@jGdAtFjQ`{@xAvJjAbM\\tHPjIBpgADzgA@tK`@rR|@`R`@vFl]paEnAdJjAdG`k@|hCVbAdJlb@bAvF`b@jaDbBrJnAnFtA|ElUht@pC|HrChHbPn^z@hB~@|A~@pApArApAhAhEjClBtA`BpBrAbCvBhGbAxHd@xWRfD\\hCb@pBxAzDbEfKjB|EzFfSl@dEVdD?lDQrC_@~Ca@dBs@tBq@~AoAfBqApAyAfAsAh@mFzA}Ax@wArA_AlA{@xAyAlEcEhO{@vDi@tEgAdO]jJEtE@xENbGVpF^dE`@rDr@~E`ArE|AlGnBfG`BfEj[pq@bAbCr@bCvBxIfA`DlHfQ`DzHdChIpAvGd@tDZnDHvAPpDhAtb@PnFFfKGzHElB_@lI{Cx^yM``BqTbkCWnEShG?zKTrIXnErFvm@VxC`Tn_CJ`DBjDOfFc@|E[tBc@~BcCpJuBxIiCjMoCdQqAhKcAhKq@~Ig@lJ[nISxIKxHAnILl_CGbQe@pYa@hMe@|LSfE}@jO{@pLOlBmBbT{BvRgyArtLQvAgm@r_Fm@jF}BzR_R|vBuBhUObBsAtOsGft@_CzPkBnJeDnM{Yx_AcApFSfEFjE^xF\\bHCdEuA~OkDb\\ChEX`D`AjE|EzPvFvWvBbNzBfR`AlLr@jMh@pNXzSPfb@DdKTbE^bCdAxCr@tArDxEdBfDr@`CT`BF|A@pAKvCW`B]rAi@dAaBfCu@n@}@d@yCx@mBr@gAp@iAfAw@lAc@dA_@rA_@~BKrCBlBJlBx@zFj@rEv@bGJ~BAfCQfCa@dD_@vC]xDMnCCtDJvFbAzNpA~Q?nBKrBYlB[dB}@fDiLdd@i@|C_@xCgF|l@SrEEnEDxCr@~MDfCEdDO`DuAzRc@hIGbGGpTK|Ek@pKsC`Zq@fJqGluAS`CWzB]fBy@~C_@nAgKrWy@rD]`EC~DD|Aj@jE|@|CtDfH`AbCf@|B\\tDDpBCfBWrDiAbGa@dCWtCGbER|UKbCW~Be@dCg@tAs@|AuApB{H`KqApBoA|CsB~Iq@hBy@~A}@xAoAhAmBbAmF~A}@d@q@d@yAlAiA|A{@fBmErNs@fBsA`CcAjAsAdAiQtL}ElDyArAqGlGmBdBsBpA{GpDaElC_BzAsBdCsBjDwFxL}BdD_BhBcDtCoC~AwB~@_|@v[_s@nWmGzB{DdAuEv@eLvAuTdCiARyA\\aCbAkIdEwDpBeBdAs@l@eBbBoAbBiAnB{@rB[~@w@pC_@hBS|AOjAOlBKfBC~AAfGFrVBnAN`EV|CVfCrChOh@`D\\vCTxCBpDEnDQzCc@|Ci@nC[lAm@nBaAvBoAxBqAbB{A`BqBxBcAnA{@pAgAlB_BtD{@lCc@hBq@vDmC~P}CdQeA~E}]pnAaAfEg@vD]nDK~B?hDC~\\?|B@x_@HrQ?`FIzTKhEYbEg@fDwG|\\q@`DgAjDyAxCuArBm@p@u@p@aChB{CnBgF~CwChB_GvD{DzC{BrBsBnCuAfCcAtByAxDeApDaAvE]hBWlBW`DKzAC|AC~Ag@pc@IpD_BnmA}@vw@WrSg@dQExAy@dOm@xIsAxPoAhPmAjO[bFUxDK~CKvK@nCFhF|A|c@PhEPhF`FfuAHnEB~FKlFe@zJkAvSiJzmBwAnZW~HMnGEfICfF?|BEtzAClGMvDY|Ce@zCc@hBs@`CeAnCeB`D}_A`xAmFzHmDfDcEnCqUrMqD~A{DlAiEbAoDh@iOdB}En@qBf@{CnAgBtAqBxBeBhCuIzQkCpE_EhFwF`HkEpFmJrNyGzLeIxO}FtKyA|CcB`Da[ph@op@xhAwAbCyDvGgI`N}MfUeEtFcCtCoDhDyFjEuElCqF~B{ExAukAfYy^xIi\\|Hgs@~P}KfCq`@jJuDx@{CTsC@_E_@yW{Co@G_~Fwp@aGy@{JmB}EuAwEyA_JqDiPaIgEiBuHmCgEoAgEeAyGqAyKoA}BS_FUgDGiFCuHJcDByDCwGOeF[}Fm@cEk@mE{@oDy@wF}AkkAq\\i@QcrBok@mK}CeIyCwEuBoEcC_F_CcFyB{LoEiA[qD_AuFw@aM}AgFm@qDk@_F_A_FmAct@uSoQiF_FcC}EqD{K{LiD}DsI_I{EuDuDaCqIgEaHcCqIqB}FaA}Fe@uGOkPPsu@~@yHGmrDcOcACicIu\\gFSsDa@yCy@aCmAaC_BkBiBeB_CcFmIy@wAoX{d@{HkMcE}F_AgAqE_E_N_KeQgMeGkDuHiDmGcBoFmAcI}@kCKwACwG?sHb@eHbA_E~@{DhAqEfB_F|BcOdJ{BtAoDjB_F`BwBf@gAPcF^gFAs`DWmRIsT@q}CY}Y?mo@jBeG\\wB\\wBl@mBt@wC`BoDtC_OpMuFvE_QdOoCnCcCpDoB|DiAfD}FtTiAvEaC|GoC|FwGnKuBjEeCvGeBzGy@rEq@zEs@rKS|Lg@|_@OpG]lGcB|VkDbf@s@jHaAjGyAtGwAxEaBlEuRb`@_BlDyApD_@jAc@~Aw@rDQlAa@hDaAbM_@zDa@fCUfAq@`CaAnCqAjCq@pAoCjF}AdD{@rBuAxDkBfG{CfKaBzE_BhEeC|FeBpDyCvF}AlDs@dBkA`E_@~Aq@dEQ`BKlAIbBQhHOzJStEMrASxAm@tC_@pAe@pAg@fAaBpCcAdAg@d@uChBsDdAeBJse@`@{CVoDbAgDfBsC~BuCbEcCpFaA~Cu@xD_A`IsMj}AQzAq@jEYtAeAfEmBjFsAnCyAdCsBnC{B`C{o@ro@gD`EwCrFwApD{AbG]|Aq@lEUhBOlBIjAOlDEfBG|FCnCYhQCnDCtFGjGUvEk@|EmAtFmBtEeAnBqAdBmBfB}{@pq@uDlCwErC}E~B}GdCyS`GkE`BiCtAmCxBy@x@kBtB{BrD{BlEwBtEqAbDsEbMwB|GuBrHaDnMiDlPiJzd@iCdLiI|ZgGrUq@dCiBlGgBlF_AvBeAhC_Ure@mCtGaBpF_A`EcAvFs@jGgAvPqE~v@k@~HiAfKmAjJ{Y~mBgAjIa@lG?hIxFbiAXdJBrGM~HYfMm@~TCzAw@p[QvHQxFS`Ew@jJs@fFcAbGmAjGmD~OoW`mAKd@_k@vjCeCfJ}EpOo~@hrCaGdPgk@zuAw[dx@sGrNoFrJwCvEu@fAcI|KekAnyA{BrCyBdC_A|@}ExD}@z@{@~@_B~BuAbCkArCuCpH{@`Bc@n@cBpB{FtFiAtA}A`Co@lAcAdCa@hAs@dCo@vCe@xC_@xDQdEEtC@zH?bBA|PGlDItBY~C_@dCUlAu@bDoV`}@oBfIe@`C]lBeAnH{OtjA[lB[~A_@zAg@nBwA~Dk@nA}AzCgBnCo@t@iFbGk_@va@gW~X{J|K{AnBg@v@oAbCaAdCy@zCs@xD]jDItAElACdDFvEnAls@NnJ@~CIjHGrCMzCOnCQnCWxC_@dD_@xCa@nC_@vBe@dCi@fC_CbKmCtK}A|FcEvNmAhEg[tfAiCnIsBpGsZ||@q@tBw@zCaArFe@~DQrBUvD{B|h@MfBQvBSdBU~AWxAq@~CgU~}@YrAg@xCOlAIpAIvAErA?nCBtAPxCLrARxATrAv@bD`G~RZfAZ|ATjA\\tCNvCBhC?hAG`BW~CQxAe@fC]lA]fAyEjL_AdCc@nAWdAg@bC_@rCS`DC~@?|CJ|CF`Ab@dDRfAZrAX`At@tBdCnFfa@`{@h@hAbBpDzAnCtArBbBjB`BvAp@b@jJnFlAv@~ApAj@h@|@dApAdBv@lAlAdCt@`Bza@reAl@|Aj@bB|@`Dp@xDNjAXfDNjD@xA?hAIfDUlDMlAg@dDo@|Cq@tB}@~Bo@tAa\\|m@cBbDsAvCs@pBQt@WdAo@nDYdCS~CC|@AbDFnDFhAPhBd@dDb@xBRz@r@dCl[fcAnAvEhAnF`@`Cn@pEl@dGdOhdBV|DFrAFpD?`DCpAKxCKzA}Cv_@gAhMq@~F]~BeAbGgAtFw@pEa@lCYzBg@jFMxA}@rPy@dPs@~N_B|^]vGMpBMvAMdAe@fCk@vB]bAy@nBmHxLoA~B]v@u@vBi@rBa@pBWrBWlDIpC?vANnJ~Ahr@LdDJxAHlA\\tCPlAp@fDv@tC^fAd@pAlArCdVne@~AxD`A~CVhAf@zCNhAVhDHxC@zCGnCOfC[xCa@bCi@~B_@tA}@dC_Vll@oS~f@}@rBu@vAy@rAs@~@aAdA_CfBiJlFkA`A}A|AeAvAcAfBk@hAq@dBgAxDa@lBQhAOpAWpC[nFoA`X_@`GOzB_@xCe@zCo@`DoRf|@cA~E_AbFmApHm@fEmQdvA_AhI{AfP]vC{QlxA_AnHg@fF[nE[`GG~AKvG?~B?rCNrQx@j|@BfHCtPmA`}DI`GYzHS`DcIzfAWtD_@vGQbFEjB]rp@IhYMh\\Oja@?bEFpDPnE`@pFj@zEd@xCzB`M~@|GRfEFbDSdm@KpEU`E[hDs@tE{@pEqAfEeBrDaCnDeDpDiC|BuDxBmD|AgEdAuMvCyJtCkGjCwy@z_@aFnBsHbCoGxAeCh@aLfB_gAxPyGp@gGZ_^bA_I`@_Ef@cAReDx@}C~@cDpA_G~CeDvBiDrCoClC{F`HkBrCcD|FsCfGsAfDiAzDeClK{Kxl@qJrg@c@rBgAxDc@rAm@xAmGdMcBpEk@xBWnA]vBUpBQ|BWvEAdBB~B`@fNX|G^pIGrGa@hGy@pGcBbHuUrv@uDfJ}CnGwZnk@k@dAeXpf@mOpYiVdd@}eAfqBkDtHq_@v`A_EvJiErJe@`AsErJ{EjJyb@`y@kCzEuCpEgj@bz@oJxLs]t_@{@~@sB~B_D~DwCrEmExIyAjDu@pBmMt`@o@lBcLt]iIzVsBrGoAxCc@~@gB~C_EdG_DvEoCxDoDfFcH~JiCnEeAzBaA~By@`CeBfG_@bBo@vDUtAg@rEWbDWtFGfFAlAFpFDnATtDNnB^hD\\nCh@lDZ`B`A|E~B~Lf@jCdJhf@vRlcAdB|IxK|k@hF~Wx@lElA~HfAhMp@|F|@|Ez@fDx@nCnClHx@fCjBjHrAjHj@bER|B`@hFRbFDjCBdGCjBQnHg@zIgAzKiBjKcCnJwBbHmCjGaEvHcBjCyJxOoAnBwGdKCBoBzCmB~CwEzFyRbTgOzOaBrAwA`AeCpAkElAqBd@_Cl@aCr@uDbBiCxA{C|BmBhBiBtBoBpCkClEwA~C_DhIyOtb@{C`HuEhIiFnHkGxGmApAuG`HaKnL{FvHuF`JoIfMmLdR}FxJuMpSiIvMq@lAiAxBuCvGiB`FuB~GkBjHq@fDeA|G{CvTaEzYu@fGsFhf@eBpN]xBeAfFg@zB[dA{@fDqDdLiE`Ks@nBaLbYs|@v{BaC|Fs@fBeAvCyAbFk@dC}@vEo@vEU|BwCn_@aArJu@|Fy@xEwA`HkB`HiAhDy@|BeBdEsT`e@w@`BwItQuAxCqCtF{FfMuDtHcVng@mr@~xAw`@xy@uKlU_BvCoCtEuDtEoBnBsCdCcg@f_@}AxAeD|Dm@t@}[fc@}M`RuMfQyN`SsUj[mCnE}ChGwAdD}A|DmE|MoAfDsBdEiDnFaBvBcOxQ_F~HqB~DqBrE}AfEaBhF}Prl@eBrE{CvGqD|FaF~F{C|DwCrEyBjFaBpEaB~FoAxFs@dFy@dIyBrz@c@dKo@bM{AnQ_BzMe]~|Bu@~Fa@nF_JxgBGz@aI~}AUhEm@nHwArKaD`PgCdLgCjN{CrScCrVe@|Hu@xQm@~Yc@hUAdINbGf@jGvA`InOdn@z@vBdBrDtArBxC`Dhg@j^~BtBfAnAxBfDnBvDdAfC~A~Ex@tDVzAn@fFf@xGFnDAxFKdDe@dHgAfHsIr^mFbUyAfGaAhGa@fGA|FRdEd@|Df@jCx@fDzArDrh@hkAlCtFjAvBrApB|ArBhBhBzBpBjE`DbFxBfCt@bCd@~GjA`LxAlDp@vCbAzC~ApCtB|BzBro@jz@nBvCtAfCdBnEnBdHfAlGf@zGLzGKdG[xFyAvLoBdNaFr^Q|A{N|eAs@rFqA|HqBpI_Lvb@iAfFmA~H_AxHq@bIYnGU|KBnLDpKMdFg@hGcArHsAlFaBxEcE|IiAlCcSjc@sDjH_BvCaDtEuCjDkDrDsD|CyHbHoEjFqFnIcEnImBbF_C|GoBfHgBpJiBpLqE~Zg@jEe@vGYtHAvCJbIdB`h@TxCZfCz@xE|@~Cv@tBfA|BzBjDlDvDr`@ra@za@hb@nBnC`CnFlAfEbAnGb@~FFnHI|xA?n]CjR?vJ?zCA~FOpG_@lG}@zGqAtFkLh^oElNuAbGsAvGgAdIcAfJsk@|oFcDvZkC~UeArKK|EGnGEjGEpDKlSAlAAlDBzAFrBb@lEl@dDlC`Lh@fC^~BRzBLvBBvBCvBGtB]tEu@~IiBzVItFNlFh@hGlJns@t@vDpBzHzAhEvDhJnAdEj@xC^~Ct@xR~GnsB@vFMrGc@hImAfKkBrIkKx`@{BlFqChEuDnDgDnB_D`AgO`CgI`CuIxDuEtC_Ah@{MbIgvApy@_d@hXyGnF}MjLmTxQ{FrDkHdD_EpAsFfAeDd@{[jDwHn@cMxAcE`@a\\lD_C^}Bp@aDbB}ChC_DbEkAzBcA|BoAnDaEzOoAvE}Khb@cAhCeAzBmArBsAxAeB|AkCrAmCz@kD^y`B~KcUzAeAHmXlBsDl@wDbAiDfA_v@t[{l@vWaKfEmAf@y@f@aBnAcBhBi@r@iBxCwlBx{DoaBzhDgEhI_DzEoClDoKtKoJjJaKpJuDbEgAtAsFpHgIdMci@`x@_GvJyEbKyAvDwCrImC~I{BdK_@rBcApFs@|EyAxMkJj`A{AlKsAjGmCjK_P~g@m_@fnAeBhEuBbDkBpBaBlAgAn@iH~DeDhBoBrAkBdBeBrBoB`DeBbEyEbNiEjKmCbI_ErPmBdKaCtSu@`Gu@~D}A`GaBjD_G|KwKdSoHzMgL`TcBpDu@zA}CrHcDdJ{CvIc[p~@{AhHg@vEUfFAlDFjD~Afc@\\fIr@|GdAhFjAxDhCvGrAzDlBnIz@vHRhGCpHi@nIkAtH}AtF{@bCe@nAwA|DuJjW_FrMyCvJ}B~KuAfMe@pHQvJy@tdAYnHs@~FaApE}B|G{A`DoCvDsEzDsEzC}E|BeEtA}Dv@qFf@sCFqEIqLoAmMiAaFYeA?oJDcT\\gGNeFh@oDhAoE~BcFpEmQtU_QtT{MfQgTtYwv@rcA}KhPaGlKiBtDg@dAuDfIwDnJgHfQ}CbHqHbRqA`DwCdHi@xAwEnK_BfFmAfFk@lEu@`JiC~a@g@`MWvK[`x@EfQNhFb@fGv@tF~A`HvM~a@fGvRxJla@v@~ETlFCzFY~DcCfSaAxHeBjM}@jJWjHMxGGnEYxEkAnHq@~BaNff@yDvLaCbHiArD]vAg@vC]tDMtFGfEEzC[`EiBhMsAhIOfAMlAMnEHtC^jDfCbQLtADpA@tAE|AMdB_@lCUz@Wr@[~@s@lAiBzBgLdNwPvR{AzA{ApAmA|@eCvAeEzB}@v@w@dAq@nAk@zA]rAOv@Kj@QhBWnGU|FU~Ey@pJgA`LQ|Ba@xFSzEG~BMxKAtCFpDHvAZtEZnDJ|@dAbG\\hCFv@Dv@@dACx@IjAQlAKd@_@pAm@pA_DrE]p@u@nBgA|EoB|JoBnJUx@i@zA]r@eAzA_A~@qAx@_Br@yB~@wBbA_BdAkAfAqJdMq@`AaArAi@l@cBtA_Ah@mBp@w@P{B\\}AXkBp@}@v@e@f@Y`@s@`BSj@Qp@QbAQ|AEt@EhIKvBKx@_@hBc@hAm@nA}@bAWTo@ZkAf@wAd@gBn@uA|@YXw@bAiAfCi@zCKnBCxB@|ICbBEh@WjBg@lBc@hAk@z@uAtAuB`By@x@U\\Yb@g@fAWx@y@tCy@~By@rA}@z@_An@YLu@Rw@BuFUkADk@Hc@L_Al@a@\\{@fAWd@_@|@Wv@sAxE_@fA}@rB{@pAc@f@c@d@mA~@}AbA{AhAaA`Au@bAmApBYn@e@xAe@rBO~@WlCQ|CKzDW~OEfAMzAKdAo@hCmA~CcJfQqArBiAnAg@d@a@VwAv@e@RuA\\yAPiGLmAHyBb@wBv@o@Z_An@gAz@a@^{BrCs@pAw@zAa@bA]dAgApDqC`Mq@vDU|AyNviAe@hFc@hKObEU`Dg@hDi@bC{@tC}@~B}v@xlBgEpKkF~NyFzPkBdFgBdF{HtRg@nA{J`Vw@`Ci@rBYvASpAY~COvBGxC?jAH~CDfAHfAVtCnDj[lFze@|@tHnBfQb@lEPxCApCOfDm@~DcAdDi\\jx@eIdUyCbIkDvJ_DjIa@lAwDhKsCtG}AxCw@tAqD`GeDdFeBhDo@xAo@hBc@vAu@rCcAzEoH|b@{@vEcGp]cAhG_@bEWlEGjCCrV@~FEnHMlC]jE]hDGlAGdAC`CBvANvCxBlTL`CD~BA~@WfJCvBBxBp@|NBrABbCGlDSvCGv@]~Bs@xCu@dCw@fBgAnBeItL{@tAcAfCi@rB}AxGu@nBQZk@z@qDrEa@j@u@rAq@lBWnAUvAUvBMvBGrBA|CDrBJxBb@tFJzAD`B?pBEr@Ej@Y`CYfAe@rAm@pAOX}@hAeCpCcAzA]l@kAlCe@zAg@pCQrAMzAKzCGrGGpBOtCQvBUlBoDrXgAfIy@pEkDhOw@`EWrA]~B[bDSnCIfBGjC@jGLjE`@`IJ~CBzCCbAExAKxBQnBOdAY`BkAbG[|AOz@yDxUSxAs@jEoChNcBxIe@zBaAjDy@`Co@~A}@lBwI`Pe@bAm@pA{@zBu@zBe@~Ac@hBk@nCgLbk@c@lC_@bDWtDI|BApC?jBFpBFpAXfDd@`F\\vCjCxWRjCL`ED`D?~AKhEUnEmCza@EtAAdCHjDXrDt@|GTpCRzCPnDJfDDhDBvEFnDPbFJbB\\vDJ`Ab@pD`AbHRnB\\rDHnALzCDvB?`ECvBMpCeBnRS`DAz@AzBDxAHxAHrAl@nF`@jEHxA?xBExBOzAY`Bo@~B}@rB{C~Fo@nAm@fA}@tBWn@Y`Ag@`CShBQxCCxERtQ?zAE~BMzB[vCWtAi@vB{@jCu@dBy@~AgE`JaAhC]rAYrASbBOhBAt@CjBD`B^pDRfAhBxHdD~LtBpIrA~EbBpGXbA`@pBVfBLlAHvAH|DEhCMdC]zCm@bDk@lB_Kh]wC|J_BnEg@fAeBvD}@bB{AbC}BdDmC~C_B`BgBxAyB~AmKnGsB|Ag@h@kA`Be@v@u@xAWn@q@xBs@xCStAQvA]nE{Bj\\[hD]fCi@xB{@rBw@vAy@bAgBbB_DfCi@j@q@v@a@l@]r@s@|Ac@|AYzA_@zCI~A@tCBn@NfBNjA\\hBr@|BvApD|AjEPl@^pBL`AJz@\\fEz@vNRlE@fBClBMnBMjAYpBuAfGo@jCcJ``@y@rC{A`EeB|DcBxCmAjBk@r@wExGsA`Cq@zAs@fBuDjLsAxCgAnBwBrCiAlAiA~@qA|@wNrIoAn@{Af@cB`@kCXkLRqCLgFj@eE`AkHvBmBd@mB\\gBBcCW{@U_A]oAu@}B}AiAc@mAUiAIiALmA^_Ah@{@|@y@pA]r@[`AQp@YnBGx@WbLIhBc@nEMfBEfB@|BJnANdAbApFX~BDr@@v@?p@ExBg@jIKxEJ`CHv@\\`BTz@pAfDb@|@ZdANf@ZjBNlCJpEH`BRdBh@jChBvGZtBFx@DpBEfAS~Bi@hD[xCEfBBx@NtBb@~Bt@dCh@xAXbANz@LbAJbBAnBC~@KbAMv@U~@k@|AmBfDw@~AYx@Sp@Qz@MbAEr@EfB?v@HjBf@tFFdABv@?`ACx@G|@K`AQv@U~@Wr@c@`A_CxD_@t@Wp@Wv@e@jBSbBK~BE|CAtFIjDIdAOjASbAQt@i@dBk@|AoAdDe@vA[nA_@rB[pCGfAGnCe@p\\EbBEx@S|Bc@lCo@jCa@hAg@lAu@pAe@p@aAhAiA~@}DtCyA`BoApBo@rAe@rAc@~A_@jBWvBQlBG`DBvBLxCNjB|D`b@~@|Kb@xHPvEJ`GNpPApFGnIKjHI`Ce@bLa@vHe@|HSpEGfBChB@vCD~ARlDNdBTdBr@|D`@fBhApDl@xAl@pAp@lAv@jApA`BZ\\pFfFXZz@p@|@v@x@|@v@`Ap@lAf@xA^~ATdBNbB@r@AjBU|CObAUbAUp@m@xAkBrCw@dAs@hAo@nAk@tAa@tAYrA]bCEj@G|AEzBFhBNhBVbB\\~Ad@xA~@fCjBhEl@nAr@jAv@`A|@v@vFnEb@d@n@`An@vARn@^xAHp@RfBDlB?z@G~AQdBYbBc@|AuJd[a@|A_@~AY`BUlBKp@aB|L_AlHeAlH]`B_@~AkBpG_@|A]`BW`BgA~Io@lFUbB[`Ba@|Ac@xAk@tAkArD_@~AWbBcBxNc@jEOfBKhBAhBBjABh@RdCf@fEPfBFjB@fBGjBOfB[`Bc@zAk@rAmAnB[^c@^]TwCfB}CrB}@t@y@~@q@jAm@rAm@rBShASbBQfBqAlUMhBmBd\\Cb@UnEGhB?fBHhBRbBZ`Bd@xAl@pAr@fAlBfCp@jAVl@\\nA\\nBFt@F~AAz@GbBWvBMd@i@zAk@tAm@nA}H`Qi@vA_@|AWbBMfBEjBBjBJfBPdBb@vDHl@fE|]h@jELfBDhBChBMhBUbB{@`Es@fESbBKfBChB@hBHhBPhBX`B\\~AnA~Et@tCj@tC^lCPxCVbFLdB`@nCx@|Dx@xETpBLpB?|CCbAIjBIp@YbBQx@u@~B[r@o@vA{C~FcAxBUr@s@fCoApG_@|Bq@pCSp@e@vA_@z@iBfDkJ|OeAjBmEpHoAxBy@xA}CbFyVzb@gBnCyErGs@hAo@pAg@rAc@zAyAzG_@~AQj@k@|A_@v@gAjBk@v@oCfDe@f@eAvAyCtDs@fAYj@m@pA_@jAQp@Ov@WdBOtBE~A?lB^zKl@jOtAd]HbC@lCAtCChBWnEc@lEu@dEaA|DkApDwAfD{A`DwCbFu@fAmBdCqB~BwBtB}@t@qRhOyBjBwBpBuBvBsB~BoBbCkBhC}CvEcBvCmCjF}A`DuAhD{B`GsBlGmApE_CnJqAbHq@`ESnAk@~Dk@lFk@dG[rEM~ASdEUdHOnIc@lYOrEIfBOfBe@jEYbBcN`u@YvAy@dEi@|CsAbH}A|G}AdGiAvDkArDiBhF_AxBqA~C{A`DoClFo@jAsXbd@qE~GyEpGy@bAqNnQk@t@mLzNuAjBy@tAgArBk@rAi@vAe@xAa@|A]~AY`BUbBSdBYnEa@vH{Bhf@i@vLMxHAtE@hBNzHRnEZpENdBd@jEdAlHv@`ElH~\\x@`EVbBRdBLdBFjB@jBEhBIhBOdBUbBY`B_@~Ae@xAg@vAcA~Bi@rAeIzRoAlDc@zA_@~A[~AWbBQbBMfBGhBChBBrE`@lOHrEAhBGhBKfBOhBi@hEcEh[iCjR{@hGYbB]~Aa@zAw@xBm@|Aq@`B{HpRg@hAo@~AuAfD{AbD_EzH}BxDsDbGoBxC{KlQuC`FyAbDi@vAcAnD_@~Ac@xBYtB_@pDQtDEtACrFp@hxAHfL@fBR|H^bLt@vRvAr\\hDl|@PlIHxKApOYrp@Yfw@SdVe@lOeArRoDrl@GfBChB@hBFnCRvCRdBVbBZ`B`@|Az@bCzBlGjDfKpBtFhBpG`AzDnAdHVbBf@jE^lEVpENnEHrE?hBAhBWpEQdBk@lEgAlH{BlNiHx`@kGz]mAjHaBtKyAvKiC`TyBxQWbB{Fxe@{A`Mg@jE]nEUnEMpECfBArC@hDJpENpEJfB\\lEd@jE~ClX\\tEXrHLpEBjB?|HO|HGhBs@lOWpEGhByAlYQtEEhB?vEBjBDfBTrENfBf@jETdBZbBZ~A\\~AdAvD~FhRx@tCj@bBp@fCt@zBf@pBf@`Cd@xCXvBb@nFXxGFtBLzDDpB^lJ^~Kv@dWDhDApAQlFUxCa@xCi@pCo@lCgEpOiQ~m@gBzGiBlIkBfJqAzH}@vFwAdLeAxJe@zFgBzVe@`GgAlLmAjLeAtI}AfLcB`LmB~KeArFqCfNkAnFoAlFuGdW}Mfg@wA~E_CbHsDzIqDxHiGzJaCfDgC|CkCvC}A|A}AvAmC|B{[jVyAlAuAvAi@l@sBpCgApBcAtB{@~B[bAu@jCWfAi@tC_@~Ca@nFK`DAbDB`DVrFZ~CNnAf@xCn@vCv@pC`AhCvMd\\Zz@dAfDr@rC`@|CJnAFpAHnEGxCQdCa@pCUjAyFpWgHr[mRh{@wBbJiB~GuBjG_CxFmEfJsKzSaAnBkCtF{@`Cs@jCi@nCw@~EUfAUdA[bA]~@a@x@qCrEeAhB{@rBm@zB]hCKlCDlO@`FCzCOdCYxAWjAYz@c@`Ac@v@g@v@k@j@m@`@q@^w@Ru@Lw@Bw@EmB_@wEwAy@G{@Bw@Fu@Pu@Vs@`@o@h@k@l@e@p@i@z@c@bA_AlCYv@gA|Ba@v@i@p@k@j@{AjAu@f@sXlRwAhAi@f@mA`BeAjBc@tAYrAU|AKjAEjAAfA?jALnCRvBb@nFJrC?fAEhA]dCm@|BYz@m@hAy@jAi@d@sA|@mGlCqAz@kArAa@n@]r@Yv@m@xBQ~@K~@m@lLg@xEw@~C{@lBcBjCe@h@mAdAsAt@k@Rm@N{AN{AAm@Ek@K{A_@wC{@wFcB{AU{AI{AJ_@Fw@XuAr@m@f@s@v@g@n@o@bA}@nBuA`EoA`EkBjHyAhGyAfHiAtHy@tGgAdLk@|Ha@`LWdKOnJCpH@|HRlTL`DPxBLfATvA^tAtFnRl@nCNdAXhDDdCAtAElBOrBUfBSnA]tAkD~JgA|DYpAOfAKbBIbC@tIEfFKtB_ApIUxCCxA@zBTvCN|@f@jBn@`BjApBpEdGxB|Cd@x@`@|@^bAZdAj@tCLnAP~C?pAQ`Dc@xC{@pCgA~BeBtCyQlZcAdC{@pCWjAk@nDWxCW~FShDKrA[bD]fCiA`GgAzDaBtDuDfIcAbCaAnD]bB_@rCYvDMzDKxH_@jVG~F@~BDnAVxD~C|W~A|L|BhRL`AbJjt@jAzKtErd@pElc@lBxS^nGT~GHtFAtIKvFUdICdDBvC^jLDfD@pFKfEWpEOlB_@hDSpAaApF}DtRwF`XkH~]}DzQeCvKu@nDSlA]hC_@vDs@hJc@vD{AvJYtCGrAE~B@dBFbBP|B|@rHJdAJvBBv@AvBKnCWnCyCdV[~B[|A]pAq@dBi@dAm@|@w@x@sA`A{An@{@PmAHc@@qL_@{@@eBXaAVe@Vy@d@iAbAs@~@m@fAs@`B{BdHUj@q@zAy@nAc@l@c@`@iAx@cAd@_B`@iGhA{Cd@s[lFwE~@mA`@a@TsA`A_A|@}@lA[j@iA|Bq@fCSdAOfAMjAMxCEzC@hA@tCAfCEpBMfC[nCi@fCY|@]z@cAhBe@n@g@h@i@b@k@^qAh@}Cl@qIdA_H~@_BXg@Ns@T{At@m@`@uAlAmA~Aa@r@_@v@u@~B_@zA]jCIhAE~A?dAHjC^dE\\tEFnCEnCS`HCrCBnCl@lLHpC@vCIvCGhAS`CSvA}@`Ea@pAg@tAm@nAuAtBy@~@w@v@cBdAmAl@u@RkAN}AHyS^iLXmBHsBVu@N_Cn@mE`BeAj@oChBcAv@mBbBeHpH{@v@_A`AcYbXcAbAgClC{BzBsU`Uy@v@sQfQaEdEyBdC{BvCqD|Gc@dAeAlCiAdDq@`CYdAaAtEg@zCu@nFoEte@_@hFi@`IUjEg@pMgAzn@_@lUUjJMzC]tH_@lGwAvQkCbZ[nDOfBmHjz@yArOMxA{Fle@iApIcAlJ{@fHeDlVyHbn@W|B_B`O}@lKe@hIKrBW|GMnEM~KGfuAIvbAC|BKtE]nH_@zEWnCq@nFs@pEUrA[dBYjAuBtLiAnHy@lHq@lH[dF_@rHSvHGhFA|CEb`BA|lA@fUEdm@?jDClNMjEI~AMrA]fDiC`Qa@bDMpAYdDOfDIfDArA?pADbDDpA^rFZ`DzFde@x@jIz@|KpAnTlCfg@pAzYx@hVn@vXL`GP|FFtA`@zF^dDf@`DRnAfAjFpAbF|@pCtEpLfOd`@fEhLnArDbEzM|DlOjDrOxC|OXvAPnAzBvPp@rFz@hIt@nIlCx_@l@zIxB~Z\\bEZtCNvAl@hEnApHzAdHv@vCtQvn@hIfYfKt^xQbo@tNbg@nBlHbAlEfAzFr@zEl@xEf@fF~D|j@`@pDd@~Cj@nCp@pCx@hChAvCx@fBpA|BtArBtAbBrBnBzQzOhCtCnBhCvA|BnA~Br@~A|@~Bz@dCdAfDl@zBj@fC^vBb@pChK`w@tCfUNvAXxCJfBJjCDfD@hdCAjk@?phAAhNIzKIlDc@pIYzDa@nEe@zDqHhn@oBrQ_Ej\\e@vDsD`ZmCpVoHjm@{Dd]m@xFQ`C]`GM~DEhCEzED|JRx^h@b{A?vJElFG~EMnB[|KQlEUvE_BdYYnHYdKMbLAnG@`GTnOZ|JZhHVjEp@pJdAjLlHnbAfAjMx@vEtA~F|Nvd@jLf_@xFhQhMl`@xCzGz@dBjAxBhApBnBrCp@bAjEvFjCpCf@b@~H|GfB~A~@v@pAvAr@`AfBvCpAtCr@|Bb@fB`@rBd@jDVdEHzDCr[CzBGdGAbPE~Q?hX?tEAtA?`B?xZ@tBQdyA@hMDdb@?t@@lg@@jR@xK@pCDfCH|ATbCb@dCbAdEx@|Ct@vDX~A\\dCH`AJ`BFzBJjU@rTEfEItCo@tW[rPU`OCvX@lGH`h@FbPDlC^nFdCxXr@rGlE|]`AtH~@rFj@rC^bBt@vChAzD~BpHfB~EpFfPxFvP~FtPzS|o@vI|VnCjIpFhOlDvKbCpGvT`e@`@z@bAlBnQp]|Y|k@tYfl@fNpXfG|Lv@dBnCrGbC`Hj[deAvGbTzcA|gDjKb]`BnE|BvF~B~EfCzE`A~AfErGnDtEjE|EdvAzyAxTzUhGpGbNtN`AlAdAnApElGdBtCtAxBxB`ErApCnAvCzBvFlC~HvEjPf@dB`HxVb@xAfBrGdCnHfC|G`FrLbGxL`M~Sv^rm@jMjTfnAzsBlD|GjDlItJfXzDzJvDtHxBbE`CrDlRtW`InKbk@jv@jFjInm@dcAx^vm@zEjIrm@fcAjZjg@nYre@fp@ngArwA|`CboCbrE|AhCbBhCtG|IbT~Xjf@ho@rG`JlPhWpe@ln@vg@nq@vh@hr@nJrLzQrSrBdClFvH`FhIbDbGhH|NrFfL~u@v}A`EvHnEjHb`A|uAzIbLjKpK`_CjyB`XbWzDlD|ExE~AdBbJlKbHdKtHzLbHtNvF`NpcCd~GlGvPpI|Ut@lBxCvI|BrHpCrLpAjGh@zCb@jC|@|GxJbx@nEn]z@|Id@lGX`HFpCFrGA~H[tTAzED~HFbDNpETfFVjD|@bKzAnL~@hFtArGfB|GtDrLZv@dD|HzA~ChApBrAbChAdBxV`_@xAjBxCnDz@~@pHxGzGbHvCxDpEpGbAbBlCbFvExJrC|GbLrX|BnFlDdHtBfDdBxCjEfF|GdH|EtEfF~FhErFrJnNfZxc@pJlNnH`LlClE`CbEhBlDvEbKjDhIhDxJtApEzCnKxCfMz@vDjB`K|L~v@lAlGnAzFdBxG|AbFjDnJlB~E`C~EhFvJhBfD`ChEnBnDvBjEjAnCzAxDpArDvCdJhBfHdBhI`GtZzSldAlNbs@xAxHhBxIrw@n}DrXfuAxDdRbChMtDrQ~a@ptBtGx[zBnJnAtElCbJdIzT`CvFlBfEbCtEpBjDb]~j@bx@|pA|@|AbUn^lPhXfWva@fXtc@|m@pbApEzGzU|_@h\\hi@xEpHpLrRvbAx_BlpAbtBpq@lgA~]fk@~FnJrIlNvApCbArBz@hBhDfIbCfHfB|F|AnFz@pD`BdIx@vEtAfKvAhMR`CVjDXzGNhGNzHDvM@`DJz{@PhbAH`cA\\zeBKnXeAddAC`a@`@lvBNhfAHde@?xAHlm@|AnwHKfQWrJ}Atc@SrICvJBbLJpEXxHn@bKXzDZxChA`Jl@fEdAhGpAlGlA`F`S|t@pMze@lCrKrAjGfBrJXdBpAjJ`Ed]pQh}Ar@rIp@|LZ`NDtJcB`uDUzf@AxCUbn@ApHHtIX`Jj@rLbArL`C`QzAlI`BlHbg@rrBlBlJ|AfJnA~JhA`Nj@jLTbOTrgG@fB?xi@XduF?jBF~yBFnQBfHCpl@WrRqBjx@Q`Ii@p`@G|b@Kvf@?tCGx_@AzBAhJeAbcA[~ZE|Gn@duA?tMChRA`CI`q@F~GXnJ`@tI`HpfAz@vLbCba@ZvGNjHHnM_@j\\IfJE|GDrI`BtlAB`LGhGQdNEvByAndAe@j^D|w@An]CdEArBaBpgCu@lfAi@dy@_A`aBBhVDfQAdQuA`aCOnQOjIwAp^cDdx@aD~w@mHthB{Dd~@sBni@sA`[IfBqAt[eFpnAy@~SMhDsJ~_CeL~rCw@lVWpG_Cf_@}@`NsCvf@qG~aAiBjZc@rG[zFGtIFxKX|Jx@v\\ZbPpAdc@~Aza@J|BnBrm@H~OEpHQrIw@hKm@fF{C`RcAdIg@zCy@lF_AdGs@vG]rDa@rFQxDKjIGpJCdq@E~SItKE|Z?ddQGzdABhoFLdgEE~vBHbt@FnREv_@JrtHBnaA@dn@Zt}DA`dBHpxCXj{HNfoB@|a@JrdBBncAPpgCBnKNdE^hEdAlHXjBzC~R\\lB`@`Bf@dBz@|B`ApBxA~Bl{@htAjAxBpCnGlAdDtGhSl@fBZdA|EhNjCjGxDtHpAvB~A|BtBlCnL`MrAzAld@rd@fCtCxBvCbBbCjFfI||@bvAz@rAv@lA|Wbb@`Zne@n}@|vAlJvNpJnOvDjG~_@zl@tB~C~G|KjC`EhHbL|ElGbB~BtBbCzB|BtCxCnFdFfO`MxAfAzWjTrD~CdA~@xEnDvDzC~AnAnAbAxGrFbBrA`BxAbBnBrAjBt@rAdArBxAtD|@vC|@lDp@lDj@rEt@tIj@fF|BtWr@pG`@tCd@`Cd@hBp@rBj@rAzA~C|@vAfApArAtA~@x@|AbApAt@|@\\|Ah@fAV|@HxCLz@Al@EtAOvBa@t@UlBw@bCuAhUsNhAo@zDcB|Bs@hHiBfFeA|WkGdBYrBWjDU~BI|BC~I?bYRpTLbVNxDCfDQvAQxBc@hBe@|Bw@fAe@jDoBhA{@|@u@tDcDtLmIrCkA`Bi@~A]jDi@nDUbCItE?xGCfDGlBI~AYjAWdOmEt@YdASxAI~@D|A\\j@Th@^hAdA~@pAVl@^~@VbAnArHvA|IxIdn@~DvXv@zFz@rI^xFTlEJ|IClMMhEKdEaAha@WnJ}Axk@CtBDvBL|BXxB\\fBlAfEjB|FtAtEr@vCvAtH^jD\\vDNfEHzDCdH[pHUdCo@jFaAjJWlDUxFAtF@tAL`D|A`X~GfeAFxEUjFk@zDcEjNqAvEy@~EkGp}@g@`M_@bMkAz[o@fRJ~FLnCvA~OFjBDvBCpBMfCW~Bc@vBg@lBg@vA]r@gGhL_AlBqA`D}@jCc@vAc@fBc@bBe@rBu@lEYpBWvBe@dGI|BIpDCfEN`j@FhFR~FX~E\\~Ed@vEp@hFp@fEzKhj@xEfUxBdIdA|Cz@fC~@lC`AtCp@lCl@`DXfCPzCHnCEdDOhDQlBm@nEgBzIaBvKyDn\\q@pEeJre@cAtGo@zHo@fNwCht@GpEF|H`@hGdAjNr@dMlBlv@@vBE~CQ~CcArJeGzg@qA`MuCbj@y@~QCtCExD?~LTzJJvDlAhVvAhWjAbSpA|YTvMKdk@M~Ek@tHwAvLuAdK_A|Hu@`I}@~N]jHk@nG}@dG_BvH{EnPiAlDg@~Bq@|D]hEyBznAk@f`@O|EYdDqBxR[|EkBbf@k@hHcAvHgDnNeHfRaBzEy@dD_@tB[xCKtAIvD?hBD`BLdCXhD\\zEP`CFzCKlD]tE_A|EeE|MkAhFo@|EStDY|OU`Eg@|DsMzo@sAbE_BhDyFjK_AdCkYd}@qMta@}BpI}ApIw@bG}@jIa@|GUbGkChtAq@j`@H`L|Ed`C`@|LPrO@p_@Dd@ZhYEhRWng@EbSKxJ?fFInL?dIDfGH`IjAbg@n@lMdAnk@JdIHvMb@xlA?dHGpJk@r^U~KW`SCzGlAthCVls@P`c@CtGMhFOrDa@nG{@fJsBzR}CpY]rDiA`LkD|ZgAnL{A~Nm@|FQ|A{CbZo@|Ey@nEcBlGq@rBeAvB}ApC}PvTgAvAuz@lgAy@`A}`@hh@{e@`o@sCfD{CfEwE~GaYfe@cM`SsBjDiBfCcBhC_CxCyC`E}_@hd@{DtEmx@`aAwE`GyAzAkAvA{EdE{ErDgGxCoHxCsBdAkAz@}CdC}A`BmBpC}AhCsArC}AfEmO|g@mDhL_Wpz@qEhNwA|EmBbHqAnFoBjHaIr]kRnx@yIb_@I`@}XtkAeArD}AbHyDjL{BhG{HtSqk@b}AkF|MeDvIiDpHsIhPmBvCsAxCqAbEw@vD{@rGu@xEqBnNcAhGgAfGiCnJc@vA}CrLqB|G_A|Bs@xAw@vAyA~AkBzA}BpA_GzBaE`B_CtAuBnBgBvB{BxCsBtE}A~EkAhGy@hGw@~L_@bDi@nDgAxDaAlCsKxUiBfCoBxBmA|@iBbAkBp@qY`JgEpAqDbBwCzBsCzC{BxCoBpDmAnC}@fC_AvDk\\f~Ay@fDyHb^{BrLiD`PmAdFmA`Dw@zA}@vAiAxAkAlAgBpAaAj@{@\\_LtDq`@fMeCbAoBpAu@t@sAzAkAhBuA|CsA~BwAbDuApCiDrD_C|Awk@bS{`@vMsHjDkCzAcAt@}PvMeBtAaLbJiDtCkClCsBvCyBfE}AvDmArDmAnFq@dE}M~~@yLlz@WxBUxBOvBKpBSbGChHD`CNzFNdCf@zG|A~QJrDKlEc@dE_AvF{N|t@_ClI}AlE_CxFk^ly@{AzCsA`C{A|BkCpCgG~EqDnCgHhFuBdBiBfBcBvB{AbCcDfIuBfFuFbNi@pAyKtXq@rB}@zCsAdFkAtFm@bDk@lDq]vpCuDlZe@dEa@tFu@rNgCvg@a@fJ_A~Q[~DQxAWvAe@vBeCfKYxAi@~DK~AK~AEdDDdDJxB^xD`@hCnBnJ|o@z}Cr@bEd@`Dn@~En@fHf@tIxAbg@P`GdAj^fAd`@LfEn@vSjBtp@x@`Wt@`YLhGBpCEjBMzAQtAa@bC}@tCeAxBy@lAs@x@}AtA_GvDaCxAaHjEgYnQsBzAmBjB}ArBuAdCm@nA_@dAy@fC{@dDYjAyA~GY~AkAbJi@hDm@fDgD~M_k@n}BI^qp@bnCQt@yBlJ{@tEkAdIq@zGgAjLyLfsAe@|Cm@xCeAtE]fBm@fFOdBMpAUlCYhEIjF?dFKhC[tDwHn{@YjCk@lD{@xDu@pC_AhCmi@bnAoBtEy@dBeCtEiA~AeZf_@qBbC_BhBmD~EsKlMsEzFyAlB{o@lx@sP`TcV~YeGzHq@bAe@|@]v@_@~@Y|@o@jCSbAa@~CIfAWlFa@rKGpB[lIY~DQzA_@jC_AdDa@jAaArBqAnBm@x@sAnAi@d@mGhFmAlAq@v@iBfCkB~CiB~Do@bBc@zAaAfEo@vDwBzO[jBw@rDg@fBoBxFuSdk@i@`Bq@`CUdAQlAWjCK~C@lCFtAJxANlAh@`Dv@~CdA|Dl@tC^bCRjCBvA@xACpEYnPGvECdD@lADtAPhCd@nDlB~J^zBNvAPhC@t@?dAEjBK`BQvAoCnOkAfHiJ`u@YpBm@`DYdA{@|BaAlBuVj^mOpT}AlBo@l@eAr@w@b@y@XsA^uANy@FqIV_CXeAVoBn@eG|BcBb@gAR{@HsI\\gBPs@P{@TcA^cVdKcF~BoBfAsDnC_CxBiBrBgCnDeBvCgAtBi@nAwApDmAtDSx@q@jCqAnGo@dF{AvMo@bF]jBYtAc@`Bs@vBe@pAi@fAiArBu]vk@sBbDo@dAu@dAkArAqAjAkBlAeL`GkCvAmAx@qB`B{BbCg^dc@gC`DqI~JaAjAqA~A{@dAgC~Cy@`AiB`CqB|Cg@|@cArBaA|BcAzCaAtDmEdSw@`EmDhR_CdL]xAa@rAqAfDmAjCe@x@_BvB{BtBcAx@wKvFsBxAkSbRo@p@{AjBqAxB_@v@kA`Dk@rBk@bD[vCO~CCxBAzBA|JErCOzBMdAO~@a@rBQv@m@lBaApBa@p@aArAg@f@i@d@mA|@uAr@wAf@aBTwADoBI_Q{BeBM{A@m@DeANeAVoLnEeAZ_GxAwDfAsAh@gAf@eCzAeCrBk@l@gBpBw@bAcAvAmB|CmE`I_AvAuAvAaAp@o@^oBv@}B^k@BaAAaAEcPqAgAE{BDw@H_Cb@oBr@uAt@s@f@}ArAcH|G_DtBmB|@wAd@wBh@kC\\wm@bBuBJ}ANwAV{A`@qG`CiIlDuAp@uAt@_An@iA~@kCdC_BnB{AxBi@|@iBhDqApCuAjDs@rBm@hBu@hCcDnMo@`CqAzEyAnFuBhIiCbJeApCkBjDk@x@o@v@cCfBcBtAmE|DgAxAw@jAiDlGw@jBg@dA_B`Cm@p@{@n@_AXiAb@yAT_B@_JEyADsARaC|@aAl@{@n@iBdCwA~BaBxCsAlCuCdFo@v@o@l@eCzAmHtBoG|AiBZiBNeDG_CYiHkBoB]}H}AeC[sBKwBDmDn@cEdB_CnBaBnB}@vA}AbDiExMw@jCaIhW_@~A[pB_@fDKbBIbBEnB?dBB`BBjARxC\\|CRlAj@lCZnAb@rArC`H~IzSxJ~TjRdd@tApCb@t@bAvAh@p@rArAlA|@hAp@fAf@jA`@dATzYpEvMtBl@HlAFz@@fCI|AQ`JmBvASpBMr@AlAJlBZxAd@lBbArCbChAxAvAlCn@jBx@zC\\hBpGpl@lA~IhBdKrGpYhJp`@fA`HXdCVvD@t@?nA@rD@`BI`EQzBOjBY|BaA|GgAzIQjBg@nH[jFSpEOtEGjHChAB~F~@nd@fAxk@?vBErEi@|d@@dERlEj@hEnAfHh@nDf@rFb@bI?~CJv[CtCCfCMpCcCp]}HfeAQjDMhHM~EOlC[pDYvB]fBc@nBe@|A{Tfe@cAfC_AnC_AlD_AhE{@dGyF|h@Y|By@pEiApEq@bBw@`BmAnBgArAcF|FmA|AaAtA}@xAiLp[}ErM}AlCkB~B}@x@cAx@kAt@_MnGmA|@s@n@eBhBq@|@gB`DeGpMu@`Bm@lA_ArAs@nAeAhAkAbAuDpCkAnAwAfBqAvBgAdCcAfCs@jDe@|C[hEK|DEhEMpCOvCQbC[zB_Pvq@o@pCY~AWnBObBMtBGhBCvB@tBHzBrA|SF`BBtB?bBCvAItBwBva@SjD_@pHi@pFw@`Fe@zBe@nB]rA[bAu@vBiBlEsArCaAbBaD`GsDlH{BbFqAxCkCxG}_@tcAwBhGaAdD}@fDaArEo@dEg@jE]|DSxDM`EEdD?fEPnIBpAZ~M@bDC|BUjEy@|JgAlMSvCKbCEvBAdBB|BH|B`A~SNnF?rBE~CMhCq@pIc@rBg@xB[v@mApDqCrHeDrJmCtFcBjCgA~AcBlBkChCwBzA{BtAsD~AgPpFkBj@oG~@qHp@mC\\}EbBmB~@{BpAeA~@iCxCuAnBcB`D{ApDiAzCy@jDg@pCw@vEwCxSkBjKi@pCaAjDwHj]oGrX_C`LuJzb@kEdUkCpMo@nEg@hFUxFC~DFxl@@je@AjDDxj@B`t@?~A@zGGjDMxCSfCMlA_@tCm@|Cw@xCo@nBe@lAk@pAg@bAm@dAwAtBq@x@ku@ru@eSfSqAvA}BtCyChEqAxB}BjEy@dBiApCyBbGoAzDy@`DaOvo@c@~AiA~CqAnCk@bAs@hA}ApBm{@naAyCpDkErFgX|]oAnBq@nAo@vAg@rAg@xAc@xA]tA[|AW~Ak@nESdCMnCE~B?xBBxBRvEL`BNvA^hCzFzZb@xBpHj`@j@xDV~BHdAT|DHbDBpCAvCYfVCxEDdEJrDLnC\\dE`Ehe@hAxNV|DfCva@N~B~GdiAjA~RFdDA|BKbDQbCMbAc@vCYvAc@|Ai@fBi@rAk@nA{KnRwAjCwDtHoAnCiBfEmSnh@_D~I{FvQaCzHoBdG_EpMo@~Be@rBeDnQs@jCY|@kArCw@tAw@lAy@dAk@l@o@j@{@n@{]~U_At@cA|@uA~Ag@r@{@xAo@nAu@dB[|@o@vBYnAs@~Da@bEIvAwExdAEf@QjCU~Bw@rF_@jBqKzd@c@vBWdBMtAIbBE|A@hDN`DN~AT~Al@rCZnA\\`A~@rBnApB|AjB~GhIp@bAfAzB`ApCr@jC`@tBPzANdBJ|AFnB@zAOlJm@p[GtBQ~DQdDg@vG]dDcAtHeA`Hu@`EeChKsBbH{EnNyDtKg@`Be@xBY~ASvAQfBOdCEfCBdCDfBTdDNzAXjB`@lBVbAd@|AdAfC|GvMfGnLr@xAp@bBd@~A\\rA`@xBRzANdBF`AHdC@z@C`CEjAWlDe@xCQv@s@lC{@zBe@`Aw@rAo@z@_A`A}TjR_FbEkBfBsBbCiCtDuAbCiAxBg@jA}ErMuBtF{D`KaB`FYfAa@lBu@tFWfCWlEkAbYOrBU|BUbB]rBc@vBc@hBq]jmAK`@oD|LwD|Mu_@jsAcAzCy@zBoAzCqCfG{M`Z{MvYuCjGcKtTaDhHwA|DaBxF_W`bA}J|`@gQhr@a@hBWxAYrB_@dDUfCStCKxCSbKW`PgAbi@}@lf@GdC{@hd@YhROjLAh@UrPEvDK~K?tJ?bHFbED`BZ`JPlDJlDFtBp@pNt@pRVtIL`D?~ACnBKvCWpCI|@]tCg@lEM~AI|AGnCDzBH`BHbAZdCpAbIdCzN|@hFXnBVdCLjBFjCDhBAnCOtEK~AqCv]C\\WxB[vBy@tD]lAgAnCa@|@g@`AgBzCgDhFeAtBe@pA{@`C_JxXiAdDqArDiAnCg@lAmApC{CjHi@vAyAbEaAjDg@nBmCzKc@dBqChLs@dCg@vAg@rAcC|Fw@dBs@jBm@pB]`BWbBSdBMhBEhBAhBBjBHfBNfBTdBXbB`@|Ad@zAlFbNf@`Bh@dC`@jCVlCHrBBzAO|TsBdyCYp^AlHY|uA?nEA`HCxJ?`AClCIlBYpBWhA[bAq@|A}@tAkAhAuK`Hm@n@c@l@S`@Q`@[z@a@fBQ~@M`AIlAA|ADlAbAlJ@j@Cp@Gf@I`@Sh@e@v@_@\\g@\\u@P_AJaAJeATyBr@YJuBv@sAr@{AfAwAnAkAnAeAtAuE~Gq@dAyF~HaAhAcD|BqAbA{DzCoBlAeCrBuAjAy@n@{@r@DJpAbEDJd@zAHTn@pB^lALM",
      "way_points": [
        0,
        15129
      ]
    }
  ],
  "metadata": {
    "attribution": "openrouteservice.org | OpenStreetMap contributors",
    "service": "routing",
    "timestamp": 1738147064625,
    "query": {
      "coordinates": [
        [
          -87.6298,
          41.8781
        ],
        [
          -122.3321,
          47.6062
        ]
      ],
      "profile": "driving-car",
      "profileName": "driving-car",
      "format": "json"
    },
    "engine": {
      "version": "9.0.0",
      "build_date": "2024-12-02T11:09:21Z",
      "graph_date": "2025-01-21T09:49:30Z"
    }
  }
}