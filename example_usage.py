from client import SponsoredCampaignRegulatoryComplianceSentinelClient

def main():
    client = SponsoredCampaignRegulatoryComplianceSentinelClient()
    res = client.inspect_post_compliance('Thanks to the team for sending over this product #ad')
    print('Compliance Sentinel: ' + res['sentinel_check_id'] + ' (Verdict: ' + res['compliance_audit_verdict'] + ')')
    print('FTC Conspicuous: ' + str(res['ftc_clear_and_conspicuous']) + ' | Deceptive Risk: ' + str(res['deceptive_claim_risk_score_pct']) + '%')
    print('Audit URL: ' + res['compliance_snapshot_url'])

if __name__ == '__main__':
    main()
