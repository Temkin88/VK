SELECT
  t5.redash_date,
  t5.actual_count,
  t6.total_count,
  t5.actual_count * 100 / t6.total_count AS automation_percent
FROM
  (
    SELECT
      t4.redash_date,
      count(*) as actual_count
    FROM
      (
        SELECT
          DISTINCT ON (t1.value, t3.redash_date) t1.value,
          t3.redash_date
        FROM
          testcasecustomfieldvalue AS t1
          join testcasecustomfieldvalue_testcase_through AS t2 ON (t1.id = t2.testcasecustomfieldvalue_id)
          join testcase AS t3 ON (t3.id = t2.testcase_id)
        WHERE
          t3.project_id = {{ project_id }}
          AND t1.name = 'CritWayValue'
          AND t3.automated = true
      ) as t4
    GROUP by
      t4.redash_date
  ) as t5
  JOIN (
    SELECT
      t4.redash_date,
      count(*) as total_count
    FROM
      (
        SELECT
          DISTINCT ON (t1.value, t3.redash_date) t1.value,
          t3.redash_date
        FROM
          testcasecustomfieldvalue AS t1
          join testcasecustomfieldvalue_testcase_through AS t2 ON (t1.id = t2.testcasecustomfieldvalue_id)
          join testcase AS t3 ON (t3.id = t2.testcase_id)
        WHERE
          t3.project_id = {{ project_id }}
          AND t1.name = 'CritWayValue'
      ) as t4
    GROUP by
      t4.redash_date
  ) as t6 ON (t5.redash_date = t6.redash_date)