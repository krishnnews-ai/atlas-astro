---
title: "Swell Freezes swETH and rswETH: Could a Suspected Security Breach Put 2,500 ETH at Risk?"
description: "Swell has suspended deposits and withdrawals for its swETH and rswETH liquid-staking tokens while it works to correct abnormal exchange rates. The incident has raised concerns about possible compromised administrative keys and a potential exposure of around 2,500 ETH."
pubDate: 2026-10-24
category: "Crypto Regulations"
image: "/images/swell-sweth-rsweth-ethereum-staking-security.png"
cover: "/images/swell-sweth-rsweth-ethereum-staking-security.png"
imageAlt: "Swell swETH and rswETH Ethereum staking security breach investigation"
slug: "swell-freezes-sweth-rsweth-security-breach-ethereum"
author: "Subhasmita Verma"
keywords: "Swell swETH, Swell rswETH, Ethereum liquid staking, Swell security breach, swETH paused, rswETH withdrawals, DeFi security, Spreek analyst, crypto hack, #Swell #Ethereum #DeFi #CryptoSecurity #CryptoRegulations"
draft: false
---

Ethereum staking protocol Swell has paused deposits and withdrawals for two of its Ether-linked tokens, swETH and rswETH, after their smart contracts began reporting exchange rates significantly above previously identified normal levels.

The move follows warnings from on-chain analyst Spreek, who raised concerns about possible administrative-key compromise and suspicious changes to the tokens' reported net asset values (NAVs). A technical report linked to the analyst also described upgrade contracts that could potentially expose approximately 2,500 ETH if executed.

Swell has said it is investigating the incident with security partners and that no ETH had been transferred out of the affected deposit and withdrawal contracts at the time of its statement. The protocol has not publicly established the precise cause of the incident, and the reported potential exposure should not be confused with a confirmed theft.

The immediate issue for holders is clear: normal deposits and withdrawals are paused while Swell works to restore the tokens' accounting values.

## What Happened to Swell's swETH and rswETH?

Swell announced the suspension after suspicious activity was reported involving the contracts for swETH and rswETH. The protocol said the next step toward restoring normal operations was to return both tokens' net asset values to the correct levels.

According to figures reported by Unchained on October 23, the swETH contract was reporting an exchange rate of approximately **1.203 ETH per swETH**, while rswETH was reporting around **1.138 ETH per token**.

Those figures were approximately 6% and 5% above the last rates that on-chain analyst Spreek had identified as normal before the suspected manipulation.

The discrepancy matters because a token's contract-reported exchange rate is not necessarily the same as the price a holder can actually receive when selling it on a decentralized exchange.

Unchained reported that swETH was trading at approximately 1.089 WETH in a Uniswap pool, while rswETH was changing hands at around 1.029 WETH on Curve. These market prices were notably below the elevated contract-reported rates.

The difference does not, by itself, establish the full extent of any financial loss. It does, however, highlight why the protocol's accounting figures and actual market liquidity need to be assessed separately.

## Why Did Swell Pause Deposits and Withdrawals?

The suspension is intended to prevent normal protocol operations from continuing while the reported accounting values are corrected and the security situation is investigated.

Deposits and withdrawals depend on the protocol's smart-contract logic and the values used to calculate how much ETH is associated with each token. If those values are inaccurate, continuing to process transactions could create additional risks for users and the protocol.

Swell's decision to pause both directions of activity also means holders cannot rely on the usual protocol withdrawal process to convert their tokens back into ETH while the restriction remains in place.

That does not automatically mean the tokens have become worthless or that every holder has lost funds. It means access through the affected protocol functions is restricted, and the final outcome depends on the investigation, the correction process and any further security measures.

As of the latest reports cited here, Swell had not provided a confirmed reopening date.

## Did Someone Compromise Swell's Administrative Keys?

Possible administrative-key compromise is one of the central concerns in the incident, but it has not been confirmed as the definitive cause by Swell.

On-chain analyst Spreek reported that the administrative keys associated with swETH and rswETH appeared to have been compromised. The analyst also described suspicious increases in the tokens' reported net asset values that appeared not to be supported by corresponding additional ETH.

The associated incident report alleged that an unknown actor had gained control of operational keys, including access connected to the system responsible for updating token exchange-rate information.

If accurate, such access could allow an attacker to interfere with the values reported by the protocol without necessarily transferring the underlying assets immediately. That distinction is important: changing an accounting rate and successfully stealing ETH are separate events.

The technical report also described potential malicious upgrade contracts. However, the existence of a deployed upgrade contract does not mean that the upgrade has been approved, executed or used to transfer funds.

The precise method of access, the identity of any responsible party and the full scope of the incident remain matters requiring confirmation.

## What Does the Reported 2,500 ETH Risk Mean?

One of the most concerning figures associated with the incident is an estimated exposure of approximately **2,513 ETH**.

Spreek's technical report described four upgrade contracts that could potentially affect ETH held across Swell-related deposit and withdrawal contracts if the relevant upgrades were approved and executed.

The report characterized this amount as potential exposure, not a confirmed loss. It also described additional security controls that would have to be overcome before the proposed upgrades could access the larger pool of funds.

That distinction is critical when interpreting reports about cryptocurrency security incidents. A vulnerability, a suspicious transaction, a deployed contract and a completed exploit are not interchangeable.

A potential exposure estimate identifies assets that may be at risk under certain conditions. It does not prove that those assets have been stolen or that the entire amount will ultimately be lost.

Swell's statement that no ETH had left the affected deposit and withdrawal contracts at the time of its update provides relevant context. Nevertheless, that statement is not a substitute for a completed independent forensic investigation.

Until the protocol and its security partners publish more definitive findings, the 2,500 ETH figure should be treated as a reported potential risk rather than a confirmed financial loss.

## Why the Exchange-Rate Difference Matters to Investors

Liquid-staking tokens are designed to represent claims associated with staked ETH. Their exchange rates and redemption mechanisms help users understand how those tokens relate to the underlying asset.

When a protocol reports an exchange rate that differs substantially from the price available in the market, users need to understand what each figure represents.

| Metric | swETH | rswETH |
|---|---:|---:|
| Reported contract exchange rate | Approximately 1.203 ETH | Approximately 1.138 ETH |
| Previously identified normal rate | Approximately 1.133 ETH | Approximately 1.082 ETH |
| Reported decentralized-exchange price | Approximately 1.089 WETH | Approximately 1.029 WETH |
| Current protocol status in the cited reports | Deposits and withdrawals paused | Deposits and withdrawals paused |

*Figures are approximate and reflect the reporting period covered by Unchained's October 23 report. Contract accounting rates and secondary-market prices are different measurements and should not be treated as directly interchangeable guarantees of redemption value.*

The practical concern is that holders may not be able to exit through the protocol while withdrawals are suspended. Meanwhile, prices on decentralized exchanges can fluctuate independently according to liquidity, trading activity and market confidence.

A quoted price in a liquidity pool is also not a guarantee that every holder can sell a large position at that price. Pool depth and transaction size can affect the actual execution price.

For users who hold swETH or rswETH in external wallets, decentralized exchanges or other DeFi applications, the consequences may therefore differ depending on how they use the tokens and which contracts or markets they interact with.

## Could the Incident Affect Other DeFi Protocols?

Potentially, but the impact depends on whether other applications use the affected tokens as collateral or rely on their reported exchange rates.

DeFi lending markets commonly use price feeds and collateral parameters to determine how much users can borrow against an asset. If a market relies on an inaccurate valuation, it can create risks for borrowers, lenders and the protocol itself.

For example, if a lending application were to value a token using an inflated accounting rate rather than a reliable market price, its collateral calculations could become distorted. Whether that can actually happen depends on the application's oracle design, safeguards and supported assets.

This is a general risk scenario, not evidence that a particular lending platform has suffered losses in the Swell incident.

Users who have deposited swETH or rswETH into other protocols should check the official status notices for those applications and understand how their positions are valued. They should not assume that every DeFi platform has the same exposure or uses the same pricing mechanism.

## What Should swETH and rswETH Holders Do Now?

For holders, the priority is to avoid creating additional risk while the investigation remains unresolved.

**First, follow Swell's official announcements.** The protocol's own updates are the most relevant source for confirmation of the pause, any security findings and the conditions for reopening deposits and withdrawals.

**Second, do not assume a normal redemption is available.** The affected protocol functions are paused in the cited reports. Avoid making plans based on an expected reopening time unless Swell confirms it.

**Third, be alert for phishing attempts.** Security incidents often attract fake support accounts, fraudulent recovery websites and messages promising to unlock funds. Never share wallet seed phrases or private keys, and do not sign unfamiliar transactions in response to unsolicited messages.

**Fourth, check any connected DeFi positions.** If swETH or rswETH is being used as collateral, supplied to a lending market or held in another smart contract, review official notices from that platform. Do not interact with unfamiliar recovery tools or contracts simply because they claim to offer a workaround.

Finally, distinguish between verified updates and speculation. The reported administrative-key compromise and approximately 2,500 ETH exposure are serious concerns, but the cause and ultimate financial impact require further confirmation.

## What Happens Next?

The next important developments are likely to be Swell's correction of the affected exchange rates, its security partners' findings and an official explanation of when deposits and withdrawals can resume.

A credible resolution should clarify whether any administrative credentials were compromised, how the abnormal values were introduced, whether the relevant contracts were upgraded or otherwise altered, and what safeguards have been implemented.

The protocol will also need to explain how its corrected accounting values relate to holders' redemption rights and how it intends to restore confidence in the affected tokens.

Until those details are available, the incident remains a security and operational concern rather than a confirmed loss of approximately 2,500 ETH.

For the broader Ethereum staking sector, the episode is another reminder that liquid-staking tokens depend not only on the value of staked assets but also on the reliability of their smart contracts, administrative controls, exchange-rate mechanisms and withdrawal processes.

## Frequently Asked Questions

### 1. Why did Swell pause swETH and rswETH?

Swell paused deposits and withdrawals while working to correct abnormal net asset values and exchange rates reported by the affected token contracts.

### 2. Has Swell lost 2,500 ETH?

A loss of 2,500 ETH has not been confirmed in the cited reports. The figure refers to potential exposure described in an on-chain analyst's technical report if certain malicious upgrades were executed.

### 3. Were Swell's administrative keys hacked?

An on-chain analyst raised concerns that relevant administrative keys may have been compromised. Swell's precise root-cause findings had not been established in the reports cited here.

### 4. Can users withdraw swETH and rswETH right now?

The protocol's deposit and withdrawal functions were reported as paused. Holders should consult Swell's official channels for the latest status and should not assume that withdrawals have resumed.

### 5. Are swETH and rswETH worthless?

The pause does not establish that either token is worthless. However, access to protocol withdrawals is restricted, and secondary-market prices may differ from the exchange rates reported by the contracts.

### 6. When will Swell resume normal operations?

No confirmed reopening date was provided in the cited reports. Swell indicated that correcting the affected net asset values was a necessary step toward resuming normal operations.

### 7. What should holders do during the pause?

Monitor official Swell updates, avoid suspicious recovery links, never disclose private keys or seed phrases, and review any positions involving the tokens on other DeFi platforms.

## Sources

- Unchained — *Swell Freezes swETH and rswETH Withdrawals Until It Corrects Their Exchange Rates* (October 23, 2026).
- Spreek — *Swell hot-key compromise: incident report* (October 22, 2026; contains analyst findings and inferences that require independent verification).
- Swell — Official statements concerning suspicious activity and the pause on swETH and rswETH deposits and withdrawals.

**Disclaimer:** This article is for informational purposes only and does not constitute financial or investment advice. Cryptocurrency and DeFi assets carry significant risks, including smart-contract vulnerabilities, liquidity constraints and loss of funds.
