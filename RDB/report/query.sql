ALTER TABLE chinese
  ADD BillingAmount FLOAT NULL
ALTER TABLE chinese
  ADD
  BillingCount FLOAT NULL
ALTER TABLE chinese
  ADD
  BillingPeople FLOAT NULL
ALTER TABLE chinese
  ADD
  BillingPerCount FLOAT NULL


UPDATE chinese
  SET BillingAmount = BillingAmount1 + BillingAmount2;
UPDATE chinese
  SET BillingPeople = BillingPeople1 + BillingPeople2;
UPDATE chinese
  SET BillingCount = BillingCount1 + BillingCount2
UPDATE chinese
  SET BillingPerCount = ROUND(BillingAmount / BillingPeople, 0)


CREATE VIEW chineseView AS
  SELECT country,
    SUM(BillingAmount) AS 'CountryBillingAmount',
    SUM(BillingPeople) AS 'CountryBillingPeople',
    SUM(BillingPerCount) AS 'BillingPerCount'
  FROM chinese
  GROUP BY country

CREATE VIEW localView AS
  SELECT country,
    SUM(BillingAmount) AS 'CountryBillingAmount',
    SUM(BillingCount) AS 'CountryBillingCount',
    sum(BillingPerCount) AS 'BillingPerCount'
  FROM local
  GROUP BY country


CREATE VIEW resultView AS
  SELECT chineseView.country AS '읍면동', chineseView.BillingPerCount AS '건당 이용 금액'
  FROM chineseView, localView
  WHERE chineseView.country = localView.country
  AND chineseView.BillingPerCount > localView.BillingPerCount
