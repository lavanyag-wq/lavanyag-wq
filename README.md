<img src="assets/banner.svg" width="960" alt="Lavanya Gurrapu: Data Scientist. Instruments that measure what the usual artefact cannot.">

<div align="center">

<img src="https://komarev.com/ghpvc/?username=lavanyag-wq&style=flat-square&color=2b6777" alt="profile views">
<img src="https://img.shields.io/badge/portfolio_repositories-3-2b6777?style=flat-square" alt="3 repositories">
<img src="https://img.shields.io/badge/tests_across_them-283-2b6777?style=flat-square" alt="283 tests">
<a href="https://lavanyag-wq.github.io"><img src="https://img.shields.io/badge/project_hub-lavanyag--wq.github.io-7cf5c8?style=flat-square" alt="project hub"></a>

</div>

<table align="center">
<tr>
<td align="center">

**3+**

YEARS IN DS

</td>
<td align="center">

**3**

REPOSITORIES

</td>
<td align="center">

**283**

TESTS

</td>
<td align="center">

**13**

DECISION RECORDS

</td>
<td align="center">

**9**

EXPERIMENTS

</td>
</tr>
</table>

> I build measurement instruments for machine learning systems: tools that
> answer the question the usual artefact structurally cannot. A parity diff
> cannot say whose bug it is, so I built the referee that can. A golden set
> cannot tell a regression from noise below its resolution floor, so I built
> the gate that refuses to rule there. A final p-value cannot report its own
> false positive rate, so I built the auditor that replays the procedure and
> measures it. Every number any of them publishes is produced by code that
> runs in CI and is checked against the prose that quotes it.

## The pivot point

```
2021          2023              2025
Microsoft --> MS Computer   --> Netflix
India         Science (US)      USA
enterprise    the deliberate    consumer scale:
ML on Azure   reset             recommendations and
                                experimentation
```

Three moves, one direction: from building predictive models inside an
enterprise stack, through a formal CS grounding, to consumer-scale systems
where the costly failures are not model failures but measurement failures:
features skewing between training and serving, experiments read before they
are done, eval sets too small to support the decisions resting on them. The
portfolio below is built at exactly that seam.

## Current focus

| At work | In the open |
| --- | --- |
| Recommendation systems, churn prediction, A/B testing frameworks and time-series forecasting over large-scale behavioral data; productionizing models with MLflow, Docker and CI/CD | The three instruments below: a retrieval regression gate that knows its own resolution, a training/serving feature referee over Delta Lake, and an A/B peeking auditor with a calibrated honest boundary |

## Tech stack, by depth

Yardstick for the meter: could I debug this in production at 3am, or have I
shipped it under supervision, or have I only built one measured project with
it. Stated so the self-assessment means something.

| technology | depth | evidence |
| --- | --- | --- |
| Python | `█████████░` | daily production language across both roles and all three repositories |
| SQL | `████████░░` | production analytics and experimentation queries since 2021 |
| scikit-learn / XGBoost | `████████░░` | churn, segmentation and forecasting models shipped in both roles |
| PySpark / Databricks | `███████░░░` | production feature pipelines at both employers; window and point-in-time semantics modelled and tested in churn-feature-referee |
| A/B testing and experiment statistics | `███████░░░` | production experimentation at work; ab-peeking-audit measures peeking inflation at 28.15% and calibrates the honest boundary |
| MLflow / Docker / CI/CD | `███████░░░` | model lifecycle in both roles; every repository here re-measures its own numbers in CI |
| Time-series forecasting (Prophet, ARIMA) | `██████░░░░` | demand and engagement forecasting shipped at both employers |
| Statsmodels | `██████░░░░` | the reference implementation in ab-peeking-audit, pinned equal to the fast engine by test |
| Delta Lake | `█████░░░░░` | one repository deep: two-commit snapshots, time travel, and the as-of-now leak measured at 248 corrupted pairs |
| RAG / embeddings / vector stores | `█████░░░░░` | academic projects plus rag-retrieval-gate: deterministic embeddings, ChromaDB adapter, retrieval metrics from scratch |
| TensorFlow / PyTorch | `████░░░░░░` | academic computer-vision projects (YOLOv3, Faster R-CNN); not yet production depth |

## Building blocks

<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/SQL-336791?style=flat-square" alt="SQL">
<img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white" alt="Spark">
<img src="https://img.shields.io/badge/Delta_Lake-00ADD4?style=flat-square" alt="Delta Lake">
<img src="https://img.shields.io/badge/Snowflake-29B5E8?style=flat-square&logo=snowflake&logoColor=white" alt="Snowflake">
<br>
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn">
<img src="https://img.shields.io/badge/XGBoost-2B6777?style=flat-square" alt="XGBoost">
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch">
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow">
<img src="https://img.shields.io/badge/statsmodels-4051B5?style=flat-square" alt="statsmodels">
<img src="https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white" alt="MLflow">
<br>
<img src="https://img.shields.io/badge/Azure_ML-0078D4?style=flat-square" alt="Azure ML">
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes">
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions">
<img src="https://img.shields.io/badge/Tableau-E97627?style=flat-square" alt="Tableau">
<img src="https://img.shields.io/badge/Power_BI-F2C811?style=flat-square" alt="Power BI">

</div>

## The projects

| repository | tests | coverage | the measurement it produced |
| --- | ---: | ---: | --- |
| [rag-retrieval-gate](https://github.com/lavanyag-wq/rag-retrieval-gate) | 136 | 98% | **No golden set can call a regression on fewer than 5 one-direction flips**: 13.9% of its own 36-query set, and the naive mean rule it replaces fired on 84.5% to 100% of identical-system resamples |
| [churn-feature-referee](https://github.com/lavanyag-wq/churn-feature-referee) | 73 | 100% | **Parity reports 0 mismatches while 35 pairs are wrong** when both sides share a window bug; the referee attributes every single-side defect, 248 of 248 on the Delta leak |
| [ab-peeking-audit](https://github.com/lavanyag-wq/ab-peeking-audit) | 74 | 100% | **Daily peeking at nominal alpha 0.05 runs 28.15% false positives**, and 81.4% of its early wins evaporate by the horizon; the calibrated honest boundary costs a measured 17.5 points of power |

## How they are all built

<table>
<tr>
<td>

**The uncomfortable number leads.**

Each README opens with what the tool cannot do or the case where it loses:
the gate's own resolution floor, the blind spot's zero, the cost of the
honest boundary.

</td>
<td>

**Numbers are machine-checked.**

Every published figure is produced by code that runs in CI and verified
against the prose by an anchor-phrase checker. Breaking one number fails
the build, and each repository proves it.

</td>
<td>

**Offline and deterministic.**

No API keys, no network at runtime. Seeded generators down to an owned
counter-based PRNG, so `make verify` reproduces every number from a fresh
clone.

</td>
</tr>
</table>

## Quick connect

<div align="center">

<a href="mailto:lavanya.g@mycvcareer.com"><img src="https://img.shields.io/badge/email-lavanya.g%40mycvcareer.com-2b6777?style=flat-square" alt="email"></a>
<a href="https://www.linkedin.com/in/FILL-IN-YOUR-HANDLE"><img src="https://img.shields.io/badge/LinkedIn-fill_in_your_handle-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn placeholder"></a>
<a href="https://lavanyag-wq.github.io"><img src="https://img.shields.io/badge/project_hub-lavanyag--wq.github.io-7cf5c8?style=flat-square" alt="project hub"></a>

</div>

<sub>The LinkedIn link above is a placeholder: the resume names LinkedIn
without a handle, so replace FILL-IN-YOUR-HANDLE before publishing.</sub>
