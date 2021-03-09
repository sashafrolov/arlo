# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots[
    "test_ballot_comparison_cvr_metadata 1"
] = """Tabulator,Batch Name,Ballot Number,Imprinted ID,Ticket Numbers,Already Audited,Audit Board
TABULATOR1,BATCH1,1,1-1-1,0.243550726331576894,N,Audit Board #1
TABULATOR1,BATCH2,2,1-2-2,0.125871889047705889,N,Audit Board #1
TABULATOR1,BATCH2,3,1-2-3,0.126622033568908859,N,Audit Board #1
TABULATOR2,BATCH2,2,2-2-2,0.053992217600758631,N,Audit Board #1
TABULATOR2,BATCH2,3,,0.255119157791673311,N,Audit Board #1
TABULATOR2,BATCH2,4,2-2-4,"0.064984443990590400,0.069414660569975443",N,Audit Board #1
TABULATOR2,BATCH2,5,2-2-5,0.442956417641278897,N,Audit Board #1
TABULATOR2,BATCH2,6,2-2-6,0.300053574780458718,N,Audit Board #1
"""

snapshots["test_ballot_comparison_two_rounds 1"] = {
    "key": "supersimple",
    "prob": None,
    "size": 30,
}

snapshots["test_ballot_comparison_two_rounds 2"] = {
    "numSamples": 13,
    "numSamplesAudited": 0,
    "numUnique": 8,
    "numUniqueAudited": 0,
    "status": "NOT_STARTED",
}

snapshots["test_ballot_comparison_two_rounds 3"] = {
    "numSamples": 17,
    "numSamplesAudited": 0,
    "numUnique": 12,
    "numUniqueAudited": 0,
    "status": "NOT_STARTED",
}

snapshots[
    "test_ballot_comparison_two_rounds 4"
] = """######## ELECTION INFO ########\r
Organization,Election Name,State\r
Test Org test_ballot_comparison_two_rounds,Test Election,CA\r
\r
######## CONTESTS ########\r
Contest Name,Targeted?,Number of Winners,Votes Allowed,Total Ballots Cast,Tabulated Votes\r
Contest 1,Targeted,1,1,22,Choice 1-1: 12; Choice 1-2: 8\r
Contest 2,Opportunistic,1,2,28,Choice 2-1: 26; Choice 2-2: 12; Choice 2-3: 14\r
\r
######## AUDIT SETTINGS ########\r
Audit Name,Audit Type,Audit Math Type,Risk Limit,Random Seed,Online Data Entry?\r
Test Audit test_ballot_comparison_two_rounds,BALLOT_COMPARISON,SUPERSIMPLE,10%,1234567890,Yes\r
\r
######## AUDIT BOARDS ########\r
Jurisdiction Name,Audit Board Name,Member 1 Name,Member 1 Affiliation,Member 2 Name,Member 2 Affiliation\r
J1,Audit Board #1,,,,\r
J2,Audit Board #1,,,,\r
\r
######## ROUNDS ########\r
Round Number,Contest Name,Targeted?,Sample Size,Risk Limit Met?,P-Value,Start Time,End Time,Audited Votes\r
1,Contest 1,Targeted,30,No,163007579.5813730061,DATETIME,DATETIME,Choice 1-1: 13; Choice 1-2: 10\r
1,Contest 2,Opportunistic,,No,3073.4982074829,DATETIME,DATETIME,Choice 2-1: 15; Choice 2-2: 9; Choice 2-3: 9\r
\r
######## SAMPLED BALLOTS ########\r
Jurisdiction Name,Tabulator,Batch Name,Ballot Position,Imprinted ID,Ticket Numbers: Contest 1,Audited?,Audit Result: Contest 1,CVR Result: Contest 1,Discrepancy: Contest 1,Audit Result: Contest 2,CVR Result: Contest 2,Discrepancy: Contest 2\r
J1,TABULATOR1,BATCH1,1,1-1-1,Round 1: 0.243550726331576894,AUDITED,Choice 1-2,Choice 1-2,,"Choice 2-1, Choice 2-2","Choice 2-1, Choice 2-2",\r
J1,TABULATOR1,BATCH2,2,1-2-2,Round 1: 0.125871889047705889,AUDITED,Choice 1-2,Choice 1-2,,"Choice 2-1, Choice 2-2","Choice 2-1, Choice 2-2",\r
J1,TABULATOR1,BATCH2,3,1-2-3,"Round 1: 0.126622033568908859, 0.570682515619614792",AUDITED,"Choice 1-1, Choice 1-2",Choice 1-1,1,"Choice 2-2, Choice 2-3","Choice 2-1, Choice 2-3",2\r
J1,TABULATOR2,BATCH2,2,2-2-2,"Round 1: 0.053992217600758631, 0.528652598036440834",AUDITED,"Choice 1-1, Choice 1-2","Choice 1-1, Choice 1-2",,"Choice 2-1, Choice 2-2, Choice 2-3","Choice 2-1, Choice 2-2, Choice 2-3",\r
J1,TABULATOR2,BATCH2,3,,Round 1: 0.255119157791673311,NOT_FOUND,,,2,,,2\r
J1,TABULATOR2,BATCH2,4,2-2-4,"Round 1: 0.064984443990590400, 0.069414660569975443",AUDITED,BLANK,,,BLANK,"Choice 2-1, Choice 2-3",1\r
J1,TABULATOR2,BATCH2,5,2-2-5,"Round 1: 0.442956417641278897, 0.492638838970333256",AUDITED,CONTEST_NOT_ON_BALLOT,,,"Choice 2-1, Choice 2-2","Choice 2-1, Choice 2-2",\r
J1,TABULATOR2,BATCH2,6,2-2-6,"Round 1: 0.300053574780458718, 0.539920212714138536",AUDITED,CONTEST_NOT_ON_BALLOT,,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
J2,TABULATOR1,BATCH1,1,1-1-1,Round 1: 0.476019554092109137,AUDITED,Choice 1-1,Choice 1-2,0,Choice 2-1,"Choice 2-1, Choice 2-2",0\r
J2,TABULATOR1,BATCH1,2,1-1-2,"Round 1: 0.511105635717372621, 0.583472201399663519",AUDITED,Choice 1-1,Choice 1-1,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
J2,TABULATOR1,BATCH1,3,1-1-3,Round 1: 0.242392535590495322,AUDITED,Choice 1-2,Choice 1-2,,"Choice 2-1, Choice 2-2","Choice 2-1, Choice 2-2",\r
J2,TABULATOR1,BATCH2,1,1-2-1,"Round 1: 0.200269401620671924, 0.588219390083415326",NOT_FOUND,,Choice 1-1,2,,"Choice 2-1, Choice 2-3",2\r
J2,TABULATOR1,BATCH2,3,1-2-3,Round 1: 0.556310137163677574,AUDITED,Choice 1-1,Choice 1-1,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
J2,TABULATOR2,BATCH1,1,2-1-1,Round 1: 0.174827909206366766,AUDITED,Choice 1-2,Choice 1-2,,"Choice 2-1, Choice 2-2","Choice 2-1, Choice 2-2",\r
J2,TABULATOR2,BATCH2,1,2-2-1,Round 1: 0.185417954749015145,AUDITED,CONTEST_NOT_ON_BALLOT,Choice 1-1,1,CONTEST_NOT_ON_BALLOT,"Choice 2-1, Choice 2-3",1\r
J2,TABULATOR2,BATCH2,2,2-2-2,"Round 1: 0.252054739518646128, 0.297145021317217438",AUDITED,"Choice 1-1, Choice 1-2","Choice 1-1, Choice 1-2",,"Choice 2-1, Choice 2-2, Choice 2-3","Choice 2-1, Choice 2-2, Choice 2-3",\r
J2,TABULATOR2,BATCH2,3,,"Round 1: 0.179114059650472941, 0.443867094961314498, 0.553767880261132538",AUDITED,Choice 1-1,,2,"Choice 2-1, Choice 2-3",,2\r
J2,TABULATOR2,BATCH2,4,2-2-4,Round 1: 0.583133559190710795,AUDITED,CONTEST_NOT_ON_BALLOT,,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
J2,TABULATOR2,BATCH2,5,2-2-5,Round 1: 0.462119987445142117,AUDITED,CONTEST_NOT_ON_BALLOT,,,"Choice 2-1, Choice 2-2","Choice 2-1, Choice 2-2",\r
J2,TABULATOR2,BATCH2,6,2-2-6,Round 1: 0.414184312862040881,AUDITED,CONTEST_NOT_ON_BALLOT,,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
"""

snapshots[
    "test_ballot_comparison_two_rounds 5"
] = """######## ELECTION INFO ########\r
Organization,Election Name,State\r
Test Org test_ballot_comparison_two_rounds,Test Election,CA\r
\r
######## CONTESTS ########\r
Contest Name,Targeted?,Number of Winners,Votes Allowed,Total Ballots Cast,Tabulated Votes\r
Contest 1,Targeted,1,1,22,Choice 1-1: 12; Choice 1-2: 8\r
Contest 2,Opportunistic,1,2,28,Choice 2-1: 26; Choice 2-2: 12; Choice 2-3: 14\r
\r
######## AUDIT SETTINGS ########\r
Audit Name,Audit Type,Audit Math Type,Risk Limit,Random Seed,Online Data Entry?\r
Test Audit test_ballot_comparison_two_rounds,BALLOT_COMPARISON,SUPERSIMPLE,10%,1234567890,Yes\r
\r
######## AUDIT BOARDS ########\r
Jurisdiction Name,Audit Board Name,Member 1 Name,Member 1 Affiliation,Member 2 Name,Member 2 Affiliation\r
J1,Audit Board #1,,,,\r
J2,Audit Board #1,,,,\r
\r
######## ROUNDS ########\r
Round Number,Contest Name,Targeted?,Sample Size,Risk Limit Met?,P-Value,Start Time,End Time,Audited Votes\r
1,Contest 1,Targeted,30,No,163007579.5813730061,DATETIME,DATETIME,Choice 1-1: 13; Choice 1-2: 10\r
1,Contest 2,Opportunistic,,No,3073.4982074829,DATETIME,DATETIME,Choice 2-1: 15; Choice 2-2: 9; Choice 2-3: 9\r
2,Contest 1,Targeted,22,Yes,0,DATETIME,DATETIME,Choice 1-1: 8; Choice 1-2: 10\r
2,Contest 2,Opportunistic,,No,1220.1312885251,DATETIME,DATETIME,Choice 2-1: 14; Choice 2-2: 7; Choice 2-3: 8\r
\r
######## SAMPLED BALLOTS ########\r
Jurisdiction Name,Tabulator,Batch Name,Ballot Position,Imprinted ID,Ticket Numbers: Contest 1,Audited?,Audit Result: Contest 1,CVR Result: Contest 1,Discrepancy: Contest 1,Audit Result: Contest 2,CVR Result: Contest 2,Discrepancy: Contest 2\r
J1,TABULATOR1,BATCH1,1,1-1-1,"Round 1: 0.243550726331576894, Round 2: 0.686337915847173217, 0.780585292625102279",AUDITED,Choice 1-2,Choice 1-2,,"Choice 2-1, Choice 2-2","Choice 2-1, Choice 2-2",\r
J1,TABULATOR1,BATCH2,2,1-2-2,"Round 1: 0.125871889047705889, Round 2: 0.752068917437552786",AUDITED,Choice 1-2,Choice 1-2,,"Choice 2-1, Choice 2-2","Choice 2-1, Choice 2-2",\r
J1,TABULATOR1,BATCH2,3,1-2-3,"Round 1: 0.126622033568908859, 0.570682515619614792",AUDITED,"Choice 1-1, Choice 1-2",Choice 1-1,1,"Choice 2-2, Choice 2-3","Choice 2-1, Choice 2-3",2\r
J1,TABULATOR2,BATCH2,2,2-2-2,"Round 1: 0.053992217600758631, 0.528652598036440834, Round 2: 0.764288236446565653",AUDITED,"Choice 1-1, Choice 1-2","Choice 1-1, Choice 1-2",,"Choice 2-1, Choice 2-2, Choice 2-3","Choice 2-1, Choice 2-2, Choice 2-3",\r
J1,TABULATOR2,BATCH2,3,,Round 1: 0.255119157791673311,NOT_FOUND,,,2,,,2\r
J1,TABULATOR2,BATCH2,4,2-2-4,"Round 1: 0.064984443990590400, 0.069414660569975443, Round 2: 0.662654312843285447, 0.739178008942093721",AUDITED,BLANK,,,BLANK,"Choice 2-1, Choice 2-3",1\r
J1,TABULATOR2,BATCH2,5,2-2-5,"Round 1: 0.442956417641278897, 0.492638838970333256",AUDITED,CONTEST_NOT_ON_BALLOT,,,"Choice 2-1, Choice 2-2","Choice 2-1, Choice 2-2",\r
J1,TABULATOR2,BATCH2,6,2-2-6,"Round 1: 0.300053574780458718, 0.539920212714138536, Round 2: 0.614239889448737812",AUDITED,CONTEST_NOT_ON_BALLOT,,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
J2,TABULATOR1,BATCH1,1,1-1-1,"Round 1: 0.476019554092109137, Round 2: 0.762943953776491170",AUDITED,Choice 1-1,Choice 1-2,0,Choice 2-1,"Choice 2-1, Choice 2-2",0\r
J2,TABULATOR1,BATCH1,2,1-1-2,"Round 1: 0.511105635717372621, 0.583472201399663519",AUDITED,Choice 1-1,Choice 1-1,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
J2,TABULATOR1,BATCH1,3,1-1-3,"Round 1: 0.242392535590495322, Round 2: 0.705264140168043487",AUDITED,Choice 1-2,Choice 1-2,,"Choice 2-1, Choice 2-2","Choice 2-1, Choice 2-2",\r
J2,TABULATOR1,BATCH2,1,1-2-1,"Round 1: 0.200269401620671924, 0.588219390083415326",NOT_FOUND,,Choice 1-1,2,,"Choice 2-1, Choice 2-3",2\r
J2,TABULATOR1,BATCH2,3,1-2-3,Round 1: 0.556310137163677574,AUDITED,Choice 1-1,Choice 1-1,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
J2,TABULATOR2,BATCH1,1,2-1-1,"Round 1: 0.174827909206366766, Round 2: 0.638759896009674755, 0.666161104573622944, 0.688295361956370024, 0.773068356532987654",AUDITED,Choice 1-2,Choice 1-2,,"Choice 2-1, Choice 2-2","Choice 2-1, Choice 2-2",\r
J2,TABULATOR2,BATCH2,1,2-2-1,Round 1: 0.185417954749015145,AUDITED,CONTEST_NOT_ON_BALLOT,Choice 1-1,1,CONTEST_NOT_ON_BALLOT,"Choice 2-1, Choice 2-3",1\r
J2,TABULATOR2,BATCH2,2,2-2-2,"Round 1: 0.252054739518646128, 0.297145021317217438, Round 2: 0.770913121904276479",AUDITED,"Choice 1-1, Choice 1-2","Choice 1-1, Choice 1-2",,"Choice 2-1, Choice 2-2, Choice 2-3","Choice 2-1, Choice 2-2, Choice 2-3",\r
J2,TABULATOR2,BATCH2,3,,"Round 1: 0.179114059650472941, 0.443867094961314498, 0.553767880261132538",AUDITED,Choice 1-1,,2,"Choice 2-1, Choice 2-3",,2\r
J2,TABULATOR2,BATCH2,4,2-2-4,"Round 1: 0.583133559190710795, Round 2: 0.685610948371080498",AUDITED,CONTEST_NOT_ON_BALLOT,,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
J2,TABULATOR2,BATCH2,5,2-2-5,"Round 1: 0.462119987445142117, Round 2: 0.593645562906652185, 0.727818415897312844",AUDITED,CONTEST_NOT_ON_BALLOT,,,"Choice 2-1, Choice 2-2","Choice 2-1, Choice 2-2",\r
J2,TABULATOR2,BATCH2,6,2-2-6,Round 1: 0.414184312862040881,AUDITED,CONTEST_NOT_ON_BALLOT,,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
J1,TABULATOR1,BATCH1,2,1-1-2,Round 2: 0.658361514845611561,AUDITED,Choice 1-1,Choice 1-1,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
J1,TABULATOR2,BATCH1,2,2-1-2,Round 2: 0.651118570553261125,AUDITED,Choice 1-1,Choice 1-1,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
J1,TABULATOR2,BATCH2,1,2-2-1,"Round 2: 0.607927957276839128, 0.787278086653253195",AUDITED,Choice 1-1,Choice 1-1,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
J2,TABULATOR2,BATCH1,2,2-1-2,Round 2: 0.677864268646804078,AUDITED,Choice 1-1,Choice 1-1,,"Choice 2-1, Choice 2-3","Choice 2-1, Choice 2-3",\r
"""

snapshots["test_set_contest_metadata_on_contest_creation 1"] = {
    "choices": [
        {"name": "Choice 2-1", "num_votes": 26},
        {"name": "Choice 2-2", "num_votes": 12},
        {"name": "Choice 2-3", "num_votes": 14},
    ],
    "total_ballots_cast": 28,
    "votes_allowed": 2,
}

snapshots["test_set_contest_metadata_on_cvr_upload 1"] = {
    "choices": [
        {"name": "Choice 2-1", "num_votes": 26},
        {"name": "Choice 2-2", "num_votes": 12},
        {"name": "Choice 2-3", "num_votes": 14},
    ],
    "total_ballots_cast": 28,
    "votes_allowed": 2,
}

snapshots["test_set_contest_metadata_on_cvr_upload 2"] = {
    "choices": [
        {"name": "Choice 2-1", "num_votes": 16},
        {"name": "Choice 2-2", "num_votes": 8},
        {"name": "Choice 2-3", "num_votes": 8},
    ],
    "total_ballots_cast": 17,
    "votes_allowed": 2,
}
